#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_count_info
short_description: Information module for Pnp Device Count
description:
- Get all Pnp Device Count.
- Returns the device count based on filter criteria. This is useful for pagination.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  serialNumber:
    description:
    - SerialNumber query parameter. Device Serial Number.
    type: str
  state_:
    description:
    - State query parameter. Device State.
    type: str
  onbState:
    description:
    - OnbState query parameter. Device Onboarding State.
    type: str
  cmState:
    description:
    - CmState query parameter. Device Connection Manager State.
    type: str
  name:
    description:
    - Name query parameter. Device Name.
    type: str
  pid:
    description:
    - Pid query parameter. Device ProductId.
    type: str
  source:
    description:
    - Source query parameter. Device Source.
    type: str
  projectId:
    description:
    - ProjectId query parameter. Device Project Id.
    type: str
  workflowId:
    description:
    - WorkflowId query parameter. Device Workflow Id.
    type: str
  projectName:
    description:
    - ProjectName query parameter. Device Project Name.
    type: str
  workflowName:
    description:
    - WorkflowName query parameter. Device Workflow Name.
    type: str
  smartAccountId:
    description:
    - SmartAccountId query parameter. Device Smart Account.
    type: str
  virtualAccountId:
    description:
    - VirtualAccountId query parameter. Device Virtual Account.
    type: str
  lastContact:
    description:
    - LastContact query parameter. Device Has Contacted lastContact > 0.
    type: bool
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_device_count,

  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-device/count,

"""

EXAMPLES = r"""
- name: Get all Pnp Device Count
  cisco.dnac.pnp_device_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    serialNumber: string
    state_: string
    onbState: string
    cmState: string
    name: string
    pid: string
    source: string
    projectId: string
    workflowId: string
    projectName: string
    workflowName: string
    smartAccountId: string
    virtualAccountId: string
    lastContact: True
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
