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

    from azext_teamschats.generated._client_factory import cf_chat_chat
    teamschats_chat_chat = CliCommandType(
        operations_tmpl='azext_teamschats.vendored_sdks.teamschats.operations._chat_chat_operations#ChatOperations.{}',
        client_factory=cf_chat_chat)
    with self.command_group('teamschats', teamschats_chat_chat, client_factory=cf_chat_chat) as g:
        g.custom_command('update', 'teamschats_update')
        g.custom_command('delete', 'teamschats_delete')
        g.custom_command('create-chat', 'teamschats_create_chat')
        g.custom_command('get-chat', 'teamschats_get_chat')
        g.custom_command('list-chat', 'teamschats_list_chat')

    from azext_teamschats.generated._client_factory import cf_chat
    teamschats_chat = CliCommandType(
        operations_tmpl='azext_teamschats.vendored_sdks.teamschats.operations._chat_operations#ChatOperations.{}',
        client_factory=cf_chat)
    with self.command_group('teamschats', teamschats_chat, client_factory=cf_chat) as g:
        g.custom_command('update', 'teamschats_update')
        g.custom_command('all-message', 'teamschats_all_message')
        g.custom_command('create-installed-app', 'teamschats_create_installed_app')
        g.custom_command('create-member', 'teamschats_create_member')
        g.custom_command('create-message', 'teamschats_create_message')
        g.custom_command('get-installed-app', 'teamschats_get_installed_app')
        g.custom_command('get-member', 'teamschats_get_member')
        g.custom_command('get-message', 'teamschats_get_message')
        g.custom_command('list-installed-app', 'teamschats_list_installed_app')
        g.custom_command('list-member', 'teamschats_list_member')
        g.custom_command('list-message', 'teamschats_list_message')

    from azext_teamschats.generated._client_factory import cf_chat_installed_app
    teamschats_chat_installed_app = CliCommandType(
        operations_tmpl='azext_teamschats.vendored_sdks.teamschats.operations._chat_installed_app_operations#ChatInstal'
        'ledAppOperations.{}',
        client_factory=cf_chat_installed_app)
    with self.command_group('teamschats', teamschats_chat_installed_app, client_factory=cf_chat_installed_app) as g:
        g.custom_command('get-team-app', 'teamschats_get_team_app')
        g.custom_command('get-team-app-definition', 'teamschats_get_team_app_definition')
        g.custom_command('upgrade', 'teamschats_upgrade')

    from azext_teamschats.generated._client_factory import cf_chat_message
    teamschats_chat_message = CliCommandType(
        operations_tmpl='azext_teamschats.vendored_sdks.teamschats.operations._chat_message_operations#ChatMessageOpera'
        'tions.{}',
        client_factory=cf_chat_message)
    with self.command_group('teamschats', teamschats_chat_message, client_factory=cf_chat_message) as g:
        g.custom_command('update', 'teamschats_update')
        g.custom_command('create-hosted-content', 'teamschats_create_hosted_content')
        g.custom_command('create-reply', 'teamschats_create_reply')
        g.custom_command('delta', 'teamschats_delta')
        g.custom_command('get-hosted-content', 'teamschats_get_hosted_content')
        g.custom_command('get-reply', 'teamschats_get_reply')
        g.custom_command('list-hosted-content', 'teamschats_list_hosted_content')
        g.custom_command('list-reply', 'teamschats_list_reply')

    from azext_teamschats.generated._client_factory import cf_chat_message_reply
    teamschats_chat_message_reply = CliCommandType(
        operations_tmpl='azext_teamschats.vendored_sdks.teamschats.operations._chat_message_reply_operations#ChatMessag'
        'eReplyOperations.{}',
        client_factory=cf_chat_message_reply)
    with self.command_group('teamschats', teamschats_chat_message_reply, client_factory=cf_chat_message_reply) as g:
        g.custom_command('delta', 'teamschats_delta')

    from azext_teamschats.generated._client_factory import cf_user
    teamschats_user = CliCommandType(
        operations_tmpl='azext_teamschats.vendored_sdks.teamschats.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('teamschats', teamschats_user, client_factory=cf_user) as g:
        g.custom_command('update', 'teamschats_update')
        g.custom_command('create-chat', 'teamschats_create_chat')
        g.custom_command('get-chat', 'teamschats_get_chat')
        g.custom_command('list-chat', 'teamschats_list_chat')
