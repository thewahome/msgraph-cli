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

from ._configuration import UsersFunctionsConfiguration
from .operations import usersactivitiesOperations
from .operations import userscalendarcalendarviewcalendarOperations
from .operations import userscalendarcalendarviewinstancesOperations
from .operations import userscalendarcalendarviewOperations
from .operations import userscalendareventscalendarOperations
from .operations import userscalendareventsinstancesOperations
from .operations import userscalendareventsOperations
from .operations import userscalendarOperations
from .operations import userscalendargroupscalendarscalendarviewcalendarOperations
from .operations import userscalendargroupscalendarscalendarviewinstancesOperations
from .operations import userscalendargroupscalendarscalendarviewOperations
from .operations import userscalendargroupscalendarseventscalendarOperations
from .operations import userscalendargroupscalendarseventsinstancesOperations
from .operations import userscalendargroupscalendarseventsOperations
from .operations import userscalendargroupscalendarsOperations
from .operations import userscalendarscalendarviewcalendarOperations
from .operations import userscalendarscalendarviewinstancesOperations
from .operations import userscalendarscalendarviewOperations
from .operations import userscalendarseventscalendarOperations
from .operations import userscalendarseventsinstancesOperations
from .operations import userscalendarseventsOperations
from .operations import userscalendarsOperations
from .operations import userscalendarviewcalendarcalendarviewOperations
from .operations import userscalendarviewcalendareventsOperations
from .operations import userscalendarviewcalendarOperations
from .operations import userscalendarviewinstancesOperations
from .operations import userscalendarviewOperations
from .operations import userscontactfolderschildfoldersOperations
from .operations import userscontactfolderscontactsOperations
from .operations import userscontactfoldersOperations
from .operations import userscontactsOperations
from .operations import userseventscalendarcalendarviewOperations
from .operations import userseventscalendareventsOperations
from .operations import userseventscalendarOperations
from .operations import userseventsinstancesOperations
from .operations import userseventsOperations
from .operations import usersmailfolderschildfoldersOperations
from .operations import usersmailfoldersmessagesOperations
from .operations import usersmailfoldersOperations
from .operations import usersmanagedappregistrationsOperations
from .operations import usersmessagesOperations
from .operations import usersOperations
from .operations import usersonenotenotebookssectiongroupssectionspagesOperations
from .operations import usersonenotenotebookssectionspagesOperations
from .operations import usersonenotenotebooksOperations
from .operations import usersonenotepagesOperations
from .operations import usersonenotepagesparentnotebooksectiongroupssectionspagesOperations
from .operations import usersonenotepagesparentnotebooksectionspagesOperations
from .operations import usersonenotepagesparentsectionpagesOperations
from .operations import usersonenotesectiongroupsparentnotebooksectionspagesOperations
from .operations import usersonenotesectiongroupssectionspagesOperations
from .operations import usersonenotesectionspagesOperations
from .operations import usersoutlookOperations
from . import models


class UsersFunctions(object):
    """UsersFunctions.

    :ivar usersactivities: usersactivitiesOperations operations
    :vartype usersactivities: users_functions.operations.usersactivitiesOperations
    :ivar userscalendarcalendarviewcalendar: userscalendarcalendarviewcalendarOperations operations
    :vartype userscalendarcalendarviewcalendar: users_functions.operations.userscalendarcalendarviewcalendarOperations
    :ivar userscalendarcalendarviewinstances: userscalendarcalendarviewinstancesOperations operations
    :vartype userscalendarcalendarviewinstances: users_functions.operations.userscalendarcalendarviewinstancesOperations
    :ivar userscalendarcalendarview: userscalendarcalendarviewOperations operations
    :vartype userscalendarcalendarview: users_functions.operations.userscalendarcalendarviewOperations
    :ivar userscalendareventscalendar: userscalendareventscalendarOperations operations
    :vartype userscalendareventscalendar: users_functions.operations.userscalendareventscalendarOperations
    :ivar userscalendareventsinstances: userscalendareventsinstancesOperations operations
    :vartype userscalendareventsinstances: users_functions.operations.userscalendareventsinstancesOperations
    :ivar userscalendarevents: userscalendareventsOperations operations
    :vartype userscalendarevents: users_functions.operations.userscalendareventsOperations
    :ivar userscalendar: userscalendarOperations operations
    :vartype userscalendar: users_functions.operations.userscalendarOperations
    :ivar userscalendargroupscalendarscalendarviewcalendar: userscalendargroupscalendarscalendarviewcalendarOperations operations
    :vartype userscalendargroupscalendarscalendarviewcalendar: users_functions.operations.userscalendargroupscalendarscalendarviewcalendarOperations
    :ivar userscalendargroupscalendarscalendarviewinstances: userscalendargroupscalendarscalendarviewinstancesOperations operations
    :vartype userscalendargroupscalendarscalendarviewinstances: users_functions.operations.userscalendargroupscalendarscalendarviewinstancesOperations
    :ivar userscalendargroupscalendarscalendarview: userscalendargroupscalendarscalendarviewOperations operations
    :vartype userscalendargroupscalendarscalendarview: users_functions.operations.userscalendargroupscalendarscalendarviewOperations
    :ivar userscalendargroupscalendarseventscalendar: userscalendargroupscalendarseventscalendarOperations operations
    :vartype userscalendargroupscalendarseventscalendar: users_functions.operations.userscalendargroupscalendarseventscalendarOperations
    :ivar userscalendargroupscalendarseventsinstances: userscalendargroupscalendarseventsinstancesOperations operations
    :vartype userscalendargroupscalendarseventsinstances: users_functions.operations.userscalendargroupscalendarseventsinstancesOperations
    :ivar userscalendargroupscalendarsevents: userscalendargroupscalendarseventsOperations operations
    :vartype userscalendargroupscalendarsevents: users_functions.operations.userscalendargroupscalendarseventsOperations
    :ivar userscalendargroupscalendars: userscalendargroupscalendarsOperations operations
    :vartype userscalendargroupscalendars: users_functions.operations.userscalendargroupscalendarsOperations
    :ivar userscalendarscalendarviewcalendar: userscalendarscalendarviewcalendarOperations operations
    :vartype userscalendarscalendarviewcalendar: users_functions.operations.userscalendarscalendarviewcalendarOperations
    :ivar userscalendarscalendarviewinstances: userscalendarscalendarviewinstancesOperations operations
    :vartype userscalendarscalendarviewinstances: users_functions.operations.userscalendarscalendarviewinstancesOperations
    :ivar userscalendarscalendarview: userscalendarscalendarviewOperations operations
    :vartype userscalendarscalendarview: users_functions.operations.userscalendarscalendarviewOperations
    :ivar userscalendarseventscalendar: userscalendarseventscalendarOperations operations
    :vartype userscalendarseventscalendar: users_functions.operations.userscalendarseventscalendarOperations
    :ivar userscalendarseventsinstances: userscalendarseventsinstancesOperations operations
    :vartype userscalendarseventsinstances: users_functions.operations.userscalendarseventsinstancesOperations
    :ivar userscalendarsevents: userscalendarseventsOperations operations
    :vartype userscalendarsevents: users_functions.operations.userscalendarseventsOperations
    :ivar userscalendars: userscalendarsOperations operations
    :vartype userscalendars: users_functions.operations.userscalendarsOperations
    :ivar userscalendarviewcalendarcalendarview: userscalendarviewcalendarcalendarviewOperations operations
    :vartype userscalendarviewcalendarcalendarview: users_functions.operations.userscalendarviewcalendarcalendarviewOperations
    :ivar userscalendarviewcalendarevents: userscalendarviewcalendareventsOperations operations
    :vartype userscalendarviewcalendarevents: users_functions.operations.userscalendarviewcalendareventsOperations
    :ivar userscalendarviewcalendar: userscalendarviewcalendarOperations operations
    :vartype userscalendarviewcalendar: users_functions.operations.userscalendarviewcalendarOperations
    :ivar userscalendarviewinstances: userscalendarviewinstancesOperations operations
    :vartype userscalendarviewinstances: users_functions.operations.userscalendarviewinstancesOperations
    :ivar userscalendarview: userscalendarviewOperations operations
    :vartype userscalendarview: users_functions.operations.userscalendarviewOperations
    :ivar userscontactfolderschildfolders: userscontactfolderschildfoldersOperations operations
    :vartype userscontactfolderschildfolders: users_functions.operations.userscontactfolderschildfoldersOperations
    :ivar userscontactfolderscontacts: userscontactfolderscontactsOperations operations
    :vartype userscontactfolderscontacts: users_functions.operations.userscontactfolderscontactsOperations
    :ivar userscontactfolders: userscontactfoldersOperations operations
    :vartype userscontactfolders: users_functions.operations.userscontactfoldersOperations
    :ivar userscontacts: userscontactsOperations operations
    :vartype userscontacts: users_functions.operations.userscontactsOperations
    :ivar userseventscalendarcalendarview: userseventscalendarcalendarviewOperations operations
    :vartype userseventscalendarcalendarview: users_functions.operations.userseventscalendarcalendarviewOperations
    :ivar userseventscalendarevents: userseventscalendareventsOperations operations
    :vartype userseventscalendarevents: users_functions.operations.userseventscalendareventsOperations
    :ivar userseventscalendar: userseventscalendarOperations operations
    :vartype userseventscalendar: users_functions.operations.userseventscalendarOperations
    :ivar userseventsinstances: userseventsinstancesOperations operations
    :vartype userseventsinstances: users_functions.operations.userseventsinstancesOperations
    :ivar usersevents: userseventsOperations operations
    :vartype usersevents: users_functions.operations.userseventsOperations
    :ivar usersmailfolderschildfolders: usersmailfolderschildfoldersOperations operations
    :vartype usersmailfolderschildfolders: users_functions.operations.usersmailfolderschildfoldersOperations
    :ivar usersmailfoldersmessages: usersmailfoldersmessagesOperations operations
    :vartype usersmailfoldersmessages: users_functions.operations.usersmailfoldersmessagesOperations
    :ivar usersmailfolders: usersmailfoldersOperations operations
    :vartype usersmailfolders: users_functions.operations.usersmailfoldersOperations
    :ivar usersmanagedappregistrations: usersmanagedappregistrationsOperations operations
    :vartype usersmanagedappregistrations: users_functions.operations.usersmanagedappregistrationsOperations
    :ivar usersmessages: usersmessagesOperations operations
    :vartype usersmessages: users_functions.operations.usersmessagesOperations
    :ivar users: usersOperations operations
    :vartype users: users_functions.operations.usersOperations
    :ivar usersonenotenotebookssectiongroupssectionspages: usersonenotenotebookssectiongroupssectionspagesOperations operations
    :vartype usersonenotenotebookssectiongroupssectionspages: users_functions.operations.usersonenotenotebookssectiongroupssectionspagesOperations
    :ivar usersonenotenotebookssectionspages: usersonenotenotebookssectionspagesOperations operations
    :vartype usersonenotenotebookssectionspages: users_functions.operations.usersonenotenotebookssectionspagesOperations
    :ivar usersonenotenotebooks: usersonenotenotebooksOperations operations
    :vartype usersonenotenotebooks: users_functions.operations.usersonenotenotebooksOperations
    :ivar usersonenotepages: usersonenotepagesOperations operations
    :vartype usersonenotepages: users_functions.operations.usersonenotepagesOperations
    :ivar usersonenotepagesparentnotebooksectiongroupssectionspages: usersonenotepagesparentnotebooksectiongroupssectionspagesOperations operations
    :vartype usersonenotepagesparentnotebooksectiongroupssectionspages: users_functions.operations.usersonenotepagesparentnotebooksectiongroupssectionspagesOperations
    :ivar usersonenotepagesparentnotebooksectionspages: usersonenotepagesparentnotebooksectionspagesOperations operations
    :vartype usersonenotepagesparentnotebooksectionspages: users_functions.operations.usersonenotepagesparentnotebooksectionspagesOperations
    :ivar usersonenotepagesparentsectionpages: usersonenotepagesparentsectionpagesOperations operations
    :vartype usersonenotepagesparentsectionpages: users_functions.operations.usersonenotepagesparentsectionpagesOperations
    :ivar usersonenotesectiongroupsparentnotebooksectionspages: usersonenotesectiongroupsparentnotebooksectionspagesOperations operations
    :vartype usersonenotesectiongroupsparentnotebooksectionspages: users_functions.operations.usersonenotesectiongroupsparentnotebooksectionspagesOperations
    :ivar usersonenotesectiongroupssectionspages: usersonenotesectiongroupssectionspagesOperations operations
    :vartype usersonenotesectiongroupssectionspages: users_functions.operations.usersonenotesectiongroupssectionspagesOperations
    :ivar usersonenotesectionspages: usersonenotesectionspagesOperations operations
    :vartype usersonenotesectionspages: users_functions.operations.usersonenotesectionspagesOperations
    :ivar usersoutlook: usersoutlookOperations operations
    :vartype usersoutlook: users_functions.operations.usersoutlookOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = UsersFunctionsConfiguration(credential, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.usersactivities = usersactivitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarcalendarviewcalendar = userscalendarcalendarviewcalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarcalendarviewinstances = userscalendarcalendarviewinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarcalendarview = userscalendarcalendarviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendareventscalendar = userscalendareventscalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendareventsinstances = userscalendareventsinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarevents = userscalendareventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendar = userscalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendarscalendarviewcalendar = userscalendargroupscalendarscalendarviewcalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendarscalendarviewinstances = userscalendargroupscalendarscalendarviewinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendarscalendarview = userscalendargroupscalendarscalendarviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendarseventscalendar = userscalendargroupscalendarseventscalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendarseventsinstances = userscalendargroupscalendarseventsinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendarsevents = userscalendargroupscalendarseventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendargroupscalendars = userscalendargroupscalendarsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarscalendarviewcalendar = userscalendarscalendarviewcalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarscalendarviewinstances = userscalendarscalendarviewinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarscalendarview = userscalendarscalendarviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarseventscalendar = userscalendarseventscalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarseventsinstances = userscalendarseventsinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarsevents = userscalendarseventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendars = userscalendarsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarviewcalendarcalendarview = userscalendarviewcalendarcalendarviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarviewcalendarevents = userscalendarviewcalendareventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarviewcalendar = userscalendarviewcalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarviewinstances = userscalendarviewinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscalendarview = userscalendarviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscontactfolderschildfolders = userscontactfolderschildfoldersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscontactfolderscontacts = userscontactfolderscontactsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscontactfolders = userscontactfoldersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userscontacts = userscontactsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userseventscalendarcalendarview = userseventscalendarcalendarviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userseventscalendarevents = userseventscalendareventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userseventscalendar = userseventscalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.userseventsinstances = userseventsinstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersevents = userseventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersmailfolderschildfolders = usersmailfolderschildfoldersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersmailfoldersmessages = usersmailfoldersmessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersmailfolders = usersmailfoldersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersmanagedappregistrations = usersmanagedappregistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersmessages = usersmessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = usersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotenotebookssectiongroupssectionspages = usersonenotenotebookssectiongroupssectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotenotebookssectionspages = usersonenotenotebookssectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotenotebooks = usersonenotenotebooksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotepages = usersonenotepagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotepagesparentnotebooksectiongroupssectionspages = usersonenotepagesparentnotebooksectiongroupssectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotepagesparentnotebooksectionspages = usersonenotepagesparentnotebooksectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotepagesparentsectionpages = usersonenotepagesparentsectionpagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotesectiongroupsparentnotebooksectionspages = usersonenotesectiongroupsparentnotebooksectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotesectiongroupssectionspages = usersonenotesectiongroupssectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersonenotesectionspages = usersonenotesectionspagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usersoutlook = usersoutlookOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> UsersFunctions
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
