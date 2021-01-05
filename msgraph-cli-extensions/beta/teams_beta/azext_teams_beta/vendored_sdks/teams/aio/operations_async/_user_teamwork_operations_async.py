# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserTeamworkOperations:
    """UserTeamworkOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~teams.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_installed_app(
        self,
        user_id: str,
        orderby: Optional[List[Union[str, "models.Enum302"]]] = None,
        select: Optional[List[Union[str, "models.Enum303"]]] = None,
        expand: Optional[List[Union[str, "models.Enum304"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfUserScopeTeamsAppInstallation"]:
        """Get installedApps from users.

        Get installedApps from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~teams.models.Enum302]
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum303]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams.models.Enum304]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfUserScopeTeamsAppInstallation or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~teams.models.CollectionOfUserScopeTeamsAppInstallation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfUserScopeTeamsAppInstallation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_installed_app.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfUserScopeTeamsAppInstallation', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps'}  # type: ignore

    async def create_installed_app(
        self,
        user_id: str,
        id: Optional[str] = None,
        microsoft_graph_entity_id: Optional[str] = None,
        azure_ad_app_id: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        publishing_state: Optional[Union[str, "models.MicrosoftGraphTeamsAppPublishingState"]] = None,
        shortdescription: Optional[str] = None,
        teams_app_id: Optional[str] = None,
        version: Optional[str] = None,
        microsoft_graph_identity_display_name: Optional[str] = None,
        microsoft_graph_identity_id: Optional[str] = None,
        display_name1: Optional[str] = None,
        id1: Optional[str] = None,
        display_name2: Optional[str] = None,
        id2: Optional[str] = None,
        id3: Optional[str] = None,
        microsoft_graph_teams_app_display_name: Optional[str] = None,
        distribution_method: Optional[Union[str, "models.MicrosoftGraphTeamsAppDistributionMethod"]] = None,
        external_id: Optional[str] = None,
        app_definitions: Optional[List["models.MicrosoftGraphTeamsAppDefinition"]] = None,
        id4: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        last_updated_date_time: Optional[datetime.datetime] = None,
        topic: Optional[str] = None,
        installed_apps: Optional[List["models.MicrosoftGraphTeamsAppInstallation"]] = None,
        members: Optional[List["models.MicrosoftGraphConversationMember"]] = None,
        messages: Optional[List["models.MicrosoftGraphChatMessage"]] = None,
        tabs: Optional[List["models.MicrosoftGraphTeamsTab"]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphUserScopeTeamsAppInstallation":
        """Create new navigation property to installedApps for users.

        Create new navigation property to installedApps for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param azure_ad_app_id:
        :type azure_ad_app_id: str
        :param description:
        :type description: str
        :param display_name: The name of the app provided by the app developer.
        :type display_name: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param publishing_state:
        :type publishing_state: str or ~teams.models.MicrosoftGraphTeamsAppPublishingState
        :param shortdescription:
        :type shortdescription: str
        :param teams_app_id: The ID from the Teams app manifest.
        :type teams_app_id: str
        :param version: The version number of the application.
        :type version: str
        :param microsoft_graph_identity_display_name: The identity's display name. Note that this may
         not always be available or up to date. For example, if a user changes their display name, the
         API may show the new value in a future response, but the items associated with the user won't
         show up as having changed when using delta.
        :type microsoft_graph_identity_display_name: str
        :param microsoft_graph_identity_id: Unique identifier for the identity.
        :type microsoft_graph_identity_id: str
        :param display_name1: The identity's display name. Note that this may not always be available
         or up to date. For example, if a user changes their display name, the API may show the new
         value in a future response, but the items associated with the user won't show up as having
         changed when using delta.
        :type display_name1: str
        :param id1: Unique identifier for the identity.
        :type id1: str
        :param display_name2: The identity's display name. Note that this may not always be available
         or up to date. For example, if a user changes their display name, the API may show the new
         value in a future response, but the items associated with the user won't show up as having
         changed when using delta.
        :type display_name2: str
        :param id2: Unique identifier for the identity.
        :type id2: str
        :param id3: Read-only.
        :type id3: str
        :param microsoft_graph_teams_app_display_name: The name of the catalog app provided by the app
         developer in the Microsoft Teams zip app package.
        :type microsoft_graph_teams_app_display_name: str
        :param distribution_method:
        :type distribution_method: str or ~teams.models.MicrosoftGraphTeamsAppDistributionMethod
        :param external_id: The ID of the catalog provided by the app developer in the Microsoft Teams
         zip app package.
        :type external_id: str
        :param app_definitions: The details for each version of the app.
        :type app_definitions: list[~teams.models.MicrosoftGraphTeamsAppDefinition]
        :param id4: Read-only.
        :type id4: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param last_updated_date_time:
        :type last_updated_date_time: ~datetime.datetime
        :param topic:
        :type topic: str
        :param installed_apps:
        :type installed_apps: list[~teams.models.MicrosoftGraphTeamsAppInstallation]
        :param members:
        :type members: list[~teams.models.MicrosoftGraphConversationMember]
        :param messages:
        :type messages: list[~teams.models.MicrosoftGraphChatMessage]
        :param tabs:
        :type tabs: list[~teams.models.MicrosoftGraphTeamsTab]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphUserScopeTeamsAppInstallation, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphUserScopeTeamsAppInstallation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphUserScopeTeamsAppInstallation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphUserScopeTeamsAppInstallation(id=id, id_teams_app_definition_id=microsoft_graph_entity_id, azure_ad_app_id=azure_ad_app_id, description=description, display_name_teams_app_definition_display_name=display_name, last_modified_date_time=last_modified_date_time, publishing_state=publishing_state, shortdescription=shortdescription, teams_app_id=teams_app_id, version=version, display_name_teams_app_definition_created_by_user_display_name=microsoft_graph_identity_display_name, id_teams_app_definition_created_by_user_id=microsoft_graph_identity_id, display_name_teams_app_definition_created_by_device_display_name=display_name1, id_teams_app_definition_created_by_device_id=id1, display_name_teams_app_definition_created_by_application_display_name=display_name2, id_teams_app_definition_created_by_application_id=id2, id_teams_app_id=id3, display_name_teams_app_display_name=microsoft_graph_teams_app_display_name, distribution_method=distribution_method, external_id=external_id, app_definitions=app_definitions, id_chat_id=id4, created_date_time=created_date_time, last_updated_date_time=last_updated_date_time, topic=topic, installed_apps=installed_apps, members=members, messages=messages, tabs=tabs)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphUserScopeTeamsAppInstallation')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphUserScopeTeamsAppInstallation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps'}  # type: ignore

    async def get_installed_app(
        self,
        user_id: str,
        user_scope_teams_app_installation_id: str,
        select: Optional[List[Union[str, "models.Enum305"]]] = None,
        expand: Optional[List[Union[str, "models.Enum306"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphUserScopeTeamsAppInstallation":
        """Get installedApps from users.

        Get installedApps from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_scope_teams_app_installation_id: key: id of userScopeTeamsAppInstallation.
        :type user_scope_teams_app_installation_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum305]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams.models.Enum306]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphUserScopeTeamsAppInstallation, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphUserScopeTeamsAppInstallation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphUserScopeTeamsAppInstallation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userScopeTeamsAppInstallation-id': self._serialize.url("user_scope_teams_app_installation_id", user_scope_teams_app_installation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphUserScopeTeamsAppInstallation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps/{userScopeTeamsAppInstallation-id}'}  # type: ignore

    async def update_installed_app(
        self,
        user_id: str,
        user_scope_teams_app_installation_id: str,
        id: Optional[str] = None,
        microsoft_graph_entity_id: Optional[str] = None,
        azure_ad_app_id: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        publishing_state: Optional[Union[str, "models.MicrosoftGraphTeamsAppPublishingState"]] = None,
        shortdescription: Optional[str] = None,
        teams_app_id: Optional[str] = None,
        version: Optional[str] = None,
        microsoft_graph_identity_display_name: Optional[str] = None,
        microsoft_graph_identity_id: Optional[str] = None,
        display_name1: Optional[str] = None,
        id1: Optional[str] = None,
        display_name2: Optional[str] = None,
        id2: Optional[str] = None,
        id3: Optional[str] = None,
        microsoft_graph_teams_app_display_name: Optional[str] = None,
        distribution_method: Optional[Union[str, "models.MicrosoftGraphTeamsAppDistributionMethod"]] = None,
        external_id: Optional[str] = None,
        app_definitions: Optional[List["models.MicrosoftGraphTeamsAppDefinition"]] = None,
        id4: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        last_updated_date_time: Optional[datetime.datetime] = None,
        topic: Optional[str] = None,
        installed_apps: Optional[List["models.MicrosoftGraphTeamsAppInstallation"]] = None,
        members: Optional[List["models.MicrosoftGraphConversationMember"]] = None,
        messages: Optional[List["models.MicrosoftGraphChatMessage"]] = None,
        tabs: Optional[List["models.MicrosoftGraphTeamsTab"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property installedApps in users.

        Update the navigation property installedApps in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_scope_teams_app_installation_id: key: id of userScopeTeamsAppInstallation.
        :type user_scope_teams_app_installation_id: str
        :param id: Read-only.
        :type id: str
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param azure_ad_app_id:
        :type azure_ad_app_id: str
        :param description:
        :type description: str
        :param display_name: The name of the app provided by the app developer.
        :type display_name: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param publishing_state:
        :type publishing_state: str or ~teams.models.MicrosoftGraphTeamsAppPublishingState
        :param shortdescription:
        :type shortdescription: str
        :param teams_app_id: The ID from the Teams app manifest.
        :type teams_app_id: str
        :param version: The version number of the application.
        :type version: str
        :param microsoft_graph_identity_display_name: The identity's display name. Note that this may
         not always be available or up to date. For example, if a user changes their display name, the
         API may show the new value in a future response, but the items associated with the user won't
         show up as having changed when using delta.
        :type microsoft_graph_identity_display_name: str
        :param microsoft_graph_identity_id: Unique identifier for the identity.
        :type microsoft_graph_identity_id: str
        :param display_name1: The identity's display name. Note that this may not always be available
         or up to date. For example, if a user changes their display name, the API may show the new
         value in a future response, but the items associated with the user won't show up as having
         changed when using delta.
        :type display_name1: str
        :param id1: Unique identifier for the identity.
        :type id1: str
        :param display_name2: The identity's display name. Note that this may not always be available
         or up to date. For example, if a user changes their display name, the API may show the new
         value in a future response, but the items associated with the user won't show up as having
         changed when using delta.
        :type display_name2: str
        :param id2: Unique identifier for the identity.
        :type id2: str
        :param id3: Read-only.
        :type id3: str
        :param microsoft_graph_teams_app_display_name: The name of the catalog app provided by the app
         developer in the Microsoft Teams zip app package.
        :type microsoft_graph_teams_app_display_name: str
        :param distribution_method:
        :type distribution_method: str or ~teams.models.MicrosoftGraphTeamsAppDistributionMethod
        :param external_id: The ID of the catalog provided by the app developer in the Microsoft Teams
         zip app package.
        :type external_id: str
        :param app_definitions: The details for each version of the app.
        :type app_definitions: list[~teams.models.MicrosoftGraphTeamsAppDefinition]
        :param id4: Read-only.
        :type id4: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param last_updated_date_time:
        :type last_updated_date_time: ~datetime.datetime
        :param topic:
        :type topic: str
        :param installed_apps:
        :type installed_apps: list[~teams.models.MicrosoftGraphTeamsAppInstallation]
        :param members:
        :type members: list[~teams.models.MicrosoftGraphConversationMember]
        :param messages:
        :type messages: list[~teams.models.MicrosoftGraphChatMessage]
        :param tabs:
        :type tabs: list[~teams.models.MicrosoftGraphTeamsTab]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphUserScopeTeamsAppInstallation(id=id, id_teams_app_definition_id=microsoft_graph_entity_id, azure_ad_app_id=azure_ad_app_id, description=description, display_name_teams_app_definition_display_name=display_name, last_modified_date_time=last_modified_date_time, publishing_state=publishing_state, shortdescription=shortdescription, teams_app_id=teams_app_id, version=version, display_name_teams_app_definition_created_by_user_display_name=microsoft_graph_identity_display_name, id_teams_app_definition_created_by_user_id=microsoft_graph_identity_id, display_name_teams_app_definition_created_by_device_display_name=display_name1, id_teams_app_definition_created_by_device_id=id1, display_name_teams_app_definition_created_by_application_display_name=display_name2, id_teams_app_definition_created_by_application_id=id2, id_teams_app_id=id3, display_name_teams_app_display_name=microsoft_graph_teams_app_display_name, distribution_method=distribution_method, external_id=external_id, app_definitions=app_definitions, id_chat_id=id4, created_date_time=created_date_time, last_updated_date_time=last_updated_date_time, topic=topic, installed_apps=installed_apps, members=members, messages=messages, tabs=tabs)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userScopeTeamsAppInstallation-id': self._serialize.url("user_scope_teams_app_installation_id", user_scope_teams_app_installation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphUserScopeTeamsAppInstallation')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps/{userScopeTeamsAppInstallation-id}'}  # type: ignore

    async def delete_installed_app(
        self,
        user_id: str,
        user_scope_teams_app_installation_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property installedApps for users.

        Delete navigation property installedApps for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_scope_teams_app_installation_id: key: id of userScopeTeamsAppInstallation.
        :type user_scope_teams_app_installation_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userScopeTeamsAppInstallation-id': self._serialize.url("user_scope_teams_app_installation_id", user_scope_teams_app_installation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps/{userScopeTeamsAppInstallation-id}'}  # type: ignore
