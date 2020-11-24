# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_devicescorporatemanagement_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.devicescorporatemanagement import DevicesCorporateManagement
    return get_mgmt_service_client(cli_ctx,
                                   DevicesCorporateManagement,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_device_app_management_device_app_management(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_device_app_management


def cf_device_app_management(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management


def cf_device_app_management_android_managed_app_protection(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_android_managed_app_protection


def cf_device_app_management_default_managed_app_protection(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_default_managed_app_protection


def cf_device_app_management_io_managed_app_protection(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_io_managed_app_protection


def cf_device_app_management_managed_app_policy(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_managed_app_policy


def cf_device_app_management_managed_app_registration(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_managed_app_registration


def cf_device_app_management_managed_app_registration_applied_policy(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_managed_app_registration_applied_policy


def cf_device_app_management_managed_app_registration_intended_policy(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_managed_app_registration_intended_policy


def cf_device_app_management_managed_ebook(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_managed_ebook


def cf_device_app_management_managed_ebook_user_state_summary(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_managed_ebook_user_state_summary


def cf_device_app_management_mobile_app_configuration(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_mobile_app_configuration


def cf_device_app_management_mobile_app(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_mobile_app


def cf_device_app_management_targeted_managed_app_configuration(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_targeted_managed_app_configuration


def cf_device_app_management_vpp_token(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).device_app_management_vpp_token


def cf_user(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).user


def cf_user_managed_device(cli_ctx, *_):
    return cf_devicescorporatemanagement_cl(cli_ctx).user_managed_device
