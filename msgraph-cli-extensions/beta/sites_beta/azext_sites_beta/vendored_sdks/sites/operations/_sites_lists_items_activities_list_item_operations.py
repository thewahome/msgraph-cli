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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SitesListsItemsActivitiesListItemOperations(object):
    """SitesListsItemsActivitiesListItemOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~sites.models
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

    def create_link(
        self,
        site_id,  # type: str
        list_id,  # type: str
        list_item_id,  # type: str
        item_activity_old_id,  # type: str
        body,  # type: "models.PathsV1SzefSitesSiteIdListsListIdItemsListitemIdActivitiesItemactivityoldIdListitemMicrosoftGraphCreatelinkPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPermission"
        """Invoke action createLink.

        Invoke action createLink.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
        :param list_item_id: key: id of listItem.
        :type list_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param body: Action parameters.
        :type body: ~sites.models.PathsV1SzefSitesSiteIdListsListIdItemsListitemIdActivitiesItemactivityoldIdListitemMicrosoftGraphCreatelinkPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPermission, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphPermission
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPermission"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_link.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsV1SzefSitesSiteIdListsListIdItemsListitemIdActivitiesItemactivityoldIdListitemMicrosoftGraphCreatelinkPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPermission', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_link.metadata = {'url': '/sites/{site-id}/lists/{list-id}/items/{listItem-id}/activities/{itemActivityOLD-id}/listItem/microsoft.graph.createLink'}  # type: ignore

    def get_activities_by_interval(
        self,
        site_id,  # type: str
        list_id,  # type: str
        list_item_id,  # type: str
        item_activity_old_id,  # type: str
        start_date_time,  # type: str
        end_date_time,  # type: str
        interval,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphItemActivityStat"]
        """Invoke function getActivitiesByInterval.

        Invoke function getActivitiesByInterval.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
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
        :rtype: list[~sites.models.MicrosoftGraphItemActivityStat]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphItemActivityStat"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_activities_by_interval.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphItemActivityStat]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_activities_by_interval.metadata = {'url': '/sites/{site-id}/lists/{list-id}/items/{listItem-id}/activities/{itemActivityOLD-id}/listItem/microsoft.graph.getActivitiesByInterval(startDateTime=\'{startDateTime}\',endDateTime=\'{endDateTime}\',interval=\'{interval}\')'}  # type: ignore
