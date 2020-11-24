# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_three_state_flag


def load_arguments(self, _):

    with self.argument_context('changenotifications delete') as c:
        c.argument('subscription_id', type=str, help='key: id of subscription', id_part='subscription')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('changenotifications create-subscription') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('application_id', type=str, help='Identifier of the application used to create the subscription. '
                   'Read-only.')
        c.argument('change_type', type=str, help='Required. Indicates the type of change in the subscribed resource '
                   'that will raise a change notification. The supported values are: created, updated, deleted. '
                   'Multiple values can be combined using a comma-separated list.Note: Drive root item and list change '
                   'notifications support only the updated changeType. User and group change notifications support '
                   'updated and deleted changeType.')
        c.argument('client_state', type=str, help='Optional. Specifies the value of the clientState property sent by '
                   'the service in each change notification. The maximum length is 128 characters. The client can '
                   'check that the change notification came from the service by comparing the value of the clientState '
                   'property sent with the subscription with the value of the clientState property received with each '
                   'change notification.')
        c.argument('creator_id', type=str, help='Identifier of the user or service principal that created the '
                   'subscription. If the app used delegated permissions to create the subscription, this field '
                   'contains the id of the signed-in user the app called on behalf of. If the app used application '
                   'permissions, this field contains the id of the service principal corresponding to the app. '
                   'Read-only.')
        c.argument('encryption_certificate', type=str, help='A base64-encoded representation of a certificate with a '
                   'public key used to encrypt resource data in change notifications. Optional. Required when '
                   'includeResourceData is true.')
        c.argument('encryption_certificate_id', type=str, help='A custom app-provided identifier to help identify the '
                   'certificate needed to decrypt resource data. Optional.')
        c.argument('expiration_date_time', help='Required. Specifies the date and time when the webhook subscription '
                   'expires. The time is in UTC, and can be an amount of time from subscription creation that varies '
                   'for the resource subscribed to.  See the table below for maximum supported subscription length of '
                   'time.')
        c.argument('include_resource_data', arg_type=get_three_state_flag(), help='When set to true, change '
                   'notifications include resource data (such as content of a chat message). Optional.')
        c.argument('latest_supported_tls_version', type=str, help='Specifies the latest version of Transport Layer '
                   'Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The '
                   'possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports '
                   'a version lower than the currently recommended version (TLS 1.2), specifying this property by a '
                   'set timeline allows them to temporarily use their deprecated version of TLS before completing '
                   'their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would '
                   'result in subscription operations failing. For subscribers whose notification endpoint already '
                   'supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the '
                   'property to v1_2.')
        c.argument('lifecycle_notification_url', type=str, help='The URL of the endpoint that receives lifecycle '
                   'notifications, including subscriptionRemoved and missed notifications. This URL must make use of '
                   'the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.')
        c.argument('notification_url', type=str, help='Required. The URL of the endpoint that will receive the change '
                   'notifications. This URL must make use of the HTTPS protocol.')
        c.argument('resource', type=str, help='Required. Specifies the resource that will be monitored for changes. Do '
                   'not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path '
                   'values for each supported resource.')

    with self.argument_context('changenotifications get-subscription') as c:
        c.argument('subscription_id', type=str, help='key: id of subscription', id_part='subscription')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('changenotifications list-subscription') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('changenotifications update-subscription') as c:
        c.argument('subscription_id', type=str, help='key: id of subscription', id_part='subscription')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('application_id', type=str, help='Identifier of the application used to create the subscription. '
                   'Read-only.')
        c.argument('change_type', type=str, help='Required. Indicates the type of change in the subscribed resource '
                   'that will raise a change notification. The supported values are: created, updated, deleted. '
                   'Multiple values can be combined using a comma-separated list.Note: Drive root item and list change '
                   'notifications support only the updated changeType. User and group change notifications support '
                   'updated and deleted changeType.')
        c.argument('client_state', type=str, help='Optional. Specifies the value of the clientState property sent by '
                   'the service in each change notification. The maximum length is 128 characters. The client can '
                   'check that the change notification came from the service by comparing the value of the clientState '
                   'property sent with the subscription with the value of the clientState property received with each '
                   'change notification.')
        c.argument('creator_id', type=str, help='Identifier of the user or service principal that created the '
                   'subscription. If the app used delegated permissions to create the subscription, this field '
                   'contains the id of the signed-in user the app called on behalf of. If the app used application '
                   'permissions, this field contains the id of the service principal corresponding to the app. '
                   'Read-only.')
        c.argument('encryption_certificate', type=str, help='A base64-encoded representation of a certificate with a '
                   'public key used to encrypt resource data in change notifications. Optional. Required when '
                   'includeResourceData is true.')
        c.argument('encryption_certificate_id', type=str, help='A custom app-provided identifier to help identify the '
                   'certificate needed to decrypt resource data. Optional.')
        c.argument('expiration_date_time', help='Required. Specifies the date and time when the webhook subscription '
                   'expires. The time is in UTC, and can be an amount of time from subscription creation that varies '
                   'for the resource subscribed to.  See the table below for maximum supported subscription length of '
                   'time.')
        c.argument('include_resource_data', arg_type=get_three_state_flag(), help='When set to true, change '
                   'notifications include resource data (such as content of a chat message). Optional.')
        c.argument('latest_supported_tls_version', type=str, help='Specifies the latest version of Transport Layer '
                   'Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The '
                   'possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports '
                   'a version lower than the currently recommended version (TLS 1.2), specifying this property by a '
                   'set timeline allows them to temporarily use their deprecated version of TLS before completing '
                   'their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would '
                   'result in subscription operations failing. For subscribers whose notification endpoint already '
                   'supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the '
                   'property to v1_2.')
        c.argument('lifecycle_notification_url', type=str, help='The URL of the endpoint that receives lifecycle '
                   'notifications, including subscriptionRemoved and missed notifications. This URL must make use of '
                   'the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle notifications.')
        c.argument('notification_url', type=str, help='Required. The URL of the endpoint that will receive the change '
                   'notifications. This URL must make use of the HTTPS protocol.')
        c.argument('resource', type=str, help='Required. Specifies the resource that will be monitored for changes. Do '
                   'not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path '
                   'values for each supported resource.')
