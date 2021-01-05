# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DriveListItemActivityListItemOperations:
    """DriveListItemActivityListItemOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create_link(
        self,
        drive_id: str,
        list_item_id: str,
        item_activity_old_id: str,
        type: Optional[str] = None,
        scope: Optional[str] = None,
        expiration_date_time: Optional[datetime.datetime] = None,
        password: Optional[str] = None,
        recipients: Optional[List["models.MicrosoftGraphDriveRecipient"]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphPermission":
        """Invoke action createLink.

        Invoke action createLink.

        :param drive_id: key: id of drive.
        :type drive_id: str
        :param list_item_id: key: id of listItem.
        :type list_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param type:
        :type type: str
        :param scope:
        :type scope: str
        :param expiration_date_time:
        :type expiration_date_time: ~datetime.datetime
        :param password:
        :type password: str
        :param recipients:
        :type recipients: list[~files.models.MicrosoftGraphDriveRecipient]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPermission, or the result of cls(response)
        :rtype: ~files.models.MicrosoftGraphPermission
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPermission"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths15G389UDrivesDriveIdListItemsListitemIdActivitiesItemactivityoldIdListitemMicrosoftGraphCreatelinkPostRequestbodyContentApplicationJsonSchema(type=type, scope=scope, expiration_date_time=expiration_date_time, password=password, recipients=recipients)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_link.metadata['url']  # type: ignore
        path_format_arguments = {
            'drive-id': self._serialize.url("drive_id", drive_id, 'str'),
            'listItem-id': self._serialize.url("list_item_id", list_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
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
        body_content = self._serialize.body(_body, 'Paths15G389UDrivesDriveIdListItemsListitemIdActivitiesItemactivityoldIdListitemMicrosoftGraphCreatelinkPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPermission', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_link.metadata = {'url': '/drives/{drive-id}/list/items/{listItem-id}/activities/{itemActivityOLD-id}/listItem/microsoft.graph.createLink'}  # type: ignore

    async def get_activity_by_interval(
        self,
        drive_id: str,
        list_item_id: str,
        item_activity_old_id: str,
        start_date_time: str,
        end_date_time: str,
        interval: str,
        **kwargs
    ) -> List["models.MicrosoftGraphItemActivityStat"]:
        """Invoke function getActivitiesByInterval.

        Invoke function getActivitiesByInterval.

        :param drive_id: key: id of drive.
        :type drive_id: str
        :param list_item_id: key: id of listItem.
        :type list_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param start_date_time:
        :type start_date_time: str
        :param end_date_time:
        :type end_date_time: str
        :param interval:
        :type interval: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphItemActivityStat, or the result of cls(response)
        :rtype: list[~files.models.MicrosoftGraphItemActivityStat]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphItemActivityStat"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_activity_by_interval.metadata['url']  # type: ignore
        path_format_arguments = {
            'drive-id': self._serialize.url("drive_id", drive_id, 'str'),
            'listItem-id': self._serialize.url("list_item_id", list_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
            'startDateTime': self._serialize.url("start_date_time", start_date_time, 'str'),
            'endDateTime': self._serialize.url("end_date_time", end_date_time, 'str'),
            'interval': self._serialize.url("interval", interval, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphItemActivityStat]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_activity_by_interval.metadata = {'url': '/drives/{drive-id}/list/items/{listItem-id}/activities/{itemActivityOLD-id}/listItem/microsoft.graph.getActivitiesByInterval(startDateTime=\'{startDateTime}\',endDateTime=\'{endDateTime}\',interval=\'{interval}\')'}  # type: ignore
