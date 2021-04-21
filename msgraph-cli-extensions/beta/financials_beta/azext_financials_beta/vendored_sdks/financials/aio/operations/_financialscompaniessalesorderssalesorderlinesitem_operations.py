# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, IO, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class financialscompaniessalesorderssalesorderlinesitemOperations:
    """financialscompaniessalesorderssalesorderlinesitemOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_item_category(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        select: Optional[List[Union[str, "models.Enum289"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.microsoftgraphitemcategory":
        """Get itemCategory from financials.

        Get itemCategory from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum289]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphitemcategory, or the result of cls(response)
        :rtype: ~financials.models.microsoftgraphitemcategory
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphitemcategory"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_item_category.metadata['url']  # type: ignore
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphitemcategory', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_item_category.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/itemCategory'}  # type: ignore

    async def update_item_category(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        body: "models.microsoftgraphitemcategory",
        **kwargs
    ) -> None:
        """Update the navigation property itemCategory in financials.

        Update the navigation property itemCategory in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param body: New navigation property values.
        :type body: ~financials.models.microsoftgraphitemcategory
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
        url = self.update_item_category.metadata['url']  # type: ignore
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
        body_content = self._serialize.body(body, 'microsoftgraphitemcategory')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_item_category.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/itemCategory'}  # type: ignore

    async def delete_item_category(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property itemCategory for financials.

        Delete navigation property itemCategory for financials.

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
        url = self.delete_item_category.metadata['url']  # type: ignore
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_item_category.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/itemCategory'}  # type: ignore

    def list_picture(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        orderby: Optional[List[Union[str, "models.Enum290"]]] = None,
        select: Optional[List[Union[str, "models.Enum291"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.collectionofpicture16"]:
        """Get picture from financials.

        Get picture from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~financials.models.Enum290]
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum291]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either collectionofpicture16 or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~financials.models.collectionofpicture16]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.collectionofpicture16"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_picture.metadata['url']  # type: ignore
                path_format_arguments = {
                    'company-id': self._serialize.url("company_id", company_id, 'str'),
                    'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
                    'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('collectionofpicture16', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.odataerror, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_picture.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture'}  # type: ignore

    async def create_picture(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        body: "models.microsoftgraphpicture",
        **kwargs
    ) -> "models.microsoftgraphpicture":
        """Create new navigation property to picture for financials.

        Create new navigation property to picture for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param body: New navigation property.
        :type body: ~financials.models.microsoftgraphpicture
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphpicture, or the result of cls(response)
        :rtype: ~financials.models.microsoftgraphpicture
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphpicture"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_picture.metadata['url']  # type: ignore
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
        body_content = self._serialize.body(body, 'microsoftgraphpicture')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphpicture', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_picture.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture'}  # type: ignore

    async def get_picture(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        picture_id: str,
        select: Optional[List[Union[str, "models.Enum292"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.microsoftgraphpicture":
        """Get picture from financials.

        Get picture from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum292]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphpicture, or the result of cls(response)
        :rtype: ~financials.models.microsoftgraphpicture
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphpicture"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphpicture', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_picture.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture/{picture-id}'}  # type: ignore

    async def update_picture(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        picture_id: str,
        body: "models.microsoftgraphpicture",
        **kwargs
    ) -> None:
        """Update the navigation property picture in financials.

        Update the navigation property picture in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :param body: New navigation property values.
        :type body: ~financials.models.microsoftgraphpicture
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
        url = self.update_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'microsoftgraphpicture')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update_picture.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture/{picture-id}'}  # type: ignore

    async def delete_picture(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        picture_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property picture for financials.

        Delete navigation property picture for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
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
        url = self.delete_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_picture.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture/{picture-id}'}  # type: ignore

    async def get_picture_content(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        picture_id: str,
        **kwargs
    ) -> IO:
        """Get media content for the navigation property picture from financials.

        Get media content for the navigation property picture from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self.get_picture_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_picture_content.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture/{picture-id}/content'}  # type: ignore

    async def set_picture_content(
        self,
        company_id: str,
        sales_order_id: str,
        sales_order_line_id: str,
        picture_id: str,
        data: IO,
        **kwargs
    ) -> None:
        """Update media content for the navigation property picture in financials.

        Update media content for the navigation property picture in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_order_id: key: id of salesOrder.
        :type sales_order_id: str
        :param sales_order_line_id: key: id of salesOrderLine.
        :type sales_order_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :param data: New media content.
        :type data: IO
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
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/json"

        # Construct URL
        url = self.set_picture_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesOrder-id': self._serialize.url("sales_order_id", sales_order_id, 'str'),
            'salesOrderLine-id': self._serialize.url("sales_order_line_id", sales_order_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['stream_content'] = data
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    set_picture_content.metadata = {'url': '/financials/companies/{company-id}/salesOrders/{salesOrder-id}/salesOrderLines/{salesOrderLine-id}/item/picture/{picture-id}/content'}  # type: ignore
