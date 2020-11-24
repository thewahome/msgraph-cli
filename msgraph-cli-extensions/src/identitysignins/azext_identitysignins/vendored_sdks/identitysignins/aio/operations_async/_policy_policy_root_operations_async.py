# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PolicyPolicyRootOperations:
    """PolicyPolicyRootOperations async operations.

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

    async def get_policy_root(
        self,
        select: Optional[List[Union[str, "models.Enum113"]]] = None,
        expand: Optional[List[Union[str, "models.Enum114"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphPolicyRoot":
        """Get policies.

        Get policies.

        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum113]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_sign_ins.models.Enum114]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPolicyRoot, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphPolicyRoot
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPolicyRoot"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_policy_root.metadata['url']  # type: ignore

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

        deserialized = self._deserialize('MicrosoftGraphPolicyRoot', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_policy_root.metadata = {'url': '/policies'}  # type: ignore

    async def update_policy_root(
        self,
        id: Optional[str] = None,
        activity_based_timeout_policies: Optional[List["models.MicrosoftGraphActivityBasedTimeoutPolicy"]] = None,
        claims_mapping_policies: Optional[List["models.MicrosoftGraphClaimsMappingPolicy"]] = None,
        home_realm_discovery_policies: Optional[List["models.MicrosoftGraphHomeRealmDiscoveryPolicy"]] = None,
        permission_grant_policies: Optional[List["models.MicrosoftGraphPermissionGrantPolicy"]] = None,
        token_issuance_policies: Optional[List["models.MicrosoftGraphTokenIssuancePolicy"]] = None,
        token_lifetime_policies: Optional[List["models.MicrosoftGraphTokenLifetimePolicy"]] = None,
        conditional_access_policies: Optional[List["models.MicrosoftGraphConditionalAccessPolicy"]] = None,
        identity_security_defaults_enforcement_policy: Optional["models.MicrosoftGraphIdentitySecurityDefaultsEnforcementPolicy"] = None,
        **kwargs
    ) -> None:
        """Update policies.

        Update policies.

        :param id: Read-only.
        :type id: str
        :param activity_based_timeout_policies:
        :type activity_based_timeout_policies: list[~identity_sign_ins.models.MicrosoftGraphActivityBasedTimeoutPolicy]
        :param claims_mapping_policies:
        :type claims_mapping_policies: list[~identity_sign_ins.models.MicrosoftGraphClaimsMappingPolicy]
        :param home_realm_discovery_policies:
        :type home_realm_discovery_policies: list[~identity_sign_ins.models.MicrosoftGraphHomeRealmDiscoveryPolicy]
        :param permission_grant_policies:
        :type permission_grant_policies: list[~identity_sign_ins.models.MicrosoftGraphPermissionGrantPolicy]
        :param token_issuance_policies:
        :type token_issuance_policies: list[~identity_sign_ins.models.MicrosoftGraphTokenIssuancePolicy]
        :param token_lifetime_policies:
        :type token_lifetime_policies: list[~identity_sign_ins.models.MicrosoftGraphTokenLifetimePolicy]
        :param conditional_access_policies:
        :type conditional_access_policies: list[~identity_sign_ins.models.MicrosoftGraphConditionalAccessPolicy]
        :param identity_security_defaults_enforcement_policy: Represents an Azure Active Directory
         object. The directoryObject type is the base type for many other directory entity types.
        :type identity_security_defaults_enforcement_policy: ~identity_sign_ins.models.MicrosoftGraphIdentitySecurityDefaultsEnforcementPolicy
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPolicyRoot(id=id, activity_based_timeout_policies=activity_based_timeout_policies, claims_mapping_policies=claims_mapping_policies, home_realm_discovery_policies=home_realm_discovery_policies, permission_grant_policies=permission_grant_policies, token_issuance_policies=token_issuance_policies, token_lifetime_policies=token_lifetime_policies, conditional_access_policies=conditional_access_policies, identity_security_defaults_enforcement_policy=identity_security_defaults_enforcement_policy)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_policy_root.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPolicyRoot')
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

    update_policy_root.metadata = {'url': '/policies'}  # type: ignore
