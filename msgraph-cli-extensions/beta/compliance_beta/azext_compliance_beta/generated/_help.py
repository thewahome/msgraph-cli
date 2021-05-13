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


helps['compliance_beta'] = '''
    type: group
    short-summary: Manage Compliance
'''

helps['compliance compliance'] = """
    type: group
    short-summary: Manage compliance compliance with compliance_beta
"""

helps['compliance compliance update'] = """
    type: command
    short-summary: "Update compliance."
"""

helps['compliance compliance show-compliance'] = """
    type: command
    short-summary: "Get compliance."
"""

helps['compliance compliance'] = """
    type: group
    short-summary: Manage compliance with compliance_beta
"""

helps['compliance compliance delete-ediscovery'] = """
    type: command
    short-summary: "Delete navigation property ediscovery for compliance."
"""

helps['compliance compliance show-ediscovery'] = """
    type: command
    short-summary: "Get ediscovery from compliance."
"""

helps['compliance compliance update-ediscovery'] = """
    type: command
    short-summary: "Update the navigation property ediscovery in compliance."
"""

helps['compliance compliance-ediscovery'] = """
    type: group
    short-summary: Manage compliance ediscovery with compliance_beta
"""

helps['compliance compliance-ediscovery create-case'] = """
    type: command
    short-summary: "Create new navigation property to cases for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery delete-case'] = """
    type: command
    short-summary: "Delete navigation property cases for compliance."
"""

helps['compliance compliance-ediscovery list-case'] = """
    type: command
    short-summary: "Get cases from compliance."
"""

helps['compliance compliance-ediscovery show-case'] = """
    type: command
    short-summary: "Get cases from compliance."
"""

helps['compliance compliance-ediscovery update-case'] = """
    type: command
    short-summary: "Update the navigation property cases in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case'] = """
    type: group
    short-summary: Manage compliance ediscovery case with compliance_beta
"""

helps['compliance compliance-ediscovery-case close'] = """
    type: command
    short-summary: "Invoke action close."
"""

helps['compliance compliance-ediscovery-case create-custodian'] = """
    type: command
    short-summary: "Create new navigation property to custodians for compliance."
    parameters:
      - name: --last-index-operation
        short-summary: "caseIndexOperation"
        long-summary: |
            Usage: --last-index-operation action=XX completed-date-time=XX created-date-time=XX display-name=XX \
percent-progress=XX status=XX id=XX

            id: Read-only.
      - name: --user-sources
        long-summary: |
            Usage: --user-sources email=XX included-sources=XX created-date-time=XX display-name=XX application=XX \
device=XX user=XX id=XX

            application: identity
            device: identity
            user: identity
            id: Read-only.

            Multiple actions can be specified by using more than one --user-sources argument.
"""

helps['compliance compliance-ediscovery-case create-review-set'] = """
    type: command
    short-summary: "Create new navigation property to reviewSets for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case delete-custodian'] = """
    type: command
    short-summary: "Delete navigation property custodians for compliance."
"""

helps['compliance compliance-ediscovery-case delete-review-set'] = """
    type: command
    short-summary: "Delete navigation property reviewSets for compliance."
"""

helps['compliance compliance-ediscovery-case list-custodian'] = """
    type: command
    short-summary: "Get custodians from compliance."
"""

helps['compliance compliance-ediscovery-case list-review-set'] = """
    type: command
    short-summary: "Get reviewSets from compliance."
"""

helps['compliance compliance-ediscovery-case reopen'] = """
    type: command
    short-summary: "Invoke action reopen."
"""

helps['compliance compliance-ediscovery-case show-custodian'] = """
    type: command
    short-summary: "Get custodians from compliance."
"""

helps['compliance compliance-ediscovery-case show-review-set'] = """
    type: command
    short-summary: "Get reviewSets from compliance."
"""

helps['compliance compliance-ediscovery-case update-custodian'] = """
    type: command
    short-summary: "Update the navigation property custodians in compliance."
    parameters:
      - name: --last-index-operation
        short-summary: "caseIndexOperation"
        long-summary: |
            Usage: --last-index-operation action=XX completed-date-time=XX created-date-time=XX display-name=XX \
percent-progress=XX status=XX id=XX

            id: Read-only.
      - name: --user-sources
        long-summary: |
            Usage: --user-sources email=XX included-sources=XX created-date-time=XX display-name=XX application=XX \
device=XX user=XX id=XX

            application: identity
            device: identity
            user: identity
            id: Read-only.

            Multiple actions can be specified by using more than one --user-sources argument.
"""

helps['compliance compliance-ediscovery-case update-review-set'] = """
    type: command
    short-summary: "Update the navigation property reviewSets in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian'] = """
    type: group
    short-summary: Manage compliance ediscovery case custodian with compliance_beta
"""

helps['compliance compliance-ediscovery-case-custodian activate'] = """
    type: command
    short-summary: "Invoke action activate."
"""

helps['compliance compliance-ediscovery-case-custodian create-site-source'] = """
    type: command
    short-summary: "Create new navigation property to siteSources for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian create-unified-group-source'] = """
    type: command
    short-summary: "Create new navigation property to unifiedGroupSources for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian create-user-source'] = """
    type: command
    short-summary: "Create new navigation property to userSources for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian delete-ref-last-index-operation'] = """
    type: command
    short-summary: "Delete ref of navigation property lastIndexOperation for compliance."
"""

helps['compliance compliance-ediscovery-case-custodian delete-site-source'] = """
    type: command
    short-summary: "Delete navigation property siteSources for compliance."
"""

helps['compliance compliance-ediscovery-case-custodian delete-unified-group-source'] = """
    type: command
    short-summary: "Delete navigation property unifiedGroupSources for compliance."
"""

helps['compliance compliance-ediscovery-case-custodian delete-user-source'] = """
    type: command
    short-summary: "Delete navigation property userSources for compliance."
"""

helps['compliance compliance-ediscovery-case-custodian list-site-source'] = """
    type: command
    short-summary: "Get siteSources from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian list-unified-group-source'] = """
    type: command
    short-summary: "Get unifiedGroupSources from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian list-user-source'] = """
    type: command
    short-summary: "Get userSources from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian release'] = """
    type: command
    short-summary: "Invoke action release."
"""

helps['compliance compliance-ediscovery-case-custodian set-ref-last-index-operation'] = """
    type: command
    short-summary: "Update the ref of navigation property lastIndexOperation in compliance."
"""

helps['compliance compliance-ediscovery-case-custodian show-last-index-operation'] = """
    type: command
    short-summary: "Get lastIndexOperation from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian show-ref-last-index-operation'] = """
    type: command
    short-summary: "Get ref of lastIndexOperation from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian show-site-source'] = """
    type: command
    short-summary: "Get siteSources from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian show-unified-group-source'] = """
    type: command
    short-summary: "Get unifiedGroupSources from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian show-user-source'] = """
    type: command
    short-summary: "Get userSources from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian update-index'] = """
    type: command
    short-summary: "Invoke action updateIndex."
"""

helps['compliance compliance-ediscovery-case-custodian update-site-source'] = """
    type: command
    short-summary: "Update the navigation property siteSources in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian update-unified-group-source'] = """
    type: command
    short-summary: "Update the navigation property unifiedGroupSources in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian update-user-source'] = """
    type: command
    short-summary: "Update the navigation property userSources in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-custodian-site-source'] = """
    type: group
    short-summary: Manage compliance ediscovery case custodian site source with compliance_beta
"""

helps['compliance compliance-ediscovery-case-custodian-site-source delete-ref-site'] = """
    type: command
    short-summary: "Delete ref of navigation property site for compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-site-source set-ref-site'] = """
    type: command
    short-summary: "Update the ref of navigation property site in compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-site-source show-ref-site'] = """
    type: command
    short-summary: "Get ref of site from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-site-source show-site'] = """
    type: command
    short-summary: "Get site from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-unified-group-source'] = """
    type: group
    short-summary: Manage compliance ediscovery case custodian unified group source with compliance_beta
"""

helps['compliance compliance-ediscovery-case-custodian-unified-group-source delete-ref-group'] = """
    type: command
    short-summary: "Delete ref of navigation property group for compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-unified-group-source set-ref-group'] = """
    type: command
    short-summary: "Update the ref of navigation property group in compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-unified-group-source show-group'] = """
    type: command
    short-summary: "Get group from compliance."
"""

helps['compliance compliance-ediscovery-case-custodian-unified-group-source show-ref-group'] = """
    type: command
    short-summary: "Get ref of group from compliance."
"""

helps['compliance compliance-ediscovery-case-review-set'] = """
    type: group
    short-summary: Manage compliance ediscovery case review set with compliance_beta
"""

helps['compliance compliance-ediscovery-case-review-set create-query'] = """
    type: command
    short-summary: "Create new navigation property to queries for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance compliance-ediscovery-case-review-set delete-query'] = """
    type: command
    short-summary: "Delete navigation property queries for compliance."
"""

helps['compliance compliance-ediscovery-case-review-set list-query'] = """
    type: command
    short-summary: "Get queries from compliance."
"""

helps['compliance compliance-ediscovery-case-review-set show-query'] = """
    type: command
    short-summary: "Get queries from compliance."
"""

helps['compliance compliance-ediscovery-case-review-set update-query'] = """
    type: command
    short-summary: "Update the navigation property queries in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""
