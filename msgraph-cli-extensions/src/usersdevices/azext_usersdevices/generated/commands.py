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

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_usersdevices.generated._client_factory import cf_user
    usersdevices_user = CliCommandType(
        operations_tmpl='azext_usersdevices.vendored_sdks.usersdevices.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('usersdevices', usersdevices_user, client_factory=cf_user) as g:
        g.custom_command('create-device', 'usersdevices_create_device')
        g.custom_command('get-device', 'usersdevices_get_device')
        g.custom_command('list-device', 'usersdevices_list_device')
        g.custom_command('update-device', 'usersdevices_update_device')
