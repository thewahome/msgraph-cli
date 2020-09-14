# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['userspeople'] = """
    type: group
    short-summary: userspeople
"""

helps['userspeople create-person'] = """
    type: command
    short-summary: "Create new navigation property to people for users"
    parameters:
      - name: --email-addresses
        long-summary: |
            Usage: --email-addresses address=XX rank=XX


            Multiple actions can be specified by using more than one --email-addresses argument.
      - name: --phones
        short-summary: "The person's phone numbers."
        long-summary: |
            Usage: --phones type=XX number=XX

            number: The phone number.

            Multiple actions can be specified by using more than one --phones argument.
      - name: --websites
        short-summary: "The person's websites."
        long-summary: |
            Usage: --websites type=XX address=XX display-name=XX

            address: The URL of the website.
            display-name: The display name of the web site.

            Multiple actions can be specified by using more than one --websites argument.
      - name: --sources
        long-summary: |
            Usage: --sources type=XX


            Multiple actions can be specified by using more than one --sources argument.
"""

helps['userspeople get-person'] = """
    type: command
    short-summary: "Get people from users"
"""

helps['userspeople list-person'] = """
    type: command
    short-summary: "Get people from users"
"""

helps['userspeople update-person'] = """
    type: command
    short-summary: "Update the navigation property people in users"
    parameters:
      - name: --email-addresses
        long-summary: |
            Usage: --email-addresses address=XX rank=XX


            Multiple actions can be specified by using more than one --email-addresses argument.
      - name: --phones
        short-summary: "The person's phone numbers."
        long-summary: |
            Usage: --phones type=XX number=XX

            number: The phone number.

            Multiple actions can be specified by using more than one --phones argument.
      - name: --websites
        short-summary: "The person's websites."
        long-summary: |
            Usage: --websites type=XX address=XX display-name=XX

            address: The URL of the website.
            display-name: The display name of the web site.

            Multiple actions can be specified by using more than one --websites argument.
      - name: --sources
        long-summary: |
            Usage: --sources type=XX


            Multiple actions can be specified by using more than one --sources argument.
"""
