#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_ids_per_device_info
short_description: Information module for Security Advisories Ids Per Device
description:
- Get Security Advisories Ids Per Device by id.
- Retrieves list of advisory IDs for a device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
    - DeviceId path parameter. Device instance UUID.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_advisory_ids_per_device used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.security_advisories.SecurityAdvisories.get_advisory_ids_per_device

- name: Paths used on the module Security Advisories Ids Per Device
  description: |-
    get /dna/intent/api/v1/security-advisory/device/{deviceId}
"""

EXAMPLES = r"""
- name: Get Security Advisories Ids Per Device by id
  cisco.dnac.security_advisories_ids_per_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    deviceId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "deviceId": "string",
          "advisoryIds": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""
