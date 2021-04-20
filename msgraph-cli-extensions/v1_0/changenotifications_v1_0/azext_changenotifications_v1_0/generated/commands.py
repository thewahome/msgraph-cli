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
from azext_changenotifications_v1_0.generated._client_factory import cf_subscriptionssubscription


changenotifications_v1_0_subscriptionssubscription = CliCommandType(
    operations_tmpl='azext_changenotifications_v1_0.vendored_sdks.changenotifications.operations._subscriptionssubscription_operations#subscriptionssubscriptionOperations.{}',
    client_factory=cf_subscriptionssubscription,
)


def load_command_table(self, _):

    with self.command_group(
        'changenotifications subscriptionssubscription',
        changenotifications_v1_0_subscriptionssubscription,
        client_factory=cf_subscriptionssubscription,
    ) as g:
        g.custom_command('create-subscription', 'changenotifications_subscriptionssubscription_create_subscription')
        g.custom_command('delete-subscription', 'changenotifications_subscriptionssubscription_delete_subscription')
        g.custom_command('list-subscription', 'changenotifications_subscriptionssubscription_list_subscription')
        g.custom_command('show-subscription', 'changenotifications_subscriptionssubscription_show_subscription')
        g.custom_command('update-subscription', 'changenotifications_subscriptionssubscription_update_subscription')

    with self.command_group('changenotifications_v1_0', is_experimental=True):
        pass
