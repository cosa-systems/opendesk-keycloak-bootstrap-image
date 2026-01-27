#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
# SPDX-License-Identifier: Apache-2.0

import os.path
import re
import sys
import yaml

def start():

    valuesFile = '/app/values.yaml'

    os.path.isfile(valuesFile)

    valuesAll = []

    with open(valuesFile, 'r') as file:
        valuesAll = yaml.safe_load(file)

    if not valuesAll:
        sys.exit(f"File '{valuesFile}' is empty!")

    checkForSecretsAndUpdate(valuesAll)

    with open('/tmp/values.yaml', 'w') as file:
        yaml.dump(valuesAll, file)

def checkForSecretsAndUpdate(valuesAll):

    for section, dictionary in valuesAll.items():
        searchAndReplaceValueOrExistingSecret(section, dictionary)

def searchAndReplaceValueOrExistingSecret(section, dictionary):

    if not isinstance(dictionary, dict):
        return

    for subSection, subDictionary in dictionary.items():
        if secret := getValueOrExistingSecret(subDictionary):
            dictionary[subSection] = secret
            break
        searchAndReplaceValueOrExistingSecret(subSection, subDictionary)

    return

def getValueOrExistingSecret(dictionary):

    if not isinstance(dictionary, dict):
        return ''

    newSecretValue = ''
    wantToFind = ('value', 'existingSecret')

    for subSection, subDictionary in dictionary.items():

        if subSection not in wantToFind:
            continue

        match subSection:
            case 'value' if not newSecretValue:
                newSecretValue = subDictionary
            case 'existingSecret':
                newSecretValue = getSecretFromFile(subDictionary)
                break

    return newSecretValue

def getSecretFromFile(dictionary):

    if 'name' not in dictionary:
        print(f"no 'name' found for existing secret, '{dictionary}'")
        return ''

    if 'key' not in dictionary:
        print(f"no 'key' found for existing secret, '{dictionary}'")
        return ''

    with open(sanitisedName(dictionary), 'r') as file:
        return file.readline().rstrip()

def sanitisedName(dictionary):

    nameAndKey = dictionary['name'] + ' ' + dictionary['key']

    sanitisedNameAndKey = re.sub(r'\W+', '-', nameAndKey)

    return './app/secrets/' + sanitisedNameAndKey

start()