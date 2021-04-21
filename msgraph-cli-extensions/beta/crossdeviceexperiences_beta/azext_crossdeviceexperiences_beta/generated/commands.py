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
from azext_crossdeviceexperiences_beta.generated._client_factory import (
    cf_user,
    cf_usersactivity,
    cf_usersactivitieshistoryitem,
)


crossdeviceexperiences_beta_user = CliCommandType(
    operations_tmpl='azext_crossdeviceexperiences_beta.vendored_sdks.crossdeviceexperiences.operations._users_operations#usersOperations.{}',
    client_factory=cf_user,
)


crossdeviceexperiences_beta_usersactivity = CliCommandType(
    operations_tmpl='azext_crossdeviceexperiences_beta.vendored_sdks.crossdeviceexperiences.operations._usersactivities_operations#usersactivitiesOperations.{}',
    client_factory=cf_usersactivity,
)


crossdeviceexperiences_beta_usersactivitieshistoryitem = CliCommandType(
    operations_tmpl='azext_crossdeviceexperiences_beta.vendored_sdks.crossdeviceexperiences.operations._usersactivitieshistoryitems_operations#usersactivitieshistoryitemsOperations.{}',
    client_factory=cf_usersactivitieshistoryitem,
)


def load_command_table(self, _):

    with self.command_group(
        'crossdeviceexperiences user', crossdeviceexperiences_beta_user, client_factory=cf_user
    ) as g:
        g.custom_command('create-activity', 'crossdeviceexperiences_user_create_activity')
        g.custom_command('create-device', 'crossdeviceexperiences_user_create_device')
        g.custom_command('delete-activity', 'crossdeviceexperiences_user_delete_activity')
        g.custom_command('delete-device', 'crossdeviceexperiences_user_delete_device')
        g.custom_command('list-activity', 'crossdeviceexperiences_user_list_activity')
        g.custom_command('list-device', 'crossdeviceexperiences_user_list_device')
        g.custom_command('show-activity', 'crossdeviceexperiences_user_show_activity')
        g.custom_command('show-device', 'crossdeviceexperiences_user_show_device')
        g.custom_command('update-activity', 'crossdeviceexperiences_user_update_activity')
        g.custom_command('update-device', 'crossdeviceexperiences_user_update_device')

    with self.command_group(
        'crossdeviceexperiences usersactivity',
        crossdeviceexperiences_beta_usersactivity,
        client_factory=cf_usersactivity,
    ) as g:
        g.custom_command('create-history-item', 'crossdeviceexperiences_usersactivity_create_history_item')
        g.custom_command('delete-history-item', 'crossdeviceexperiences_usersactivity_delete_history_item')
        g.custom_command('list-history-item', 'crossdeviceexperiences_usersactivity_list_history_item')
        g.custom_command('show-history-item', 'crossdeviceexperiences_usersactivity_show_history_item')
        g.custom_command('update-history-item', 'crossdeviceexperiences_usersactivity_update_history_item')

    with self.command_group(
        'crossdeviceexperiences usersactivitieshistoryitem',
        crossdeviceexperiences_beta_usersactivitieshistoryitem,
        client_factory=cf_usersactivitieshistoryitem,
    ) as g:
        g.custom_command('delete-ref-activity', 'crossdeviceexperiences_usersactivitieshistoryitem_delete_ref_activity')
        g.custom_command('set-ref-activity', 'crossdeviceexperiences_usersactivitieshistoryitem_set_ref_activity')
        g.custom_command('show-activity', 'crossdeviceexperiences_usersactivitieshistoryitem_show_activity')
        g.custom_command('show-ref-activity', 'crossdeviceexperiences_usersactivitieshistoryitem_show_ref_activity')

    with self.command_group('crossdeviceexperiences_beta', is_experimental=True):
        pass
