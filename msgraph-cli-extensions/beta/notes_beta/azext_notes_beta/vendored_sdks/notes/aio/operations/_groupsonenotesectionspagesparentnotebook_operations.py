# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class groupsonenotesectionspagesparentnotebookOperations:
    """groupsonenotesectionspagesparentnotebookOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~notes.models
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

    def list_section_groups(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        orderby: Optional[List[Union[str, "models.Enum288"]]] = None,
        select: Optional[List[Union[str, "models.Enum289"]]] = None,
        expand: Optional[List[Union[str, "models.Enum290"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.collectionofsectiongroup14"]:
        """Get sectionGroups from groups.

        Get sectionGroups from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~notes.models.Enum288]
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum289]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum290]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofsectiongroup14 or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~notes.models.collectionofsectiongroup14]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofsectiongroup14"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_section_groups.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                    'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
                    'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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
            deserialized = self._deserialize('collectionofsectiongroup14', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_section_groups.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sectionGroups'}  # type: ignore

    async def create_section_groups(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        body: "models.microsoftgraphsectiongroup",
        **kwargs
    ) -> "models.microsoftgraphsectiongroup":
        """Create new navigation property to sectionGroups for groups.

        Create new navigation property to sectionGroups for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param body: New navigation property.
        :type body: ~notes.models.microsoftgraphsectiongroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphsectiongroup, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphsectiongroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphsectiongroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_section_groups.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphsectiongroup')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphsectiongroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_section_groups.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sectionGroups'}  # type: ignore

    async def get_section_groups(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        section_group_id: str,
        select: Optional[List[Union[str, "models.Enum291"]]] = None,
        expand: Optional[List[Union[str, "models.Enum292"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphsectiongroup":
        """Get sectionGroups from groups.

        Get sectionGroups from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param section_group_id: key: id of sectionGroup.
        :type section_group_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum291]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum292]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphsectiongroup, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphsectiongroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphsectiongroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_section_groups.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'sectionGroup-id': self._serialize.url("section_group_id", section_group_id, 'str'),
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

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphsectiongroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_section_groups.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sectionGroups/{sectionGroup-id}'}  # type: ignore

    async def update_section_groups(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        section_group_id: str,
        body: "models.microsoftgraphsectiongroup",
        **kwargs
    ) -> None:
        """Update the navigation property sectionGroups in groups.

        Update the navigation property sectionGroups in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param section_group_id: key: id of sectionGroup.
        :type section_group_id: str
        :param body: New navigation property values.
        :type body: ~notes.models.microsoftgraphsectiongroup
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
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_section_groups.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'sectionGroup-id': self._serialize.url("section_group_id", section_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphsectiongroup')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_section_groups.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sectionGroups/{sectionGroup-id}'}  # type: ignore

    async def delete_section_groups(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        section_group_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property sectionGroups for groups.

        Delete navigation property sectionGroups for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param section_group_id: key: id of sectionGroup.
        :type section_group_id: str
        :param if_match: ETag.
        :type if_match: str
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
        accept = "application/json"

        # Construct URL
        url = self.delete_section_groups.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'sectionGroup-id': self._serialize.url("section_group_id", section_group_id, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_section_groups.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sectionGroups/{sectionGroup-id}'}  # type: ignore

    def list_sections(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        orderby: Optional[List[Union[str, "models.Enum307"]]] = None,
        select: Optional[List[Union[str, "models.Enum308"]]] = None,
        expand: Optional[List[Union[str, "models.Enum309"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.collectionofonenotesection15"]:
        """Get sections from groups.

        Get sections from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~notes.models.Enum307]
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum308]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum309]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofonenotesection15 or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~notes.models.collectionofonenotesection15]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofonenotesection15"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_sections.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                    'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
                    'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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
            deserialized = self._deserialize('collectionofonenotesection15', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_sections.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sections'}  # type: ignore

    async def create_sections(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        body: "models.microsoftgraphonenotesection",
        **kwargs
    ) -> "models.microsoftgraphonenotesection":
        """Create new navigation property to sections for groups.

        Create new navigation property to sections for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param body: New navigation property.
        :type body: ~notes.models.microsoftgraphonenotesection
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphonenotesection, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphonenotesection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphonenotesection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_sections.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphonenotesection')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphonenotesection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_sections.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sections'}  # type: ignore

    async def get_sections(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        onenote_section_id1: str,
        select: Optional[List[Union[str, "models.Enum310"]]] = None,
        expand: Optional[List[Union[str, "models.Enum311"]]] = None,
        **kwargs
    ) -> "models.microsoftgraphonenotesection":
        """Get sections from groups.

        Get sections from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param onenote_section_id1: key: id of onenoteSection.
        :type onenote_section_id1: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum310]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum311]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphonenotesection, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphonenotesection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphonenotesection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_sections.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenoteSection-id1': self._serialize.url("onenote_section_id1", onenote_section_id1, 'str'),
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

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphonenotesection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_sections.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sections/{onenoteSection-id1}'}  # type: ignore

    async def update_sections(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        onenote_section_id1: str,
        body: "models.microsoftgraphonenotesection",
        **kwargs
    ) -> None:
        """Update the navigation property sections in groups.

        Update the navigation property sections in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param onenote_section_id1: key: id of onenoteSection.
        :type onenote_section_id1: str
        :param body: New navigation property values.
        :type body: ~notes.models.microsoftgraphonenotesection
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
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_sections.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenoteSection-id1': self._serialize.url("onenote_section_id1", onenote_section_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphonenotesection')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_sections.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sections/{onenoteSection-id1}'}  # type: ignore

    async def delete_sections(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_page_id: str,
        onenote_section_id1: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property sections for groups.

        Delete navigation property sections for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param onenote_section_id1: key: id of onenoteSection.
        :type onenote_section_id1: str
        :param if_match: ETag.
        :type if_match: str
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
        accept = "application/json"

        # Construct URL
        url = self.delete_sections.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenoteSection-id1': self._serialize.url("onenote_section_id1", onenote_section_id1, 'str'),
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
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_sections.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}/parentNotebook/sections/{onenoteSection-id1}'}  # type: ignore
