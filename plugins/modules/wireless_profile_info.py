#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profile_info
short_description: Information module for Wireless Profile
description:
- Get all Wireless Profile.
- Gets either one or all the wireless network profiles if no name is provided for network-profile.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  profileName:
    description:
    - ProfileName query parameter. Wireless Network Profile Name.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_wireless_profile used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.wireless.Wireless.get_wireless_profile

- name: Paths used on the module Wireless Profile
  description: |-
    get /dna/intent/api/v1/wireless/profile
"""

EXAMPLES = r"""
- name: Get all Wireless Profile
  cisco.dnac.wireless_profile_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    profileName: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "profileDetails": {
          "name": "string",
          "sites": [
            "string"
          ],
          "ssidDetails": [
            {
              "name": "string",
              "type": "string",
              "enableFabric": true,
              "flexConnect": {
                "enableFlexConnect": true,
                "localToVlan": 0
              },
              "interfaceName": "string"
            }
          ]
        }
      }
    ]
"""
