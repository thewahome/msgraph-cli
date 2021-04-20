# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class groupsonenotesectionsOperations(object):
    """groupsonenotesectionsOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_pages(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum281"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum282"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum283"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.collectionofonenotepage7"]
        """Get pages from groups.

        Get pages from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~notes.models.Enum281]
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum282]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum283]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofonenotepage7 or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~notes.models.collectionofonenotepage7]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofonenotepage7"]
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
                url = self.list_pages.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                    'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('collectionofonenotepage7', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_pages.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages'}  # type: ignore

    def create_pages(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        body,  # type: "models.microsoftgraphonenotepage"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphonenotepage"
        """Create new navigation property to pages for groups.

        Create new navigation property to pages for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param body: New navigation property.
        :type body: ~notes.models.microsoftgraphonenotepage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphonenotepage, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphonenotepage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphonenotepage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_pages.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphonenotepage')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphonenotepage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_pages.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages'}  # type: ignore

    def get_pages(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        onenote_page_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum284"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum285"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphonenotepage"
        """Get pages from groups.

        Get pages from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum284]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum285]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphonenotepage, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphonenotepage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphonenotepage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_pages.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphonenotepage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_pages.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}'}  # type: ignore

    def update_pages(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        onenote_page_id,  # type: str
        body,  # type: "models.microsoftgraphonenotepage"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property pages in groups.

        Update the navigation property pages in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param body: New navigation property values.
        :type body: ~notes.models.microsoftgraphonenotepage
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
        url = self.update_pages.metadata['url']  # type: ignore
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
        body_content = self._serialize.body(body, 'microsoftgraphonenotepage')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_pages.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}'}  # type: ignore

    def delete_pages(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        onenote_page_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property pages for groups.

        Delete navigation property pages for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
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
        url = self.delete_pages.metadata['url']  # type: ignore
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
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_pages.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/pages/{onenotePage-id}'}  # type: ignore

    def get_parent_notebook(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum314"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum315"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphnotebook"
        """Get parentNotebook from groups.

        Get parentNotebook from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum314]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum315]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphnotebook, or the result of cls(response)
        :rtype: ~notes.models.microsoftgraphnotebook
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphnotebook"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphnotebook', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent_notebook.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentNotebook'}  # type: ignore

    def update_parent_notebook(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        body,  # type: "models.microsoftgraphnotebook"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property parentNotebook in groups.

        Update the navigation property parentNotebook in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param body: New navigation property values.
        :type body: ~notes.models.microsoftgraphnotebook
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
        url = self.update_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphnotebook')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_parent_notebook.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentNotebook'}  # type: ignore

    def delete_parent_notebook(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property parentNotebook for groups.

        Delete navigation property parentNotebook for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
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
        url = self.delete_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_parent_notebook.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentNotebook'}  # type: ignore

    def get_parent_section_group(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum340"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum341"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphsectiongroup"
        """Get parentSectionGroup from groups.

        Get parentSectionGroup from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum340]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum341]
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
        url = self.get_parent_section_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphsectiongroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent_section_group.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentSectionGroup'}  # type: ignore

    def update_parent_section_group(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        body,  # type: "models.microsoftgraphsectiongroup"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property parentSectionGroup in groups.

        Update the navigation property parentSectionGroup in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
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
        url = self.update_parent_section_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_parent_section_group.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentSectionGroup'}  # type: ignore

    def delete_parent_section_group(
        self,
        group_id,  # type: str
        onenote_section_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property parentSectionGroup for groups.

        Delete navigation property parentSectionGroup for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
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
        url = self.delete_parent_section_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_parent_section_group.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentSectionGroup'}  # type: ignore
