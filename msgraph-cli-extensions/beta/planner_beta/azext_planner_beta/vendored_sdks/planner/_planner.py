# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import PlannerConfiguration
from .operations import groupsOperations
from .operations import groupsplannerOperations
from .operations import groupsplannerplansOperations
from .operations import groupsplannerplansbucketsOperations
from .operations import groupsplannerplansbucketstasksOperations
from .operations import groupsplannerplanstasksOperations
from .operations import plannerplannerOperations
from .operations import plannerOperations
from .operations import plannerbucketsOperations
from .operations import plannerbucketstasksOperations
from .operations import plannerplansOperations
from .operations import plannerplansbucketsOperations
from .operations import plannerplansbucketstasksOperations
from .operations import plannerplanstasksOperations
from .operations import plannertasksOperations
from .operations import usersOperations
from .operations import usersplannerOperations
from .operations import usersplannerplansOperations
from .operations import usersplannerplansbucketsOperations
from .operations import usersplannerplansbucketstasksOperations
from .operations import usersplannerplanstasksOperations
from .operations import usersplannertasksOperations
from . import models


class Planner(object):
    """Planner.

    :ivar groups: groupsOperations operations
    :vartype groups: planner.operations.groupsOperations
    :ivar groupsplanner: groupsplannerOperations operations
    :vartype groupsplanner: planner.operations.groupsplannerOperations
    :ivar groupsplannerplans: groupsplannerplansOperations operations
    :vartype groupsplannerplans: planner.operations.groupsplannerplansOperations
    :ivar groupsplannerplansbuckets: groupsplannerplansbucketsOperations operations
    :vartype groupsplannerplansbuckets: planner.operations.groupsplannerplansbucketsOperations
    :ivar groupsplannerplansbucketstasks: groupsplannerplansbucketstasksOperations operations
    :vartype groupsplannerplansbucketstasks: planner.operations.groupsplannerplansbucketstasksOperations
    :ivar groupsplannerplanstasks: groupsplannerplanstasksOperations operations
    :vartype groupsplannerplanstasks: planner.operations.groupsplannerplanstasksOperations
    :ivar plannerplanner: plannerplannerOperations operations
    :vartype plannerplanner: planner.operations.plannerplannerOperations
    :ivar planner: plannerOperations operations
    :vartype planner: planner.operations.plannerOperations
    :ivar plannerbuckets: plannerbucketsOperations operations
    :vartype plannerbuckets: planner.operations.plannerbucketsOperations
    :ivar plannerbucketstasks: plannerbucketstasksOperations operations
    :vartype plannerbucketstasks: planner.operations.plannerbucketstasksOperations
    :ivar plannerplans: plannerplansOperations operations
    :vartype plannerplans: planner.operations.plannerplansOperations
    :ivar plannerplansbuckets: plannerplansbucketsOperations operations
    :vartype plannerplansbuckets: planner.operations.plannerplansbucketsOperations
    :ivar plannerplansbucketstasks: plannerplansbucketstasksOperations operations
    :vartype plannerplansbucketstasks: planner.operations.plannerplansbucketstasksOperations
    :ivar plannerplanstasks: plannerplanstasksOperations operations
    :vartype plannerplanstasks: planner.operations.plannerplanstasksOperations
    :ivar plannertasks: plannertasksOperations operations
    :vartype plannertasks: planner.operations.plannertasksOperations
    :ivar users: usersOperations operations
    :vartype users: planner.operations.usersOperations
    :ivar usersplanner: usersplannerOperations operations
    :vartype usersplanner: planner.operations.usersplannerOperations
    :ivar usersplannerplans: usersplannerplansOperations operations
    :vartype usersplannerplans: planner.operations.usersplannerplansOperations
    :ivar usersplannerplansbuckets: usersplannerplansbucketsOperations operations
    :vartype usersplannerplansbuckets: planner.operations.usersplannerplansbucketsOperations
    :ivar usersplannerplansbucketstasks: usersplannerplansbucketstasksOperations operations
    :vartype usersplannerplansbucketstasks: planner.operations.usersplannerplansbucketstasksOperations
    :ivar usersplannerplanstasks: usersplannerplanstasksOperations operations
    :vartype usersplannerplanstasks: planner.operations.usersplannerplanstasksOperations
    :ivar usersplannertasks: usersplannertasksOperations operations
    :vartype usersplannertasks: planner.operations.usersplannertasksOperations
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
            base_url = 'https://graph.microsoft.com/beta'
        self._config = PlannerConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.groups = groupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groupsplanner = groupsplannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groupsplannerplans = groupsplannerplansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groupsplannerplansbuckets = groupsplannerplansbucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groupsplannerplansbucketstasks = groupsplannerplansbucketstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groupsplannerplanstasks = groupsplannerplanstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerplanner = plannerplannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner = plannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerbuckets = plannerbucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerbucketstasks = plannerbucketstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerplans = plannerplansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerplansbuckets = plannerplansbucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerplansbucketstasks = plannerplansbucketstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannerplanstasks = plannerplanstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.plannertasks = plannertasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = usersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersplanner = usersplannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersplannerplans = usersplannerplansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersplannerplansbuckets = usersplannerplansbucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersplannerplansbucketstasks = usersplannerplansbucketstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersplannerplanstasks = usersplannerplanstasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersplannertasks = usersplannertasksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Planner
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
