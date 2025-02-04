# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType
from azext_applications_v1_0.generated._client_factory import (
    cf_application_application,
    cf_application,
    cf_group,
    cf_service_principal_service_principal,
    cf_service_principal,
    cf_user,
)


applications_v1_0_application_application = CliCommandType(
    operations_tmpl='azext_applications_v1_0.vendored_sdks.applications.operations._applications_application_operations#ApplicationsApplicationOperations.{}',
    client_factory=cf_application_application,
)


applications_v1_0_application = CliCommandType(
    operations_tmpl='azext_applications_v1_0.vendored_sdks.applications.operations._applications_operations#ApplicationsOperations.{}',
    client_factory=cf_application,
)


applications_v1_0_group = CliCommandType(
    operations_tmpl=(
        'azext_applications_v1_0.vendored_sdks.applications.operations._groups_operations#GroupsOperations.{}'
    ),
    client_factory=cf_group,
)


applications_v1_0_service_principal_service_principal = CliCommandType(
    operations_tmpl='azext_applications_v1_0.vendored_sdks.applications.operations._service_principals_service_principal_operations#ServicePrincipalsServicePrincipalOperations.{}',
    client_factory=cf_service_principal_service_principal,
)


applications_v1_0_service_principal = CliCommandType(
    operations_tmpl='azext_applications_v1_0.vendored_sdks.applications.operations._service_principals_operations#ServicePrincipalsOperations.{}',
    client_factory=cf_service_principal,
)


applications_v1_0_user = CliCommandType(
    operations_tmpl=(
        'azext_applications_v1_0.vendored_sdks.applications.operations._users_operations#UsersOperations.{}'
    ),
    client_factory=cf_user,
)


def load_command_table(self, _):

    with self.command_group(
        'applications application', applications_v1_0_application_application, client_factory=cf_application_application
    ) as g:
        g.custom_command('list', 'applications_application_list')
        g.custom_command('create', 'applications_application_create')
        g.custom_command('update', 'applications_application_update')
        g.custom_command('delete-application', 'applications_application_delete_application')
        g.custom_command('set-logo', 'applications_application_set_logo')
        g.custom_command('show-application', 'applications_application_show_application')
        g.custom_command('show-logo', 'applications_application_show_logo')

    with self.command_group(
        'applications application', applications_v1_0_application, client_factory=cf_application
    ) as g:
        g.custom_command('add-key', 'applications_application_add_key')
        g.custom_command('add-password', 'applications_application_add_password')
        g.custom_command('check-member-group', 'applications_application_check_member_group')
        g.custom_command('check-member-object', 'applications_application_check_member_object')
        g.custom_command('create-extension-property', 'applications_application_create_extension_property')
        g.custom_command(
            'create-ref-home-realm-discovery-policy', 'applications_application_create_ref_home_realm_discovery_policy'
        )
        g.custom_command('create-ref-owner', 'applications_application_create_ref_owner')
        g.custom_command(
            'create-ref-token-issuance-policy', 'applications_application_create_ref_token_issuance_policy'
        )
        g.custom_command(
            'create-ref-token-lifetime-policy', 'applications_application_create_ref_token_lifetime_policy'
        )
        g.custom_command('delete-extension-property', 'applications_application_delete_extension_property')
        g.custom_command('delete-ref-created-on-behalf-of', 'applications_application_delete_ref_created_on_behalf_of')
        g.custom_command('delta', 'applications_application_delta')
        g.custom_command(
            'get-available-extension-property', 'applications_application_get_available_extension_property'
        )
        g.custom_command('get-by-id', 'applications_application_get_by_id')
        g.custom_command('get-member-group', 'applications_application_get_member_group')
        g.custom_command('get-member-object', 'applications_application_get_member_object')
        g.custom_command('list-extension-property', 'applications_application_list_extension_property')
        g.custom_command(
            'list-home-realm-discovery-policy', 'applications_application_list_home_realm_discovery_policy'
        )
        g.custom_command('list-owner', 'applications_application_list_owner')
        g.custom_command(
            'list-ref-home-realm-discovery-policy', 'applications_application_list_ref_home_realm_discovery_policy'
        )
        g.custom_command('list-ref-owner', 'applications_application_list_ref_owner')
        g.custom_command('list-ref-token-issuance-policy', 'applications_application_list_ref_token_issuance_policy')
        g.custom_command('list-ref-token-lifetime-policy', 'applications_application_list_ref_token_lifetime_policy')
        g.custom_command('list-token-issuance-policy', 'applications_application_list_token_issuance_policy')
        g.custom_command('list-token-lifetime-policy', 'applications_application_list_token_lifetime_policy')
        g.custom_command('remove-key', 'applications_application_remove_key')
        g.custom_command('remove-password', 'applications_application_remove_password')
        g.custom_command('restore', 'applications_application_restore')
        g.custom_command('set-ref-created-on-behalf-of', 'applications_application_set_ref_created_on_behalf_of')
        g.custom_command('show-created-on-behalf-of', 'applications_application_show_created_on_behalf_of')
        g.custom_command('show-extension-property', 'applications_application_show_extension_property')
        g.custom_command('show-ref-created-on-behalf-of', 'applications_application_show_ref_created_on_behalf_of')
        g.custom_command('update-extension-property', 'applications_application_update_extension_property')
        g.custom_command('validate-property', 'applications_application_validate_property')

    with self.command_group('applications group', applications_v1_0_group, client_factory=cf_group) as g:
        g.custom_command('create-app-role-assignment', 'applications_group_create_app_role_assignment')
        g.custom_command('delete-app-role-assignment', 'applications_group_delete_app_role_assignment')
        g.custom_command('list-app-role-assignment', 'applications_group_list_app_role_assignment')
        g.custom_command('show-app-role-assignment', 'applications_group_show_app_role_assignment')
        g.custom_command('update-app-role-assignment', 'applications_group_update_app_role_assignment')

    with self.command_group(
        'applications service-principal-service-principal',
        applications_v1_0_service_principal_service_principal,
        client_factory=cf_service_principal_service_principal,
    ) as g:
        g.custom_command(
            'create-service-principal', 'applications_service_principal_service_principal_create_service_principal'
        )
        g.custom_command(
            'delete-service-principal', 'applications_service_principal_service_principal_delete_service_principal'
        )
        g.custom_command(
            'list-service-principal', 'applications_service_principal_service_principal_list_service_principal'
        )
        g.custom_command(
            'show-service-principal', 'applications_service_principal_service_principal_show_service_principal'
        )
        g.custom_command(
            'update-service-principal', 'applications_service_principal_service_principal_update_service_principal'
        )

    with self.command_group(
        'applications service-principal', applications_v1_0_service_principal, client_factory=cf_service_principal
    ) as g:
        g.custom_command('add-key', 'applications_service_principal_add_key')
        g.custom_command('add-password', 'applications_service_principal_add_password')
        g.custom_command('check-member-group', 'applications_service_principal_check_member_group')
        g.custom_command('check-member-object', 'applications_service_principal_check_member_object')
        g.custom_command('create-app-role-assigned-to', 'applications_service_principal_create_app_role_assigned_to')
        g.custom_command('create-app-role-assignment', 'applications_service_principal_create_app_role_assignment')
        g.custom_command('create-endpoint', 'applications_service_principal_create_endpoint')
        g.custom_command(
            'create-ref-claim-mapping-policy', 'applications_service_principal_create_ref_claim_mapping_policy'
        )
        g.custom_command('create-ref-created-object', 'applications_service_principal_create_ref_created_object')
        g.custom_command(
            'create-ref-home-realm-discovery-policy',
            'applications_service_principal_create_ref_home_realm_discovery_policy',
        )
        g.custom_command('create-ref-member-of', 'applications_service_principal_create_ref_member_of')
        g.custom_command(
            'create-ref-oauth2-permission-grant', 'applications_service_principal_create_ref_oauth2_permission_grant'
        )
        g.custom_command('create-ref-owned-object', 'applications_service_principal_create_ref_owned_object')
        g.custom_command('create-ref-owner', 'applications_service_principal_create_ref_owner')
        g.custom_command(
            'create-ref-token-issuance-policy', 'applications_service_principal_create_ref_token_issuance_policy'
        )
        g.custom_command(
            'create-ref-token-lifetime-policy', 'applications_service_principal_create_ref_token_lifetime_policy'
        )
        g.custom_command(
            'create-ref-transitive-member-of', 'applications_service_principal_create_ref_transitive_member_of'
        )
        g.custom_command('delete-app-role-assigned-to', 'applications_service_principal_delete_app_role_assigned_to')
        g.custom_command('delete-app-role-assignment', 'applications_service_principal_delete_app_role_assignment')
        g.custom_command('delete-endpoint', 'applications_service_principal_delete_endpoint')
        g.custom_command('delta', 'applications_service_principal_delta')
        g.custom_command(
            'get-available-extension-property', 'applications_service_principal_get_available_extension_property'
        )
        g.custom_command('get-by-id', 'applications_service_principal_get_by_id')
        g.custom_command('get-member-group', 'applications_service_principal_get_member_group')
        g.custom_command('get-member-object', 'applications_service_principal_get_member_object')
        g.custom_command('list-app-role-assigned-to', 'applications_service_principal_list_app_role_assigned_to')
        g.custom_command('list-app-role-assignment', 'applications_service_principal_list_app_role_assignment')
        g.custom_command('list-claim-mapping-policy', 'applications_service_principal_list_claim_mapping_policy')
        g.custom_command('list-created-object', 'applications_service_principal_list_created_object')
        g.custom_command('list-endpoint', 'applications_service_principal_list_endpoint')
        g.custom_command(
            'list-home-realm-discovery-policy', 'applications_service_principal_list_home_realm_discovery_policy'
        )
        g.custom_command('list-member-of', 'applications_service_principal_list_member_of')
        g.custom_command('list-oauth2-permission-grant', 'applications_service_principal_list_oauth2_permission_grant')
        g.custom_command('list-owned-object', 'applications_service_principal_list_owned_object')
        g.custom_command('list-owner', 'applications_service_principal_list_owner')
        g.custom_command(
            'list-ref-claim-mapping-policy', 'applications_service_principal_list_ref_claim_mapping_policy'
        )
        g.custom_command('list-ref-created-object', 'applications_service_principal_list_ref_created_object')
        g.custom_command(
            'list-ref-home-realm-discovery-policy',
            'applications_service_principal_list_ref_home_realm_discovery_policy',
        )
        g.custom_command('list-ref-member-of', 'applications_service_principal_list_ref_member_of')
        g.custom_command(
            'list-ref-oauth2-permission-grant', 'applications_service_principal_list_ref_oauth2_permission_grant'
        )
        g.custom_command('list-ref-owned-object', 'applications_service_principal_list_ref_owned_object')
        g.custom_command('list-ref-owner', 'applications_service_principal_list_ref_owner')
        g.custom_command(
            'list-ref-token-issuance-policy', 'applications_service_principal_list_ref_token_issuance_policy'
        )
        g.custom_command(
            'list-ref-token-lifetime-policy', 'applications_service_principal_list_ref_token_lifetime_policy'
        )
        g.custom_command(
            'list-ref-transitive-member-of', 'applications_service_principal_list_ref_transitive_member_of'
        )
        g.custom_command('list-token-issuance-policy', 'applications_service_principal_list_token_issuance_policy')
        g.custom_command('list-token-lifetime-policy', 'applications_service_principal_list_token_lifetime_policy')
        g.custom_command('list-transitive-member-of', 'applications_service_principal_list_transitive_member_of')
        g.custom_command('remove-key', 'applications_service_principal_remove_key')
        g.custom_command('remove-password', 'applications_service_principal_remove_password')
        g.custom_command('restore', 'applications_service_principal_restore')
        g.custom_command('show-app-role-assigned-to', 'applications_service_principal_show_app_role_assigned_to')
        g.custom_command('show-app-role-assignment', 'applications_service_principal_show_app_role_assignment')
        g.custom_command('show-endpoint', 'applications_service_principal_show_endpoint')
        g.custom_command('update-app-role-assigned-to', 'applications_service_principal_update_app_role_assigned_to')
        g.custom_command('update-app-role-assignment', 'applications_service_principal_update_app_role_assignment')
        g.custom_command('update-endpoint', 'applications_service_principal_update_endpoint')
        g.custom_command('validate-property', 'applications_service_principal_validate_property')

    with self.command_group('applications user', applications_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('create-app-role-assignment', 'applications_user_create_app_role_assignment')
        g.custom_command('delete-app-role-assignment', 'applications_user_delete_app_role_assignment')
        g.custom_command('list-app-role-assignment', 'applications_user_list_app_role_assignment')
        g.custom_command('show-app-role-assignment', 'applications_user_show_app_role_assignment')
        g.custom_command('update-app-role-assignment', 'applications_user_update_app_role_assignment')

    with self.command_group('applications_v1_0', is_experimental=True):
        pass
