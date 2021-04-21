# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class userscalendargroupscalendarscalendarviewOperations:
    """userscalendargroupscalendarscalendarviewOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_actions.models
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

    async def accept(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        event_id: str,
        body: "models.paths1tzbvorusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphacceptpostrequestbodycontentapplicationjsonschema",
        **kwargs
    ) -> None:
        """Invoke action accept.

        Invoke action accept.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths1tzbvorusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphacceptpostrequestbodycontentapplicationjsonschema
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
        url = self.accept.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths1tzbvorusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphacceptpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    accept.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}/calendarView/{event-id}/microsoft.graph.accept'}  # type: ignore

    async def decline(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        event_id: str,
        body: "models.paths1o1ne8tusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphdeclinepostrequestbodycontentapplicationjsonschema",
        **kwargs
    ) -> None:
        """Invoke action decline.

        Invoke action decline.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.paths1o1ne8tusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphdeclinepostrequestbodycontentapplicationjsonschema
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
        url = self.decline.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'paths1o1ne8tusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphdeclinepostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    decline.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}/calendarView/{event-id}/microsoft.graph.decline'}  # type: ignore

    async def dismiss_reminder(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        event_id: str,
        **kwargs
    ) -> None:
        """Invoke action dismissReminder.

        Invoke action dismissReminder.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param event_id: key: id of event.
        :type event_id: str
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
        url = self.dismiss_reminder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    dismiss_reminder.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}/calendarView/{event-id}/microsoft.graph.dismissReminder'}  # type: ignore

    async def snooze_reminder(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        event_id: str,
        body: "models.pathstvg0qfusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphsnoozereminderpostrequestbodycontentapplicationjsonschema",
        **kwargs
    ) -> None:
        """Invoke action snoozeReminder.

        Invoke action snoozeReminder.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.pathstvg0qfusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphsnoozereminderpostrequestbodycontentapplicationjsonschema
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
        url = self.snooze_reminder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'pathstvg0qfusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphsnoozereminderpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    snooze_reminder.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}/calendarView/{event-id}/microsoft.graph.snoozeReminder'}  # type: ignore

    async def tentatively_accept(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        event_id: str,
        body: "models.pathsrzk26rusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphtentativelyacceptpostrequestbodycontentapplicationjsonschema",
        **kwargs
    ) -> None:
        """Invoke action tentativelyAccept.

        Invoke action tentativelyAccept.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param body: Action parameters.
        :type body: ~users_actions.models.pathsrzk26rusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphtentativelyacceptpostrequestbodycontentapplicationjsonschema
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
        url = self.tentatively_accept.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'pathsrzk26rusersuseridcalendargroupscalendargroupidcalendarscalendaridcalendarvieweventidmicrosoftgraphtentativelyacceptpostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    tentatively_accept.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}/calendarView/{event-id}/microsoft.graph.tentativelyAccept'}  # type: ignore
