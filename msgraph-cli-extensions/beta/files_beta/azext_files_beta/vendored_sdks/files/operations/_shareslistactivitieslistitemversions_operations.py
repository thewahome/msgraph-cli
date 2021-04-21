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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class shareslistactivitieslistitemversionsOperations(object):
    """shareslistactivitieslistitemversionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~files.models
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

    def get_fields(
        self,
        shared_drive_item_id,  # type: str
        item_activity_old_id,  # type: str
        list_item_version_id,  # type: str
        select=None,  # type: Optional[List[str]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphfieldvalueset"
        """Get fields from shares.

        Get fields from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param list_item_version_id: key: id of listItemVersion.
        :type list_item_version_id: str
        :param select: Select properties to be returned.
        :type select: list[str]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphfieldvalueset, or the result of cls(response)
        :rtype: ~files.models.microsoftgraphfieldvalueset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphfieldvalueset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_fields.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
            'listItemVersion-id': self._serialize.url("list_item_version_id", list_item_version_id, 'str'),
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

        deserialized = self._deserialize('microsoftgraphfieldvalueset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_fields.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem/versions/{listItemVersion-id}/fields'}  # type: ignore

    def update_fields(
        self,
        shared_drive_item_id,  # type: str
        item_activity_old_id,  # type: str
        list_item_version_id,  # type: str
        body,  # type: "models.microsoftgraphfieldvalueset"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property fields in shares.

        Update the navigation property fields in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param list_item_version_id: key: id of listItemVersion.
        :type list_item_version_id: str
        :param body: New navigation property values.
        :type body: ~files.models.microsoftgraphfieldvalueset
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
        url = self.update_fields.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
            'listItemVersion-id': self._serialize.url("list_item_version_id", list_item_version_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphfieldvalueset')
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

    update_fields.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem/versions/{listItemVersion-id}/fields'}  # type: ignore

    def delete_fields(
        self,
        shared_drive_item_id,  # type: str
        item_activity_old_id,  # type: str
        list_item_version_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property fields for shares.

        Delete navigation property fields for shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param list_item_version_id: key: id of listItemVersion.
        :type list_item_version_id: str
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
        url = self.delete_fields.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
            'listItemVersion-id': self._serialize.url("list_item_version_id", list_item_version_id, 'str'),
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

    delete_fields.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem/versions/{listItemVersion-id}/fields'}  # type: ignore

    def restore_version(
        self,
        shared_drive_item_id,  # type: str
        item_activity_old_id,  # type: str
        list_item_version_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action restoreVersion.

        Invoke action restoreVersion.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param list_item_version_id: key: id of listItemVersion.
        :type list_item_version_id: str
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
        url = self.restore_version.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
            'listItemVersion-id': self._serialize.url("list_item_version_id", list_item_version_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    restore_version.metadata = {'url': '/shares/{sharedDriveItem-id}/list/activities/{itemActivityOLD-id}/listItem/versions/{listItemVersion-id}/microsoft.graph.restoreVersion'}  # type: ignore
