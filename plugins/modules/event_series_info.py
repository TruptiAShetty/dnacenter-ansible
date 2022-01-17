#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_series_info
short_description: Information module for Event Series
description:
- Get all Event Series.
- Get the list of Published Notifications.
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
    - EventIds query parameter. The registered EventId should be provided.
    type: str
  startTime:
    description:
    - StartTime query parameter. Start Time in milliseconds.
    type: int
  endTime:
    description:
    - EndTime query parameter. End Time in milliseconds.
    type: int
  category:
    description:
    - Category query parameter.
    type: str
  type:
    description:
    - Type query parameter.
    type: str
  severity:
    description:
    - Severity query parameter.
    type: str
  domain:
    description:
    - Domain query parameter.
    type: str
  subDomain:
    description:
    - SubDomain query parameter. Sub Domain.
    type: str
  source:
    description:
    - Source query parameter.
    type: str
  offset:
    description:
    - Offset query parameter. Start Offset.
    type: int
  limit:
    description:
    - Limit query parameter. # of records.
    type: int
  sortBy:
    description:
    - SortBy query parameter. Sort By column.
    type: str
  order:
    description:
    - Order query parameter. Ascending/Descending order asc/desc.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_notifications used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.event_management.EventManagement.get_notifications

- name: Paths used on the module Event Series
  description: |-
    get /dna/intent/api/v1/event/event-series
"""

EXAMPLES = r"""
- name: Get all Event Series
  cisco.dnac.event_series_info:
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
    startTime: 0
    endTime: 0
    category: string
    type: string
    severity: string
    domain: string
    subDomain: string
    source: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
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
        "eventId": "string",
        "instanceId": "string",
        "nameSpace": "string",
        "name": "string",
        "description": "string",
        "version": "string",
        "category": "string",
        "domain": "string",
        "subDomain": "string",
        "type": "string",
        "severity": "string",
        "source": "string",
        "timestamp": "string",
        "details": "string",
        "eventHierarchy": "string"
      }
    ]
"""
