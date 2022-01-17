#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_namespace_files_info
short_description: Information module for File Namespace Files
description:
- Get File Namespace Files by name.
- Returns list of files under a specific namespace.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  nameSpace:
    description:
    - NameSpace path parameter. A listing of fileId's.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_list_of_files used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.file.File.get_list_of_files

- name: Paths used on the module File Namespace Files
  description: |-
    get /dna/intent/api/v1/file/namespace/{nameSpace}
"""

EXAMPLES = r"""
- name: Get File Namespace Files by name
  cisco.dnac.file_namespace_files_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    nameSpace: string
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
          "attributeInfo": {},
          "downloadPath": "string",
          "encrypted": true,
          "fileFormat": "string",
          "fileSize": "string",
          "id": "string",
          "md5Checksum": "string",
          "name": "string",
          "nameSpace": "string",
          "sftpServerList": [
            {}
          ],
          "sha1Checksum": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""
