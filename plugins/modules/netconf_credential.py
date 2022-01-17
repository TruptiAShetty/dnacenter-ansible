#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: netconf_credential
short_description: Resource module for Netconf Credential
description:
- Manage operations create and update of the resource Netconf Credential.
- Updates global netconf credentials.
- Adds global netconf credentials.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Netconf Credential's comments.
    type: str
  credentialType:
    description: Netconf Credential's credentialType.
    type: str
  description:
    description: Netconf Credential's description.
    type: str
  id:
    description: Netconf Credential's id.
    type: str
  instanceTenantId:
    description: Netconf Credential's instanceTenantId.
    type: str
  instanceUuid:
    description: Netconf Credential's instanceUuid.
    type: str
  netconfPort:
    description: Netconf Credential's netconfPort.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function update_netconf_credentials used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.update_netconf_credentials

- name: SDK function create_netconf_credentials used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.create_netconf_credentials

- name: Paths used on the module Netconf Credential
  description: |-
    put /dna/intent/api/v1/global-credential/netconf,
    post /dna/intent/api/v1/global-credential/netconf
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.netconf_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    netconfPort: string

- name: Create
  cisco.dnac.netconf_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    netconfPort: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
