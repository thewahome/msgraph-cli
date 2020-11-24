# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import UsersConfiguration
from .operations import UserUserOperations
from .operations import UserOperations
from .operations import UserOutlookOperations
from .operations import UserSettingOperations
from .operations import UserTodoOperations
from .operations import UserTodoListOperations
from .operations import UserTodoListTaskOperations
from . import models


class Users(object):
    """Users.

    :ivar user_user: UserUserOperations operations
    :vartype user_user: users.operations.UserUserOperations
    :ivar user: UserOperations operations
    :vartype user: users.operations.UserOperations
    :ivar user_outlook: UserOutlookOperations operations
    :vartype user_outlook: users.operations.UserOutlookOperations
    :ivar user_setting: UserSettingOperations operations
    :vartype user_setting: users.operations.UserSettingOperations
    :ivar user_todo: UserTodoOperations operations
    :vartype user_todo: users.operations.UserTodoOperations
    :ivar user_todo_list: UserTodoListOperations operations
    :vartype user_todo_list: users.operations.UserTodoListOperations
    :ivar user_todo_list_task: UserTodoListTaskOperations operations
    :vartype user_todo_list_task: users.operations.UserTodoListTaskOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
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
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = UsersConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.user_user = UserUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook = UserOutlookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_setting = UserSettingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo = UserTodoOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list = UserTodoListOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list_task = UserTodoListTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Users
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
