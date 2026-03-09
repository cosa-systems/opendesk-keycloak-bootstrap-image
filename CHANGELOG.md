# [1.4.0](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.3.0...v1.4.0) (2026-03-09)


### Features

* **Dockerfile:** Update to alpie v3.23.3 ([b12ab0c](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/b12ab0ca284c8376cd09bc1b49f1d813ed9e3598))

# [1.3.0](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.2.3...v1.3.0) (2025-03-11)


### Features

* Reference dedicated secret for admin credentials ([d15a3de](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/d15a3deccb800c402a12456f2731365855fd1ba7))

## [1.2.3](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.2.2...v1.2.3) (2024-09-24)


### Bug Fixes

* **keycloak.py:** Test if expected realm is available. ([cf1c562](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/cf1c5621c6a549c45079074d41843353faec5af5))

## [1.2.2](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.2.1...v1.2.2) (2024-09-24)


### Bug Fixes

* **docker:** Bump base image and Python3. ([69a7719](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/69a7719949dd1fd4471c797ca95f6efbf90e949c))
* **keycloak.py:** Test if Keycloak hostname is resolvable with retries. ([7c227b1](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/7c227b1973d323671da950ccbd66382f5a289ad6))

## [1.2.1](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.2.0...v1.2.1) (2024-08-07)


### Bug Fixes

* **reconciliation:** Allow managed object names to passed into the script. ([8bc9afd](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/8bc9afd01678f0c6ae1e482958c14ceb37cd3edb))

# [1.2.0](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.1.0...v1.2.0) (2024-07-16)


### Features

* **kcom.py:** Support for custom oidc object definitions. ([d3b45ed](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/d3b45edb2f044b42d3eadc31d5a13ae5a527f7b2))

# [1.1.0](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.0.5...v1.1.0) (2024-07-15)


### Features

* Remove diff handling for clients and client scopes, re-create them (all) when script is executed. ([d35db60](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/d35db60a03599168a96a06d9ab1c77403c89dc8c))

## [1.0.5](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.0.4...v1.0.5) (2024-05-14)


### Bug Fixes

* **kcom.py:** Improve logging output ([5ac1932](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/5ac193273f5a3c03028d69d12ac347dcd9a39475))
* Update Alpine to 3.19.1 and pin installed apk packages ([63d9f1a](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/63d9f1a6bd55d77723022177aa648af3f942b838))

## [1.0.4](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/compare/v1.0.3...v1.0.4) (2023-12-27)


### Bug Fixes

* **ci:** Move to Open CoDE ([75bae33](https://gitlab.opencode.de/bmi/opendesk/components/platform-development/images/opendesk-keycloak-bootstrap/commit/75bae3373f9b93d7a742a0cb0cb7123aaa59ce58))

## [1.0.3](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/compare/v1.0.2...v1.0.3) (2023-12-14)


### Bug Fixes

* **values:** Intracluster config support ([ae1f3ae](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/ae1f3ae580782484346e300101315cdf4821aacf))

## [1.0.2](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/compare/v1.0.1...v1.0.2) (2023-12-13)


### Bug Fixes

* **ci:** Update to new gitlab-config version ([b7abaa9](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/b7abaa9b027dba12e38a507875f83216e8213951))

## [1.0.1](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/compare/v1.0.0...v1.0.1) (2023-12-07)


### Bug Fixes

* **docker:** Remove apk cache ([50b4883](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/50b4883691744d35b7e0afeee128fcd01b12e145))
* **docker:** Remove apk cache ([7c27ff8](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/7c27ff837fbc7b1d8c7bf9de60800e24984fd7bb))

# 1.0.0 (2023-11-28)


### Bug Fixes

* **keycloak:** Initial commit ([24a6f5a](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/24a6f5a9188e2b9bf1d1cf0029b130a693d80e92))

## [1.0.1](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/compare/v1.0.0...v1.0.1) (2023-11-24)


### Bug Fixes

* **ci:** Satisfy linter ([b3a90b4](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/b3a90b4d671797d5d47ad119d921ae2b8060b5d3))

# 1.0.0 (2023-11-24)


### Bug Fixes

* **all:** Add jmespath and deepdiff parameters ([d09c738](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/d09c738efb8140bf8b5f37a5061aef99c9ef1200))
* **all:** Add pip and install requirements ([4ca89cf](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/4ca89cfa0d77484247e973bfd01820816d81bfe5))
* **all:** Add pip and install requirements ([fe49a0f](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/fe49a0f0c9c2fae9f2a092ebdde50d9c8827f41f))
* **all:** Add pip and install requirements ([894b209](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/894b209a85751892321a2e93f17d31c25913b328))
* **all:** Copy & Paste mistake ([8f17d68](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/8f17d686d36ca470c50947a2ae484c4406c5bbd4))
* **all:** Fix variable name ([eb79a61](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/eb79a61f09743ebecc811517dbc956388e87b21c))
* **all:** Fullfill requirements ([8ae6479](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/8ae6479ddc26c5186a5436be04f0c3a3c5ef532b))
* **all:** License headers ([9ec1fce](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/9ec1fce0d0b29bdc681439380937a8d2199ff9fa))
* **all:** Set file exec permissions ([903e61c](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/903e61c9a06ee01c3e6d541868b417fdb96896cd))
* **ansible:** Add temp dir ([7c4a697](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/7c4a69753251424821cb540a0db5b8c5469af8a4))
* **ansible:** Add temp dir ([efa1b34](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/efa1b349402edfd3dd6e4bb47397967a33ff54f0))
* **ansible:** Add temp dir ([a06f783](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/a06f783aafbcb0135eeefc9636e27a33645ca9c9))
* **docs:** Add README.md ([8976db6](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/8976db65fa0b25c890582e47075bd984bf60ba20))
* **entrypoint:** Support ansible execution ([1ca51ed](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/1ca51ed6f851e43ffaed3d82175478d3d116fd60))
* **init:** Initial commit ([357ab76](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/357ab76baf25626f8b97826efd8de525ba4432d4))
* **init:** Initial commit ([89f8aef](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/89f8aef840321412c24a121f71b027e297196ee1))
* **init:** Initial commit ([3e9f830](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/3e9f830778da0c10af1f30761483ef862380791f))
* **init:** Initial commit ([e920530](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/e9205308367cc0d278b97cb82607ca7fb52a131a))
* **kcom:** Read KC secret from values ([4ba2859](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/4ba2859cbcbdaa13e11676309992aa392d20a7f2))
* **keycloak.py:** Add logging ([888cc92](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/888cc9294138d6e27dbea32293c7834c98cff345))
* **keycloak.py:** Add UMC as wantlist client ([ece3ef4](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/ece3ef469a9a7fee5f327153cda111a60423c343))
* **keycloak.py:** Check of valid change categories ([55fba03](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/55fba03abd92897fec10b5f623bf28175eae3384))
* **requirements:** Add logging ([50d700e](https://gitlab.souvap-univention.de/souvap/tooling/images/opendesk-keycloak-bootstrap/commit/50d700e5111240b4fb1daae499ec1daa152a0b8a))
