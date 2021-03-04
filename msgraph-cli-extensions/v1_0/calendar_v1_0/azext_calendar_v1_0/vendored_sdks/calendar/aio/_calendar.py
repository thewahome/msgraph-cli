# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import CalendarConfiguration
from .operations import GroupOperations
from .operations import GroupCalendarOperations
from .operations import GroupCalendarCalendarViewOperations
from .operations import GroupCalendarEventOperations
from .operations import GroupCalendarViewOperations
from .operations import GroupCalendarViewCalendarOperations
from .operations import GroupEventOperations
from .operations import GroupEventCalendarOperations
from .operations import PlacePlaceOperations
from .operations import UserOperations
from .operations import UserCalendarOperations
from .operations import UserCalendarCalendarViewOperations
from .operations import UserCalendarEventOperations
from .operations import UserCalendarGroupOperations
from .operations import UserCalendarGroupCalendarOperations
from .operations import UserCalendarGroupCalendarCalendarViewOperations
from .operations import UserCalendarGroupCalendarEventOperations
from .operations import UserCalendarOperations
from .operations import UserCalendarCalendarViewOperations
from .operations import UserCalendarEventOperations
from .operations import UserCalendarViewOperations
from .operations import UserCalendarViewCalendarOperations
from .operations import UserEventOperations
from .operations import UserEventCalendarOperations
from .. import models


class Calendar(object):
    """Calendar.

    :ivar group: GroupOperations operations
    :vartype group: calendar.aio.operations.GroupOperations
    :ivar group_calendar: GroupCalendarOperations operations
    :vartype group_calendar: calendar.aio.operations.GroupCalendarOperations
    :ivar group_calendar_calendar_view: GroupCalendarCalendarViewOperations operations
    :vartype group_calendar_calendar_view: calendar.aio.operations.GroupCalendarCalendarViewOperations
    :ivar group_calendar_event: GroupCalendarEventOperations operations
    :vartype group_calendar_event: calendar.aio.operations.GroupCalendarEventOperations
    :ivar group_calendar_view: GroupCalendarViewOperations operations
    :vartype group_calendar_view: calendar.aio.operations.GroupCalendarViewOperations
    :ivar group_calendar_view_calendar: GroupCalendarViewCalendarOperations operations
    :vartype group_calendar_view_calendar: calendar.aio.operations.GroupCalendarViewCalendarOperations
    :ivar group_event: GroupEventOperations operations
    :vartype group_event: calendar.aio.operations.GroupEventOperations
    :ivar group_event_calendar: GroupEventCalendarOperations operations
    :vartype group_event_calendar: calendar.aio.operations.GroupEventCalendarOperations
    :ivar place_place: PlacePlaceOperations operations
    :vartype place_place: calendar.aio.operations.PlacePlaceOperations
    :ivar user: UserOperations operations
    :vartype user: calendar.aio.operations.UserOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: calendar.aio.operations.UserCalendarOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: calendar.aio.operations.UserCalendarCalendarViewOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: calendar.aio.operations.UserCalendarEventOperations
    :ivar user_calendar_group: UserCalendarGroupOperations operations
    :vartype user_calendar_group: calendar.aio.operations.UserCalendarGroupOperations
    :ivar user_calendar_group_calendar: UserCalendarGroupCalendarOperations operations
    :vartype user_calendar_group_calendar: calendar.aio.operations.UserCalendarGroupCalendarOperations
    :ivar user_calendar_group_calendar_calendar_view: UserCalendarGroupCalendarCalendarViewOperations operations
    :vartype user_calendar_group_calendar_calendar_view: calendar.aio.operations.UserCalendarGroupCalendarCalendarViewOperations
    :ivar user_calendar_group_calendar_event: UserCalendarGroupCalendarEventOperations operations
    :vartype user_calendar_group_calendar_event: calendar.aio.operations.UserCalendarGroupCalendarEventOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: calendar.aio.operations.UserCalendarOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: calendar.aio.operations.UserCalendarCalendarViewOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: calendar.aio.operations.UserCalendarEventOperations
    :ivar user_calendar_view: UserCalendarViewOperations operations
    :vartype user_calendar_view: calendar.aio.operations.UserCalendarViewOperations
    :ivar user_calendar_view_calendar: UserCalendarViewCalendarOperations operations
    :vartype user_calendar_view_calendar: calendar.aio.operations.UserCalendarViewCalendarOperations
    :ivar user_event: UserEventOperations operations
    :vartype user_event: calendar.aio.operations.UserEventOperations
    :ivar user_event_calendar: UserEventCalendarOperations operations
    :vartype user_event_calendar: calendar.aio.operations.UserEventCalendarOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = CalendarConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar = GroupCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_calendar_view = GroupCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_event = GroupCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_view = GroupCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_view_calendar = GroupCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_event = GroupEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_event_calendar = GroupEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.place_place = PlacePlaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group = UserCalendarGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar = UserCalendarGroupCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view = UserCalendarGroupCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event = UserCalendarGroupCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view = UserCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar = UserCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event = UserEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar = UserEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Calendar":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
