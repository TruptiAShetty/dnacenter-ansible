#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to operate the Authentication and Policy Servers in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["Muthu Rakesh, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: ise_radius_integration_workflow_manager
short_description: Resource module for Authentication and Policy Servers
description:
- Manage operations on Authentication and Policy Servers.
- API to create Authentication and Policy Server Access Configuration.
- API to update Authentication and Policy Server Access Configuration.
- API to delete Authentication and Policy Server Access Configuration.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Muthu Rakesh (@MUTHU-RAKESH-27)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ "merged", "deleted" ]
    default: merged
  config:
    description:
    - List of details of Authentication and Policy Servers being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      authentication_policy_server:
        description: Manages the Authentication and Policy Servers.
        type: dict
        suboptions:
          server_type:
            description:
            - Type of the Authentication and Policy Server.
            - ISE for Cisco ISE servers.
            - AAA for Non-Cisco ISE servers.
            type: str
            choices: [ "AAA", "ISE" ]
            default: AAA
          server_ip_address:
            description: IP Address of the Authentication and Policy Server.
            type: str
            required: True
          shared_secret:
            description:
            - Shared secret between devices and authentication and policy server.
            - Shared secret must have 4 to 100 characters with no spaces or the following characters - ["<", "?"].
            - Shared secret is a Read-Only parameter.
            type: str
          protocol:
            description:
            - Type of protocol for authentication and policy server.
            - RADIUS provides centralized services (AAA) for users in remote access scenarios.
            - TACACS focuses on access control and administrative authentication for network devices.
            type: str
            choices: [ "TACACS", "RADIUS", "RADIUS_TACACS" ]
            default: RADIUS
          encryption_scheme:
            description:
            - Type of encryption scheme for additional security.
            - If encryption scheme is given, then message authenticator code and encryption keys need to be required.
            - Updation of encryption scheme is not possible.
            - >
              KEYWRAP is used for securely wrapping and unwrapping encryption keys,
              ensuring their confidentiality during transmission or storage.
            - >
              RADSEC is an extension of RADIUS that provides secure communication
              between RADIUS clients and servers over TLS/SSL. Enhances enhancing the
              confidentiality and integrity of authentication and accounting data exchange.
            type: str
            choices: [ "KEYWRAP", "RADSEC" ]
          encryption_key:
            description:
            - Encryption key used to encrypt shared secret.
            - Updation of encryption scheme is not possible.
            - Required when encryption_scheme is provided.
            - >
              When ASCII format is selected, Encryption Key may contain
              alphanumeric and special characters. Key must be 16 char long.
            type: str
          message_authenticator_code_key:
            description:
            - Message key used to encrypt shared secret.
            - Updation of message key is not possible.
            - Required when encryption_scheme is provided.
            - >
              Message Authentication Code Key may contain alphanumeric and special characters.
              Key must be 20 char long.
            type: str
          authentication_port:
            description:
            - Authentication port of RADIUS server.
            - Updation of authentication port is not possible.
            - Authentication port should be from 1 to 65535.
            type: int
            default: 1812
          accounting_port:
            description:
            - Accounting port of RADIUS server.
            - Updation of accounting port is not possible.
            - Accounting port should be from 1 to 65535.
            type: int
            default: 1813
          retries:
            description:
            - Number of communication retries between devices and authentication and policy server.
            - Retries should be from 1 to 3.
            type: int
            default: 3
          timeout:
            description:
            - Number of seconds before timing out between devices and authentication and policy server.
            - Timeout should be from 2 to 20.
            type: int
            default: 4
          role:
            description:
            - Role of authentication and policy server.
            - Updation of role is not possible
            type: str
            default: secondary
          pxgrid_enabled:
            description:
            - Set True to enable the Pxgrid and False to disable the Pxgrid.
            - Pxgrid is available only for the Cisco ISE Servers.
            - >
              PxGrid facilitates seamless integration and information sharing across products,
              enhancing threat detection and response capabilities within the network ecosystem.
            type: bool
            default: True
          use_dnac_cert_for_pxgrid:
            description: Set True to use the Cisco Catalyst Center certificate for the Pxgrid.
            type: bool
            default: False
          cisco_ise_dtos:
            description:
            - List of Cisco ISE Data Transfer Objects (DTOs).
            - Required when server_type is set to ISE.
            type: list
            elements: dict
            suboptions:
              user_name:
                description:
                - User name of the Cisco ISE server.
                - Required for passing the cisco_ise_dtos.
                type: str
              password:
                description:
                - Password of the Cisco ISE server.
                - Password must have 4 to 127 characters with no spaces or the following characters - "<".
                - Required for passing the cisco_ise_dtos.
                type: str
              fqdn:
                description:
                - Fully-qualified domain name of the Cisco ISE server.
                - Required for passing the cisco_ise_dtos.
                type: str
              ip_address:
                description:
                - IP Address of the Cisco ISE Server.
                - Required for passing the cisco_ise_dtos.
                type: str
              description:
                description: Description about the Cisco ISE server.
                type: str
              ssh_key:
                description: SSH key of the Cisco ISE server.
                type: str
          external_cisco_ise_ip_addr_dtos:
            description: External Cisco ISE IP address data transfer objects for future use.
            type: list
            elements: dict
            suboptions:
              external_cisco_ise_ip_addresses:
                description: External Cisco ISE IP addresses.
                type: list
                elements: dict
                suboptions:
                  external_ip_address:
                    description: External Cisco ISE IP address.
                    type: str
              ise_type:
                description: Type of the Authentication and Policy Server.
                type: str
          trusted_server:
            description:
            - Indicates whether the certificate is trustworthy for the server.
            - Serves as a validation of its authenticity and reliability in secure connections.
            default: True
            type: bool
          ise_integration_wait_time:
            description:
            - Indicates the sleep time after initiating the Cisco ISE integration process.
            - Maximum sleep time should be less or equal to 120 seconds.
            default: 20
            type: int
requirements:
- dnacentersdk >= 2.7.1
- python >= 3.9
notes:
  - SDK Method used are
    system_settings.SystemSettings.add_authentication_and_policy_server_access_configuration,
    system_settings.SystemSettings.edit_authentication_and_policy_server_access_configuration,
    system_settings.SystemSettings.accept_cisco_ise_server_certificate_for_cisco_ise_server_integration,
    system_settings.SystemSettings.delete_authentication_and_policy_server_access_configuration,

  - Paths used are
    post /dna/intent/api/v1/authentication-policy-servers,
    put /dna/intent/api/v1/authentication-policy-servers/${id},
    put /dna/intent/api/v1/integrate-ise/${id},
    delete /dna/intent/api/v1/authentication-policy-servers/${id}

"""

EXAMPLES = r"""
- name: Create an AAA server.
  cisco.dnac.ise_radius_integration_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - authentication_policy_server:
        server_type: AAA
        server_ip_address: 10.0.0.1
        shared_secret: "12345"
        protocol: RADIUS_TACACS
        encryption_scheme: KEYWRAP
        encryption_key: "1234567890123456"
        message_authenticator_code_key: asdfghjklasdfghjklas
        authentication_port: 1812
        accounting_port: 1813
        retries: 3
        timeout: 4
        role: secondary

- name: Create an Cisco ISE server.
  cisco.dnac.ise_radius_integration_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - authentication_policy_server:
        server_type: ISE
        server_ip_address: 10.0.0.2
        shared_secret: "12345"
        protocol: RADIUS_TACACS
        encryption_scheme: KEYWRAP
        encryption_key: "1234567890123456"
        message_authenticator_code_key: asdfghjklasdfghjklas
        authentication_port: 1812
        accounting_port: 1813
        retries: 3
        timeout: 4
        role: primary
        use_dnac_cert_for_pxgrid: False
        pxgrid_enabled: True
        cisco_ise_dtos:
        - user_name: Cisco ISE
          password: "12345"
          fqdn: abs.cisco.com
          ip_address: 10.0.0.2
          description: Cisco ISE
        trusted_server: True
        ise_integration_wait_time: 20

- name: Update an AAA server.
  cisco.dnac.ise_radius_integration_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - authentication_policy_server:
        server_type: AAA
        server_ip_address: 10.0.0.1
        protocol: RADIUS_TACACS
        retries: 3
        timeout: 5

- name: Update an Cisco ISE server.
  cisco.dnac.ise_radius_integration_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - authentication_policy_server:
        server_type: ISE
        server_ip_address: 10.0.0.2
        protocol: RADIUS_TACACS
        retries: 3
        timeout: 5
        use_dnac_cert_for_pxgrid: False
        pxgrid_enabled: True
        cisco_ise_dtos:
        - user_name: Cisco ISE
          password: "12345"
          fqdn: abs.cisco.com
          ip_address: 10.0.0.2
          description: Cisco ISE

- name: Delete an Authentication and Policy server.
  cisco.dnac.ise_radius_integration_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: True
    config:
    - authentication_policy_server:
        server_ip_address: 10.0.0.1
"""

RETURN = r"""
# Case_1: Successful creation of Authentication and Policy Server.
response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_2: Successful updation of Authentication and Policy Server.
response_2:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_3: Successful creation/updation of network
response_3:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

import copy
import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class IseRadiusIntegration(DnacBase):
    """Class containing member attributes for ise_radius_integration_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.max_timeout = self.params.get('dnac_api_task_timeout')
        self.result["response"] = [
            {"authenticationPolicyServer": {"response": {}, "msg": {}}}
        ]
        self.authentication_policy_server_obj_params = \
            self.get_obj_params("authenticationPolicyServer")
        self.validation_string = ""

    def validate_input(self):
        """
        Checks if the configuration parameters provided in the playbook
        meet the expected structure and data types,
        as defined in the 'temp_spec' dictionary.

        Parameters:
            None

        Returns:
            self

        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        # temp_spec is the specification for the expected structure of configuration parameters
        temp_spec = {
            "authentication_policy_server": {
                "type": "dict",
                "server_type": {"type": 'string', "choices": ["AAA", "ISE"]},
                "server_ip_address": {"type": 'string'},
                "shared_secret": {"type": 'string'},
                "protocol": {"type": 'string', "choices": ["TACACS", "RADIUS", "RADIUS_TACACS"]},
                "encryption_scheme": {"type": 'string'},
                "message_authenticator_code_key": {"type": 'string'},
                "encryption_key": {"type": 'string'},
                "authentication_port": {"type": 'integer'},
                "accounting_port": {"type": 'integer'},
                "retries": {"type": 'integer'},
                "timeout": {"type": 'integer'},
                "role": {"type": 'string'},
                "pxgrid_enabled": {"type": 'bool'},
                "use_dnac_cert_for_pxgrid": {"type": 'bool'},
                "cisco_ise_dtos": {
                    "type": 'list',
                    "user_name": {"type": 'string'},
                    "password": {"type": 'string'},
                    "fqdn": {"type": 'string'},
                    "ip_address": {"type": 'string'},
                    "description": {"type": 'string'},
                    "ssh_key": {"type": 'string'},
                },
                "external_cisco_ise_ip_addr_dtos": {
                    "type": 'list',
                    "external_cisco_ise_ip_addresses": {
                        "type": 'list',
                        "external_ip_address": {"type": 'string'},
                    },
                    "ise_type": {"type": 'string'},
                },
                "trusted_server": {"type": 'bool'},
                "ise_integration_wait_time": {"type": 'integer'}
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format("\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log("Successfully validated playbook config params: {0}".format(valid_temp), "INFO")
        self.msg = "Successfully validated input from the playbook"
        self.status = "success"
        return self

    def requires_update(self, have, want, obj_params):
        """
        Check if the template config given requires update by comparing
        current information wih the requested information.

        This method compares the current global pool, reserve pool,
        or network details from Cisco Catalyst Center with the user-provided details
        from the playbook, using a specified schema for comparison.

        Parameters:
            have (dict) - Current information from the Cisco Catalyst Center
                          (global pool, reserve pool, network details)
            want (dict) - Users provided information from the playbook
            obj_params (list of tuples) - A list of parameter mappings specifying which
                                          Cisco Catalyst Center parameters (dnac_param)
                                          correspond to the user-provided
                                          parameters (ansible_param).

        Returns:
            bool - True if any parameter specified in obj_params differs between
            current_obj and requested_obj, indicating that an update is required.
            False if all specified parameters are equal.

        """

        current_obj = have
        requested_obj = want
        self.log("Current State (have): {0}".format(current_obj), "DEBUG")
        self.log("Desired State (want): {0}".format(requested_obj), "DEBUG")

        return any(not dnac_compare_equality(current_obj.get(dnac_param),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def get_obj_params(self, get_object):
        """
        Get the required comparison obj_params value

        Parameters:
            get_object (str) - identifier for the required obj_params

        Returns:
            obj_params (list) - obj_params value for comparison.
        """

        try:
            obj_params = []
            if get_object == "authenticationPolicyServer":
                obj_params = [
                    ("protocol", "protocol"),
                    ("retries", "retries"),
                    ("timeoutSeconds", "timeoutSeconds")
                ]
            else:
                raise ValueError("Received an unexpected value for 'get_object': {0}"
                                 .format(get_object))
        except Exception as msg:
            self.log("Received exception: {0}".format(msg), "CRITICAL")

        return obj_params

    def get_auth_server_params(self, auth_server_info):
        """
        Process Authentication and Policy Server params from playbook data for
        Authentication and Policy Server config in Cisco Catalyst Center.

        Parameters:
            auth_server_info (dict) - Cisco Catalyst Center data containing
            information about the Authentication and Policy Server.

        Returns:
            dict or None - Processed Authentication and Policy Server data in a format suitable
            for Cisco Catalyst Center configuration, or None if auth_server_info is empty.
        """

        if not auth_server_info:
            self.log("Authentication and Policy Server data is empty", "INFO")
            return None

        self.log("Authentication and Policy Server Details: {0}".format(auth_server_info), "DEBUG")
        auth_server = {
            "authenticationPort": auth_server_info.get("authenticationPort"),
            "accountingPort": auth_server_info.get("accountingPort"),
            "isIseEnabled": auth_server_info.get("iseEnabled"),
            "ipAddress": auth_server_info.get("ipAddress"),
            "pxgridEnabled": auth_server_info.get("pxgridEnabled"),
            "useDnacCertForPxgrid": auth_server_info.get("useDnacCertForPxgrid"),
            "port": auth_server_info.get("port"),
            "protocol": auth_server_info.get("protocol"),
            "retries": str(auth_server_info.get("retries")),
            "role": auth_server_info.get("role"),
            "timeoutSeconds": str(auth_server_info.get("timeoutSeconds")),
            "encryptionScheme": auth_server_info.get("encryptionScheme")
        }
        self.log("Formated Authentication and Policy Server details: {0}"
                 .format(auth_server), "DEBUG")
        if auth_server.get("isIseEnabled") is True:
            auth_server_ise_info = auth_server_info.get("ciscoIseDtos")
            auth_server.update({"ciscoIseDtos": []})
            for ise_credential in auth_server_ise_info:
                auth_server.get("ciscoIseDtos").append({
                    "userName": ise_credential.get("userName"),
                    "fqdn": ise_credential.get("fqdn"),
                    "ipAddress": ise_credential.get("ipAddress"),
                    "subscriberName": ise_credential.get("subscriberName"),
                    "description": ise_credential.get("description")
                })

        return auth_server

    def auth_server_exists(self, ipAddress):
        """
        Check if the Authentication and Policy Server with the given ipAddress exists

        Parameters:
            ipAddress (str) - The ipAddress of the Authentication and
                              Policy Server to check for existence.

        Returns:
            dict - A dictionary containing information about the
                   Authentication and Policy Server's existence:
            - 'exists' (bool): True if the Authentication and Policy Server exists, False otherwise.
            - 'id' (str or None): The ID of the Authentication and Policy Server if it exists
                                  or None if it doesn't.
            - 'details' (dict or None): Details of the Authentication and Policy Server if it exists
                                        else None.
        """

        AuthServer = {
            "exists": False,
            "details": None,
            "id": None
        }
        response = self.dnac._exec(
            family="system_settings",
            function='get_authentication_and_policy_servers',
        )
        if not isinstance(response, dict):
            self.log("Failed to retrieve the Authentication and Policy Server details - "
                     "Response is not a dictionary", "CRITICAL")
            return AuthServer

        all_auth_server_details = response.get("response")
        auth_server_details = get_dict_result(all_auth_server_details, "ipAddress", ipAddress)
        self.log("Authentication and Policy Server Ip Address: {0}"
                 .format(ipAddress), "DEBUG")
        self.log("Authentication and Policy Server details: {0}"
                 .format(auth_server_details), "DEBUG")
        if not auth_server_details:
            self.log("Global pool {0} does not exist".format(ipAddress), "INFO")
            return AuthServer

        AuthServer.update({"exists": True})
        AuthServer.update({"id": auth_server_details.get("instanceUuid")})
        AuthServer["details"] = self.get_auth_server_params(auth_server_details)

        self.log("Formatted Authenticaion and Policy Server details: {0}".format(AuthServer), "DEBUG")
        return AuthServer

    def get_have_authentication_policy_server(self, config):
        """
        Get the current Authentication and Policy Server information from
        Cisco Catalyst Center based on the provided playbook details.
        check this API using check_return_status.

        Parameters:
            config (dict) - Playbook details containing
            Authentication and Policy Server configuration.

        Returns:
            self - The current object with updated
            Authentication and Policy Server information.
        """

        AuthServer = {
            "exists": False,
            "details": None,
            "id": None
        }
        authentication_policy_server = config.get("authentication_policy_server")
        if authentication_policy_server is None:
            self.msg = "authentication_policy_server in config is missing in the playbook"
            self.status = "failed"
            return self

        ip_address = authentication_policy_server.get("server_ip_address")
        if ip_address is None:
            self.msg = "Missing parameter 'server_ip_address' is required."
            self.status = "failed"
            return self

        AuthServer = self.auth_server_exists(ip_address)
        self.log("Authentication and Policy Server exists: {0}"
                 .format(AuthServer.get("exists")), "DEBUG")
        self.log("Authentication and Policy Server details: {0}"
                 .format(AuthServer.get("details")), "DEBUG")
        self.log("Authentication and Policy Server Id: {0}"
                 .format(AuthServer.get("id")), "DEBUG")
        self.have.update({"authenticationPolicyServer": AuthServer})
        self.msg = "Collecting the Authentication and Policy Server " + \
                   "details from the Cisco Catalyst Center."
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current Authentication and Policy Server details from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing
            Authentication and Policy Server configuration.

        Returns:
            self - The current object with updated
            Authentication and Policy Server information.
        """

        if config.get("authentication_policy_server") is not None:
            self.get_have_authentication_policy_server(config).check_return_status()

        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.msg = "Successfully retrieved the details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_want_authentication_policy_server(self, auth_policy_server):
        """
        Get all the Authentication Policy Server information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            auth_policy_server (dict) - Playbook authentication policy server details
            containing IpAddress, authentication port, accounting port, Cisco ISE Details,
            protocol, retries, role, timeout seconds, encryption details.

        Returns:
            self - The current object with updated desired Authentication Policy Server information.
        """

        auth_server = {}
        auth_server_exists = self.have.get("authenticationPolicyServer").get("exists")
        auth_server_details = self.have.get("authenticationPolicyServer").get("details")
        trusted_server = False
        if not auth_server_exists:
            server_type = auth_policy_server.get("server_type")
            if server_type not in ["ISE", "AAA", None]:
                self.msg = "The server_type should either be ISE or AAA but not {0}.".format(server_type)
                self.status = "failed"
                return self

            if server_type == "ISE":
                auth_server.update({"isIseEnabled": True})
            else:
                auth_server.update({"isIseEnabled": False})
        else:
            auth_server.update({"isIseEnabled": auth_server_details.get("isIseEnabled")})

        auth_server.update({"ipAddress": auth_policy_server.get("server_ip_address")})

        auth_server_exists = self.have.get("authenticationPolicyServer").get("exists")

        if not auth_server_exists:
            shared_secret = auth_policy_server.get("shared_secret")
            if not shared_secret:
                self.msg = "Missing parameter 'shared_secret' is required."
                self.status = "failed"
                return self

            shared_secret = str(shared_secret)
            if len(shared_secret) < 4 or len(shared_secret) > 100:
                self.msg = "The 'shared_secret' should contain between 4 and 100 characters."
                self.status = "failed"
                return self

            invalid_chars = " ?<"
            for char in invalid_chars:
                if char in shared_secret:
                    self.msg = "The 'shared_secret' should not contain spaces or the characters '?', '<'."
                    self.status = "failed"
                    return self

            auth_server.update({"sharedSecret": shared_secret})

        protocol = auth_policy_server.get("protocol")
        if protocol not in ["RADIUS", "TACACS", "RADIUS_TACACS", None]:
            self.msg = "protocol should either be ['RADIUS', 'TACACS', 'RADIUS_TACACS']." + \
                       "It should not be {0}".format(protocol)
            self.status = "failed"
            return self

        if protocol is not None:
            auth_server.update({"protocol": protocol})
        else:
            if not auth_server_exists:
                auth_server.update({"protocol": "RADIUS"})
            else:
                auth_server.update({"protocol": auth_server_details.get("protocol")})

        auth_server.update({"port": 49})

        if not auth_server_exists:
            encryption_scheme = auth_policy_server.get("encryption_scheme")
            if encryption_scheme not in ["KEYWRAP", "RADSEC", None]:
                self.msg = "The encryption_scheme should be in ['KEYWRAP', 'RADSEC']. " + \
                           "It should not be {0}.".format(encryption_scheme)
                self.status = "failed"
                return self

            if encryption_scheme:
                auth_server.update({"encryptionScheme": encryption_scheme})

            if encryption_scheme == "KEYWRAP":
                message_key = auth_policy_server.get("message_authenticator_code_key")
                if not message_key:
                    self.msg = "The 'message_authenticator_code_key' should not be empty if the encryption_scheme is 'KEYWRAP'."
                    self.status = "failed"
                    return self

                message_key = str(message_key)
                message_key_length = len(message_key)
                if message_key_length != 20:
                    self.msg = "The 'message_authenticator_code_key' should be exactly 20 characters."
                    self.status = "failed"
                    return self

                auth_server.update({"messageKey": message_key})

                encryption_key = auth_policy_server.get("encryption_key")
                if not encryption_key:
                    self.msg = "The encryption_key should not be empty if encryption_scheme is 'KEYWRAP'."
                    self.status = "failed"
                    return self

                encryption_key = str(encryption_key)
                encryption_key_length = len(encryption_key)
                if encryption_key_length != 16:
                    self.msg = "The 'encryption_key' must be 16 characters long. It may contain alphanumeric and special characters."
                    self.status = "failed"
                    return self

                auth_server.update({"encryptionKey": encryption_key})

        if not auth_server_exists:
            authentication_port = auth_policy_server.get("authentication_port")
            if not authentication_port:
                authentication_port = 1812

            if not str(authentication_port).isdigit():
                self.msg = "The 'authentication_port' should contain only digits."
                self.status = "failed"
                return self

            if authentication_port < 1 or authentication_port > 65535:
                self.msg = "The 'authentication_port' should be from 1 to 65535."
                self.status = "failed"
                return self

            auth_server.update({"authenticationPort": authentication_port})
        else:
            auth_server.update({"authenticationPort": auth_server_details.get("authenticationPort")})

        if not auth_server_exists:
            accounting_port = auth_policy_server.get("accounting_port")
            if not accounting_port:
                accounting_port = 1813

            if not str(accounting_port).isdigit():
                self.msg = "The 'accounting_port' should contain only digits."
                self.status = "failed"
                return self

            if accounting_port < 1 or accounting_port > 65535:
                self.msg = "The 'accounting_port' should be from 1 to 65535."
                self.status = "failed"
                return self

            auth_server.update({"accountingPort": accounting_port})
        else:
            auth_server.update({"accountingPort": auth_server_details.get("accountingPort")})

        retries = auth_policy_server.get("retries")
        if not retries:
            if not auth_server_exists:
                auth_server.update({"retries": "3"})
            else:
                auth_server.update({"retries": auth_server_details.get("retries")})
        else:
            try:
                retries_int = int(retries)
                if retries_int < 1 or retries_int > 3:
                    self.msg = "The 'retries' should be from 1 to 3."
                    self.status = "failed"
                    return self
            except ValueError:
                self.msg = "The 'retries' should contain only from 0-9."
                self.status = "failed"
                return self

            auth_server.update({"retries": str(retries)})

        timeout = auth_policy_server.get("timeout")
        if not auth_server_exists:
            default_timeout = "4"
        else:
            default_timeout = str(auth_server_details.get("timeoutSeconds"))

        # If 'timeout' is not provided, use 'default_timeout'
        if timeout is None:
            auth_server.update({"timeoutSeconds": default_timeout})
        else:
            try:
                timeout_int = int(timeout)
                if timeout_int < 2 or timeout_int > 20:
                    self.msg = "The 'timeout' should be from 2 to 20."
                    self.status = "failed"
                    return self

                auth_server.update({"timeoutSeconds": str(timeout)})
            except ValueError:
                self.msg = "The 'time_out' must contain only digits."
                self.status = "failed"
                return self

        # Determine the role based on whether the auth server exists and if the role is specified
        if not auth_server_exists:
            # Use the role from 'auth_policy_server' if available, otherwise default to "secondary"
            role = auth_policy_server.get("role", "secondary")
        else:
            # Use the role from 'auth_server_details'
            role = auth_server_details.get("role")

        auth_server.update({"role": role})

        if auth_server.get("isIseEnabled"):
            cisco_ise_dtos = auth_policy_server.get("cisco_ise_dtos")
            if not cisco_ise_dtos:
                self.msg = "Missing parameter 'cisco_ise_dtos' " + \
                           "required when server_type is 'ISE'."
                self.status = "failed"
                return self

            auth_server.update({"ciscoIseDtos": []})
            position_ise_creds = 0
            for ise_credential in cisco_ise_dtos:
                auth_server.get("ciscoIseDtos").append({})
                user_name = ise_credential.get("user_name")
                if not user_name:
                    if not auth_server_exists:
                        self.msg = "Missing parameter 'user_name' is required when server_type is ISE."
                        self.status = "failed"
                        return self

                    user_name = auth_server_details.get("ciscoIseDtos")[0].get("userName")

                auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                    "userName": user_name
                })

                password = ise_credential.get("password")
                if not password:
                    self.msg = "Missing parameter 'password' is required when server_type is ISE."
                    self.status = "failed"
                    return self

                if not 4 <= len(password) <= 127:
                    self.msg = ""
                    self.status = "failed"
                    return self

                auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                    "password": password
                })

                fqdn = ise_credential.get("fqdn")
                if not fqdn:
                    if not auth_server_exists:
                        self.msg = "Missing parameter 'fqdn' is required when server_type is ISE."
                        self.status = "failed"
                        return self

                    fqdn = auth_server_details.get("ciscoIseDtos")[0].get("fqdn")

                auth_server.get("ciscoIseDtos")[position_ise_creds].update({"fqdn": fqdn})

                ip_address = ise_credential.get("ip_address")
                if not ip_address:
                    self.msg = "Missing parameter 'ip_address' is required when server_type is ISE."
                    self.status = "failed"
                    return self

                auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                    "ipAddress": ip_address
                })

                if not auth_server_exists:
                    auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                        "subscriberName": "ersadmin"
                    })
                else:
                    auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                        "subscriberName": auth_server_details.get("ciscoIseDtos")[0].get("subscriberName")
                    })

                description = ise_credential.get("description")
                if description:
                    auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                        "description": description
                    })

                ssh_key = ise_credential.get("ssh_key")
                if ssh_key:
                    auth_server.get("ciscoIseDtos")[position_ise_creds].update({
                        "sshkey": str(ssh_key)
                    })

                position_ise_creds += 1

            pxgrid_enabled = auth_policy_server.get("pxgrid_enabled")
            if pxgrid_enabled is None:
                if auth_server_exists:
                    pxgrid_enabled = auth_server_details.get("pxgridEnabled")
                else:
                    pxgrid_enabled = True

            auth_server.update({"pxgridEnabled": pxgrid_enabled})

            use_dnac_cert_for_pxgrid = auth_policy_server.get("use_dnac_cert_for_pxgrid")
            if use_dnac_cert_for_pxgrid is None:
                if auth_server_exists:
                    use_dnac_cert_for_pxgrid = auth_server_details.get("useDnacCertForPxgrid")
                else:
                    use_dnac_cert_for_pxgrid = False

            auth_server.update({"useDnacCertForPxgrid": use_dnac_cert_for_pxgrid})

            external_cisco_ise_ip_addr_dtos = auth_policy_server \
                .get("external_cisco_ise_ip_addr_dtos")
            if external_cisco_ise_ip_addr_dtos:
                auth_server.update({"externalCiscoIseIpAddrDtos": []})
                position_ise_addresses = 0
                for external_cisco_ise in external_cisco_ise_ip_addr_dtos:
                    external_cisco_ise_ip_addresses = external_cisco_ise \
                        .get("external_cisco_ise_ip_addresses")
                    if external_cisco_ise_ip_addresses:
                        auth_server.get("externalCiscoIseIpAddrDtos").append({})
                        auth_server.get("externalCiscoIseIpAddrDtos")[position_ise_addresses] \
                            .update({"externalCiscoIseIpAddresses": []})
                        position_ise_address = 0
                        for external_ip_address in external_cisco_ise_ip_addresses:
                            auth_server.get("externalCiscoIseIpAddrDtos")[position_ise_addresses] \
                                .get("externalCiscoIseIpAddresses").append({})
                            auth_server.get("externalCiscoIseIpAddrDtos")[position_ise_addresses] \
                                .get("externalCiscoIseIpAddresses")[position_ise_address].update({
                                    "externalIpAddress": external_ip_address.get("external_ip_address")
                                })
                            position_ise_address += 1
                    ise_type = external_cisco_ise.get("ise_type")
                    if ise_type:
                        auth_server.get("externalCiscoIseIpAddrDtos")[position_ise_addresses] \
                            .update({"type": ise_type})
                    position_ise_addresses += 1

            trusted_server = auth_policy_server.get("trusted_server")
            if auth_policy_server.get("trusted_server") is None:
                trusted_server = True
            else:
                trusted_server = auth_policy_server.get("trusted_server")

            self.want.update({"trusted_server": trusted_server})

            ise_integration_wait_time = auth_policy_server.get("ise_integration_wait_time")
            if ise_integration_wait_time is None:
                ise_integration_wait_time = 20
            else:
                try:
                    ise_integration_wait_time_int = int(ise_integration_wait_time)
                    if ise_integration_wait_time_int < 1 or ise_integration_wait_time_int > 120:
                        self.msg = "The ise_integration_wait_time should be from 1 to 120 seconds."
                        self.status = "failed"
                        return self

                except ValueError:
                    self.msg = "The 'ise_integration_wait_time' should contain only digits."
                    self.status = "failed"
                    return self

            self.want.update({"ise_integration_wait_time": ise_integration_wait_time})

        self.log("Authentication and Policy Server playbook details: {0}"
                 .format(auth_server), "DEBUG")
        self.want.update({"authenticationPolicyServer": auth_server})
        self.msg = "Collecting the Authentication and Policy Server details from the playbook"
        self.status = "success"
        return self

    def get_want(self, config):
        """
        Get all the Authentication Policy Server related information from playbook

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            None
        """

        if config.get("authentication_policy_server"):
            auth_policy_server = config.get("authentication_policy_server")
            self.get_want_authentication_policy_server(auth_policy_server).check_return_status()

        self.log("Desired State (want): {0}".format(self.want), "INFO")
        self.msg = "Successfully retrieved details from the playbook"
        self.status = "success"
        return self

    def accept_cisco_ise_server_certificate(self, ipAddress, trusted_server):
        """
        Accept the Cisco ISE server certificate in Cisco Catalyst
        Center provided in the playbook.

        Parameters:
            ipAddress (str) - The Ip address of the Authentication and Policy Server to be deleted.
            trusted_server (bool) - Indicates whether the certificate is trustworthy for the server.

        Returns:
            None
        """

        try:
            AuthServer = self.auth_server_exists(ipAddress)
            if not AuthServer:
                self.msg = "Error while retrieving the Authentication and Policy Server {0} \
                            details.".format(ipAddress)
                self.log(str(self.msg, "CRITICAL"))
                self.status = "failed"
                return self

            cisco_ise_id = AuthServer.get("id")
            if not cisco_ise_id:
                self.msg = "Error while retrieving the Authentication and Policy Server {0} id." \
                           .format(ipAddress)
                self.log(str(self.msg, "CRITICAL"))
                self.status = "failed"
                return self

            response = self.dnac._exec(
                family="system_settings",
                function="accept_cisco_ise_server_certificate_for_cisco_ise_server_integration",
                params={
                    "id": cisco_ise_id,
                    "isCertAcceptedByUser": trusted_server
                },
            )
            self.log("Received API response for 'accept_cisco_ise_server_certificate_"
                     "for_cisco_ise_server_integration': {0}".format(response), "DEBUG")
        except Exception as msg:
            self.log("Exception occurred while accepting the certificate of {0}: {1}"
                     .format(ipAddress, msg))
            return None
        return

    def check_auth_server_response_status(self, response, validation_string_set, api_name):
        """
        Checks the status of a task related to updating the authentication and policy server
        by polling the task details until it completes or a timeout is reached.

        Parameters:
            response (dict): The initial response from the task creation API.
            validation_string_set (set): A set of strings expected to be found in the task progress for a successful operation.
            api_name (str): Name of the function during the SDK call.

        Returns:
            self - The current object with updated desired Authentication Policy Server information.
        """

        response = response.get("response")
        if response.get("errorcode") is not None:
            self.msg = response.get("detail")
            self.status = "failed"
            return self

        task_id = response.get("taskId")
        start_time = time.time()
        sleep_time = self.max_timeout / 1000
        while True:
            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = "Max timeout of {0} sec has reached for the execution id '{1}'.".format(self.max_timeout, task_id) + \
                           "Exiting the loop due to unexpected API '{0}' status.".format(api_name)
                self.status = "failed"
                break

            task_details = self.get_task_details(task_id)
            self.log('Getting task details from task ID {0}: {1}'.format(task_id, task_details), "DEBUG")
            if task_details.get("isError") is True:
                failure_reason = task_details.get("failureReason")
                if failure_reason:
                    self.msg = str(failure_reason)
                else:
                    self.msg = str(task_details.get("progress"))
                self.status = "failed"
                break

            for validation_string in validation_string_set:
                if validation_string in task_details.get("progress").lower():
                    self.result['changed'] = True
                    self.validation_string = validation_string
                    self.status = "success"
                    break

            if self.result['changed'] is True:
                self.log("The task with task id '{0}' is successfully executed".format(task_id), "DEBUG")
                break

            # sleep time after checking the status of the response from the API
            self.log("The time interval before checking the next response, sleep for {0}".format(sleep_time))
            time.sleep(sleep_time)
            self.log("Progress set to {0} for taskid: {1}".format(task_details.get('progress'), task_id), "DEBUG")

        return self

    def format_payload_for_update(self, have_auth_server, want_auth_server):
        """
        Format the parameter of the payload for updating the authentication and policy server
        in accordance with the information in the Cisco Catalyst Ceter.

        Parameters:
            have_auth_server (dict) - Authentication and policy server information from the Cisco Catalyst Center.
            want_auth_server (dict) - Authentication and policy server information from the Playbook.

        Returns:
            self - The current object with updated desired Authentication Policy Server information.
        """

        update_params = ["authenticationPort", "accountingPort", "role"]
        for item in update_params:
            have_auth_server_item = have_auth_server.get(item)
            want_auth_server_item = want_auth_server.get(item)
            if want_auth_server_item is None:
                want_auth_server.update({item: have_auth_server_item})

            elif have_auth_server_item != want_auth_server_item:
                self.msg = "Update does not support modifying '{0}'. Here you are trying to update '{1}'." \
                           .format(update_params, item)
                self.status = "failed"
                return self

        have_auth_server_protocol = have_auth_server.get("protocol")
        want_auth_server_protocol = want_auth_server.get("protocol")
        if have_auth_server_protocol != want_auth_server_protocol:
            if want_auth_server_protocol != "RADIUS_TACACS":
                self.msg = "'protocol' can only be updated to 'RADIUS_TACACS' not from '{0}' to '{1}'" \
                           .format(have_auth_server_protocol, want_auth_server_protocol)
                self.status = "failed"
                return self

        self.log("Successfully formatted the parameter of the payload for updating the authentication and policy server.")
        self.msg = "Successfully formatted the parameter of the payload for updating the authentication and policy server."
        self.status = "success"
        return self

    def update_auth_policy_server(self, ipAddress):
        """
        Update/Create Authentication and Policy Server in Cisco
        Catalyst Center with fields provided in playbook.

        Parameters:
            ipAddress (str) - The Ip address of the Authentication and Policy Server to be deleted.

        Returns:
            None
        """

        result_auth_server = self.result.get("response")[0].get("authenticationPolicyServer")
        result_auth_server.get("response").update({ipAddress: {}})

        # Check Authentication and Policy Server exist, if not create and return
        is_ise_server = self.want.get("authenticationPolicyServer").get("isIseEnabled")
        if not self.have.get("authenticationPolicyServer").get("exists"):
            auth_server_params = self.want.get("authenticationPolicyServer")
            self.log("Desired State for Authentication and Policy Server (want): {0}"
                     .format(auth_server_params), "DEBUG")
            function_name = "add_authentication_and_policy_server_access_configuration"
            response = self.dnac._exec(
                family="system_settings",
                function=function_name,
                params=auth_server_params,
            )
            validation_string_set = ("successfully created aaa settings", "operation sucessful")
            self.check_auth_server_response_status(response, validation_string_set, function_name)
            if self.status == "failed":
                self.log(self.msg, "ERROR")
                return

            if is_ise_server and self.validation_string == "operation sucessful":
                trusted_server = self.want.get("trusted_server")
                self.accept_cisco_ise_server_certificate(ipAddress, trusted_server)
                ise_integration_wait_time = self.want.get("ise_integration_wait_time")
                time.sleep(ise_integration_wait_time)
                response = self.dnac._exec(
                    family="system_settings",
                    function='get_authentication_and_policy_servers',
                    params={"is_ise_enabled": True}
                )
                response = response.get("response")
                if response is None:
                    self.msg = "Failed to retrieve the information from the API 'get_authentication_and_policy_servers' of {0}." \
                               .format(ipAddress)
                    self.status = "failed"
                    return

                ise_server_details = get_dict_result(response, "ipAddress", ipAddress)
                ise_state_set = {"FAILED", "INPROGRESS"}
                state = ise_server_details.get("state")
                if state in ise_state_set:
                    if state == "INPROGRESS":
                        self.msg = "The Cisco ISE server '{ip}' integration is incomplete, currently in 'INPROGRESS' state. ".format(ip=ipAddress) + \
                                   "The integration has exceeded the expected duration of '{wait_time}' second(s)." \
                                   .format(wait_time=ise_integration_wait_time)
                    elif state == "FAILED":
                        self.msg = "The Cisco ISE server '{ip}' integration has failed and in 'FAILED' state." \
                                   .format(ip=ipAddress)
                        if self.want.get("trusted_server") is False:
                            self.msg += " This is the first time Cisco Catalyst Center has encountered " + \
                                        "this certificate from Cisco ISE, and it is not yet trusted."

                    self.log(str(self.msg), "ERROR")
                    self.status = "failed"
                    return

            self.log("Successfully created Authentication and Policy Server '{0}'."
                     .format(ipAddress), "INFO")
            result_auth_server.get("response").get(ipAddress) \
                .update({
                    "authenticationPolicyServer Details": self.want
                        .get("authenticationPolicyServer")
                        })
            result_auth_server.get("msg").update({
                ipAddress: "Authentication and Policy Server Created Successfully"
            })
            return

        # Authentication and Policy Server exists, check update is required
        # Edit API not working, remove this
        self.format_payload_for_update(self.have.get("authenticationPolicyServer").get("details"),
                                       self.want.get("authenticationPolicyServer")).check_return_status()
        is_ise_server_enabled = self.have.get("authenticationPolicyServer").get("details").get("isIseEnabled")
        if not (is_ise_server_enabled or self.requires_update(self.have.get("authenticationPolicyServer").get("details"),
                                                              self.want.get("authenticationPolicyServer"),
                                                              self.authentication_policy_server_obj_params)):
            self.log("Authentication and Policy Server '{0}' doesn't require an update"
                     .format(ipAddress), "INFO")
            result_auth_server.get("response").get(ipAddress).update({
                "Cisco Catalyst Center params":
                self.have.get("authenticationPolicyServer").get("details")
            })
            result_auth_server.get("response").get(ipAddress).update({
                "Id": self.have.get("authenticationPolicyServer").get("id")
            })
            result_auth_server.get("msg").update({
                ipAddress: "Authentication and Policy Server doesn't require an update"
            })
            return

        self.log("Authentication and Policy Server requires update", "DEBUG")

        # Authenticaiton and Policy Server Exists
        auth_server_params = copy.deepcopy(self.want.get("authenticationPolicyServer"))
        auth_server_params.update({"id": self.have.get("authenticationPolicyServer").get("id")})
        self.log("Desired State for Authentication and Policy Server (want): {0}"
                 .format(auth_server_params), "DEBUG")
        self.log("Current State for Authentication and Policy Server (have): {0}"
                 .format(self.have.get("authenticationPolicyServer").get("details")), "DEBUG")
        function_name = "edit_authentication_and_policy_server_access_configuration"
        response = self.dnac._exec(
            family="system_settings",
            function=function_name,
            params=auth_server_params,
        )
        validation_string_set = ("successfully updated aaa settings", "operation sucessful")
        self.check_auth_server_response_status(response, validation_string_set, function_name)
        if self.status == "failed":
            self.log(self.msg, "ERROR")
            return

        self.log("Authentication and Policy Server '{0}' updated successfully"
                 .format(ipAddress), "INFO")
        result_auth_server.get("response").get(ipAddress) \
            .update({"Id": self.have.get("authenticationPolicyServer").get("id")})
        result_auth_server.get("msg").update({
            ipAddress: "Authentication and Policy Server Updated Successfully"
        })
        return

    def get_diff_merged(self, config):
        """
        Update or create Authentication and Policy Server in
        Cisco Catalyst Center based on the playbook details.

        Parameters:
            config (list of dict) - Playbook details containing
            Authentication and Policy Server information.

        Returns:
            self
        """

        if config.get("authentication_policy_server") is not None:
            ipAddress = config.get("authentication_policy_server").get("server_ip_address")
            self.update_auth_policy_server(ipAddress)

        return self

    def delete_auth_policy_server(self, ipAddress):
        """
        Delete a Authentication and Policy Server by server Ip address in Cisco Catalyst Center.

        Parameters:
            ipAddress (str) - The Ip address of the Authentication and Policy Server to be deleted.

        Returns:
            self
        """

        auth_server_exists = self.have.get("authenticationPolicyServer").get("exists")
        result_auth_server = self.result.get("response")[0].get("authenticationPolicyServer")
        if not auth_server_exists:
            result_auth_server.get("response").update({
                ipAddress: "Authentication and Policy Server not found"
            })
            self.msg = "Authentication and Policy Server not found."
            self.status = "success"
            return self

        response = self.dnac._exec(
            family="system_settings",
            function="delete_authentication_and_policy_server_access_configuration",
            params={"id": self.have.get("authenticationPolicyServer").get("id")},
        )

        self.log("Received API response for 'delete_authentication_and_"
                 "policy_server_access_configuration': {0}".format(response), "DEBUG")

        # Check the task status
        validation_string = "successfully deleted aaa settings"
        self.check_task_response_status(response, validation_string, "delete_authentication_and_policy_server_access_configuration").check_return_status()
        taskid = response.get("response").get("taskId")

        # Update result information
        result_auth_server.get("response").update({ipAddress: {}})
        result_auth_server.get("response").get(ipAddress).update({"Task Id": taskid})
        result_auth_server.get("msg").update({
            ipAddress: "Authentication and Policy Server deleted successfully."
        })
        self.msg = "Authentication and Policy Server - {0} deleted successfully.".format(ipAddress)
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """
        Delete Authentication and Policy Server from the Cisco Catalyst Center.

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            self
        """

        if config.get("authentication_policy_server") is not None:
            ipAddress = config.get("authentication_policy_server").get("server_ip_address")
            self.delete_auth_policy_server(ipAddress).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing
            Authentication and Policy Server configuration.

        Returns:
            self
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Requested State (want): {0}".format(self.want), "INFO")
        if config.get("authentication_policy_server") is not None:
            self.log("Desired State of Authentication and Policy Server (want): {0}"
                     .format(self.want.get("authenticationPolicyServer")), "DEBUG")
            self.log("Current State of Authentication and Policy Server (have): {0}"
                     .format(self.have.get("authenticationPolicyServer")
                             .get("details")), "DEBUG")
            check_list = ["isIseEnabled", "ipAddress", "pxgridEnabled",
                          "useDnacCertForPxgrid", "port", "protocol",
                          "retries", "role", "timeoutSeconds", "encryptionScheme"]
            auth_server_have = self.have.get("authenticationPolicyServer").get("details")
            auth_server_want = self.want.get("authenticationPolicyServer")
            for item in check_list:
                if auth_server_have.get(item) and auth_server_want.get(item) and \
                        auth_server_have.get(item) != auth_server_want.get(item):
                    self.msg = "Authentication and Policy Server " + \
                               "Config is not applied to the Cisco Catalyst Center."
                    self.status = "failed"
                    return self

            self.log("Successfully validated Authentication and Policy Server '{0}'."
                     .format(self.want.get("authenticationPolicyServer").get("ipAddress")), "INFO")
            self.result.get("response")[0].get("authenticationPolicyServer").update({
                "Validation": "Success"
            })

        self.msg = "Successfully validated the Authentication and Policy Server."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict) - Playbook details containing
            Authentication and Policy Server configuration.

        Returns:
            self
        """

        self.get_have(config)
        ipAddress = config.get("authentication_policy_server").get("server_ip_address")
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Authentication and Policy Server deleted from the Cisco Catalyst Center: {0}"
                 .format(ipAddress), "INFO")
        if config.get("authentication_policy_server") is not None:
            auth_server_exists = self.have.get("authenticationPolicyServer").get("exists")
            if auth_server_exists:
                self.msg = "Authentication and Policy Server " + \
                           "Config is not applied to the Cisco Catalyst Center."
                self.status = "failed"
                return self

            self.log("Successfully validated absence of Authentication and Policy Server '{0}'."
                     .format(config.get("authentication_policy_server").get("ip_address")), "INFO")
            self.result.get("response")[0].get("authenticationPolicyServer").update({
                "Validation": "Success"
            })

        self.msg = "Successfully validated the absence of Authentication and Policy Server."
        self.status = "success"
        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values

        Parameters:
            None

        Returns:
            None
        """

        self.have.clear()
        self.want.clear()
        return


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": 'True'},
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        'dnac_api_task_timeout': {'type': 'int', "default": 1200},
        'dnac_task_poll_interval': {'type': 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_ise_radius = IseRadiusIntegration(module)
    state = ccc_ise_radius.params.get("state")
    config_verify = ccc_ise_radius.params.get("config_verify")
    if state not in ccc_ise_radius.supported_states:
        ccc_ise_radius.status = "invalid"
        ccc_ise_radius.msg = "State {0} is invalid".format(state)
        ccc_ise_radius.check_return_status()

    ccc_ise_radius.validate_input().check_return_status()

    for config in ccc_ise_radius.config:
        ccc_ise_radius.reset_values()
        ccc_ise_radius.get_have(config).check_return_status()
        if state != "deleted":
            ccc_ise_radius.get_want(config).check_return_status()
        ccc_ise_radius.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_ise_radius.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_ise_radius.result)


if __name__ == "__main__":
    main()
