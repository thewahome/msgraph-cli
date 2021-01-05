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


helps['mail'] = """
    type: group
    short-summary: mail
"""

helps['mail delete'] = """
    type: command
    short-summary: "Delete navigation property inferenceClassification for users"
"""

helps['mail create-mail-folder'] = """
    type: command
    short-summary: "Create new navigation property to mailFolders for users"
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail create-message'] = """
    type: command
    short-summary: "Create new navigation property to messages for users"
"""

helps['mail get-inference-classification'] = """
    type: command
    short-summary: "Get inferenceClassification from users"
"""

helps['mail get-mail-folder'] = """
    type: command
    short-summary: "Get mailFolders from users"
"""

helps['mail get-message'] = """
    type: command
    short-summary: "Get messages from users"
"""

helps['mail get-message-content'] = """
    type: command
    short-summary: "Get media content for the navigation property messages from users"
"""

helps['mail list-mail-folder'] = """
    type: command
    short-summary: "Get mailFolders from users"
"""

helps['mail list-message'] = """
    type: command
    short-summary: "Get messages from users"
"""

helps['mail set-message-content'] = """
    type: command
    short-summary: "Update media content for the navigation property messages in users"
"""

helps['mail update-inference-classification'] = """
    type: command
    short-summary: "Update the navigation property inferenceClassification in users"
    parameters:
      - name: --overrides
        short-summary: "A set of overrides for a user to always classify messages from specific senders in certain \
ways: focused, or other. Read-only. Nullable."
        long-summary: |
            Usage: --overrides classify-as=XX address=XX name=XX id=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
            id: Read-only.

            Multiple actions can be specified by using more than one --overrides argument.
"""

helps['mail update-mail-folder'] = """
    type: command
    short-summary: "Update the navigation property mailFolders in users"
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail update-message'] = """
    type: command
    short-summary: "Update the navigation property messages in users"
"""

helps['mail'] = """
    type: group
    short-summary: mail
"""

helps['mail delete'] = """
    type: command
    short-summary: "Delete navigation property overrides for users"
"""

helps['mail create-override'] = """
    type: command
    short-summary: "Create new navigation property to overrides for users"
"""

helps['mail get-override'] = """
    type: command
    short-summary: "Get overrides from users"
"""

helps['mail list-override'] = """
    type: command
    short-summary: "Get overrides from users"
"""

helps['mail update-override'] = """
    type: command
    short-summary: "Update the navigation property overrides in users"
"""

helps['mail'] = """
    type: group
    short-summary: mail
"""

helps['mail delete'] = """
    type: command
    short-summary: "Delete navigation property userConfigurations for users"
"""

helps['mail create-child-folder'] = """
    type: command
    short-summary: "Create new navigation property to childFolders for users"
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail create-message'] = """
    type: command
    short-summary: "Create new navigation property to messages for users"
"""

helps['mail create-message-rule'] = """
    type: command
    short-summary: "Create new navigation property to messageRules for users"
"""

helps['mail create-multi-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to multiValueExtendedProperties for users"
"""

helps['mail create-single-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to singleValueExtendedProperties for users"
"""

helps['mail create-user-configuration'] = """
    type: command
    short-summary: "Create new navigation property to userConfigurations for users"
"""

helps['mail get-child-folder'] = """
    type: command
    short-summary: "Get childFolders from users"
"""

helps['mail get-message'] = """
    type: command
    short-summary: "Get messages from users"
"""

helps['mail get-message-content'] = """
    type: command
    short-summary: "Get media content for the navigation property messages from users"
"""

helps['mail get-message-rule'] = """
    type: command
    short-summary: "Get messageRules from users"
"""

helps['mail get-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users"
"""

helps['mail get-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users"
"""

helps['mail get-user-configuration'] = """
    type: command
    short-summary: "Get userConfigurations from users"
"""

helps['mail list-child-folder'] = """
    type: command
    short-summary: "Get childFolders from users"
"""

helps['mail list-message'] = """
    type: command
    short-summary: "Get messages from users"
"""

helps['mail list-message-rule'] = """
    type: command
    short-summary: "Get messageRules from users"
"""

helps['mail list-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users"
"""

helps['mail list-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users"
"""

helps['mail list-user-configuration'] = """
    type: command
    short-summary: "Get userConfigurations from users"
"""

helps['mail set-message-content'] = """
    type: command
    short-summary: "Update media content for the navigation property messages in users"
"""

helps['mail update-child-folder'] = """
    type: command
    short-summary: "Update the navigation property childFolders in users"
    parameters:
      - name: --multi-value-extended-properties
        short-summary: "The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --single-value-extended-properties
        short-summary: "The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable."
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['mail update-message'] = """
    type: command
    short-summary: "Update the navigation property messages in users"
"""

helps['mail update-message-rule'] = """
    type: command
    short-summary: "Update the navigation property messageRules in users"
"""

helps['mail update-multi-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property multiValueExtendedProperties in users"
"""

helps['mail update-single-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property singleValueExtendedProperties in users"
"""

helps['mail update-user-configuration'] = """
    type: command
    short-summary: "Update the navigation property userConfigurations in users"
"""

helps['mail'] = """
    type: group
    short-summary: mail
"""

helps['mail delete'] = """
    type: command
    short-summary: "Delete navigation property singleValueExtendedProperties for users"
"""

helps['mail create-attachment'] = """
    type: command
    short-summary: "Create new navigation property to attachments for users"
"""

helps['mail create-extension'] = """
    type: command
    short-summary: "Create new navigation property to extensions for users"
"""

helps['mail create-mention'] = """
    type: command
    short-summary: "Create new navigation property to mentions for users"
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail create-multi-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to multiValueExtendedProperties for users"
"""

helps['mail create-single-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to singleValueExtendedProperties for users"
"""

helps['mail get-attachment'] = """
    type: command
    short-summary: "Get attachments from users"
"""

helps['mail get-extension'] = """
    type: command
    short-summary: "Get extensions from users"
"""

helps['mail get-mention'] = """
    type: command
    short-summary: "Get mentions from users"
"""

helps['mail get-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users"
"""

helps['mail get-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users"
"""

helps['mail list-attachment'] = """
    type: command
    short-summary: "Get attachments from users"
"""

helps['mail list-extension'] = """
    type: command
    short-summary: "Get extensions from users"
"""

helps['mail list-mention'] = """
    type: command
    short-summary: "Get mentions from users"
"""

helps['mail list-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users"
"""

helps['mail list-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users"
"""

helps['mail update-attachment'] = """
    type: command
    short-summary: "Update the navigation property attachments in users"
"""

helps['mail update-extension'] = """
    type: command
    short-summary: "Update the navigation property extensions in users"
"""

helps['mail update-mention'] = """
    type: command
    short-summary: "Update the navigation property mentions in users"
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail update-multi-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property multiValueExtendedProperties in users"
"""

helps['mail update-single-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property singleValueExtendedProperties in users"
"""

helps['mail'] = """
    type: group
    short-summary: mail
"""

helps['mail delete'] = """
    type: command
    short-summary: "Delete navigation property singleValueExtendedProperties for users"
"""

helps['mail create-attachment'] = """
    type: command
    short-summary: "Create new navigation property to attachments for users"
"""

helps['mail create-extension'] = """
    type: command
    short-summary: "Create new navigation property to extensions for users"
"""

helps['mail create-mention'] = """
    type: command
    short-summary: "Create new navigation property to mentions for users"
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail create-multi-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to multiValueExtendedProperties for users"
"""

helps['mail create-single-value-extended-property'] = """
    type: command
    short-summary: "Create new navigation property to singleValueExtendedProperties for users"
"""

helps['mail get-attachment'] = """
    type: command
    short-summary: "Get attachments from users"
"""

helps['mail get-extension'] = """
    type: command
    short-summary: "Get extensions from users"
"""

helps['mail get-mention'] = """
    type: command
    short-summary: "Get mentions from users"
"""

helps['mail get-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users"
"""

helps['mail get-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users"
"""

helps['mail list-attachment'] = """
    type: command
    short-summary: "Get attachments from users"
"""

helps['mail list-extension'] = """
    type: command
    short-summary: "Get extensions from users"
"""

helps['mail list-mention'] = """
    type: command
    short-summary: "Get mentions from users"
"""

helps['mail list-multi-value-extended-property'] = """
    type: command
    short-summary: "Get multiValueExtendedProperties from users"
"""

helps['mail list-single-value-extended-property'] = """
    type: command
    short-summary: "Get singleValueExtendedProperties from users"
"""

helps['mail update-attachment'] = """
    type: command
    short-summary: "Update the navigation property attachments in users"
"""

helps['mail update-extension'] = """
    type: command
    short-summary: "Update the navigation property extensions in users"
"""

helps['mail update-mention'] = """
    type: command
    short-summary: "Update the navigation property mentions in users"
    parameters:
      - name: --created-by
        short-summary: "emailAddress"
        long-summary: |
            Usage: --created-by address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
      - name: --mentioned
        short-summary: "emailAddress"
        long-summary: |
            Usage: --mentioned address=XX name=XX

            address: The email address of the person or entity.
            name: The display name of the person or entity.
"""

helps['mail update-multi-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property multiValueExtendedProperties in users"
"""

helps['mail update-single-value-extended-property'] = """
    type: command
    short-summary: "Update the navigation property singleValueExtendedProperties in users"
"""
