# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DeviceAppManagementDeviceAppManagementOperations(object):
    """DeviceAppManagementDeviceAppManagementOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~devices_corporate_management.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_device_app_management(
        self,
        select=None,  # type: Optional[List[Union[str, "models.Get0ItemsItem"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get1ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphDeviceAppManagement"
        """Get deviceAppManagement.

        Get deviceAppManagement.

        :param select: Select properties to be returned.
        :type select: list[str or ~devices_corporate_management.models.Get0ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~devices_corporate_management.models.Get1ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDeviceAppManagement, or the result of cls(response)
        :rtype: ~devices_corporate_management.models.MicrosoftGraphDeviceAppManagement
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDeviceAppManagement"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_device_app_management.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDeviceAppManagement', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_device_app_management.metadata = {'url': '/deviceAppManagement'}  # type: ignore

    def update_device_app_management(
        self,
        id=None,  # type: Optional[str]
        is_enabled_for_microsoft_store_for_business=None,  # type: Optional[bool]
        microsoft_store_for_business_language=None,  # type: Optional[str]
        microsoft_store_for_business_last_completed_application_sync_time=None,  # type: Optional[datetime.datetime]
        microsoft_store_for_business_last_successful_sync_date_time=None,  # type: Optional[datetime.datetime]
        managed_e_books=None,  # type: Optional[List["models.MicrosoftGraphManagedEBook"]]
        mobile_app_categories=None,  # type: Optional[List["models.MicrosoftGraphMobileAppCategory"]]
        mobile_app_configurations=None,  # type: Optional[List["models.MicrosoftGraphManagedDeviceMobileAppConfiguration"]]
        mobile_apps=None,  # type: Optional[List["models.MicrosoftGraphMobileApp"]]
        vpp_tokens=None,  # type: Optional[List["models.MicrosoftGraphVppToken"]]
        android_managed_app_protections=None,  # type: Optional[List["models.MicrosoftGraphAndroidManagedAppProtection"]]
        default_managed_app_protections=None,  # type: Optional[List["models.MicrosoftGraphDefaultManagedAppProtection"]]
        ios_managed_app_protections=None,  # type: Optional[List["models.MicrosoftGraphIosManagedAppProtection"]]
        managed_app_policies=None,  # type: Optional[List["models.MicrosoftGraphManagedAppPolicy"]]
        managed_app_registrations=None,  # type: Optional[List["models.MicrosoftGraphManagedAppRegistration"]]
        managed_app_statuses=None,  # type: Optional[List["models.MicrosoftGraphManagedAppStatus"]]
        mdm_windows_information_protection_policies=None,  # type: Optional[List["models.MicrosoftGraphMdmWindowsInformationProtectionPolicy"]]
        targeted_managed_app_configurations=None,  # type: Optional[List["models.MicrosoftGraphTargetedManagedAppConfiguration"]]
        windows_information_protection_policies=None,  # type: Optional[List["models.MicrosoftGraphWindowsInformationProtectionPolicy"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update deviceAppManagement.

        Update deviceAppManagement.

        :param id: Read-only.
        :type id: str
        :param is_enabled_for_microsoft_store_for_business: Whether the account is enabled for syncing
         applications from the Microsoft Store for Business.
        :type is_enabled_for_microsoft_store_for_business: bool
        :param microsoft_store_for_business_language: The locale information used to sync applications
         from the Microsoft Store for Business. Cultures that are specific to a country/region. The
         names of these cultures follow RFC 4646 (Windows Vista and later). The format is
         -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and
         <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US
         for English (United States) is a specific culture.
        :type microsoft_store_for_business_language: str
        :param microsoft_store_for_business_last_completed_application_sync_time: The last time an
         application sync from the Microsoft Store for Business was completed.
        :type microsoft_store_for_business_last_completed_application_sync_time: ~datetime.datetime
        :param microsoft_store_for_business_last_successful_sync_date_time: The last time the apps from
         the Microsoft Store for Business were synced successfully for the account.
        :type microsoft_store_for_business_last_successful_sync_date_time: ~datetime.datetime
        :param managed_e_books: The Managed eBook.
        :type managed_e_books: list[~devices_corporate_management.models.MicrosoftGraphManagedEBook]
        :param mobile_app_categories: The mobile app categories.
        :type mobile_app_categories: list[~devices_corporate_management.models.MicrosoftGraphMobileAppCategory]
        :param mobile_app_configurations: The Managed Device Mobile Application Configurations.
        :type mobile_app_configurations: list[~devices_corporate_management.models.MicrosoftGraphManagedDeviceMobileAppConfiguration]
        :param mobile_apps: The mobile apps.
        :type mobile_apps: list[~devices_corporate_management.models.MicrosoftGraphMobileApp]
        :param vpp_tokens: List of Vpp tokens for this organization.
        :type vpp_tokens: list[~devices_corporate_management.models.MicrosoftGraphVppToken]
        :param android_managed_app_protections: Android managed app policies.
        :type android_managed_app_protections: list[~devices_corporate_management.models.MicrosoftGraphAndroidManagedAppProtection]
        :param default_managed_app_protections: Default managed app policies.
        :type default_managed_app_protections: list[~devices_corporate_management.models.MicrosoftGraphDefaultManagedAppProtection]
        :param ios_managed_app_protections: iOS managed app policies.
        :type ios_managed_app_protections: list[~devices_corporate_management.models.MicrosoftGraphIosManagedAppProtection]
        :param managed_app_policies: Managed app policies.
        :type managed_app_policies: list[~devices_corporate_management.models.MicrosoftGraphManagedAppPolicy]
        :param managed_app_registrations: The managed app registrations.
        :type managed_app_registrations: list[~devices_corporate_management.models.MicrosoftGraphManagedAppRegistration]
        :param managed_app_statuses: The managed app statuses.
        :type managed_app_statuses: list[~devices_corporate_management.models.MicrosoftGraphManagedAppStatus]
        :param mdm_windows_information_protection_policies: Windows information protection for apps
         running on devices which are MDM enrolled.
        :type mdm_windows_information_protection_policies: list[~devices_corporate_management.models.MicrosoftGraphMdmWindowsInformationProtectionPolicy]
        :param targeted_managed_app_configurations: Targeted managed app configurations.
        :type targeted_managed_app_configurations: list[~devices_corporate_management.models.MicrosoftGraphTargetedManagedAppConfiguration]
        :param windows_information_protection_policies: Windows information protection for apps running
         on devices which are not MDM enrolled.
        :type windows_information_protection_policies: list[~devices_corporate_management.models.MicrosoftGraphWindowsInformationProtectionPolicy]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.MicrosoftGraphDeviceAppManagement(id=id, is_enabled_for_microsoft_store_for_business=is_enabled_for_microsoft_store_for_business, microsoft_store_for_business_language=microsoft_store_for_business_language, microsoft_store_for_business_last_completed_application_sync_time=microsoft_store_for_business_last_completed_application_sync_time, microsoft_store_for_business_last_successful_sync_date_time=microsoft_store_for_business_last_successful_sync_date_time, managed_e_books=managed_e_books, mobile_app_categories=mobile_app_categories, mobile_app_configurations=mobile_app_configurations, mobile_apps=mobile_apps, vpp_tokens=vpp_tokens, android_managed_app_protections=android_managed_app_protections, default_managed_app_protections=default_managed_app_protections, ios_managed_app_protections=ios_managed_app_protections, managed_app_policies=managed_app_policies, managed_app_registrations=managed_app_registrations, managed_app_statuses=managed_app_statuses, mdm_windows_information_protection_policies=mdm_windows_information_protection_policies, targeted_managed_app_configurations=targeted_managed_app_configurations, windows_information_protection_policies=windows_information_protection_policies)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_device_app_management.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphDeviceAppManagement')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_device_app_management.metadata = {'url': '/deviceAppManagement'}  # type: ignore
