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


helps['crossdeviceexperiences'] = """
    type: group
    short-summary: crossdeviceexperiences
"""

helps['crossdeviceexperiences delete'] = """
    type: command
    short-summary: "Delete navigation property activities for users"
"""

helps['crossdeviceexperiences create-activity'] = """
    type: command
    short-summary: "Create new navigation property to activities for users"
    parameters:
      - name: --visual-elements-attribution
        short-summary: "imageInfo"
        long-summary: |
            Usage: --visual-elements-attribution add-image-query=XX alternate-text=XX alternative-text=XX icon-url=XX

            add-image-query: Optional; parameter used to indicate the server is able to render image dynamically in \
response to parameterization. For example – a high contrast image
            alternate-text: Optional; alt-text accessible content for the image
            icon-url: Optional; URI that points to an icon which represents the application used to generate the \
activity
"""

helps['crossdeviceexperiences get-activity'] = """
    type: command
    short-summary: "Get activities from users"
"""

helps['crossdeviceexperiences list-activity'] = """
    type: command
    short-summary: "Get activities from users"
"""

helps['crossdeviceexperiences update-activity'] = """
    type: command
    short-summary: "Update the navigation property activities in users"
    parameters:
      - name: --visual-elements-attribution
        short-summary: "imageInfo"
        long-summary: |
            Usage: --visual-elements-attribution add-image-query=XX alternate-text=XX alternative-text=XX icon-url=XX

            add-image-query: Optional; parameter used to indicate the server is able to render image dynamically in \
response to parameterization. For example – a high contrast image
            alternate-text: Optional; alt-text accessible content for the image
            icon-url: Optional; URI that points to an icon which represents the application used to generate the \
activity
"""

helps['crossdeviceexperiences'] = """
    type: group
    short-summary: crossdeviceexperiences
"""

helps['crossdeviceexperiences delete'] = """
    type: command
    short-summary: "Delete navigation property historyItems for users"
"""

helps['crossdeviceexperiences create-history-item'] = """
    type: command
    short-summary: "Create new navigation property to historyItems for users"
"""

helps['crossdeviceexperiences get-history-item'] = """
    type: command
    short-summary: "Get historyItems from users"
"""

helps['crossdeviceexperiences list-history-item'] = """
    type: command
    short-summary: "Get historyItems from users"
"""

helps['crossdeviceexperiences update-history-item'] = """
    type: command
    short-summary: "Update the navigation property historyItems in users"
"""

helps['crossdeviceexperiences'] = """
    type: group
    short-summary: crossdeviceexperiences
"""

helps['crossdeviceexperiences delete'] = """
    type: command
    short-summary: "Delete ref of navigation property activity for users"
"""

helps['crossdeviceexperiences get-activity'] = """
    type: command
    short-summary: "Get activity from users"
"""

helps['crossdeviceexperiences get-ref-activity'] = """
    type: command
    short-summary: "Get ref of activity from users"
"""

helps['crossdeviceexperiences set-ref-activity'] = """
    type: command
    short-summary: "Update the ref of navigation property activity in users"
"""
