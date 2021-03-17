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

    from azext_teams_v1_0.generated._client_factory import cf_chat_chat

    teams_v1_0_chat_chat = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._chat_chat_operations#ChatChatOperations.{}',
        client_factory=cf_chat_chat,
    )
    with self.command_group('teams chat-chat', teams_v1_0_chat_chat, client_factory=cf_chat_chat) as g:
        g.custom_command('create-chat', 'teams_chat_chat_create_chat')
        g.custom_command('delete-chat', 'teams_chat_chat_delete_chat')
        g.custom_command('list-chat', 'teams_chat_chat_list_chat')
        g.custom_command('show-chat', 'teams_chat_chat_show_chat')
        g.custom_command('update-chat', 'teams_chat_chat_update_chat')

    from azext_teams_v1_0.generated._client_factory import cf_chat

    teams_v1_0_chat = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._chat_operations#ChatOperations.{}',
        client_factory=cf_chat,
    )
    with self.command_group('teams chat', teams_v1_0_chat, client_factory=cf_chat) as g:
        g.custom_command('show-all-message', 'teams_chat_show_all_message')

    from azext_teams_v1_0.generated._client_factory import cf_group

    teams_v1_0_group = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._group_operations#GroupOperations.{}',
        client_factory=cf_group,
    )
    with self.command_group('teams group', teams_v1_0_group, client_factory=cf_group) as g:
        g.custom_command('delete-team', 'teams_group_delete_team')
        g.custom_command('show-team', 'teams_group_show_team')
        g.custom_command('update-team', 'teams_group_update_team')

    from azext_teams_v1_0.generated._client_factory import cf_team_team

    teams_v1_0_team_team = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_team_operations#TeamTeamOperations.{}',
        client_factory=cf_team_team,
    )
    with self.command_group('teams team', teams_v1_0_team_team, client_factory=cf_team_team) as g:
        g.custom_command('list', 'teams_team_list')
        g.custom_command('create', 'teams_team_create')
        g.custom_command('delete-team', 'teams_team_delete_team')
        g.custom_command('show-team', 'teams_team_show_team')

    from azext_teams_v1_0.generated._client_factory import cf_team

    teams_v1_0_team = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_operations#TeamOperations.{}',
        client_factory=cf_team,
    )
    with self.command_group('teams team', teams_v1_0_team, client_factory=cf_team) as g:
        g.custom_command('archive', 'teams_team_archive')
        g.custom_command('clone', 'teams_team_clone')
        g.custom_command('create-channel', 'teams_team_create_channel')
        g.custom_command('create-installed-app', 'teams_team_create_installed_app')
        g.custom_command('create-member', 'teams_team_create_member')
        g.custom_command('create-operation', 'teams_team_create_operation')
        g.custom_command('delete-channel', 'teams_team_delete_channel')
        g.custom_command('delete-installed-app', 'teams_team_delete_installed_app')
        g.custom_command('delete-member', 'teams_team_delete_member')
        g.custom_command('delete-operation', 'teams_team_delete_operation')
        g.custom_command('delete-primary-channel', 'teams_team_delete_primary_channel')
        g.custom_command('delete-ref-group', 'teams_team_delete_ref_group')
        g.custom_command('delete-ref-template', 'teams_team_delete_ref_template')
        g.custom_command('delete-schedule', 'teams_team_delete_schedule')
        g.custom_command('list-channel', 'teams_team_list_channel')
        g.custom_command('list-installed-app', 'teams_team_list_installed_app')
        g.custom_command('list-member', 'teams_team_list_member')
        g.custom_command('list-operation', 'teams_team_list_operation')
        g.custom_command('set-ref-group', 'teams_team_set_ref_group')
        g.custom_command('set-ref-template', 'teams_team_set_ref_template')
        g.custom_command('show-all-message', 'teams_team_show_all_message')
        g.custom_command('show-channel', 'teams_team_show_channel')
        g.custom_command('show-group', 'teams_team_show_group')
        g.custom_command('show-installed-app', 'teams_team_show_installed_app')
        g.custom_command('show-member', 'teams_team_show_member')
        g.custom_command('show-operation', 'teams_team_show_operation')
        g.custom_command('show-primary-channel', 'teams_team_show_primary_channel')
        g.custom_command('show-ref-group', 'teams_team_show_ref_group')
        g.custom_command('show-ref-template', 'teams_team_show_ref_template')
        g.custom_command('show-schedule', 'teams_team_show_schedule')
        g.custom_command('show-template', 'teams_team_show_template')
        g.custom_command('unarchive', 'teams_team_unarchive')
        g.custom_command('update-channel', 'teams_team_update_channel')
        g.custom_command('update-installed-app', 'teams_team_update_installed_app')
        g.custom_command('update-member', 'teams_team_update_member')
        g.custom_command('update-operation', 'teams_team_update_operation')
        g.custom_command('update-primary-channel', 'teams_team_update_primary_channel')
        g.custom_command('update-schedule', 'teams_team_update_schedule')

    from azext_teams_v1_0.generated._client_factory import cf_team_channel

    teams_v1_0_team_channel = CliCommandType(
        operations_tmpl=(
            'azext_teams_v1_0.vendored_sdks.teams.operations._team_channel_operations#TeamChannelOperations.{}'
        ),
        client_factory=cf_team_channel,
    )
    with self.command_group('teams team-channel', teams_v1_0_team_channel, client_factory=cf_team_channel) as g:
        g.custom_command('create-member', 'teams_team_channel_create_member')
        g.custom_command('create-message', 'teams_team_channel_create_message')
        g.custom_command('create-tab', 'teams_team_channel_create_tab')
        g.custom_command('delete-file-folder', 'teams_team_channel_delete_file_folder')
        g.custom_command('delete-member', 'teams_team_channel_delete_member')
        g.custom_command('delete-message', 'teams_team_channel_delete_message')
        g.custom_command('delete-tab', 'teams_team_channel_delete_tab')
        g.custom_command('list-member', 'teams_team_channel_list_member')
        g.custom_command('list-message', 'teams_team_channel_list_message')
        g.custom_command('list-tab', 'teams_team_channel_list_tab')
        g.custom_command('show-file-folder', 'teams_team_channel_show_file_folder')
        g.custom_command('show-member', 'teams_team_channel_show_member')
        g.custom_command('show-message', 'teams_team_channel_show_message')
        g.custom_command('show-tab', 'teams_team_channel_show_tab')
        g.custom_command('update-file-folder', 'teams_team_channel_update_file_folder')
        g.custom_command('update-member', 'teams_team_channel_update_member')
        g.custom_command('update-message', 'teams_team_channel_update_message')
        g.custom_command('update-tab', 'teams_team_channel_update_tab')

    from azext_teams_v1_0.generated._client_factory import cf_team_channel_message

    teams_v1_0_team_channel_message = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_channel_message_operations#TeamChannelMessageOperations.{}',
        client_factory=cf_team_channel_message,
    )
    with self.command_group(
        'teams team-channel-message', teams_v1_0_team_channel_message, client_factory=cf_team_channel_message
    ) as g:
        g.custom_command('create-hosted-content', 'teams_team_channel_message_create_hosted_content')
        g.custom_command('create-reply', 'teams_team_channel_message_create_reply')
        g.custom_command('delete-hosted-content', 'teams_team_channel_message_delete_hosted_content')
        g.custom_command('delete-reply', 'teams_team_channel_message_delete_reply')
        g.custom_command('list-hosted-content', 'teams_team_channel_message_list_hosted_content')
        g.custom_command('list-reply', 'teams_team_channel_message_list_reply')
        g.custom_command('show-hosted-content', 'teams_team_channel_message_show_hosted_content')
        g.custom_command('show-reply', 'teams_team_channel_message_show_reply')
        g.custom_command('update-hosted-content', 'teams_team_channel_message_update_hosted_content')
        g.custom_command('update-reply', 'teams_team_channel_message_update_reply')

    from azext_teams_v1_0.generated._client_factory import cf_team_channel_tab

    teams_v1_0_team_channel_tab = CliCommandType(
        operations_tmpl=(
            'azext_teams_v1_0.vendored_sdks.teams.operations._team_channel_tab_operations#TeamChannelTabOperations.{}'
        ),
        client_factory=cf_team_channel_tab,
    )
    with self.command_group(
        'teams team-channel-tab', teams_v1_0_team_channel_tab, client_factory=cf_team_channel_tab
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_team_channel_tab_delete_ref_team_app')
        g.custom_command('set-ref-team-app', 'teams_team_channel_tab_set_ref_team_app')
        g.custom_command('show-ref-team-app', 'teams_team_channel_tab_show_ref_team_app')
        g.custom_command('show-team-app', 'teams_team_channel_tab_show_team_app')

    from azext_teams_v1_0.generated._client_factory import cf_team_installed_app

    teams_v1_0_team_installed_app = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_installed_app_operations#TeamInstalledAppOperations.{}',
        client_factory=cf_team_installed_app,
    )
    with self.command_group(
        'teams team-installed-app', teams_v1_0_team_installed_app, client_factory=cf_team_installed_app
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_team_installed_app_delete_ref_team_app')
        g.custom_command('delete-ref-team-app-definition', 'teams_team_installed_app_delete_ref_team_app_definition')
        g.custom_command('set-ref-team-app', 'teams_team_installed_app_set_ref_team_app')
        g.custom_command('set-ref-team-app-definition', 'teams_team_installed_app_set_ref_team_app_definition')
        g.custom_command('show-ref-team-app', 'teams_team_installed_app_show_ref_team_app')
        g.custom_command('show-ref-team-app-definition', 'teams_team_installed_app_show_ref_team_app_definition')
        g.custom_command('show-team-app', 'teams_team_installed_app_show_team_app')
        g.custom_command('show-team-app-definition', 'teams_team_installed_app_show_team_app_definition')
        g.custom_command('upgrade', 'teams_team_installed_app_upgrade')

    from azext_teams_v1_0.generated._client_factory import cf_team_primary_channel

    teams_v1_0_team_primary_channel = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_primary_channel_operations#TeamPrimaryChannelOperations.{}',
        client_factory=cf_team_primary_channel,
    )
    with self.command_group(
        'teams team-primary-channel', teams_v1_0_team_primary_channel, client_factory=cf_team_primary_channel
    ) as g:
        g.custom_command('create-member', 'teams_team_primary_channel_create_member')
        g.custom_command('create-message', 'teams_team_primary_channel_create_message')
        g.custom_command('create-tab', 'teams_team_primary_channel_create_tab')
        g.custom_command('delete-file-folder', 'teams_team_primary_channel_delete_file_folder')
        g.custom_command('delete-member', 'teams_team_primary_channel_delete_member')
        g.custom_command('delete-message', 'teams_team_primary_channel_delete_message')
        g.custom_command('delete-tab', 'teams_team_primary_channel_delete_tab')
        g.custom_command('list-member', 'teams_team_primary_channel_list_member')
        g.custom_command('list-message', 'teams_team_primary_channel_list_message')
        g.custom_command('list-tab', 'teams_team_primary_channel_list_tab')
        g.custom_command('show-file-folder', 'teams_team_primary_channel_show_file_folder')
        g.custom_command('show-member', 'teams_team_primary_channel_show_member')
        g.custom_command('show-message', 'teams_team_primary_channel_show_message')
        g.custom_command('show-tab', 'teams_team_primary_channel_show_tab')
        g.custom_command('update-file-folder', 'teams_team_primary_channel_update_file_folder')
        g.custom_command('update-member', 'teams_team_primary_channel_update_member')
        g.custom_command('update-message', 'teams_team_primary_channel_update_message')
        g.custom_command('update-tab', 'teams_team_primary_channel_update_tab')

    from azext_teams_v1_0.generated._client_factory import cf_team_primary_channel_message

    teams_v1_0_team_primary_channel_message = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_primary_channel_message_operations#TeamPrimaryChannelMessageOperations.{}',
        client_factory=cf_team_primary_channel_message,
    )
    with self.command_group(
        'teams team-primary-channel-message',
        teams_v1_0_team_primary_channel_message,
        client_factory=cf_team_primary_channel_message,
    ) as g:
        g.custom_command('create-hosted-content', 'teams_team_primary_channel_message_create_hosted_content')
        g.custom_command('create-reply', 'teams_team_primary_channel_message_create_reply')
        g.custom_command('delete-hosted-content', 'teams_team_primary_channel_message_delete_hosted_content')
        g.custom_command('delete-reply', 'teams_team_primary_channel_message_delete_reply')
        g.custom_command('list-hosted-content', 'teams_team_primary_channel_message_list_hosted_content')
        g.custom_command('list-reply', 'teams_team_primary_channel_message_list_reply')
        g.custom_command('show-hosted-content', 'teams_team_primary_channel_message_show_hosted_content')
        g.custom_command('show-reply', 'teams_team_primary_channel_message_show_reply')
        g.custom_command('update-hosted-content', 'teams_team_primary_channel_message_update_hosted_content')
        g.custom_command('update-reply', 'teams_team_primary_channel_message_update_reply')

    from azext_teams_v1_0.generated._client_factory import cf_team_primary_channel_tab

    teams_v1_0_team_primary_channel_tab = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._team_primary_channel_tab_operations#TeamPrimaryChannelTabOperations.{}',
        client_factory=cf_team_primary_channel_tab,
    )
    with self.command_group(
        'teams team-primary-channel-tab',
        teams_v1_0_team_primary_channel_tab,
        client_factory=cf_team_primary_channel_tab,
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_team_primary_channel_tab_delete_ref_team_app')
        g.custom_command('set-ref-team-app', 'teams_team_primary_channel_tab_set_ref_team_app')
        g.custom_command('show-ref-team-app', 'teams_team_primary_channel_tab_show_ref_team_app')
        g.custom_command('show-team-app', 'teams_team_primary_channel_tab_show_team_app')

    from azext_teams_v1_0.generated._client_factory import cf_team_schedule

    teams_v1_0_team_schedule = CliCommandType(
        operations_tmpl=(
            'azext_teams_v1_0.vendored_sdks.teams.operations._team_schedule_operations#TeamScheduleOperations.{}'
        ),
        client_factory=cf_team_schedule,
    )
    with self.command_group('teams team-schedule', teams_v1_0_team_schedule, client_factory=cf_team_schedule) as g:
        g.custom_command('create-offer-shift-request', 'teams_team_schedule_create_offer_shift_request')
        g.custom_command('create-open-shift', 'teams_team_schedule_create_open_shift')
        g.custom_command('create-open-shift-change-request', 'teams_team_schedule_create_open_shift_change_request')
        g.custom_command('create-scheduling-group', 'teams_team_schedule_create_scheduling_group')
        g.custom_command('create-shift', 'teams_team_schedule_create_shift')
        g.custom_command('create-swap-shift-change-request', 'teams_team_schedule_create_swap_shift_change_request')
        g.custom_command('create-time-off', 'teams_team_schedule_create_time_off')
        g.custom_command('create-time-off-reason', 'teams_team_schedule_create_time_off_reason')
        g.custom_command('create-time-off-request', 'teams_team_schedule_create_time_off_request')
        g.custom_command('delete-offer-shift-request', 'teams_team_schedule_delete_offer_shift_request')
        g.custom_command('delete-open-shift', 'teams_team_schedule_delete_open_shift')
        g.custom_command('delete-open-shift-change-request', 'teams_team_schedule_delete_open_shift_change_request')
        g.custom_command('delete-scheduling-group', 'teams_team_schedule_delete_scheduling_group')
        g.custom_command('delete-shift', 'teams_team_schedule_delete_shift')
        g.custom_command('delete-swap-shift-change-request', 'teams_team_schedule_delete_swap_shift_change_request')
        g.custom_command('delete-time-off', 'teams_team_schedule_delete_time_off')
        g.custom_command('delete-time-off-reason', 'teams_team_schedule_delete_time_off_reason')
        g.custom_command('delete-time-off-request', 'teams_team_schedule_delete_time_off_request')
        g.custom_command('list-offer-shift-request', 'teams_team_schedule_list_offer_shift_request')
        g.custom_command('list-open-shift', 'teams_team_schedule_list_open_shift')
        g.custom_command('list-open-shift-change-request', 'teams_team_schedule_list_open_shift_change_request')
        g.custom_command('list-scheduling-group', 'teams_team_schedule_list_scheduling_group')
        g.custom_command('list-shift', 'teams_team_schedule_list_shift')
        g.custom_command('list-swap-shift-change-request', 'teams_team_schedule_list_swap_shift_change_request')
        g.custom_command('list-time-off', 'teams_team_schedule_list_time_off')
        g.custom_command('list-time-off-reason', 'teams_team_schedule_list_time_off_reason')
        g.custom_command('list-time-off-request', 'teams_team_schedule_list_time_off_request')
        g.custom_command('share', 'teams_team_schedule_share')
        g.custom_command('show-offer-shift-request', 'teams_team_schedule_show_offer_shift_request')
        g.custom_command('show-open-shift', 'teams_team_schedule_show_open_shift')
        g.custom_command('show-open-shift-change-request', 'teams_team_schedule_show_open_shift_change_request')
        g.custom_command('show-scheduling-group', 'teams_team_schedule_show_scheduling_group')
        g.custom_command('show-shift', 'teams_team_schedule_show_shift')
        g.custom_command('show-swap-shift-change-request', 'teams_team_schedule_show_swap_shift_change_request')
        g.custom_command('show-time-off', 'teams_team_schedule_show_time_off')
        g.custom_command('show-time-off-reason', 'teams_team_schedule_show_time_off_reason')
        g.custom_command('show-time-off-request', 'teams_team_schedule_show_time_off_request')
        g.custom_command('update-offer-shift-request', 'teams_team_schedule_update_offer_shift_request')
        g.custom_command('update-open-shift', 'teams_team_schedule_update_open_shift')
        g.custom_command('update-open-shift-change-request', 'teams_team_schedule_update_open_shift_change_request')
        g.custom_command('update-scheduling-group', 'teams_team_schedule_update_scheduling_group')
        g.custom_command('update-shift', 'teams_team_schedule_update_shift')
        g.custom_command('update-swap-shift-change-request', 'teams_team_schedule_update_swap_shift_change_request')
        g.custom_command('update-time-off', 'teams_team_schedule_update_time_off')
        g.custom_command('update-time-off-reason', 'teams_team_schedule_update_time_off_reason')
        g.custom_command('update-time-off-request', 'teams_team_schedule_update_time_off_request')

    from azext_teams_v1_0.generated._client_factory import cf_teamwork_teamwork

    teams_v1_0_teamwork_teamwork = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._teamwork_teamwork_operations#TeamworkTeamworkOperations.{}',
        client_factory=cf_teamwork_teamwork,
    )
    with self.command_group(
        'teams teamwork-teamwork', teams_v1_0_teamwork_teamwork, client_factory=cf_teamwork_teamwork
    ) as g:
        g.custom_command('show-teamwork', 'teams_teamwork_teamwork_show_teamwork')
        g.custom_command('update-teamwork', 'teams_teamwork_teamwork_update_teamwork')

    from azext_teams_v1_0.generated._client_factory import cf_teamwork

    teams_v1_0_teamwork = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._teamwork_operations#TeamworkOperations.{}',
        client_factory=cf_teamwork,
    )
    with self.command_group('teams teamwork', teams_v1_0_teamwork, client_factory=cf_teamwork) as g:
        g.custom_command('create-workforce-integration', 'teams_teamwork_create_workforce_integration')
        g.custom_command('delete-workforce-integration', 'teams_teamwork_delete_workforce_integration')
        g.custom_command('list-workforce-integration', 'teams_teamwork_list_workforce_integration')
        g.custom_command('show-workforce-integration', 'teams_teamwork_show_workforce_integration')
        g.custom_command('update-workforce-integration', 'teams_teamwork_update_workforce_integration')

    from azext_teams_v1_0.generated._client_factory import cf_user

    teams_v1_0_user = CliCommandType(
        operations_tmpl='azext_teams_v1_0.vendored_sdks.teams.operations._user_operations#UserOperations.{}',
        client_factory=cf_user,
    )
    with self.command_group('teams user', teams_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('create-joined-team', 'teams_user_create_joined_team')
        g.custom_command('delete-joined-team', 'teams_user_delete_joined_team')
        g.custom_command('list-joined-team', 'teams_user_list_joined_team')
        g.custom_command('show-joined-team', 'teams_user_show_joined_team')
        g.custom_command('update-joined-team', 'teams_user_update_joined_team')

    with self.command_group('teams_v1_0', is_experimental=True):
        pass
