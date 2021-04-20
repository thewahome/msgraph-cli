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


helps['people_v1_0'] = '''
    type: group
    short-summary: Manage People
'''

helps['people user'] = """
    type: group
    short-summary: Manage user with people_v1_0
"""

helps['people user create-person'] = """
    type: command
    short-summary: "Create new navigation property to people for users."
    parameters:
      - name: --person-type
        short-summary: "personType"
        long-summary: |
            Usage: --person-type class=XX subclass=XX

            class: The type of data source, such as Person.
            subclass: The secondary type of data source, such as OrganizationUser.
      - name: --phones
        short-summary: "The person's phone numbers."
        long-summary: |
            Usage: --phones language=XX number=XX region=XX type=XX

            number: The phone number.

            Multiple actions can be specified by using more than one --phones argument.
      - name: --scored-email-addresses
        short-summary: "The person's email addresses."
        long-summary: |
            Usage: --scored-email-addresses address=XX item-id=XX relevance-score=XX selection-likelihood=XX

            address: The email address.
            relevance-score: The relevance score of the email address. A relevance score is used as a sort key, in \
relation to the other returned results. A higher relevance score value corresponds to a more relevant result. \
Relevance is determined by the user’s communication and collaboration patterns and business relationships.

            Multiple actions can be specified by using more than one --scored-email-addresses argument.
      - name: --websites
        short-summary: "The person's websites."
        long-summary: |
            Usage: --websites address=XX display-name=XX type=XX

            address: The URL of the website.
            display-name: The display name of the web site.

            Multiple actions can be specified by using more than one --websites argument.
"""

helps['people user delete-insight'] = """
    type: command
    short-summary: "Delete navigation property insights for users."
"""

helps['people user delete-person'] = """
    type: command
    short-summary: "Delete navigation property people for users."
"""

helps['people user list-person'] = """
    type: command
    short-summary: "Get people from users."
"""

helps['people user show-insight'] = """
    type: command
    short-summary: "Get insights from users."
"""

helps['people user show-person'] = """
    type: command
    short-summary: "Get people from users."
"""

helps['people user update-insight'] = """
    type: command
    short-summary: "Update the navigation property insights in users."
"""

helps['people user update-person'] = """
    type: command
    short-summary: "Update the navigation property people in users."
    parameters:
      - name: --person-type
        short-summary: "personType"
        long-summary: |
            Usage: --person-type class=XX subclass=XX

            class: The type of data source, such as Person.
            subclass: The secondary type of data source, such as OrganizationUser.
      - name: --phones
        short-summary: "The person's phone numbers."
        long-summary: |
            Usage: --phones language=XX number=XX region=XX type=XX

            number: The phone number.

            Multiple actions can be specified by using more than one --phones argument.
      - name: --scored-email-addresses
        short-summary: "The person's email addresses."
        long-summary: |
            Usage: --scored-email-addresses address=XX item-id=XX relevance-score=XX selection-likelihood=XX

            address: The email address.
            relevance-score: The relevance score of the email address. A relevance score is used as a sort key, in \
relation to the other returned results. A higher relevance score value corresponds to a more relevant result. \
Relevance is determined by the user’s communication and collaboration patterns and business relationships.

            Multiple actions can be specified by using more than one --scored-email-addresses argument.
      - name: --websites
        short-summary: "The person's websites."
        long-summary: |
            Usage: --websites address=XX display-name=XX type=XX

            address: The URL of the website.
            display-name: The display name of the web site.

            Multiple actions can be specified by using more than one --websites argument.
"""

helps['people usersinsight'] = """
    type: group
    short-summary: Manage usersinsight with people_v1_0
"""

helps['people usersinsight create-shared'] = """
    type: command
    short-summary: "Create new navigation property to shared for users."
    parameters:
      - name: --resource-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --resource-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
      - name: --resource-visualization
        short-summary: "resourceVisualization"
        long-summary: |
            Usage: --resource-visualization container-display-name=XX container-type=XX container-web-url=XX \
media-type=XX preview-image-url=XX preview-text=XX title=XX type=XX

            container-display-name: A string describing where the item is stored. For example, the name of a \
SharePoint site or the user name identifying the owner of the OneDrive storing the item.
            container-type: Can be used for filtering by the type of container in which the file is stored. Such as \
Site or OneDriveBusiness.
            container-web-url: A path leading to the folder in which the item is stored.
            media-type: The item's media type. Can be used for filtering for a specific type of file based on \
supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
            preview-image-url: A URL leading to the preview image for the item.
            preview-text: A preview text for the item.
            title: The item's title text.
            type: The item's media type. Can be used for filtering for a specific file based on a specific type. See \
below for supported types.
      - name: --shared-by
        short-summary: "insightIdentity"
        long-summary: |
            Usage: --shared-by address=XX display-name=XX id=XX

            address: The email address of the user who shared the item.
            display-name: The display name of the user who shared the item.
            id: The id of the user who shared the item.
      - name: --sharing-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --sharing-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
"""

helps['people usersinsight create-trending'] = """
    type: command
    short-summary: "Create new navigation property to trending for users."
    parameters:
      - name: --resource-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --resource-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
      - name: --resource-visualization
        short-summary: "resourceVisualization"
        long-summary: |
            Usage: --resource-visualization container-display-name=XX container-type=XX container-web-url=XX \
media-type=XX preview-image-url=XX preview-text=XX title=XX type=XX

            container-display-name: A string describing where the item is stored. For example, the name of a \
SharePoint site or the user name identifying the owner of the OneDrive storing the item.
            container-type: Can be used for filtering by the type of container in which the file is stored. Such as \
Site or OneDriveBusiness.
            container-web-url: A path leading to the folder in which the item is stored.
            media-type: The item's media type. Can be used for filtering for a specific type of file based on \
supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
            preview-image-url: A URL leading to the preview image for the item.
            preview-text: A preview text for the item.
            title: The item's title text.
            type: The item's media type. Can be used for filtering for a specific file based on a specific type. See \
below for supported types.
"""

helps['people usersinsight create-used'] = """
    type: command
    short-summary: "Create new navigation property to used for users."
    parameters:
      - name: --last-used
        short-summary: "usageDetails"
        long-summary: |
            Usage: --last-used last-accessed-date-time=XX last-modified-date-time=XX

            last-accessed-date-time: The date and time the resource was last accessed by the user. The timestamp \
represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan \
1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.
            last-modified-date-time: The date and time the resource was last modified by the user. The timestamp \
represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan \
1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.
      - name: --resource-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --resource-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
      - name: --resource-visualization
        short-summary: "resourceVisualization"
        long-summary: |
            Usage: --resource-visualization container-display-name=XX container-type=XX container-web-url=XX \
media-type=XX preview-image-url=XX preview-text=XX title=XX type=XX

            container-display-name: A string describing where the item is stored. For example, the name of a \
SharePoint site or the user name identifying the owner of the OneDrive storing the item.
            container-type: Can be used for filtering by the type of container in which the file is stored. Such as \
Site or OneDriveBusiness.
            container-web-url: A path leading to the folder in which the item is stored.
            media-type: The item's media type. Can be used for filtering for a specific type of file based on \
supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
            preview-image-url: A URL leading to the preview image for the item.
            preview-text: A preview text for the item.
            title: The item's title text.
            type: The item's media type. Can be used for filtering for a specific file based on a specific type. See \
below for supported types.
"""

helps['people usersinsight delete-shared'] = """
    type: command
    short-summary: "Delete navigation property shared for users."
"""

helps['people usersinsight delete-trending'] = """
    type: command
    short-summary: "Delete navigation property trending for users."
"""

helps['people usersinsight delete-used'] = """
    type: command
    short-summary: "Delete navigation property used for users."
"""

helps['people usersinsight list-shared'] = """
    type: command
    short-summary: "Get shared from users."
"""

helps['people usersinsight list-trending'] = """
    type: command
    short-summary: "Get trending from users."
"""

helps['people usersinsight list-used'] = """
    type: command
    short-summary: "Get used from users."
"""

helps['people usersinsight show-shared'] = """
    type: command
    short-summary: "Get shared from users."
"""

helps['people usersinsight show-trending'] = """
    type: command
    short-summary: "Get trending from users."
"""

helps['people usersinsight show-used'] = """
    type: command
    short-summary: "Get used from users."
"""

helps['people usersinsight update-shared'] = """
    type: command
    short-summary: "Update the navigation property shared in users."
    parameters:
      - name: --resource-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --resource-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
      - name: --resource-visualization
        short-summary: "resourceVisualization"
        long-summary: |
            Usage: --resource-visualization container-display-name=XX container-type=XX container-web-url=XX \
media-type=XX preview-image-url=XX preview-text=XX title=XX type=XX

            container-display-name: A string describing where the item is stored. For example, the name of a \
SharePoint site or the user name identifying the owner of the OneDrive storing the item.
            container-type: Can be used for filtering by the type of container in which the file is stored. Such as \
Site or OneDriveBusiness.
            container-web-url: A path leading to the folder in which the item is stored.
            media-type: The item's media type. Can be used for filtering for a specific type of file based on \
supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
            preview-image-url: A URL leading to the preview image for the item.
            preview-text: A preview text for the item.
            title: The item's title text.
            type: The item's media type. Can be used for filtering for a specific file based on a specific type. See \
below for supported types.
      - name: --shared-by
        short-summary: "insightIdentity"
        long-summary: |
            Usage: --shared-by address=XX display-name=XX id=XX

            address: The email address of the user who shared the item.
            display-name: The display name of the user who shared the item.
            id: The id of the user who shared the item.
      - name: --sharing-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --sharing-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
"""

helps['people usersinsight update-trending'] = """
    type: command
    short-summary: "Update the navigation property trending in users."
    parameters:
      - name: --resource-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --resource-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
      - name: --resource-visualization
        short-summary: "resourceVisualization"
        long-summary: |
            Usage: --resource-visualization container-display-name=XX container-type=XX container-web-url=XX \
media-type=XX preview-image-url=XX preview-text=XX title=XX type=XX

            container-display-name: A string describing where the item is stored. For example, the name of a \
SharePoint site or the user name identifying the owner of the OneDrive storing the item.
            container-type: Can be used for filtering by the type of container in which the file is stored. Such as \
Site or OneDriveBusiness.
            container-web-url: A path leading to the folder in which the item is stored.
            media-type: The item's media type. Can be used for filtering for a specific type of file based on \
supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
            preview-image-url: A URL leading to the preview image for the item.
            preview-text: A preview text for the item.
            title: The item's title text.
            type: The item's media type. Can be used for filtering for a specific file based on a specific type. See \
below for supported types.
"""

helps['people usersinsight update-used'] = """
    type: command
    short-summary: "Update the navigation property used in users."
    parameters:
      - name: --last-used
        short-summary: "usageDetails"
        long-summary: |
            Usage: --last-used last-accessed-date-time=XX last-modified-date-time=XX

            last-accessed-date-time: The date and time the resource was last accessed by the user. The timestamp \
represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan \
1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.
            last-modified-date-time: The date and time the resource was last modified by the user. The timestamp \
represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan \
1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.
      - name: --resource-reference
        short-summary: "resourceReference"
        long-summary: |
            Usage: --resource-reference id=XX type=XX web-url=XX

            id: The item's unique identifier.
            type: A string value that can be used to classify the item, such as 'microsoft.graph.driveItem'
            web-url: A URL leading to the referenced item.
      - name: --resource-visualization
        short-summary: "resourceVisualization"
        long-summary: |
            Usage: --resource-visualization container-display-name=XX container-type=XX container-web-url=XX \
media-type=XX preview-image-url=XX preview-text=XX title=XX type=XX

            container-display-name: A string describing where the item is stored. For example, the name of a \
SharePoint site or the user name identifying the owner of the OneDrive storing the item.
            container-type: Can be used for filtering by the type of container in which the file is stored. Such as \
Site or OneDriveBusiness.
            container-web-url: A path leading to the folder in which the item is stored.
            media-type: The item's media type. Can be used for filtering for a specific type of file based on \
supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
            preview-image-url: A URL leading to the preview image for the item.
            preview-text: A preview text for the item.
            title: The item's title text.
            type: The item's media type. Can be used for filtering for a specific file based on a specific type. See \
below for supported types.
"""

helps['people usersinsightsshared'] = """
    type: group
    short-summary: Manage usersinsightsshared with people_v1_0
"""

helps['people usersinsightsshared delete-ref-last-shared-method'] = """
    type: command
    short-summary: "Delete ref of navigation property lastSharedMethod for users."
"""

helps['people usersinsightsshared delete-ref-resource'] = """
    type: command
    short-summary: "Delete ref of navigation property resource for users."
"""

helps['people usersinsightsshared set-ref-last-shared-method'] = """
    type: command
    short-summary: "Update the ref of navigation property lastSharedMethod in users."
"""

helps['people usersinsightsshared set-ref-resource'] = """
    type: command
    short-summary: "Update the ref of navigation property resource in users."
"""

helps['people usersinsightsshared show-last-shared-method'] = """
    type: command
    short-summary: "Get lastSharedMethod from users."
"""

helps['people usersinsightsshared show-ref-last-shared-method'] = """
    type: command
    short-summary: "Get ref of lastSharedMethod from users."
"""

helps['people usersinsightsshared show-ref-resource'] = """
    type: command
    short-summary: "Get ref of resource from users."
"""

helps['people usersinsightsshared show-resource'] = """
    type: command
    short-summary: "Get resource from users."
"""

helps['people usersinsightstrending'] = """
    type: group
    short-summary: Manage usersinsightstrending with people_v1_0
"""

helps['people usersinsightstrending delete-ref-resource'] = """
    type: command
    short-summary: "Delete ref of navigation property resource for users."
"""

helps['people usersinsightstrending set-ref-resource'] = """
    type: command
    short-summary: "Update the ref of navigation property resource in users."
"""

helps['people usersinsightstrending show-ref-resource'] = """
    type: command
    short-summary: "Get ref of resource from users."
"""

helps['people usersinsightstrending show-resource'] = """
    type: command
    short-summary: "Get resource from users."
"""

helps['people usersinsightsused'] = """
    type: group
    short-summary: Manage usersinsightsused with people_v1_0
"""

helps['people usersinsightsused delete-ref-resource'] = """
    type: command
    short-summary: "Delete ref of navigation property resource for users."
"""

helps['people usersinsightsused set-ref-resource'] = """
    type: command
    short-summary: "Update the ref of navigation property resource in users."
"""

helps['people usersinsightsused show-ref-resource'] = """
    type: command
    short-summary: "Get ref of resource from users."
"""

helps['people usersinsightsused show-resource'] = """
    type: command
    short-summary: "Get resource from users."
"""
