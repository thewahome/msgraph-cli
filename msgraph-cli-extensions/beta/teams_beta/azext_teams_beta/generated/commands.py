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
from azext_teams_beta.generated._client_factory import (
    cf_appcatalog,
    cf_appcatalogsteamsapp,
    cf_chatschat,
    cf_chat,
    cf_chatsinstalledapp,
    cf_chatsmember,
    cf_chatsmessage,
    cf_chatsmessagesreply,
    cf_chatstab,
    cf_group,
    cf_teamsteam,
    cf_team,
    cf_teamschannel,
    cf_teamschannelsmember,
    cf_teamschannelsmessage,
    cf_teamschannelsmessagesreply,
    cf_teamschannelstab,
    cf_teamsinstalledapp,
    cf_teamsmember,
    cf_teamsprimarychannel,
    cf_teamsprimarychannelmember,
    cf_teamsprimarychannelmessage,
    cf_teamsprimarychannelmessagesreply,
    cf_teamsprimarychanneltab,
    cf_teamsschedule,
    cf_teamsscheduletimecard,
    cf_teamwork,
    cf_teamwork,
    cf_user,
    cf_usersteamwork,
    cf_usersteamworkinstalledapp,
)


teams_beta_appcatalog = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._appcatalogs_operations#appcatalogsOperations.{}',
    client_factory=cf_appcatalog,
)


teams_beta_appcatalogsteamsapp = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._appcatalogsteamsapps_operations#appcatalogsteamsappsOperations.{}',
    client_factory=cf_appcatalogsteamsapp,
)


teams_beta_chatschat = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._chatschat_operations#chatschatOperations.{}',
    client_factory=cf_chatschat,
)


teams_beta_chat = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._chats_operations#chatsOperations.{}',
    client_factory=cf_chat,
)


teams_beta_chatsinstalledapp = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._chatsinstalledapps_operations#chatsinstalledappsOperations.{}'
    ),
    client_factory=cf_chatsinstalledapp,
)


teams_beta_chatsmember = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._chatsmembers_operations#chatsmembersOperations.{}'
    ),
    client_factory=cf_chatsmember,
)


teams_beta_chatsmessage = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._chatsmessages_operations#chatsmessagesOperations.{}'
    ),
    client_factory=cf_chatsmessage,
)


teams_beta_chatsmessagesreply = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._chatsmessagesreplies_operations#chatsmessagesrepliesOperations.{}',
    client_factory=cf_chatsmessagesreply,
)


teams_beta_chatstab = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._chatstabs_operations#chatstabsOperations.{}',
    client_factory=cf_chatstab,
)


teams_beta_group = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._groups_operations#groupsOperations.{}',
    client_factory=cf_group,
)


teams_beta_teamsteam = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsteam_operations#teamsteamOperations.{}',
    client_factory=cf_teamsteam,
)


teams_beta_team = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teams_operations#teamsOperations.{}',
    client_factory=cf_team,
)


teams_beta_teamschannel = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._teamschannels_operations#teamschannelsOperations.{}'
    ),
    client_factory=cf_teamschannel,
)


teams_beta_teamschannelsmember = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamschannelsmembers_operations#teamschannelsmembersOperations.{}',
    client_factory=cf_teamschannelsmember,
)


teams_beta_teamschannelsmessage = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamschannelsmessages_operations#teamschannelsmessagesOperations.{}',
    client_factory=cf_teamschannelsmessage,
)


teams_beta_teamschannelsmessagesreply = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamschannelsmessagesreplies_operations#teamschannelsmessagesrepliesOperations.{}',
    client_factory=cf_teamschannelsmessagesreply,
)


teams_beta_teamschannelstab = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._teamschannelstabs_operations#teamschannelstabsOperations.{}'
    ),
    client_factory=cf_teamschannelstab,
)


teams_beta_teamsinstalledapp = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._teamsinstalledapps_operations#teamsinstalledappsOperations.{}'
    ),
    client_factory=cf_teamsinstalledapp,
)


teams_beta_teamsmember = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._teamsmembers_operations#teamsmembersOperations.{}'
    ),
    client_factory=cf_teamsmember,
)


teams_beta_teamsprimarychannel = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsprimarychannel_operations#teamsprimarychannelOperations.{}',
    client_factory=cf_teamsprimarychannel,
)


teams_beta_teamsprimarychannelmember = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsprimarychannelmembers_operations#teamsprimarychannelmembersOperations.{}',
    client_factory=cf_teamsprimarychannelmember,
)


teams_beta_teamsprimarychannelmessage = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsprimarychannelmessages_operations#teamsprimarychannelmessagesOperations.{}',
    client_factory=cf_teamsprimarychannelmessage,
)


teams_beta_teamsprimarychannelmessagesreply = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsprimarychannelmessagesreplies_operations#teamsprimarychannelmessagesrepliesOperations.{}',
    client_factory=cf_teamsprimarychannelmessagesreply,
)


teams_beta_teamsprimarychanneltab = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsprimarychanneltabs_operations#teamsprimarychanneltabsOperations.{}',
    client_factory=cf_teamsprimarychanneltab,
)


teams_beta_teamsschedule = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._teamsschedule_operations#teamsscheduleOperations.{}'
    ),
    client_factory=cf_teamsschedule,
)


teams_beta_teamsscheduletimecard = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamsscheduletimecards_operations#teamsscheduletimecardsOperations.{}',
    client_factory=cf_teamsscheduletimecard,
)


teams_beta_teamwork = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._teamworkteamwork_operations#teamworkteamworkOperations.{}'
    ),
    client_factory=cf_teamwork,
)


teams_beta_teamwork = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._teamwork_operations#teamworkOperations.{}',
    client_factory=cf_teamwork,
)


teams_beta_user = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._users_operations#usersOperations.{}',
    client_factory=cf_user,
)


teams_beta_usersteamwork = CliCommandType(
    operations_tmpl=(
        'azext_teams_beta.vendored_sdks.teams.operations._usersteamwork_operations#usersteamworkOperations.{}'
    ),
    client_factory=cf_usersteamwork,
)


teams_beta_usersteamworkinstalledapp = CliCommandType(
    operations_tmpl='azext_teams_beta.vendored_sdks.teams.operations._usersteamworkinstalledapps_operations#usersteamworkinstalledappsOperations.{}',
    client_factory=cf_usersteamworkinstalledapp,
)


def load_command_table(self, _):

    with self.command_group('teams appcatalog', teams_beta_appcatalog, client_factory=cf_appcatalog) as g:
        g.custom_command('create-team-app', 'teams_appcatalog_create_team_app')
        g.custom_command('delete-team-app', 'teams_appcatalog_delete_team_app')
        g.custom_command('list-team-app', 'teams_appcatalog_list_team_app')
        g.custom_command('show-team-app', 'teams_appcatalog_show_team_app')
        g.custom_command('update-team-app', 'teams_appcatalog_update_team_app')

    with self.command_group(
        'teams appcatalogsteamsapp', teams_beta_appcatalogsteamsapp, client_factory=cf_appcatalogsteamsapp
    ) as g:
        g.custom_command('create-app-definition', 'teams_appcatalogsteamsapp_create_app_definition')
        g.custom_command('delete-app-definition', 'teams_appcatalogsteamsapp_delete_app_definition')
        g.custom_command('list-app-definition', 'teams_appcatalogsteamsapp_list_app_definition')
        g.custom_command('show-app-definition', 'teams_appcatalogsteamsapp_show_app_definition')
        g.custom_command('update-app-definition', 'teams_appcatalogsteamsapp_update_app_definition')

    with self.command_group('teams chatschat', teams_beta_chatschat, client_factory=cf_chatschat) as g:
        g.custom_command('create-chat', 'teams_chatschat_create_chat')
        g.custom_command('delete-chat', 'teams_chatschat_delete_chat')
        g.custom_command('list-chat', 'teams_chatschat_list_chat')
        g.custom_command('show-chat', 'teams_chatschat_show_chat')
        g.custom_command('update-chat', 'teams_chatschat_update_chat')

    with self.command_group('teams chat', teams_beta_chat, client_factory=cf_chat) as g:
        g.custom_command('all-message', 'teams_chat_all_message')
        g.custom_command('create-installed-app', 'teams_chat_create_installed_app')
        g.custom_command('create-member', 'teams_chat_create_member')
        g.custom_command('create-message', 'teams_chat_create_message')
        g.custom_command('create-tab', 'teams_chat_create_tab')
        g.custom_command('delete-installed-app', 'teams_chat_delete_installed_app')
        g.custom_command('delete-member', 'teams_chat_delete_member')
        g.custom_command('delete-message', 'teams_chat_delete_message')
        g.custom_command('delete-tab', 'teams_chat_delete_tab')
        g.custom_command('list-installed-app', 'teams_chat_list_installed_app')
        g.custom_command('list-member', 'teams_chat_list_member')
        g.custom_command('list-message', 'teams_chat_list_message')
        g.custom_command('list-tab', 'teams_chat_list_tab')
        g.custom_command('send-activity-notification', 'teams_chat_send_activity_notification')
        g.custom_command('show-all-message', 'teams_chat_show_all_message')
        g.custom_command('show-installed-app', 'teams_chat_show_installed_app')
        g.custom_command('show-member', 'teams_chat_show_member')
        g.custom_command('show-message', 'teams_chat_show_message')
        g.custom_command('show-tab', 'teams_chat_show_tab')
        g.custom_command('update-installed-app', 'teams_chat_update_installed_app')
        g.custom_command('update-member', 'teams_chat_update_member')
        g.custom_command('update-message', 'teams_chat_update_message')
        g.custom_command('update-tab', 'teams_chat_update_tab')

    with self.command_group(
        'teams chatsinstalledapp', teams_beta_chatsinstalledapp, client_factory=cf_chatsinstalledapp
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_chatsinstalledapp_delete_ref_team_app')
        g.custom_command('delete-ref-team-app-definition', 'teams_chatsinstalledapp_delete_ref_team_app_definition')
        g.custom_command('set-ref-team-app', 'teams_chatsinstalledapp_set_ref_team_app')
        g.custom_command('set-ref-team-app-definition', 'teams_chatsinstalledapp_set_ref_team_app_definition')
        g.custom_command('show-ref-team-app', 'teams_chatsinstalledapp_show_ref_team_app')
        g.custom_command('show-ref-team-app-definition', 'teams_chatsinstalledapp_show_ref_team_app_definition')
        g.custom_command('show-team-app', 'teams_chatsinstalledapp_show_team_app')
        g.custom_command('show-team-app-definition', 'teams_chatsinstalledapp_show_team_app_definition')
        g.custom_command('upgrade', 'teams_chatsinstalledapp_upgrade')

    with self.command_group('teams chatsmember', teams_beta_chatsmember, client_factory=cf_chatsmember) as g:
        g.custom_command('add', 'teams_chatsmember_add')

    with self.command_group('teams chatsmessage', teams_beta_chatsmessage, client_factory=cf_chatsmessage) as g:
        g.custom_command('create-hosted-content', 'teams_chatsmessage_create_hosted_content')
        g.custom_command('create-reply', 'teams_chatsmessage_create_reply')
        g.custom_command('delete-hosted-content', 'teams_chatsmessage_delete_hosted_content')
        g.custom_command('delete-reply', 'teams_chatsmessage_delete_reply')
        g.custom_command('delta', 'teams_chatsmessage_delta')
        g.custom_command('list-hosted-content', 'teams_chatsmessage_list_hosted_content')
        g.custom_command('list-reply', 'teams_chatsmessage_list_reply')
        g.custom_command('set-hosted-content-content', 'teams_chatsmessage_set_hosted_content_content')
        g.custom_command('show-hosted-content', 'teams_chatsmessage_show_hosted_content')
        g.custom_command('show-hosted-content-content', 'teams_chatsmessage_show_hosted_content_content')
        g.custom_command('show-reply', 'teams_chatsmessage_show_reply')
        g.custom_command('update-hosted-content', 'teams_chatsmessage_update_hosted_content')
        g.custom_command('update-reply', 'teams_chatsmessage_update_reply')

    with self.command_group(
        'teams chatsmessagesreply', teams_beta_chatsmessagesreply, client_factory=cf_chatsmessagesreply
    ) as g:
        g.custom_command('delta', 'teams_chatsmessagesreply_delta')

    with self.command_group('teams chatstab', teams_beta_chatstab, client_factory=cf_chatstab) as g:
        g.custom_command('delete-ref-team-app', 'teams_chatstab_delete_ref_team_app')
        g.custom_command('set-ref-team-app', 'teams_chatstab_set_ref_team_app')
        g.custom_command('show-ref-team-app', 'teams_chatstab_show_ref_team_app')
        g.custom_command('show-team-app', 'teams_chatstab_show_team_app')

    with self.command_group('teams group', teams_beta_group, client_factory=cf_group) as g:
        g.custom_command('delete-team', 'teams_group_delete_team')
        g.custom_command('show-team', 'teams_group_show_team')
        g.custom_command('update-team', 'teams_group_update_team')

    with self.command_group('teams teamsteam', teams_beta_teamsteam, client_factory=cf_teamsteam) as g:
        g.custom_command('create-team', 'teams_teamsteam_create_team')
        g.custom_command('delete-team', 'teams_teamsteam_delete_team')
        g.custom_command('list-team', 'teams_teamsteam_list_team')
        g.custom_command('show-team', 'teams_teamsteam_show_team')
        g.custom_command('update-team', 'teams_teamsteam_update_team')

    with self.command_group('teams team', teams_beta_team, client_factory=cf_team) as g:
        g.custom_command('all-message', 'teams_team_all_message')
        g.custom_command('archive', 'teams_team_archive')
        g.custom_command('clone', 'teams_team_clone')
        g.custom_command('complete-migration', 'teams_team_complete_migration')
        g.custom_command('create-channel', 'teams_team_create_channel')
        g.custom_command('create-installed-app', 'teams_team_create_installed_app')
        g.custom_command('create-member', 'teams_team_create_member')
        g.custom_command('create-operation', 'teams_team_create_operation')
        g.custom_command('create-ref-owner', 'teams_team_create_ref_owner')
        g.custom_command('delete-channel', 'teams_team_delete_channel')
        g.custom_command('delete-installed-app', 'teams_team_delete_installed_app')
        g.custom_command('delete-member', 'teams_team_delete_member')
        g.custom_command('delete-operation', 'teams_team_delete_operation')
        g.custom_command('delete-photo', 'teams_team_delete_photo')
        g.custom_command('delete-primary-channel', 'teams_team_delete_primary_channel')
        g.custom_command('delete-ref-group', 'teams_team_delete_ref_group')
        g.custom_command('delete-ref-template', 'teams_team_delete_ref_template')
        g.custom_command('delete-schedule', 'teams_team_delete_schedule')
        g.custom_command('list-channel', 'teams_team_list_channel')
        g.custom_command('list-installed-app', 'teams_team_list_installed_app')
        g.custom_command('list-member', 'teams_team_list_member')
        g.custom_command('list-operation', 'teams_team_list_operation')
        g.custom_command('list-owner', 'teams_team_list_owner')
        g.custom_command('list-ref-owner', 'teams_team_list_ref_owner')
        g.custom_command('send-activity-notification', 'teams_team_send_activity_notification')
        g.custom_command('set-photo-content', 'teams_team_set_photo_content')
        g.custom_command('set-ref-group', 'teams_team_set_ref_group')
        g.custom_command('set-ref-template', 'teams_team_set_ref_template')
        g.custom_command('show-all-message', 'teams_team_show_all_message')
        g.custom_command('show-channel', 'teams_team_show_channel')
        g.custom_command('show-group', 'teams_team_show_group')
        g.custom_command('show-installed-app', 'teams_team_show_installed_app')
        g.custom_command('show-member', 'teams_team_show_member')
        g.custom_command('show-operation', 'teams_team_show_operation')
        g.custom_command('show-photo', 'teams_team_show_photo')
        g.custom_command('show-photo-content', 'teams_team_show_photo_content')
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
        g.custom_command('update-photo', 'teams_team_update_photo')
        g.custom_command('update-primary-channel', 'teams_team_update_primary_channel')
        g.custom_command('update-schedule', 'teams_team_update_schedule')

    with self.command_group('teams teamschannel', teams_beta_teamschannel, client_factory=cf_teamschannel) as g:
        g.custom_command('all-message', 'teams_teamschannel_all_message')
        g.custom_command('complete-migration', 'teams_teamschannel_complete_migration')
        g.custom_command('create-member', 'teams_teamschannel_create_member')
        g.custom_command('create-message', 'teams_teamschannel_create_message')
        g.custom_command('create-tab', 'teams_teamschannel_create_tab')
        g.custom_command('delete-file-folder', 'teams_teamschannel_delete_file_folder')
        g.custom_command('delete-member', 'teams_teamschannel_delete_member')
        g.custom_command('delete-message', 'teams_teamschannel_delete_message')
        g.custom_command('delete-tab', 'teams_teamschannel_delete_tab')
        g.custom_command('list-member', 'teams_teamschannel_list_member')
        g.custom_command('list-message', 'teams_teamschannel_list_message')
        g.custom_command('list-tab', 'teams_teamschannel_list_tab')
        g.custom_command('set-file-folder-content', 'teams_teamschannel_set_file_folder_content')
        g.custom_command('show-file-folder', 'teams_teamschannel_show_file_folder')
        g.custom_command('show-file-folder-content', 'teams_teamschannel_show_file_folder_content')
        g.custom_command('show-member', 'teams_teamschannel_show_member')
        g.custom_command('show-message', 'teams_teamschannel_show_message')
        g.custom_command('show-tab', 'teams_teamschannel_show_tab')
        g.custom_command('update-file-folder', 'teams_teamschannel_update_file_folder')
        g.custom_command('update-member', 'teams_teamschannel_update_member')
        g.custom_command('update-message', 'teams_teamschannel_update_message')
        g.custom_command('update-tab', 'teams_teamschannel_update_tab')

    with self.command_group(
        'teams teamschannelsmember', teams_beta_teamschannelsmember, client_factory=cf_teamschannelsmember
    ) as g:
        g.custom_command('add', 'teams_teamschannelsmember_add')

    with self.command_group(
        'teams teamschannelsmessage', teams_beta_teamschannelsmessage, client_factory=cf_teamschannelsmessage
    ) as g:
        g.custom_command('create-hosted-content', 'teams_teamschannelsmessage_create_hosted_content')
        g.custom_command('create-reply', 'teams_teamschannelsmessage_create_reply')
        g.custom_command('delete-hosted-content', 'teams_teamschannelsmessage_delete_hosted_content')
        g.custom_command('delete-reply', 'teams_teamschannelsmessage_delete_reply')
        g.custom_command('delta', 'teams_teamschannelsmessage_delta')
        g.custom_command('list-hosted-content', 'teams_teamschannelsmessage_list_hosted_content')
        g.custom_command('list-reply', 'teams_teamschannelsmessage_list_reply')
        g.custom_command('set-hosted-content-content', 'teams_teamschannelsmessage_set_hosted_content_content')
        g.custom_command('show-hosted-content', 'teams_teamschannelsmessage_show_hosted_content')
        g.custom_command('show-hosted-content-content', 'teams_teamschannelsmessage_show_hosted_content_content')
        g.custom_command('show-reply', 'teams_teamschannelsmessage_show_reply')
        g.custom_command('update-hosted-content', 'teams_teamschannelsmessage_update_hosted_content')
        g.custom_command('update-reply', 'teams_teamschannelsmessage_update_reply')

    with self.command_group(
        'teams teamschannelsmessagesreply',
        teams_beta_teamschannelsmessagesreply,
        client_factory=cf_teamschannelsmessagesreply,
    ) as g:
        g.custom_command('delta', 'teams_teamschannelsmessagesreply_delta')

    with self.command_group(
        'teams teamschannelstab', teams_beta_teamschannelstab, client_factory=cf_teamschannelstab
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_teamschannelstab_delete_ref_team_app')
        g.custom_command('set-ref-team-app', 'teams_teamschannelstab_set_ref_team_app')
        g.custom_command('show-ref-team-app', 'teams_teamschannelstab_show_ref_team_app')
        g.custom_command('show-team-app', 'teams_teamschannelstab_show_team_app')

    with self.command_group(
        'teams teamsinstalledapp', teams_beta_teamsinstalledapp, client_factory=cf_teamsinstalledapp
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_teamsinstalledapp_delete_ref_team_app')
        g.custom_command('delete-ref-team-app-definition', 'teams_teamsinstalledapp_delete_ref_team_app_definition')
        g.custom_command('set-ref-team-app', 'teams_teamsinstalledapp_set_ref_team_app')
        g.custom_command('set-ref-team-app-definition', 'teams_teamsinstalledapp_set_ref_team_app_definition')
        g.custom_command('show-ref-team-app', 'teams_teamsinstalledapp_show_ref_team_app')
        g.custom_command('show-ref-team-app-definition', 'teams_teamsinstalledapp_show_ref_team_app_definition')
        g.custom_command('show-team-app', 'teams_teamsinstalledapp_show_team_app')
        g.custom_command('show-team-app-definition', 'teams_teamsinstalledapp_show_team_app_definition')
        g.custom_command('upgrade', 'teams_teamsinstalledapp_upgrade')

    with self.command_group('teams teamsmember', teams_beta_teamsmember, client_factory=cf_teamsmember) as g:
        g.custom_command('add', 'teams_teamsmember_add')

    with self.command_group(
        'teams teamsprimarychannel', teams_beta_teamsprimarychannel, client_factory=cf_teamsprimarychannel
    ) as g:
        g.custom_command('complete-migration', 'teams_teamsprimarychannel_complete_migration')
        g.custom_command('create-member', 'teams_teamsprimarychannel_create_member')
        g.custom_command('create-message', 'teams_teamsprimarychannel_create_message')
        g.custom_command('create-tab', 'teams_teamsprimarychannel_create_tab')
        g.custom_command('delete-file-folder', 'teams_teamsprimarychannel_delete_file_folder')
        g.custom_command('delete-member', 'teams_teamsprimarychannel_delete_member')
        g.custom_command('delete-message', 'teams_teamsprimarychannel_delete_message')
        g.custom_command('delete-tab', 'teams_teamsprimarychannel_delete_tab')
        g.custom_command('list-member', 'teams_teamsprimarychannel_list_member')
        g.custom_command('list-message', 'teams_teamsprimarychannel_list_message')
        g.custom_command('list-tab', 'teams_teamsprimarychannel_list_tab')
        g.custom_command('set-file-folder-content', 'teams_teamsprimarychannel_set_file_folder_content')
        g.custom_command('show-file-folder', 'teams_teamsprimarychannel_show_file_folder')
        g.custom_command('show-file-folder-content', 'teams_teamsprimarychannel_show_file_folder_content')
        g.custom_command('show-member', 'teams_teamsprimarychannel_show_member')
        g.custom_command('show-message', 'teams_teamsprimarychannel_show_message')
        g.custom_command('show-tab', 'teams_teamsprimarychannel_show_tab')
        g.custom_command('update-file-folder', 'teams_teamsprimarychannel_update_file_folder')
        g.custom_command('update-member', 'teams_teamsprimarychannel_update_member')
        g.custom_command('update-message', 'teams_teamsprimarychannel_update_message')
        g.custom_command('update-tab', 'teams_teamsprimarychannel_update_tab')

    with self.command_group(
        'teams teamsprimarychannelmember',
        teams_beta_teamsprimarychannelmember,
        client_factory=cf_teamsprimarychannelmember,
    ) as g:
        g.custom_command('add', 'teams_teamsprimarychannelmember_add')

    with self.command_group(
        'teams teamsprimarychannelmessage',
        teams_beta_teamsprimarychannelmessage,
        client_factory=cf_teamsprimarychannelmessage,
    ) as g:
        g.custom_command('create-hosted-content', 'teams_teamsprimarychannelmessage_create_hosted_content')
        g.custom_command('create-reply', 'teams_teamsprimarychannelmessage_create_reply')
        g.custom_command('delete-hosted-content', 'teams_teamsprimarychannelmessage_delete_hosted_content')
        g.custom_command('delete-reply', 'teams_teamsprimarychannelmessage_delete_reply')
        g.custom_command('delta', 'teams_teamsprimarychannelmessage_delta')
        g.custom_command('list-hosted-content', 'teams_teamsprimarychannelmessage_list_hosted_content')
        g.custom_command('list-reply', 'teams_teamsprimarychannelmessage_list_reply')
        g.custom_command('set-hosted-content-content', 'teams_teamsprimarychannelmessage_set_hosted_content_content')
        g.custom_command('show-hosted-content', 'teams_teamsprimarychannelmessage_show_hosted_content')
        g.custom_command('show-hosted-content-content', 'teams_teamsprimarychannelmessage_show_hosted_content_content')
        g.custom_command('show-reply', 'teams_teamsprimarychannelmessage_show_reply')
        g.custom_command('update-hosted-content', 'teams_teamsprimarychannelmessage_update_hosted_content')
        g.custom_command('update-reply', 'teams_teamsprimarychannelmessage_update_reply')

    with self.command_group(
        'teams teamsprimarychannelmessagesreply',
        teams_beta_teamsprimarychannelmessagesreply,
        client_factory=cf_teamsprimarychannelmessagesreply,
    ) as g:
        g.custom_command('delta', 'teams_teamsprimarychannelmessagesreply_delta')

    with self.command_group(
        'teams teamsprimarychanneltab', teams_beta_teamsprimarychanneltab, client_factory=cf_teamsprimarychanneltab
    ) as g:
        g.custom_command('delete-ref-team-app', 'teams_teamsprimarychanneltab_delete_ref_team_app')
        g.custom_command('set-ref-team-app', 'teams_teamsprimarychanneltab_set_ref_team_app')
        g.custom_command('show-ref-team-app', 'teams_teamsprimarychanneltab_show_ref_team_app')
        g.custom_command('show-team-app', 'teams_teamsprimarychanneltab_show_team_app')

    with self.command_group('teams teamsschedule', teams_beta_teamsschedule, client_factory=cf_teamsschedule) as g:
        g.custom_command('create-offer-shift-request', 'teams_teamsschedule_create_offer_shift_request')
        g.custom_command('create-open-shift', 'teams_teamsschedule_create_open_shift')
        g.custom_command('create-open-shift-change-request', 'teams_teamsschedule_create_open_shift_change_request')
        g.custom_command('create-scheduling-group', 'teams_teamsschedule_create_scheduling_group')
        g.custom_command('create-shift', 'teams_teamsschedule_create_shift')
        g.custom_command('create-swap-shift-change-request', 'teams_teamsschedule_create_swap_shift_change_request')
        g.custom_command('create-time-card', 'teams_teamsschedule_create_time_card')
        g.custom_command('create-time-off', 'teams_teamsschedule_create_time_off')
        g.custom_command('create-time-off-reason', 'teams_teamsschedule_create_time_off_reason')
        g.custom_command('create-time-off-request', 'teams_teamsschedule_create_time_off_request')
        g.custom_command('delete-offer-shift-request', 'teams_teamsschedule_delete_offer_shift_request')
        g.custom_command('delete-open-shift', 'teams_teamsschedule_delete_open_shift')
        g.custom_command('delete-open-shift-change-request', 'teams_teamsschedule_delete_open_shift_change_request')
        g.custom_command('delete-scheduling-group', 'teams_teamsschedule_delete_scheduling_group')
        g.custom_command('delete-shift', 'teams_teamsschedule_delete_shift')
        g.custom_command('delete-swap-shift-change-request', 'teams_teamsschedule_delete_swap_shift_change_request')
        g.custom_command('delete-time-card', 'teams_teamsschedule_delete_time_card')
        g.custom_command('delete-time-off', 'teams_teamsschedule_delete_time_off')
        g.custom_command('delete-time-off-reason', 'teams_teamsschedule_delete_time_off_reason')
        g.custom_command('delete-time-off-request', 'teams_teamsschedule_delete_time_off_request')
        g.custom_command('list-offer-shift-request', 'teams_teamsschedule_list_offer_shift_request')
        g.custom_command('list-open-shift', 'teams_teamsschedule_list_open_shift')
        g.custom_command('list-open-shift-change-request', 'teams_teamsschedule_list_open_shift_change_request')
        g.custom_command('list-scheduling-group', 'teams_teamsschedule_list_scheduling_group')
        g.custom_command('list-shift', 'teams_teamsschedule_list_shift')
        g.custom_command('list-swap-shift-change-request', 'teams_teamsschedule_list_swap_shift_change_request')
        g.custom_command('list-time-card', 'teams_teamsschedule_list_time_card')
        g.custom_command('list-time-off', 'teams_teamsschedule_list_time_off')
        g.custom_command('list-time-off-reason', 'teams_teamsschedule_list_time_off_reason')
        g.custom_command('list-time-off-request', 'teams_teamsschedule_list_time_off_request')
        g.custom_command('share', 'teams_teamsschedule_share')
        g.custom_command('show-offer-shift-request', 'teams_teamsschedule_show_offer_shift_request')
        g.custom_command('show-open-shift', 'teams_teamsschedule_show_open_shift')
        g.custom_command('show-open-shift-change-request', 'teams_teamsschedule_show_open_shift_change_request')
        g.custom_command('show-scheduling-group', 'teams_teamsschedule_show_scheduling_group')
        g.custom_command('show-shift', 'teams_teamsschedule_show_shift')
        g.custom_command('show-swap-shift-change-request', 'teams_teamsschedule_show_swap_shift_change_request')
        g.custom_command('show-time-card', 'teams_teamsschedule_show_time_card')
        g.custom_command('show-time-off', 'teams_teamsschedule_show_time_off')
        g.custom_command('show-time-off-reason', 'teams_teamsschedule_show_time_off_reason')
        g.custom_command('show-time-off-request', 'teams_teamsschedule_show_time_off_request')
        g.custom_command('update-offer-shift-request', 'teams_teamsschedule_update_offer_shift_request')
        g.custom_command('update-open-shift', 'teams_teamsschedule_update_open_shift')
        g.custom_command('update-open-shift-change-request', 'teams_teamsschedule_update_open_shift_change_request')
        g.custom_command('update-scheduling-group', 'teams_teamsschedule_update_scheduling_group')
        g.custom_command('update-shift', 'teams_teamsschedule_update_shift')
        g.custom_command('update-swap-shift-change-request', 'teams_teamsschedule_update_swap_shift_change_request')
        g.custom_command('update-time-card', 'teams_teamsschedule_update_time_card')
        g.custom_command('update-time-off', 'teams_teamsschedule_update_time_off')
        g.custom_command('update-time-off-reason', 'teams_teamsschedule_update_time_off_reason')
        g.custom_command('update-time-off-request', 'teams_teamsschedule_update_time_off_request')

    with self.command_group(
        'teams teamsscheduletimecard', teams_beta_teamsscheduletimecard, client_factory=cf_teamsscheduletimecard
    ) as g:
        g.custom_command('clock-in', 'teams_teamsscheduletimecard_clock_in')
        g.custom_command('clock-out', 'teams_teamsscheduletimecard_clock_out')
        g.custom_command('confirm', 'teams_teamsscheduletimecard_confirm')
        g.custom_command('end-break', 'teams_teamsscheduletimecard_end_break')
        g.custom_command('start-break', 'teams_teamsscheduletimecard_start_break')

    with self.command_group('teams teamwork', teams_beta_teamwork, client_factory=cf_teamwork) as g:
        g.custom_command('show-teamwork', 'teams_teamwork_show_teamwork')
        g.custom_command('update-teamwork', 'teams_teamwork_update_teamwork')

    with self.command_group('teams teamwork', teams_beta_teamwork, client_factory=cf_teamwork) as g:
        g.custom_command('create-workforce-integration', 'teams_teamwork_create_workforce_integration')
        g.custom_command('delete-workforce-integration', 'teams_teamwork_delete_workforce_integration')
        g.custom_command('list-workforce-integration', 'teams_teamwork_list_workforce_integration')
        g.custom_command('show-workforce-integration', 'teams_teamwork_show_workforce_integration')
        g.custom_command('update-workforce-integration', 'teams_teamwork_update_workforce_integration')

    with self.command_group('teams user', teams_beta_user, client_factory=cf_user) as g:
        g.custom_command('create-chat', 'teams_user_create_chat')
        g.custom_command('create-joined-team', 'teams_user_create_joined_team')
        g.custom_command('delete-chat', 'teams_user_delete_chat')
        g.custom_command('delete-joined-team', 'teams_user_delete_joined_team')
        g.custom_command('delete-teamwork', 'teams_user_delete_teamwork')
        g.custom_command('list-chat', 'teams_user_list_chat')
        g.custom_command('list-joined-team', 'teams_user_list_joined_team')
        g.custom_command('show-chat', 'teams_user_show_chat')
        g.custom_command('show-joined-team', 'teams_user_show_joined_team')
        g.custom_command('show-teamwork', 'teams_user_show_teamwork')
        g.custom_command('update-chat', 'teams_user_update_chat')
        g.custom_command('update-joined-team', 'teams_user_update_joined_team')
        g.custom_command('update-teamwork', 'teams_user_update_teamwork')

    with self.command_group('teams usersteamwork', teams_beta_usersteamwork, client_factory=cf_usersteamwork) as g:
        g.custom_command('create-installed-app', 'teams_usersteamwork_create_installed_app')
        g.custom_command('delete-installed-app', 'teams_usersteamwork_delete_installed_app')
        g.custom_command('list-installed-app', 'teams_usersteamwork_list_installed_app')
        g.custom_command('show-installed-app', 'teams_usersteamwork_show_installed_app')
        g.custom_command('update-installed-app', 'teams_usersteamwork_update_installed_app')

    with self.command_group(
        'teams usersteamworkinstalledapp',
        teams_beta_usersteamworkinstalledapp,
        client_factory=cf_usersteamworkinstalledapp,
    ) as g:
        g.custom_command('delete-ref-chat', 'teams_usersteamworkinstalledapp_delete_ref_chat')
        g.custom_command('set-ref-chat', 'teams_usersteamworkinstalledapp_set_ref_chat')
        g.custom_command('show-chat', 'teams_usersteamworkinstalledapp_show_chat')
        g.custom_command('show-ref-chat', 'teams_usersteamworkinstalledapp_show_ref_chat')

    with self.command_group('teams_beta', is_experimental=True):
        pass
