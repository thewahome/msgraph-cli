# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class Get2ItemsItem(str, Enum):

    id = "id"
    creation_date_time = "creationDateTime"
    start_date_time = "startDateTime"
    end_date_time = "endDateTime"
    canceled_date_time = "canceledDateTime"
    expiration_date_time = "expirationDateTime"
    entry_exit_announcement = "entryExitAnnouncement"
    join_url = "joinUrl"
    subject = "subject"
    is_cancelled = "isCancelled"
    participants = "participants"
    is_broadcast = "isBroadcast"
    access_level = "accessLevel"
    capabilities = "capabilities"
    audio_conferencing = "audioConferencing"
    chat_info = "chatInfo"
    video_teleconference_id = "videoTeleconferenceId"
    external_id = "externalId"
    join_information = "joinInformation"

class Get6ItemsItem(str, Enum):

    id = "id"
    id_desc = "id desc"
    creation_date_time = "creationDateTime"
    creation_date_time_desc = "creationDateTime desc"
    start_date_time = "startDateTime"
    start_date_time_desc = "startDateTime desc"
    end_date_time = "endDateTime"
    end_date_time_desc = "endDateTime desc"
    canceled_date_time = "canceledDateTime"
    canceled_date_time_desc = "canceledDateTime desc"
    expiration_date_time = "expirationDateTime"
    expiration_date_time_desc = "expirationDateTime desc"
    entry_exit_announcement = "entryExitAnnouncement"
    entry_exit_announcement_desc = "entryExitAnnouncement desc"
    join_url = "joinUrl"
    join_url_desc = "joinUrl desc"
    subject = "subject"
    subject_desc = "subject desc"
    is_cancelled = "isCancelled"
    is_cancelled_desc = "isCancelled desc"
    participants = "participants"
    participants_desc = "participants desc"
    is_broadcast = "isBroadcast"
    is_broadcast_desc = "isBroadcast desc"
    access_level = "accessLevel"
    access_level_desc = "accessLevel desc"
    capabilities = "capabilities"
    capabilities_desc = "capabilities desc"
    audio_conferencing = "audioConferencing"
    audio_conferencing_desc = "audioConferencing desc"
    chat_info = "chatInfo"
    chat_info_desc = "chatInfo desc"
    video_teleconference_id = "videoTeleconferenceId"
    video_teleconference_id_desc = "videoTeleconferenceId desc"
    external_id = "externalId"
    external_id_desc = "externalId desc"
    join_information = "joinInformation"
    join_information_desc = "joinInformation desc"

class Get7ItemsItem(str, Enum):

    id = "id"
    creation_date_time = "creationDateTime"
    start_date_time = "startDateTime"
    end_date_time = "endDateTime"
    canceled_date_time = "canceledDateTime"
    expiration_date_time = "expirationDateTime"
    entry_exit_announcement = "entryExitAnnouncement"
    join_url = "joinUrl"
    subject = "subject"
    is_cancelled = "isCancelled"
    participants = "participants"
    is_broadcast = "isBroadcast"
    access_level = "accessLevel"
    capabilities = "capabilities"
    audio_conferencing = "audioConferencing"
    chat_info = "chatInfo"
    video_teleconference_id = "videoTeleconferenceId"
    external_id = "externalId"
    join_information = "joinInformation"

class MicrosoftGraphAccessLevel(str, Enum):

    everyone = "everyone"
    invited = "invited"
    locked = "locked"
    same_enterprise = "sameEnterprise"
    same_enterprise_and_federated = "sameEnterpriseAndFederated"

class MicrosoftGraphBodyType(str, Enum):

    text = "text"
    html = "html"

class MicrosoftGraphMeetingCapabilities(str, Enum):

    question_and_answer = "questionAndAnswer"
    unknown_future_value = "unknownFutureValue"
