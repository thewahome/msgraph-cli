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

    from azext_cloudcommunications.generated._client_factory import cf_communication_cloud_communication
    cloudcommunications_communication_cloud_communication = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_cloud_co'
        'mmunication_operations#CommunicationCloudCommunicationOperations.{}',
        client_factory=cf_communication_cloud_communication)
    with self.command_group('cloudcommunications', cloudcommunications_communication_cloud_communication,
                            client_factory=cf_communication_cloud_communication) as g:
        g.custom_command('get-cloud-communication', 'cloudcommunications_get_cloud_communication')
        g.custom_command('update-cloud-communication', 'cloudcommunications_update_cloud_communication')

    from azext_cloudcommunications.generated._client_factory import cf_communication
    cloudcommunications_communication = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_operatio'
        'ns#CommunicationOperations.{}',
        client_factory=cf_communication)
    with self.command_group('cloudcommunications', cloudcommunications_communication,
                            client_factory=cf_communication) as g:
        g.custom_command('delete', 'cloudcommunications_delete', confirmation=True)
        g.custom_command('create-call', 'cloudcommunications_create_call')
        g.custom_command('create-call-record', 'cloudcommunications_create_call_record')
        g.custom_command('create-online-meeting', 'cloudcommunications_create_online_meeting')
        g.custom_command('get-call', 'cloudcommunications_get_call')
        g.custom_command('get-call-record', 'cloudcommunications_get_call_record')
        g.custom_command('get-online-meeting', 'cloudcommunications_get_online_meeting')
        g.custom_command('list-call', 'cloudcommunications_list_call')
        g.custom_command('list-call-record', 'cloudcommunications_list_call_record')
        g.custom_command('list-online-meeting', 'cloudcommunications_list_online_meeting')
        g.custom_command('update-call', 'cloudcommunications_update_call')
        g.custom_command('update-call-record', 'cloudcommunications_update_call_record')
        g.custom_command('update-online-meeting', 'cloudcommunications_update_online_meeting')

    from azext_cloudcommunications.generated._client_factory import cf_communication_call_record
    cloudcommunications_communication_call_record = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_call_rec'
        'ord_operations#CommunicationCallRecordOperations.{}',
        client_factory=cf_communication_call_record)
    with self.command_group('cloudcommunications', cloudcommunications_communication_call_record,
                            client_factory=cf_communication_call_record) as g:
        g.custom_command('delete', 'cloudcommunications_delete', confirmation=True)
        g.custom_command('create-session', 'cloudcommunications_create_session')
        g.custom_command('get-session', 'cloudcommunications_get_session')
        g.custom_command('list-session', 'cloudcommunications_list_session')
        g.custom_command('update-session', 'cloudcommunications_update_session')

    from azext_cloudcommunications.generated._client_factory import cf_communication_call_record_session
    cloudcommunications_communication_call_record_session = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_call_rec'
        'ord_session_operations#CommunicationCallRecordSessionOperations.{}',
        client_factory=cf_communication_call_record_session)
    with self.command_group('cloudcommunications', cloudcommunications_communication_call_record_session,
                            client_factory=cf_communication_call_record_session) as g:
        g.custom_command('delete', 'cloudcommunications_delete', confirmation=True)
        g.custom_command('create-segment', 'cloudcommunications_create_segment')
        g.custom_command('get-segment', 'cloudcommunications_get_segment')
        g.custom_command('list-segment', 'cloudcommunications_list_segment')
        g.custom_command('update-segment', 'cloudcommunications_update_segment')

    from azext_cloudcommunications.generated._client_factory import cf_communication_call
    cloudcommunications_communication_call = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_call_ope'
        'rations#CommunicationCallOperations.{}',
        client_factory=cf_communication_call)
    with self.command_group('cloudcommunications', cloudcommunications_communication_call,
                            client_factory=cf_communication_call) as g:
        g.custom_command('delete', 'cloudcommunications_delete', confirmation=True)
        g.custom_command('answer', 'cloudcommunications_answer')
        g.custom_command('cancel-media-processing', 'cloudcommunications_cancel_media_processing')
        g.custom_command('change-screen-sharing-role', 'cloudcommunications_change_screen_sharing_role')
        g.custom_command('create-operation', 'cloudcommunications_create_operation')
        g.custom_command('create-participant', 'cloudcommunications_create_participant')
        g.custom_command('get-operation', 'cloudcommunications_get_operation')
        g.custom_command('get-participant', 'cloudcommunications_get_participant')
        g.custom_command('keep-alive', 'cloudcommunications_keep_alive')
        g.custom_command('list-operation', 'cloudcommunications_list_operation')
        g.custom_command('list-participant', 'cloudcommunications_list_participant')
        g.custom_command('log-teleconference-device-quality', 'cloudcommunications_log_teleconference_device_quality')
        g.custom_command('mute', 'cloudcommunications_mute')
        g.custom_command('play-prompt', 'cloudcommunications_play_prompt')
        g.custom_command('record-response', 'cloudcommunications_record_response')
        g.custom_command('redirect', 'cloudcommunications_redirect')
        g.custom_command('reject', 'cloudcommunications_reject')
        g.custom_command('subscribe-to-tone', 'cloudcommunications_subscribe_to_tone')
        g.custom_command('transfer', 'cloudcommunications_transfer')
        g.custom_command('unmute', 'cloudcommunications_unmute')
        g.custom_command('update-operation', 'cloudcommunications_update_operation')
        g.custom_command('update-participant', 'cloudcommunications_update_participant')
        g.custom_command('update-recording-status', 'cloudcommunications_update_recording_status')

    from azext_cloudcommunications.generated._client_factory import cf_communication_call_participant
    cloudcommunications_communication_call_participant = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_call_par'
        'ticipant_operations#CommunicationCallParticipantOperations.{}',
        client_factory=cf_communication_call_participant)
    with self.command_group('cloudcommunications', cloudcommunications_communication_call_participant,
                            client_factory=cf_communication_call_participant) as g:
        g.custom_command('invite', 'cloudcommunications_invite')
        g.custom_command('mute', 'cloudcommunications_mute')

    from azext_cloudcommunications.generated._client_factory import cf_communication_online_meeting
    cloudcommunications_communication_online_meeting = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._communication_online_m'
        'eeting_operations#CommunicationOnlineMeetingOperations.{}',
        client_factory=cf_communication_online_meeting)
    with self.command_group('cloudcommunications', cloudcommunications_communication_online_meeting,
                            client_factory=cf_communication_online_meeting) as g:
        g.custom_command('create-or-get', 'cloudcommunications_create_or_get')

    from azext_cloudcommunications.generated._client_factory import cf_user
    cloudcommunications_user = CliCommandType(
        operations_tmpl='azext_cloudcommunications.vendored_sdks.cloudcommunications.operations._user_operations#UserOp'
        'erations.{}',
        client_factory=cf_user)
    with self.command_group('cloudcommunications', cloudcommunications_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'cloudcommunications_delete', confirmation=True)
        g.custom_command('create-online-meeting', 'cloudcommunications_create_online_meeting')
        g.custom_command('get-online-meeting', 'cloudcommunications_get_online_meeting')
        g.custom_command('list-online-meeting', 'cloudcommunications_list_online_meeting')
        g.custom_command('update-online-meeting', 'cloudcommunications_update_online_meeting')
