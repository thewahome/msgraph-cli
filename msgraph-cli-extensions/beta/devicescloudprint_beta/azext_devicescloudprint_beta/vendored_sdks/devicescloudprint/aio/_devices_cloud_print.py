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

from ._configuration import DevicesCloudPrintConfiguration
from .operations import PrintPrintOperations
from .operations import PrintOperations
from .operations import PrintPrintersOperations
from .operations import PrintPrintersTaskTriggersOperations
from .operations import PrintPrinterSharesOperations
from .operations import PrintPrinterSharesPrinterOperations
from .operations import PrintReportsOperations
from .operations import PrintServicesOperations
from .operations import PrintSharesOperations
from .operations import PrintSharesPrinterOperations
from .operations import PrintTaskDefinitionsOperations
from .operations import PrintTaskDefinitionsTasksOperations
from .. import models


class DevicesCloudPrint(object):
    """DevicesCloudPrint.

    :ivar print_print: PrintPrintOperations operations
    :vartype print_print: devices_cloud_print.aio.operations.PrintPrintOperations
    :ivar print: PrintOperations operations
    :vartype print: devices_cloud_print.aio.operations.PrintOperations
    :ivar print_printers: PrintPrintersOperations operations
    :vartype print_printers: devices_cloud_print.aio.operations.PrintPrintersOperations
    :ivar print_printers_task_triggers: PrintPrintersTaskTriggersOperations operations
    :vartype print_printers_task_triggers: devices_cloud_print.aio.operations.PrintPrintersTaskTriggersOperations
    :ivar print_printer_shares: PrintPrinterSharesOperations operations
    :vartype print_printer_shares: devices_cloud_print.aio.operations.PrintPrinterSharesOperations
    :ivar print_printer_shares_printer: PrintPrinterSharesPrinterOperations operations
    :vartype print_printer_shares_printer: devices_cloud_print.aio.operations.PrintPrinterSharesPrinterOperations
    :ivar print_reports: PrintReportsOperations operations
    :vartype print_reports: devices_cloud_print.aio.operations.PrintReportsOperations
    :ivar print_services: PrintServicesOperations operations
    :vartype print_services: devices_cloud_print.aio.operations.PrintServicesOperations
    :ivar print_shares: PrintSharesOperations operations
    :vartype print_shares: devices_cloud_print.aio.operations.PrintSharesOperations
    :ivar print_shares_printer: PrintSharesPrinterOperations operations
    :vartype print_shares_printer: devices_cloud_print.aio.operations.PrintSharesPrinterOperations
    :ivar print_task_definitions: PrintTaskDefinitionsOperations operations
    :vartype print_task_definitions: devices_cloud_print.aio.operations.PrintTaskDefinitionsOperations
    :ivar print_task_definitions_tasks: PrintTaskDefinitionsTasksOperations operations
    :vartype print_task_definitions_tasks: devices_cloud_print.aio.operations.PrintTaskDefinitionsTasksOperations
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
            base_url = 'https://graph.microsoft.com/beta'
        self._config = DevicesCloudPrintConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.print_print = PrintPrintOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print = PrintOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_printers = PrintPrintersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_printers_task_triggers = PrintPrintersTaskTriggersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_printer_shares = PrintPrinterSharesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_printer_shares_printer = PrintPrinterSharesPrinterOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_reports = PrintReportsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_services = PrintServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_shares = PrintSharesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_shares_printer = PrintSharesPrinterOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_task_definitions = PrintTaskDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.print_task_definitions_tasks = PrintTaskDefinitionsTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DevicesCloudPrint":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
