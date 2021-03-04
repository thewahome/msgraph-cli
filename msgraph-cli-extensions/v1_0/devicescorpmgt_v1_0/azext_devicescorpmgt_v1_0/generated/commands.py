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
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_device_app_management

    devicescorpmgt_v1_0_device_app_management_device_app_management = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_device_app_management_operations#DeviceAppManagementDeviceAppManagementOperations.{}',
        client_factory=cf_device_app_management_device_app_management,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-device-app-management',
        devicescorpmgt_v1_0_device_app_management_device_app_management,
        client_factory=cf_device_app_management_device_app_management,
    ) as g:
        g.custom_command(
            'show-device-app-management',
            'devicescorpmgt_device_app_management_device_app_management_show_device_app_management',
        )
        g.custom_command(
            'update-device-app-management',
            'devicescorpmgt_device_app_management_device_app_management_update_device_app_management',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management

    devicescorpmgt_v1_0_device_app_management = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_operations#DeviceAppManagementOperations.{}',
        client_factory=cf_device_app_management,
    )
    with self.command_group(
        'devicescorpmgt device-app-management',
        devicescorpmgt_v1_0_device_app_management,
        client_factory=cf_device_app_management,
    ) as g:
        g.custom_command('delete', 'devicescorpmgt_device_app_management_delete', confirmation=True)
        g.custom_command(
            'create-android-managed-app-protection',
            'devicescorpmgt_device_app_management_create_android_managed_app_protection',
        )
        g.custom_command(
            'create-default-managed-app-protection',
            'devicescorpmgt_device_app_management_create_default_managed_app_protection',
        )
        g.custom_command(
            'create-io-managed-app-protection', 'devicescorpmgt_device_app_management_create_io_managed_app_protection'
        )
        g.custom_command('create-managed-app-policy', 'devicescorpmgt_device_app_management_create_managed_app_policy')
        g.custom_command(
            'create-managed-app-registration', 'devicescorpmgt_device_app_management_create_managed_app_registration'
        )
        g.custom_command(
            'create-managed-app-statuses', 'devicescorpmgt_device_app_management_create_managed_app_statuses'
        )
        g.custom_command('create-managed-e-book', 'devicescorpmgt_device_app_management_create_managed_e_book')
        g.custom_command(
            'create-mdm-window-information-protection-policy',
            'devicescorpmgt_device_app_management_create_mdm_window_information_protection_policy',
        )
        g.custom_command('create-mobile-app', 'devicescorpmgt_device_app_management_create_mobile_app')
        g.custom_command(
            'create-mobile-app-category', 'devicescorpmgt_device_app_management_create_mobile_app_category'
        )
        g.custom_command(
            'create-mobile-app-configuration', 'devicescorpmgt_device_app_management_create_mobile_app_configuration'
        )
        g.custom_command(
            'create-targeted-managed-app-configuration',
            'devicescorpmgt_device_app_management_create_targeted_managed_app_configuration',
        )
        g.custom_command('create-vpp-token', 'devicescorpmgt_device_app_management_create_vpp_token')
        g.custom_command(
            'create-window-information-protection-policy',
            'devicescorpmgt_device_app_management_create_window_information_protection_policy',
        )
        g.custom_command(
            'list-android-managed-app-protection',
            'devicescorpmgt_device_app_management_list_android_managed_app_protection',
        )
        g.custom_command(
            'list-default-managed-app-protection',
            'devicescorpmgt_device_app_management_list_default_managed_app_protection',
        )
        g.custom_command(
            'list-io-managed-app-protection', 'devicescorpmgt_device_app_management_list_io_managed_app_protection'
        )
        g.custom_command('list-managed-app-policy', 'devicescorpmgt_device_app_management_list_managed_app_policy')
        g.custom_command(
            'list-managed-app-registration', 'devicescorpmgt_device_app_management_list_managed_app_registration'
        )
        g.custom_command('list-managed-app-statuses', 'devicescorpmgt_device_app_management_list_managed_app_statuses')
        g.custom_command('list-managed-e-book', 'devicescorpmgt_device_app_management_list_managed_e_book')
        g.custom_command(
            'list-mdm-window-information-protection-policy',
            'devicescorpmgt_device_app_management_list_mdm_window_information_protection_policy',
        )
        g.custom_command('list-mobile-app', 'devicescorpmgt_device_app_management_list_mobile_app')
        g.custom_command('list-mobile-app-category', 'devicescorpmgt_device_app_management_list_mobile_app_category')
        g.custom_command(
            'list-mobile-app-configuration', 'devicescorpmgt_device_app_management_list_mobile_app_configuration'
        )
        g.custom_command(
            'list-targeted-managed-app-configuration',
            'devicescorpmgt_device_app_management_list_targeted_managed_app_configuration',
        )
        g.custom_command('list-vpp-token', 'devicescorpmgt_device_app_management_list_vpp_token')
        g.custom_command(
            'list-window-information-protection-policy',
            'devicescorpmgt_device_app_management_list_window_information_protection_policy',
        )
        g.custom_command(
            'show-android-managed-app-protection',
            'devicescorpmgt_device_app_management_show_android_managed_app_protection',
        )
        g.custom_command(
            'show-default-managed-app-protection',
            'devicescorpmgt_device_app_management_show_default_managed_app_protection',
        )
        g.custom_command(
            'show-io-managed-app-protection', 'devicescorpmgt_device_app_management_show_io_managed_app_protection'
        )
        g.custom_command('show-managed-app-policy', 'devicescorpmgt_device_app_management_show_managed_app_policy')
        g.custom_command(
            'show-managed-app-registration', 'devicescorpmgt_device_app_management_show_managed_app_registration'
        )
        g.custom_command('show-managed-app-statuses', 'devicescorpmgt_device_app_management_show_managed_app_statuses')
        g.custom_command('show-managed-e-book', 'devicescorpmgt_device_app_management_show_managed_e_book')
        g.custom_command(
            'show-mdm-window-information-protection-policy',
            'devicescorpmgt_device_app_management_show_mdm_window_information_protection_policy',
        )
        g.custom_command('show-mobile-app', 'devicescorpmgt_device_app_management_show_mobile_app')
        g.custom_command('show-mobile-app-category', 'devicescorpmgt_device_app_management_show_mobile_app_category')
        g.custom_command(
            'show-mobile-app-configuration', 'devicescorpmgt_device_app_management_show_mobile_app_configuration'
        )
        g.custom_command(
            'show-targeted-managed-app-configuration',
            'devicescorpmgt_device_app_management_show_targeted_managed_app_configuration',
        )
        g.custom_command('show-vpp-token', 'devicescorpmgt_device_app_management_show_vpp_token')
        g.custom_command(
            'show-window-information-protection-policy',
            'devicescorpmgt_device_app_management_show_window_information_protection_policy',
        )
        g.custom_command(
            'sync-microsoft-store-for-business-app',
            'devicescorpmgt_device_app_management_sync_microsoft_store_for_business_app',
        )
        g.custom_command(
            'update-android-managed-app-protection',
            'devicescorpmgt_device_app_management_update_android_managed_app_protection',
        )
        g.custom_command(
            'update-default-managed-app-protection',
            'devicescorpmgt_device_app_management_update_default_managed_app_protection',
        )
        g.custom_command(
            'update-io-managed-app-protection', 'devicescorpmgt_device_app_management_update_io_managed_app_protection'
        )
        g.custom_command('update-managed-app-policy', 'devicescorpmgt_device_app_management_update_managed_app_policy')
        g.custom_command(
            'update-managed-app-registration', 'devicescorpmgt_device_app_management_update_managed_app_registration'
        )
        g.custom_command(
            'update-managed-app-statuses', 'devicescorpmgt_device_app_management_update_managed_app_statuses'
        )
        g.custom_command('update-managed-e-book', 'devicescorpmgt_device_app_management_update_managed_e_book')
        g.custom_command(
            'update-mdm-window-information-protection-policy',
            'devicescorpmgt_device_app_management_update_mdm_window_information_protection_policy',
        )
        g.custom_command('update-mobile-app', 'devicescorpmgt_device_app_management_update_mobile_app')
        g.custom_command(
            'update-mobile-app-category', 'devicescorpmgt_device_app_management_update_mobile_app_category'
        )
        g.custom_command(
            'update-mobile-app-configuration', 'devicescorpmgt_device_app_management_update_mobile_app_configuration'
        )
        g.custom_command(
            'update-targeted-managed-app-configuration',
            'devicescorpmgt_device_app_management_update_targeted_managed_app_configuration',
        )
        g.custom_command('update-vpp-token', 'devicescorpmgt_device_app_management_update_vpp_token')
        g.custom_command(
            'update-window-information-protection-policy',
            'devicescorpmgt_device_app_management_update_window_information_protection_policy',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import (
        cf_device_app_management_android_managed_app_protection,
    )

    devicescorpmgt_v1_0_device_app_management_android_managed_app_protection = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_android_managed_app_protection_operations#DeviceAppManagementAndroidManagedAppProtectionOperations.{}',
        client_factory=cf_device_app_management_android_managed_app_protection,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-android-managed-app-protection',
        devicescorpmgt_v1_0_device_app_management_android_managed_app_protection,
        client_factory=cf_device_app_management_android_managed_app_protection,
    ) as g:
        g.custom_command(
            'delete', 'devicescorpmgt_device_app_management_android_managed_app_protection_delete', confirmation=True
        )
        g.custom_command('create-app', 'devicescorpmgt_device_app_management_android_managed_app_protection_create_app')
        g.custom_command('list-app', 'devicescorpmgt_device_app_management_android_managed_app_protection_list_app')
        g.custom_command('show-app', 'devicescorpmgt_device_app_management_android_managed_app_protection_show_app')
        g.custom_command(
            'show-deployment-summary',
            'devicescorpmgt_device_app_management_android_managed_app_protection_show_deployment_summary',
        )
        g.custom_command('update-app', 'devicescorpmgt_device_app_management_android_managed_app_protection_update_app')
        g.custom_command(
            'update-deployment-summary',
            'devicescorpmgt_device_app_management_android_managed_app_protection_update_deployment_summary',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import (
        cf_device_app_management_default_managed_app_protection,
    )

    devicescorpmgt_v1_0_device_app_management_default_managed_app_protection = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_default_managed_app_protection_operations#DeviceAppManagementDefaultManagedAppProtectionOperations.{}',
        client_factory=cf_device_app_management_default_managed_app_protection,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-default-managed-app-protection',
        devicescorpmgt_v1_0_device_app_management_default_managed_app_protection,
        client_factory=cf_device_app_management_default_managed_app_protection,
    ) as g:
        g.custom_command(
            'delete', 'devicescorpmgt_device_app_management_default_managed_app_protection_delete', confirmation=True
        )
        g.custom_command('create-app', 'devicescorpmgt_device_app_management_default_managed_app_protection_create_app')
        g.custom_command('list-app', 'devicescorpmgt_device_app_management_default_managed_app_protection_list_app')
        g.custom_command('show-app', 'devicescorpmgt_device_app_management_default_managed_app_protection_show_app')
        g.custom_command(
            'show-deployment-summary',
            'devicescorpmgt_device_app_management_default_managed_app_protection_show_deployment_summary',
        )
        g.custom_command('update-app', 'devicescorpmgt_device_app_management_default_managed_app_protection_update_app')
        g.custom_command(
            'update-deployment-summary',
            'devicescorpmgt_device_app_management_default_managed_app_protection_update_deployment_summary',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_io_managed_app_protection

    devicescorpmgt_v1_0_device_app_management_io_managed_app_protection = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_io_managed_app_protection_operations#DeviceAppManagementIoManagedAppProtectionOperations.{}',
        client_factory=cf_device_app_management_io_managed_app_protection,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-io-managed-app-protection',
        devicescorpmgt_v1_0_device_app_management_io_managed_app_protection,
        client_factory=cf_device_app_management_io_managed_app_protection,
    ) as g:
        g.custom_command(
            'delete', 'devicescorpmgt_device_app_management_io_managed_app_protection_delete', confirmation=True
        )
        g.custom_command('create-app', 'devicescorpmgt_device_app_management_io_managed_app_protection_create_app')
        g.custom_command('list-app', 'devicescorpmgt_device_app_management_io_managed_app_protection_list_app')
        g.custom_command('show-app', 'devicescorpmgt_device_app_management_io_managed_app_protection_show_app')
        g.custom_command(
            'show-deployment-summary',
            'devicescorpmgt_device_app_management_io_managed_app_protection_show_deployment_summary',
        )
        g.custom_command('update-app', 'devicescorpmgt_device_app_management_io_managed_app_protection_update_app')
        g.custom_command(
            'update-deployment-summary',
            'devicescorpmgt_device_app_management_io_managed_app_protection_update_deployment_summary',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_managed_app_policy

    devicescorpmgt_v1_0_device_app_management_managed_app_policy = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_managed_app_policy_operations#DeviceAppManagementManagedAppPolicyOperations.{}',
        client_factory=cf_device_app_management_managed_app_policy,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-managed-app-policy',
        devicescorpmgt_v1_0_device_app_management_managed_app_policy,
        client_factory=cf_device_app_management_managed_app_policy,
    ) as g:
        g.custom_command('target-app', 'devicescorpmgt_device_app_management_managed_app_policy_target_app')

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_managed_app_registration

    devicescorpmgt_v1_0_device_app_management_managed_app_registration = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_managed_app_registration_operations#DeviceAppManagementManagedAppRegistrationOperations.{}',
        client_factory=cf_device_app_management_managed_app_registration,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-managed-app-registration',
        devicescorpmgt_v1_0_device_app_management_managed_app_registration,
        client_factory=cf_device_app_management_managed_app_registration,
    ) as g:
        g.custom_command(
            'delete', 'devicescorpmgt_device_app_management_managed_app_registration_delete', confirmation=True
        )
        g.custom_command(
            'create-applied-policy',
            'devicescorpmgt_device_app_management_managed_app_registration_create_applied_policy',
        )
        g.custom_command(
            'create-intended-policy',
            'devicescorpmgt_device_app_management_managed_app_registration_create_intended_policy',
        )
        g.custom_command(
            'create-operation', 'devicescorpmgt_device_app_management_managed_app_registration_create_operation'
        )
        g.custom_command(
            'list-applied-policy', 'devicescorpmgt_device_app_management_managed_app_registration_list_applied_policy'
        )
        g.custom_command(
            'list-intended-policy', 'devicescorpmgt_device_app_management_managed_app_registration_list_intended_policy'
        )
        g.custom_command(
            'list-operation', 'devicescorpmgt_device_app_management_managed_app_registration_list_operation'
        )
        g.custom_command(
            'show-applied-policy', 'devicescorpmgt_device_app_management_managed_app_registration_show_applied_policy'
        )
        g.custom_command(
            'show-intended-policy', 'devicescorpmgt_device_app_management_managed_app_registration_show_intended_policy'
        )
        g.custom_command(
            'show-operation', 'devicescorpmgt_device_app_management_managed_app_registration_show_operation'
        )
        g.custom_command(
            'show-user-id-with-flagged-app-registration',
            'devicescorpmgt_device_app_management_managed_app_registration_show_user_id_with_flagged_app_registration',
        )
        g.custom_command(
            'update-applied-policy',
            'devicescorpmgt_device_app_management_managed_app_registration_update_applied_policy',
        )
        g.custom_command(
            'update-intended-policy',
            'devicescorpmgt_device_app_management_managed_app_registration_update_intended_policy',
        )
        g.custom_command(
            'update-operation', 'devicescorpmgt_device_app_management_managed_app_registration_update_operation'
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import (
        cf_device_app_management_managed_app_registration_applied_policy,
    )

    devicescorpmgt_v1_0_device_app_management_managed_app_registration_applied_policy = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_managed_app_registration_applied_policy_operations#DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations.{}',
        client_factory=cf_device_app_management_managed_app_registration_applied_policy,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-managed-app-registration-applied-policy',
        devicescorpmgt_v1_0_device_app_management_managed_app_registration_applied_policy,
        client_factory=cf_device_app_management_managed_app_registration_applied_policy,
    ) as g:
        g.custom_command(
            'target-app', 'devicescorpmgt_device_app_management_managed_app_registration_applied_policy_target_app'
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import (
        cf_device_app_management_managed_app_registration_intended_policy,
    )

    devicescorpmgt_v1_0_device_app_management_managed_app_registration_intended_policy = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_managed_app_registration_intended_policy_operations#DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations.{}',
        client_factory=cf_device_app_management_managed_app_registration_intended_policy,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-managed-app-registration-intended-policy',
        devicescorpmgt_v1_0_device_app_management_managed_app_registration_intended_policy,
        client_factory=cf_device_app_management_managed_app_registration_intended_policy,
    ) as g:
        g.custom_command(
            'target-app', 'devicescorpmgt_device_app_management_managed_app_registration_intended_policy_target_app'
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_managed_ebook

    devicescorpmgt_v1_0_device_app_management_managed_ebook = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_managed_ebook_operations#DeviceAppManagementManagedEBookOperations.{}',
        client_factory=cf_device_app_management_managed_ebook,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-managed-e-book',
        devicescorpmgt_v1_0_device_app_management_managed_ebook,
        client_factory=cf_device_app_management_managed_ebook,
    ) as g:
        g.custom_command('delete', 'devicescorpmgt_device_app_management_managed_e_book_delete', confirmation=True)
        g.custom_command('assign', 'devicescorpmgt_device_app_management_managed_e_book_assign')
        g.custom_command('create-assignment', 'devicescorpmgt_device_app_management_managed_e_book_create_assignment')
        g.custom_command(
            'create-device-state', 'devicescorpmgt_device_app_management_managed_e_book_create_device_state'
        )
        g.custom_command(
            'create-user-state-summary', 'devicescorpmgt_device_app_management_managed_e_book_create_user_state_summary'
        )
        g.custom_command('list-assignment', 'devicescorpmgt_device_app_management_managed_e_book_list_assignment')
        g.custom_command('list-device-state', 'devicescorpmgt_device_app_management_managed_e_book_list_device_state')
        g.custom_command(
            'list-user-state-summary', 'devicescorpmgt_device_app_management_managed_e_book_list_user_state_summary'
        )
        g.custom_command('show-assignment', 'devicescorpmgt_device_app_management_managed_e_book_show_assignment')
        g.custom_command('show-device-state', 'devicescorpmgt_device_app_management_managed_e_book_show_device_state')
        g.custom_command(
            'show-install-summary', 'devicescorpmgt_device_app_management_managed_e_book_show_install_summary'
        )
        g.custom_command(
            'show-user-state-summary', 'devicescorpmgt_device_app_management_managed_e_book_show_user_state_summary'
        )
        g.custom_command('update-assignment', 'devicescorpmgt_device_app_management_managed_e_book_update_assignment')
        g.custom_command(
            'update-device-state', 'devicescorpmgt_device_app_management_managed_e_book_update_device_state'
        )
        g.custom_command(
            'update-install-summary', 'devicescorpmgt_device_app_management_managed_e_book_update_install_summary'
        )
        g.custom_command(
            'update-user-state-summary', 'devicescorpmgt_device_app_management_managed_e_book_update_user_state_summary'
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import (
        cf_device_app_management_managed_ebook_user_state_summary,
    )

    devicescorpmgt_v1_0_device_app_management_managed_ebook_user_state_summary = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_managed_ebook_user_state_summary_operations#DeviceAppManagementManagedEBookUserStateSummaryOperations.{}',
        client_factory=cf_device_app_management_managed_ebook_user_state_summary,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-managed-e-book-user-state-summary',
        devicescorpmgt_v1_0_device_app_management_managed_ebook_user_state_summary,
        client_factory=cf_device_app_management_managed_ebook_user_state_summary,
    ) as g:
        g.custom_command(
            'delete', 'devicescorpmgt_device_app_management_managed_e_book_user_state_summary_delete', confirmation=True
        )
        g.custom_command(
            'create-device-state',
            'devicescorpmgt_device_app_management_managed_e_book_user_state_summary_create_device_state',
        )
        g.custom_command(
            'list-device-state',
            'devicescorpmgt_device_app_management_managed_e_book_user_state_summary_list_device_state',
        )
        g.custom_command(
            'show-device-state',
            'devicescorpmgt_device_app_management_managed_e_book_user_state_summary_show_device_state',
        )
        g.custom_command(
            'update-device-state',
            'devicescorpmgt_device_app_management_managed_e_book_user_state_summary_update_device_state',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_mobile_app_configuration

    devicescorpmgt_v1_0_device_app_management_mobile_app_configuration = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_mobile_app_configuration_operations#DeviceAppManagementMobileAppConfigurationOperations.{}',
        client_factory=cf_device_app_management_mobile_app_configuration,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-mobile-app-configuration',
        devicescorpmgt_v1_0_device_app_management_mobile_app_configuration,
        client_factory=cf_device_app_management_mobile_app_configuration,
    ) as g:
        g.custom_command(
            'delete', 'devicescorpmgt_device_app_management_mobile_app_configuration_delete', confirmation=True
        )
        g.custom_command('assign', 'devicescorpmgt_device_app_management_mobile_app_configuration_assign')
        g.custom_command(
            'create-assignment', 'devicescorpmgt_device_app_management_mobile_app_configuration_create_assignment'
        )
        g.custom_command(
            'create-device-statuses',
            'devicescorpmgt_device_app_management_mobile_app_configuration_create_device_statuses',
        )
        g.custom_command(
            'create-user-statuses', 'devicescorpmgt_device_app_management_mobile_app_configuration_create_user_statuses'
        )
        g.custom_command(
            'list-assignment', 'devicescorpmgt_device_app_management_mobile_app_configuration_list_assignment'
        )
        g.custom_command(
            'list-device-statuses', 'devicescorpmgt_device_app_management_mobile_app_configuration_list_device_statuses'
        )
        g.custom_command(
            'list-user-statuses', 'devicescorpmgt_device_app_management_mobile_app_configuration_list_user_statuses'
        )
        g.custom_command(
            'show-assignment', 'devicescorpmgt_device_app_management_mobile_app_configuration_show_assignment'
        )
        g.custom_command(
            'show-device-status-summary',
            'devicescorpmgt_device_app_management_mobile_app_configuration_show_device_status_summary',
        )
        g.custom_command(
            'show-device-statuses', 'devicescorpmgt_device_app_management_mobile_app_configuration_show_device_statuses'
        )
        g.custom_command(
            'show-user-status-summary',
            'devicescorpmgt_device_app_management_mobile_app_configuration_show_user_status_summary',
        )
        g.custom_command(
            'show-user-statuses', 'devicescorpmgt_device_app_management_mobile_app_configuration_show_user_statuses'
        )
        g.custom_command(
            'update-assignment', 'devicescorpmgt_device_app_management_mobile_app_configuration_update_assignment'
        )
        g.custom_command(
            'update-device-status-summary',
            'devicescorpmgt_device_app_management_mobile_app_configuration_update_device_status_summary',
        )
        g.custom_command(
            'update-device-statuses',
            'devicescorpmgt_device_app_management_mobile_app_configuration_update_device_statuses',
        )
        g.custom_command(
            'update-user-status-summary',
            'devicescorpmgt_device_app_management_mobile_app_configuration_update_user_status_summary',
        )
        g.custom_command(
            'update-user-statuses', 'devicescorpmgt_device_app_management_mobile_app_configuration_update_user_statuses'
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_mobile_app

    devicescorpmgt_v1_0_device_app_management_mobile_app = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_mobile_app_operations#DeviceAppManagementMobileAppOperations.{}',
        client_factory=cf_device_app_management_mobile_app,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-mobile-app',
        devicescorpmgt_v1_0_device_app_management_mobile_app,
        client_factory=cf_device_app_management_mobile_app,
    ) as g:
        g.custom_command('delete', 'devicescorpmgt_device_app_management_mobile_app_delete', confirmation=True)
        g.custom_command('assign', 'devicescorpmgt_device_app_management_mobile_app_assign')
        g.custom_command('create-assignment', 'devicescorpmgt_device_app_management_mobile_app_create_assignment')
        g.custom_command('create-ref-category', 'devicescorpmgt_device_app_management_mobile_app_create_ref_category')
        g.custom_command('list-assignment', 'devicescorpmgt_device_app_management_mobile_app_list_assignment')
        g.custom_command('list-category', 'devicescorpmgt_device_app_management_mobile_app_list_category')
        g.custom_command('list-ref-category', 'devicescorpmgt_device_app_management_mobile_app_list_ref_category')
        g.custom_command('show-assignment', 'devicescorpmgt_device_app_management_mobile_app_show_assignment')
        g.custom_command('update-assignment', 'devicescorpmgt_device_app_management_mobile_app_update_assignment')

    from azext_devicescorpmgt_v1_0.generated._client_factory import (
        cf_device_app_management_targeted_managed_app_configuration,
    )

    devicescorpmgt_v1_0_device_app_management_targeted_managed_app_configuration = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_targeted_managed_app_configuration_operations#DeviceAppManagementTargetedManagedAppConfigurationOperations.{}',
        client_factory=cf_device_app_management_targeted_managed_app_configuration,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-targeted-managed-app-configuration',
        devicescorpmgt_v1_0_device_app_management_targeted_managed_app_configuration,
        client_factory=cf_device_app_management_targeted_managed_app_configuration,
    ) as g:
        g.custom_command(
            'delete',
            'devicescorpmgt_device_app_management_targeted_managed_app_configuration_delete',
            confirmation=True,
        )
        g.custom_command('assign', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_assign')
        g.custom_command(
            'create-app', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_create_app'
        )
        g.custom_command(
            'create-assignment',
            'devicescorpmgt_device_app_management_targeted_managed_app_configuration_create_assignment',
        )
        g.custom_command('list-app', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_list_app')
        g.custom_command(
            'list-assignment', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_list_assignment'
        )
        g.custom_command('show-app', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_show_app')
        g.custom_command(
            'show-assignment', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_show_assignment'
        )
        g.custom_command(
            'show-deployment-summary',
            'devicescorpmgt_device_app_management_targeted_managed_app_configuration_show_deployment_summary',
        )
        g.custom_command(
            'target-app', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_target_app'
        )
        g.custom_command(
            'update-app', 'devicescorpmgt_device_app_management_targeted_managed_app_configuration_update_app'
        )
        g.custom_command(
            'update-assignment',
            'devicescorpmgt_device_app_management_targeted_managed_app_configuration_update_assignment',
        )
        g.custom_command(
            'update-deployment-summary',
            'devicescorpmgt_device_app_management_targeted_managed_app_configuration_update_deployment_summary',
        )

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_device_app_management_vpp_token

    devicescorpmgt_v1_0_device_app_management_vpp_token = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._device_app_management_vpp_token_operations#DeviceAppManagementVppTokenOperations.{}',
        client_factory=cf_device_app_management_vpp_token,
    )
    with self.command_group(
        'devicescorpmgt device-app-management-vpp-token',
        devicescorpmgt_v1_0_device_app_management_vpp_token,
        client_factory=cf_device_app_management_vpp_token,
    ) as g:
        g.custom_command('sync-license', 'devicescorpmgt_device_app_management_vpp_token_sync_license')

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_user

    devicescorpmgt_v1_0_user = CliCommandType(
        operations_tmpl=(
            'azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._user_operations#UserOperations.{}'
        ),
        client_factory=cf_user,
    )
    with self.command_group('devicescorpmgt user', devicescorpmgt_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'devicescorpmgt_user_delete', confirmation=True)
        g.custom_command(
            'create-device-management-troubleshooting-event',
            'devicescorpmgt_user_create_device_management_troubleshooting_event',
        )
        g.custom_command('create-managed-device', 'devicescorpmgt_user_create_managed_device')
        g.custom_command(
            'create-ref-managed-app-registration', 'devicescorpmgt_user_create_ref_managed_app_registration'
        )
        g.custom_command(
            'list-device-management-troubleshooting-event',
            'devicescorpmgt_user_list_device_management_troubleshooting_event',
        )
        g.custom_command('list-managed-app-registration', 'devicescorpmgt_user_list_managed_app_registration')
        g.custom_command('list-managed-device', 'devicescorpmgt_user_list_managed_device')
        g.custom_command('list-ref-managed-app-registration', 'devicescorpmgt_user_list_ref_managed_app_registration')
        g.custom_command(
            'show-device-management-troubleshooting-event',
            'devicescorpmgt_user_show_device_management_troubleshooting_event',
        )
        g.custom_command('show-managed-device', 'devicescorpmgt_user_show_managed_device')
        g.custom_command(
            'update-device-management-troubleshooting-event',
            'devicescorpmgt_user_update_device_management_troubleshooting_event',
        )
        g.custom_command('update-managed-device', 'devicescorpmgt_user_update_managed_device')

    from azext_devicescorpmgt_v1_0.generated._client_factory import cf_user_managed_device

    devicescorpmgt_v1_0_user_managed_device = CliCommandType(
        operations_tmpl='azext_devicescorpmgt_v1_0.vendored_sdks.devicescorpmgt.operations._user_managed_device_operations#UserManagedDeviceOperations.{}',
        client_factory=cf_user_managed_device,
    )
    with self.command_group(
        'devicescorpmgt user-managed-device',
        devicescorpmgt_v1_0_user_managed_device,
        client_factory=cf_user_managed_device,
    ) as g:
        g.custom_command('delete', 'devicescorpmgt_user_managed_device_delete', confirmation=True)
        g.custom_command(
            'create-device-compliance-policy-state',
            'devicescorpmgt_user_managed_device_create_device_compliance_policy_state',
        )
        g.custom_command(
            'create-device-configuration-state', 'devicescorpmgt_user_managed_device_create_device_configuration_state'
        )
        g.custom_command(
            'list-device-compliance-policy-state',
            'devicescorpmgt_user_managed_device_list_device_compliance_policy_state',
        )
        g.custom_command(
            'list-device-configuration-state', 'devicescorpmgt_user_managed_device_list_device_configuration_state'
        )
        g.custom_command('show-device-category', 'devicescorpmgt_user_managed_device_show_device_category')
        g.custom_command(
            'show-device-compliance-policy-state',
            'devicescorpmgt_user_managed_device_show_device_compliance_policy_state',
        )
        g.custom_command(
            'show-device-configuration-state', 'devicescorpmgt_user_managed_device_show_device_configuration_state'
        )
        g.custom_command('update-device-category', 'devicescorpmgt_user_managed_device_update_device_category')
        g.custom_command(
            'update-device-compliance-policy-state',
            'devicescorpmgt_user_managed_device_update_device_compliance_policy_state',
        )
        g.custom_command(
            'update-device-configuration-state', 'devicescorpmgt_user_managed_device_update_device_configuration_state'
        )

    with self.command_group('devicescorpmgt_v1_0', is_experimental=True):
        pass
