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
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class financialscompaniessalesorderssalesorderlinesOperations(object):
    """financialscompaniessalesorderssalesorderlinesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~financials.models
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

    def get_account(
        self,
        company_id,  # type: str
        sales_order_id,  # type: str
        sales_order_line_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum286"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphaccount"
        """Get account from financials.

        Get account from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum286]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphaccount, or the result of cls(response)
        :rtype: ~financials.models.microsoftgraphaccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphaccount"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
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

        deserialized = self._deserialize('microsoftgraphaccount', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_account.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/account'}  # type: ignore

    def update_account(
        self,
        company_id,  # type: str
        sales_order_id,  # type: str
        sales_order_line_id,  # type: str
        body,  # type: "models.microsoftgraphaccount"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property account in financials.

        Update the navigation property account in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param body: New navigation property values.
        :type body: ~financials.models.microsoftgraphaccount
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
        url = self.update_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphaccount')
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

    update_account.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/account'}  # type: ignore

    def delete_account(
        self,
        company_id,  # type: str
        sales_order_id,  # type: str
        sales_order_line_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property account for financials.

        Delete navigation property account for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
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
        url = self.delete_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
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

    delete_account.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/account'}  # type: ignore

    def get_item(
        self,
        company_id,  # type: str
        sales_order_id,  # type: str
        sales_order_line_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum287"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum288"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.microsoftgraphitem"
        """Get item from financials.

        Get item from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum287]
        :param expand: Expand related entities.
        :type expand: list[str or ~financials.models.Enum288]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphitem, or the result of cls(response)
        :rtype: ~financials.models.microsoftgraphitem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphitem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
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

        deserialized = self._deserialize('microsoftgraphitem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_item.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item'}  # type: ignore

    def update_item(
        self,
        company_id,  # type: str
        sales_order_id,  # type: str
        sales_order_line_id,  # type: str
        body,  # type: "models.microsoftgraphitem"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property item in financials.

        Update the navigation property item in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param body: New navigation property values.
        :type body: ~financials.models.microsoftgraphitem
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
        url = self.update_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphitem')
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

    update_item.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item'}  # type: ignore

    def delete_item(
        self,
        company_id,  # type: str
        sales_order_id,  # type: str
        sales_order_line_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property item for financials.

        Delete navigation property item for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
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
        url = self.delete_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
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

    delete_item.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item'}  # type: ignore
