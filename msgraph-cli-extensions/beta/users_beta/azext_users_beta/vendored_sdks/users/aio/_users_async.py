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

from ._configuration_async import UsersConfiguration
from .operations_async import UserUserOperations
from .operations_async import UserOperations
from .operations_async import UserOutlookOperations
from .operations_async import UserOutlookTaskFolderOperations
from .operations_async import UserOutlookTaskFolderTaskOperations
from .operations_async import UserOutlookTaskGroupOperations
from .operations_async import UserOutlookTaskGroupTaskFolderOperations
from .operations_async import UserOutlookTaskGroupTaskFolderTaskOperations
from .operations_async import UserOutlookTaskOperations
from .operations_async import UserSettingOperations
from .operations_async import UserTodoOperations
from .operations_async import UserTodoListOperations
from .operations_async import UserTodoListTaskOperations
from .. import models


class Users(object):
    """Users.

    :ivar user_user: UserUserOperations operations
    :vartype user_user: users.aio.operations_async.UserUserOperations
    :ivar user: UserOperations operations
    :vartype user: users.aio.operations_async.UserOperations
    :ivar user_outlook: UserOutlookOperations operations
    :vartype user_outlook: users.aio.operations_async.UserOutlookOperations
    :ivar user_outlook_task_folder: UserOutlookTaskFolderOperations operations
    :vartype user_outlook_task_folder: users.aio.operations_async.UserOutlookTaskFolderOperations
    :ivar user_outlook_task_folder_task: UserOutlookTaskFolderTaskOperations operations
    :vartype user_outlook_task_folder_task: users.aio.operations_async.UserOutlookTaskFolderTaskOperations
    :ivar user_outlook_task_group: UserOutlookTaskGroupOperations operations
    :vartype user_outlook_task_group: users.aio.operations_async.UserOutlookTaskGroupOperations
    :ivar user_outlook_task_group_task_folder: UserOutlookTaskGroupTaskFolderOperations operations
    :vartype user_outlook_task_group_task_folder: users.aio.operations_async.UserOutlookTaskGroupTaskFolderOperations
    :ivar user_outlook_task_group_task_folder_task: UserOutlookTaskGroupTaskFolderTaskOperations operations
    :vartype user_outlook_task_group_task_folder_task: users.aio.operations_async.UserOutlookTaskGroupTaskFolderTaskOperations
    :ivar user_outlook_task: UserOutlookTaskOperations operations
    :vartype user_outlook_task: users.aio.operations_async.UserOutlookTaskOperations
    :ivar user_setting: UserSettingOperations operations
    :vartype user_setting: users.aio.operations_async.UserSettingOperations
    :ivar user_todo: UserTodoOperations operations
    :vartype user_todo: users.aio.operations_async.UserTodoOperations
    :ivar user_todo_list: UserTodoListOperations operations
    :vartype user_todo_list: users.aio.operations_async.UserTodoListOperations
    :ivar user_todo_list_task: UserTodoListTaskOperations operations
    :vartype user_todo_list_task: users.aio.operations_async.UserTodoListTaskOperations
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
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
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
            base_url = 'https://graph.microsoft.com/beta'
        self._config = UsersConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.user_user = UserUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook = UserOutlookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook_task_folder = UserOutlookTaskFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook_task_folder_task = UserOutlookTaskFolderTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook_task_group = UserOutlookTaskGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook_task_group_task_folder = UserOutlookTaskGroupTaskFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook_task_group_task_folder_task = UserOutlookTaskGroupTaskFolderTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook_task = UserOutlookTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_setting = UserSettingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo = UserTodoOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list = UserTodoListOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list_task = UserTodoListTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Users":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
