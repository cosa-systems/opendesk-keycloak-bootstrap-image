#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

import sys
import json
import logging
import requests
from deepdiff import DeepDiff

KNOWN_OBJECTS = {
    'clientScopes': {
        'path': '/client-scopes',
        'default_objects': [ 'acr','web-origins','email','profile','microprofile-jwt','role_list','offline_access','roles','address','phone' ]
    },
    'clients': {
        'path': '/clients',
        'default_objects': [ 'UMC', '${client_account}', '${client_account-console}', '${client_admin-cli}', '${client_broker}', '${client_realm-management}', '${client_security-admin-console}' ]
    }
}

class Keycloak:

    def __init__(self, adm_username, adm_password, realm, base_url):
        self.adm_username = adm_username
        self.adm_password = adm_password
        self.realm = realm
        self.base_url = base_url
        self.access_token = None
        self.base_path = '/admin/realms/'+self.realm
        logging.info(f"Init for {self.base_url} and user {self.adm_username}")

    def __get_knownobjects_details(self, type, attribute):
        if type not in KNOWN_OBJECTS:
            sys.exit(f"! Object type {type} not yet supported")
        if attribute not in KNOWN_OBJECTS[type]:
            sys.exit(f"! Attribute {attribute} not found for {type} in KNOWN_OBJECTS")
        else:
            return KNOWN_OBJECTS[type][attribute]


    def __get_subpath(self, type):
        return self.__get_knownobjects_details(type, 'path')

    def __get_defaultnames(self, type):
        return self.__get_knownobjects_details(type, 'default_objects')

    def __api_call(self,
                subpath=None,
                method='post',
                data=None,
                query_param=None):
        req = getattr(requests, method)
        payload = json.dumps(data) if data else ""
        url = self.base_url+self.base_path+subpath
        res = req(url,
                    data=payload,
                    params=query_param,
                    headers={'Content-Type': 'application/json',
                            'Authorization': f"Bearer {self.access_token}" }
                )
        if res.status_code == 401:
            self.__get_access_token()
            res = req(url,
                        data=payload,
                        params=query_param,
                        headers={'Content-Type': 'application/json',
                                'Authorization': f"Bearer {self.access_token}" }
                    )
        if (res.status_code == 404):
            sys.exit(f"! HTTP404: Not found when {method}-ing to {url} with payload '{payload}'")
        elif (res.status_code == 400):
            sys.exit(f"! HTTP400: Bad Reqest when {method}-ing to {url} with payload '{payload}'")
        elif (res.status_code in [200, 201, 204, 409]):
            logging.info(f"Successful {method} to {url}")
            return res
        else:
            sys.exit(f"! Unhandled response {res} when {method}-ing to {url} with payload '{payload}'")

    def __get_access_token(self):
        logging.info("Requesting access token")
        res = requests.post(self.base_url+'/'+'/realms/master/protocol/openid-connect/token',
                      data={
                        'client_id': 'admin-cli',
                        'username': self.adm_username,
                        'password': self.adm_password,
                        'grant_type': 'password'
                      })
        if not res.status_code == 200:
            sys.exit("bad response:"+res.content)
        else:
          json_res = res.json()
          self.access_token = json_res["access_token"]

    def __get_object_id(self, type, name):
        typepath = self.__get_subpath(type)
        res = self.__api_call(subpath=typepath, method='get')
        for object in res.json():
            if 'name' not in object:
                logging.warning(f"Object has no name defined, skipping while searching for namematch with {name}")
                continue
            if object['name'] == name:
                logging.info(f"{type} object {name} has ID {object['id']}")
                return object['id']
        logging.warning(f"{type} object {name} not found")
        return None

    def reconcile_objecttype(self, type, names = []):
        typepath = self.__get_subpath(type)
        res = self.__api_call(subpath=typepath, method='get')
        want_list = names + self.__get_defaultnames(type)
        for object in res.json():
            if 'name' not in object:
                logging.error(f"Object has no name defined, ignoring for reconciliation")
                continue
            if object['name'] not in want_list:
                logging.warning(f"Deleting object {object['name']} with id {object['id']} as it is not on wantlist")
                objectpath=typepath+'/'+object['id']
                res = self.__api_call(subpath=objectpath, method='delete')
                if res.status_code == 204:
                    logging.info(f"Object deleted")

    def create_or_update_object(self, type, data):
        typepath = self.__get_subpath(type)
        res = self.__api_call(subpath=typepath, data=data)
        if (res.status_code == 409):
            logging.info("Object already exists, querying for compare")
            id = self.__get_object_id(type, data['name'])
            objectpath=typepath+'/'+id
            res = self.__api_call(subpath=objectpath, method='get')
            diff = DeepDiff(data, res.json(), ignore_order=True, group_by='name')
            if "values_changed" in diff or "set_item_added" in diff:
                logging.info(f"Found object updates: {diff['values_changed']} trying to update the relevant object")
                res = self.__api_call(subpath=objectpath, data=data, method='put')
                if res.status_code == 204:
                    logging.info(f"Object update successful")
            else:
                logging.info(f"No object relevant update(s) found, only {diff.keys()}")

