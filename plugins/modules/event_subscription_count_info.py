#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_count_info
short_description: Information module for Event Subscription Count
description:
- Get all Event Subscription Count.
- Returns the Count of EventSubscriptions.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  eventIds:
    description:
    - EventIds query parameter. List of subscriptions related to the respective eventIds.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function count_of_event_subscriptions used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.event_management.EventManagement.count_of_event_subscriptions

- name: Paths used on the module Event Subscription Count
  description: |-
    get /dna/intent/api/v1/event/subscription/count
"""

EXAMPLES = r"""
- name: Get all Event Subscription Count
  cisco.dnac.event_subscription_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    eventIds: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0
    }
"""
