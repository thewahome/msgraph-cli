# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_reports_v1_0_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_reports_v1_0.vendored_sdks.reports import Reports
    return get_mgmt_service_client(cli_ctx,
                                   Reports,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_audit_log_audit_log_root(cli_ctx, *_):
    return cf_reports_v1_0_cl(cli_ctx).audit_log_audit_log_root


def cf_audit_log(cli_ctx, *_):
    return cf_reports_v1_0_cl(cli_ctx).audit_log


def cf_report_report_root(cli_ctx, *_):
    return cf_reports_v1_0_cl(cli_ctx).report_report_root


def cf_report(cli_ctx, *_):
    return cf_reports_v1_0_cl(cli_ctx).report
