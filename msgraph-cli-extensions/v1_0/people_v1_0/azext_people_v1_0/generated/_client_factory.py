# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_people_v1_0_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.people import People
    return get_mgmt_service_client(cli_ctx,
                                   People,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user(cli_ctx, *_):
    return cf_people_v1_0_cl(cli_ctx).user


def cf_user_insight(cli_ctx, *_):
    return cf_people_v1_0_cl(cli_ctx).user_insight


def cf_user_insight_shared(cli_ctx, *_):
    return cf_people_v1_0_cl(cli_ctx).user_insight_shared


def cf_user_insight_trending(cli_ctx, *_):
    return cf_people_v1_0_cl(cli_ctx).user_insight_trending


def cf_user_insight_used(cli_ctx, *_):
    return cf_people_v1_0_cl(cli_ctx).user_insight_used
