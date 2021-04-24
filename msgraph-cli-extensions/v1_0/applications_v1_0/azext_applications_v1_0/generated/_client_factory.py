# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_applications_v1_0_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_applications_v1_0.vendored_sdks.applications import Applications
    return get_mgmt_service_client(cli_ctx,
                                   Applications,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_application_application(cli_ctx, *_):
    return cf_applications_v1_0_cl(cli_ctx).applications_application


def cf_application(cli_ctx, *_):
    return cf_applications_v1_0_cl(cli_ctx).applications


def cf_group(cli_ctx, *_):
    return cf_applications_v1_0_cl(cli_ctx).groups


def cf_service_principal_service_principal(cli_ctx, *_):
    return cf_applications_v1_0_cl(cli_ctx).service_principals_service_principal


def cf_service_principal(cli_ctx, *_):
    return cf_applications_v1_0_cl(cli_ctx).service_principals


def cf_user(cli_ctx, *_):
    return cf_applications_v1_0_cl(cli_ctx).users
