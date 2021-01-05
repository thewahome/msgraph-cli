# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RiskDetectionRiskDetectionOperations:
    """RiskDetectionRiskDetectionOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_sign_ins.models
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

    def list_risk_detection(
        self,
        orderby: Optional[List[Union[str, "models.Enum252"]]] = None,
        select: Optional[List[Union[str, "models.Enum253"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfRiskDetection"]:
        """Get entities from riskDetections.

        Get entities from riskDetections.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_sign_ins.models.Enum252]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum253]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfRiskDetection or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~identity_sign_ins.models.CollectionOfRiskDetection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfRiskDetection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_risk_detection.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfRiskDetection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_risk_detection.metadata = {'url': '/riskDetections'}  # type: ignore

    async def create_risk_detection(
        self,
        id: Optional[str] = None,
        activity: Optional[Union[str, "models.MicrosoftGraphActivityType"]] = None,
        activity_date_time: Optional[datetime.datetime] = None,
        additional_info: Optional[str] = None,
        correlation_id: Optional[str] = None,
        detected_date_time: Optional[datetime.datetime] = None,
        detection_timing_type: Optional[Union[str, "models.MicrosoftGraphRiskDetectionTimingType"]] = None,
        ip_address: Optional[str] = None,
        last_updated_date_time: Optional[datetime.datetime] = None,
        request_id_parameter: Optional[str] = None,
        risk_detail: Optional[Union[str, "models.MicrosoftGraphRiskDetail"]] = None,
        risk_event_type: Optional[str] = None,
        risk_level: Optional[Union[str, "models.MicrosoftGraphRiskLevel"]] = None,
        risk_state: Optional[Union[str, "models.MicrosoftGraphRiskState"]] = None,
        risk_type: Optional[Union[str, "models.MicrosoftGraphRiskEventType"]] = None,
        source: Optional[str] = None,
        token_issuer_type: Optional[Union[str, "models.MicrosoftGraphTokenIssuerType"]] = None,
        user_display_name: Optional[str] = None,
        user_id: Optional[str] = None,
        user_principal_name: Optional[str] = None,
        city: Optional[str] = None,
        country_or_region: Optional[str] = None,
        geo_coordinates: Optional["models.MicrosoftGraphGeoCoordinates"] = None,
        state: Optional[str] = None,
        **kwargs
    ) -> "models.MicrosoftGraphRiskDetection":
        """Add new entity to riskDetections.

        Add new entity to riskDetections.

        :param id: Read-only.
        :type id: str
        :param activity:
        :type activity: str or ~identity_sign_ins.models.MicrosoftGraphActivityType
        :param activity_date_time: Date and time that the risky activity occurred.
        :type activity_date_time: ~datetime.datetime
        :param additional_info: Additional information associated with the risk detection in JSON
         format.
        :type additional_info: str
        :param correlation_id: Correlation ID of the sign-in associated with the risk detection. This
         property is null if the risk detection is not associated with a sign-in.
        :type correlation_id: str
        :param detected_date_time: Date and time that the risk was detected.
        :type detected_date_time: ~datetime.datetime
        :param detection_timing_type:
        :type detection_timing_type: str or ~identity_sign_ins.models.MicrosoftGraphRiskDetectionTimingType
        :param ip_address: Provides the IP address of the client from where the risk occurred.
        :type ip_address: str
        :param last_updated_date_time: Date and time that the risk detection was last updated.
        :type last_updated_date_time: ~datetime.datetime
        :param request_id_parameter: Request ID of the sign-in associated with the risk detection. This
         property is null if the risk detection is not associated with a sign-in.
        :type request_id_parameter: str
        :param risk_detail:
        :type risk_detail: str or ~identity_sign_ins.models.MicrosoftGraphRiskDetail
        :param risk_event_type: The type of risk event detected. The possible values are
         unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures,
         malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials,
         investigationsThreatIntelligence, genericadminConfirmedUserCompromised, mcasImpossibleTravel,
         mcasSuspiciousInboxManipulationRules, investigationsThreatIntelligenceSigninLinked,
         maliciousIPAddressValidCredentialsBlockedIP, and unknownFutureValue. If the risk detection is a
         premium detection, will show generic.
        :type risk_event_type: str
        :param risk_level:
        :type risk_level: str or ~identity_sign_ins.models.MicrosoftGraphRiskLevel
        :param risk_state:
        :type risk_state: str or ~identity_sign_ins.models.MicrosoftGraphRiskState
        :param risk_type:
        :type risk_type: str or ~identity_sign_ins.models.MicrosoftGraphRiskEventType
        :param source: Source of the risk detection. For example, 'activeDirectory'.
        :type source: str
        :param token_issuer_type:
        :type token_issuer_type: str or ~identity_sign_ins.models.MicrosoftGraphTokenIssuerType
        :param user_display_name: The user principal name (UPN) of the user.
        :type user_display_name: str
        :param user_id: Unique ID of the user.
        :type user_id: str
        :param user_principal_name: The user principal name (UPN) of the user.
        :type user_principal_name: str
        :param city: Provides the city where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type city: str
        :param country_or_region: Provides the country code info (2 letter code) where the sign-in
         originated.  This is calculated using latitude/longitude information from the sign-in activity.
        :type country_or_region: str
        :param geo_coordinates: geoCoordinates.
        :type geo_coordinates: ~identity_sign_ins.models.MicrosoftGraphGeoCoordinates
        :param state: Provides the State where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type state: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphRiskDetection, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphRiskDetection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphRiskDetection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphRiskDetection(id=id, activity=activity, activity_date_time=activity_date_time, additional_info=additional_info, correlation_id=correlation_id, detected_date_time=detected_date_time, detection_timing_type=detection_timing_type, ip_address=ip_address, last_updated_date_time=last_updated_date_time, request_id=request_id_parameter, risk_detail=risk_detail, risk_event_type=risk_event_type, risk_level=risk_level, risk_state=risk_state, risk_type=risk_type, source=source, token_issuer_type=token_issuer_type, user_display_name=user_display_name, user_id=user_id, user_principal_name=user_principal_name, city=city, country_or_region=country_or_region, geo_coordinates=geo_coordinates, state=state)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_risk_detection.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphRiskDetection')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphRiskDetection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_risk_detection.metadata = {'url': '/riskDetections'}  # type: ignore

    async def get_risk_detection(
        self,
        risk_detection_id: str,
        select: Optional[List[Union[str, "models.Enum260"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphRiskDetection":
        """Get entity from riskDetections by key.

        Get entity from riskDetections by key.

        :param risk_detection_id: key: id of riskDetection.
        :type risk_detection_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum260]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphRiskDetection, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphRiskDetection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphRiskDetection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_risk_detection.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskDetection-id': self._serialize.url("risk_detection_id", risk_detection_id, 'str'),
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
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphRiskDetection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_risk_detection.metadata = {'url': '/riskDetections/{riskDetection-id}'}  # type: ignore

    async def update_risk_detection(
        self,
        risk_detection_id: str,
        id: Optional[str] = None,
        activity: Optional[Union[str, "models.MicrosoftGraphActivityType"]] = None,
        activity_date_time: Optional[datetime.datetime] = None,
        additional_info: Optional[str] = None,
        correlation_id: Optional[str] = None,
        detected_date_time: Optional[datetime.datetime] = None,
        detection_timing_type: Optional[Union[str, "models.MicrosoftGraphRiskDetectionTimingType"]] = None,
        ip_address: Optional[str] = None,
        last_updated_date_time: Optional[datetime.datetime] = None,
        request_id_parameter: Optional[str] = None,
        risk_detail: Optional[Union[str, "models.MicrosoftGraphRiskDetail"]] = None,
        risk_event_type: Optional[str] = None,
        risk_level: Optional[Union[str, "models.MicrosoftGraphRiskLevel"]] = None,
        risk_state: Optional[Union[str, "models.MicrosoftGraphRiskState"]] = None,
        risk_type: Optional[Union[str, "models.MicrosoftGraphRiskEventType"]] = None,
        source: Optional[str] = None,
        token_issuer_type: Optional[Union[str, "models.MicrosoftGraphTokenIssuerType"]] = None,
        user_display_name: Optional[str] = None,
        user_id: Optional[str] = None,
        user_principal_name: Optional[str] = None,
        city: Optional[str] = None,
        country_or_region: Optional[str] = None,
        geo_coordinates: Optional["models.MicrosoftGraphGeoCoordinates"] = None,
        state: Optional[str] = None,
        **kwargs
    ) -> None:
        """Update entity in riskDetections.

        Update entity in riskDetections.

        :param risk_detection_id: key: id of riskDetection.
        :type risk_detection_id: str
        :param id: Read-only.
        :type id: str
        :param activity:
        :type activity: str or ~identity_sign_ins.models.MicrosoftGraphActivityType
        :param activity_date_time: Date and time that the risky activity occurred.
        :type activity_date_time: ~datetime.datetime
        :param additional_info: Additional information associated with the risk detection in JSON
         format.
        :type additional_info: str
        :param correlation_id: Correlation ID of the sign-in associated with the risk detection. This
         property is null if the risk detection is not associated with a sign-in.
        :type correlation_id: str
        :param detected_date_time: Date and time that the risk was detected.
        :type detected_date_time: ~datetime.datetime
        :param detection_timing_type:
        :type detection_timing_type: str or ~identity_sign_ins.models.MicrosoftGraphRiskDetectionTimingType
        :param ip_address: Provides the IP address of the client from where the risk occurred.
        :type ip_address: str
        :param last_updated_date_time: Date and time that the risk detection was last updated.
        :type last_updated_date_time: ~datetime.datetime
        :param request_id_parameter: Request ID of the sign-in associated with the risk detection. This
         property is null if the risk detection is not associated with a sign-in.
        :type request_id_parameter: str
        :param risk_detail:
        :type risk_detail: str or ~identity_sign_ins.models.MicrosoftGraphRiskDetail
        :param risk_event_type: The type of risk event detected. The possible values are
         unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures,
         malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials,
         investigationsThreatIntelligence, genericadminConfirmedUserCompromised, mcasImpossibleTravel,
         mcasSuspiciousInboxManipulationRules, investigationsThreatIntelligenceSigninLinked,
         maliciousIPAddressValidCredentialsBlockedIP, and unknownFutureValue. If the risk detection is a
         premium detection, will show generic.
        :type risk_event_type: str
        :param risk_level:
        :type risk_level: str or ~identity_sign_ins.models.MicrosoftGraphRiskLevel
        :param risk_state:
        :type risk_state: str or ~identity_sign_ins.models.MicrosoftGraphRiskState
        :param risk_type:
        :type risk_type: str or ~identity_sign_ins.models.MicrosoftGraphRiskEventType
        :param source: Source of the risk detection. For example, 'activeDirectory'.
        :type source: str
        :param token_issuer_type:
        :type token_issuer_type: str or ~identity_sign_ins.models.MicrosoftGraphTokenIssuerType
        :param user_display_name: The user principal name (UPN) of the user.
        :type user_display_name: str
        :param user_id: Unique ID of the user.
        :type user_id: str
        :param user_principal_name: The user principal name (UPN) of the user.
        :type user_principal_name: str
        :param city: Provides the city where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type city: str
        :param country_or_region: Provides the country code info (2 letter code) where the sign-in
         originated.  This is calculated using latitude/longitude information from the sign-in activity.
        :type country_or_region: str
        :param geo_coordinates: geoCoordinates.
        :type geo_coordinates: ~identity_sign_ins.models.MicrosoftGraphGeoCoordinates
        :param state: Provides the State where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type state: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphRiskDetection(id=id, activity=activity, activity_date_time=activity_date_time, additional_info=additional_info, correlation_id=correlation_id, detected_date_time=detected_date_time, detection_timing_type=detection_timing_type, ip_address=ip_address, last_updated_date_time=last_updated_date_time, request_id=request_id_parameter, risk_detail=risk_detail, risk_event_type=risk_event_type, risk_level=risk_level, risk_state=risk_state, risk_type=risk_type, source=source, token_issuer_type=token_issuer_type, user_display_name=user_display_name, user_id=user_id, user_principal_name=user_principal_name, city=city, country_or_region=country_or_region, geo_coordinates=geo_coordinates, state=state)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_risk_detection.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskDetection-id': self._serialize.url("risk_detection_id", risk_detection_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphRiskDetection')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_risk_detection.metadata = {'url': '/riskDetections/{riskDetection-id}'}  # type: ignore

    async def delete_risk_detection(
        self,
        risk_detection_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete entity from riskDetections.

        Delete entity from riskDetections.

        :param risk_detection_id: key: id of riskDetection.
        :type risk_detection_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_risk_detection.metadata['url']  # type: ignore
        path_format_arguments = {
            'riskDetection-id': self._serialize.url("risk_detection_id", risk_detection_id, 'str'),
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
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_risk_detection.metadata = {'url': '/riskDetections/{riskDetection-id}'}  # type: ignore
