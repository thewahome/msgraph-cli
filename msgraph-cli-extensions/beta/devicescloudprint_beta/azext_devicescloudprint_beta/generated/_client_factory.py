# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_devicescloudprint_beta_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_devicescloudprint_beta.vendored_sdks.devicescloudprint import DevicesCloudPrint
    return get_mgmt_service_client(cli_ctx,
                                   DevicesCloudPrint,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_print_print(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_print


def cf_print(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print


def cf_print_printer(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_printer


def cf_print_printer_task_trigger(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_printer_task_trigger


def cf_print_printer_share(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_printer_share


def cf_print_printer_share_printer(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_printer_share_printer


def cf_print_report(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_report


def cf_print_service(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_service


def cf_print_share(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_share


def cf_print_share_printer(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_share_printer


def cf_print_task_definition(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_task_definition


def cf_print_task_definition_task(cli_ctx, *_):
    return cf_devicescloudprint_beta_cl(cli_ctx).print_task_definition_task
