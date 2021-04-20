# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class collectionofsubscription(msrest.serialization.Model):
    """Collection of subscription.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~change_notifications.models.microsoftgraphsubscription]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[microsoftgraphsubscription]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        value: Optional[List["microsoftgraphsubscription"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(collectionofsubscription, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.value = value
        self.odata_next_link = odata_next_link


class microsoftgraphentity(msrest.serialization.Model):
    """entity.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphentity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id


class microsoftgraphsubscription(microsoftgraphentity):
    """subscription.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param application_id: Identifier of the application used to create the subscription. Read-
     only.
    :type application_id: str
    :param change_type: Required. Indicates the type of change in the subscribed resource that will
     raise a change notification. The supported values are: created, updated, deleted. Multiple
     values can be combined using a comma-separated list.Note: Drive root item and list change
     notifications support only the updated changeType. User and group change notifications support
     updated and deleted changeType.
    :type change_type: str
    :param client_state: Optional. Specifies the value of the clientState property sent by the
     service in each change notification. The maximum length is 128 characters. The client can check
     that the change notification came from the service by comparing the value of the clientState
     property sent with the subscription with the value of the clientState property received with
     each change notification.
    :type client_state: str
    :param creator_id: Identifier of the user or service principal that created the subscription.
     If the app used delegated permissions to create the subscription, this field contains the id of
     the signed-in user the app called on behalf of. If the app used application permissions, this
     field contains the id of the service principal corresponding to the app. Read-only.
    :type creator_id: str
    :param encryption_certificate: A base64-encoded representation of a certificate with a public
     key used to encrypt resource data in change notifications. Optional. Required when
     includeResourceData is true.
    :type encryption_certificate: str
    :param encryption_certificate_id: A custom app-provided identifier to help identify the
     certificate needed to decrypt resource data. Optional.
    :type encryption_certificate_id: str
    :param expiration_date_time: Required. Specifies the date and time when the webhook
     subscription expires. The time is in UTC, and can be an amount of time from subscription
     creation that varies for the resource subscribed to.  See the table below for maximum supported
     subscription length of time.
    :type expiration_date_time: ~datetime.datetime
    :param include_properties:
    :type include_properties: bool
    :param include_resource_data: When set to true, change notifications include resource data
     (such as content of a chat message). Optional.
    :type include_resource_data: bool
    :param latest_supported_tls_version: Specifies the latest version of Transport Layer Security
     (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible
     values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a
     version lower than the currently recommended version (TLS 1.2), specifying this property by a
     set timeline allows them to temporarily use their deprecated version of TLS before completing
     their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline
     would result in subscription operations failing. For subscribers whose notification endpoint
     already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph
     defaults the property to v1_2.
    :type latest_supported_tls_version: str
    :param lifecycle_notification_url: The URL of the endpoint that receives lifecycle
     notifications, including subscriptionRemoved and missed notifications. This URL must make use
     of the HTTPS protocol. Optional. Read more about how Outlook resources use lifecycle
     notifications.
    :type lifecycle_notification_url: str
    :param notification_url: Required. The URL of the endpoint that will receive the change
     notifications. This URL must make use of the HTTPS protocol.
    :type notification_url: str
    :param resource: Required. Specifies the resource that will be monitored for changes. Do not
     include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values
     for each supported resource.
    :type resource: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'client_state': {'key': 'clientState', 'type': 'str'},
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'encryption_certificate': {'key': 'encryptionCertificate', 'type': 'str'},
        'encryption_certificate_id': {'key': 'encryptionCertificateId', 'type': 'str'},
        'expiration_date_time': {'key': 'expirationDateTime', 'type': 'iso-8601'},
        'include_properties': {'key': 'includeProperties', 'type': 'bool'},
        'include_resource_data': {'key': 'includeResourceData', 'type': 'bool'},
        'latest_supported_tls_version': {'key': 'latestSupportedTlsVersion', 'type': 'str'},
        'lifecycle_notification_url': {'key': 'lifecycleNotificationUrl', 'type': 'str'},
        'notification_url': {'key': 'notificationUrl', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        application_id: Optional[str] = None,
        change_type: Optional[str] = None,
        client_state: Optional[str] = None,
        creator_id: Optional[str] = None,
        encryption_certificate: Optional[str] = None,
        encryption_certificate_id: Optional[str] = None,
        expiration_date_time: Optional[datetime.datetime] = None,
        include_properties: Optional[bool] = None,
        include_resource_data: Optional[bool] = None,
        latest_supported_tls_version: Optional[str] = None,
        lifecycle_notification_url: Optional[str] = None,
        notification_url: Optional[str] = None,
        resource: Optional[str] = None,
        **kwargs
    ):
        super(microsoftgraphsubscription, self).__init__(id=id, **kwargs)
        self.additional_properties = additional_properties
        self.application_id = application_id
        self.change_type = change_type
        self.client_state = client_state
        self.creator_id = creator_id
        self.encryption_certificate = encryption_certificate
        self.encryption_certificate_id = encryption_certificate_id
        self.expiration_date_time = expiration_date_time
        self.include_properties = include_properties
        self.include_resource_data = include_resource_data
        self.latest_supported_tls_version = latest_supported_tls_version
        self.lifecycle_notification_url = lifecycle_notification_url
        self.notification_url = notification_url
        self.resource = resource


class odataerror(msrest.serialization.Model):
    """odataerror.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~change_notifications.models.odataerrormain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'error': {'key': 'error', 'type': 'odataerrormain'},
    }

    def __init__(
        self,
        *,
        error: "odataerrormain",
        additional_properties: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(odataerror, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.error = error


class odataerrordetail(msrest.serialization.Model):
    """odataerrordetail.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(odataerrordetail, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target


class odataerrormain(msrest.serialization.Model):
    """odataerrormain.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~change_notifications.models.odataerrordetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: dict[str, object]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[odataerrordetail]'},
        'innererror': {'key': 'innererror', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        details: Optional[List["odataerrordetail"]] = None,
        innererror: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(odataerrormain, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror
