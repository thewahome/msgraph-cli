# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class GroupPlannerPlanBucketOperations(object):
    """GroupPlannerPlanBucketOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~planner.models
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

    def list_task(
        self,
        group_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum13"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum14"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get10ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPlannerTask"]
        """Get tasks from groups.

        Get tasks from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~planner.models.Enum13]
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum14]
        :param expand: Expand related entities.
        :type expand: list[str or ~planner.models.Get10ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPlannerTask or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~planner.models.CollectionOfPlannerTask]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPlannerTask"]
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
                url = self.list_task.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                    'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
                    'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfPlannerTask', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_task.metadata = {'url': '/groups/{group-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks'}  # type: ignore

    def create_task(
        self,
        group_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        id=None,  # type: Optional[str]
        active_checklist_item_count=None,  # type: Optional[int]
        applied_categories=None,  # type: Optional[Dict[str, object]]
        assignee_priority=None,  # type: Optional[str]
        assignments=None,  # type: Optional[Dict[str, object]]
        bucket_id=None,  # type: Optional[str]
        checklist_item_count=None,  # type: Optional[int]
        completed_date_time=None,  # type: Optional[datetime.datetime]
        conversation_thread_id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        due_date_time=None,  # type: Optional[datetime.datetime]
        has_description=None,  # type: Optional[bool]
        order_hint=None,  # type: Optional[str]
        percent_complete=None,  # type: Optional[int]
        plan_id=None,  # type: Optional[str]
        preview_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphPlannerPreviewType"]]
        reference_count=None,  # type: Optional[int]
        start_date_time=None,  # type: Optional[datetime.datetime]
        title=None,  # type: Optional[str]
        bucket_task_board_format=None,  # type: Optional["models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat"]
        progress_task_board_format=None,  # type: Optional["models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat"]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        checklist=None,  # type: Optional[Dict[str, object]]
        description=None,  # type: Optional[str]
        microsoft_graph_planner_preview_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphPlannerPreviewType"]]
        references=None,  # type: Optional[Dict[str, object]]
        id1=None,  # type: Optional[str]
        order_hints_by_assignee=None,  # type: Optional[Dict[str, object]]
        unassigned_order_hint=None,  # type: Optional[str]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerTask"
        """Create new navigation property to tasks for groups.

        Create new navigation property to tasks for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param id: Read-only.
        :type id: str
        :param active_checklist_item_count: Number of checklist items with value set to false,
         representing incomplete items.
        :type active_checklist_item_count: int
        :param applied_categories: plannerAppliedCategories.
        :type applied_categories: dict[str, object]
        :param assignee_priority: Hint used to order items of this type in a list view. The format is
         defined as outlined here.
        :type assignee_priority: str
        :param assignments: plannerAssignments.
        :type assignments: dict[str, object]
        :param bucket_id: Bucket ID to which the task belongs. The bucket needs to be in the plan that
         the task is in. It is 28 characters long and case-sensitive. Format validation is done on the
         service.
        :type bucket_id: str
        :param checklist_item_count: Number of checklist items that are present on the task.
        :type checklist_item_count: int
        :param completed_date_time: Read-only. Date and time at which the 'percentComplete' of the task
         is set to '100'. The Timestamp type represents date and time information using ISO 8601 format
         and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this:
         '2014-01-01T00:00:00Z'.
        :type completed_date_time: ~datetime.datetime
        :param conversation_thread_id: Thread ID of the conversation on the task. This is the ID of the
         conversation thread object created in the group.
        :type conversation_thread_id: str
        :param created_date_time: Read-only. Date and time at which the task is created. The Timestamp
         type represents date and time information using ISO 8601 format and is always in UTC time. For
         example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param due_date_time: Date and time at which the task is due. The Timestamp type represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type due_date_time: ~datetime.datetime
        :param has_description: Read-only. Value is true if the details object of the task has a non-
         empty description and false otherwise.
        :type has_description: bool
        :param order_hint: Hint used to order items of this type in a list view. The format is defined
         as outlined here.
        :type order_hint: str
        :param percent_complete: Percentage of task completion. When set to 100, the task is considered
         completed.
        :type percent_complete: int
        :param plan_id: Plan ID to which the task belongs.
        :type plan_id: str
        :param preview_type:
        :type preview_type: str or ~planner.models.MicrosoftGraphPlannerPreviewType
        :param reference_count: Number of external references that exist on the task.
        :type reference_count: int
        :param start_date_time: Date and time at which the task starts. The Timestamp type represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type start_date_time: ~datetime.datetime
        :param title: Title of the task.
        :type title: str
        :param bucket_task_board_format: plannerBucketTaskBoardTaskFormat.
        :type bucket_task_board_format: ~planner.models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat
        :param progress_task_board_format: plannerProgressTaskBoardTaskFormat.
        :type progress_task_board_format: ~planner.models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param checklist: plannerChecklistItems.
        :type checklist: dict[str, object]
        :param description: Description of the task.
        :type description: str
        :param microsoft_graph_planner_preview_type:
        :type microsoft_graph_planner_preview_type: str or ~planner.models.MicrosoftGraphPlannerPreviewType
        :param references: plannerExternalReferences.
        :type references: dict[str, object]
        :param id1: Read-only.
        :type id1: str
        :param order_hints_by_assignee: plannerOrderHintsByAssignee.
        :type order_hints_by_assignee: dict[str, object]
        :param unassigned_order_hint: Hint value used to order the task on the AssignedTo view of the
         Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary
         does not provide an order hint for the user the task is assigned to. The format is defined as
         outlined here.
        :type unassigned_order_hint: str
        :param application: identity.
        :type application: ~planner.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~planner.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~planner.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~planner.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~planner.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~planner.models.MicrosoftGraphIdentity
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerTask, or the result of cls(response)
        :rtype: ~planner.models.MicrosoftGraphPlannerTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerTask"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerTask(id=id, active_checklist_item_count=active_checklist_item_count, applied_categories=applied_categories, assignee_priority=assignee_priority, assignments=assignments, bucket_id=bucket_id, checklist_item_count=checklist_item_count, completed_date_time=completed_date_time, conversation_thread_id=conversation_thread_id, created_date_time=created_date_time, due_date_time=due_date_time, has_description=has_description, order_hint=order_hint, percent_complete=percent_complete, plan_id=plan_id, preview_type=preview_type, reference_count=reference_count, start_date_time=start_date_time, title=title, bucket_task_board_format=bucket_task_board_format, progress_task_board_format=progress_task_board_format, id_details_id=microsoft_graph_entity_id, checklist=checklist, description=description, preview_type_details_preview_type=microsoft_graph_planner_preview_type, references=references, id_assigned_to_task_board_format_id=id1, order_hints_by_assignee=order_hints_by_assignee, unassigned_order_hint=unassigned_order_hint, application_created_by_application=application, device_created_by_device=device, user_created_by_user=user, application_completed_by_application=microsoft_graph_identity_application, device_completed_by_device=microsoft_graph_identity_device, user_completed_by_user=microsoft_graph_identity_user)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerTask')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPlannerTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_task.metadata = {'url': '/groups/{group-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks'}  # type: ignore

    def get_task(
        self,
        group_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum16"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get5ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerTask"
        """Get tasks from groups.

        Get tasks from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum16]
        :param expand: Expand related entities.
        :type expand: list[str or ~planner.models.Get5ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerTask, or the result of cls(response)
        :rtype: ~planner.models.MicrosoftGraphPlannerTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerTask"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPlannerTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_task.metadata = {'url': '/groups/{group-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}'}  # type: ignore

    def update_task(
        self,
        group_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        id=None,  # type: Optional[str]
        active_checklist_item_count=None,  # type: Optional[int]
        applied_categories=None,  # type: Optional[Dict[str, object]]
        assignee_priority=None,  # type: Optional[str]
        assignments=None,  # type: Optional[Dict[str, object]]
        bucket_id=None,  # type: Optional[str]
        checklist_item_count=None,  # type: Optional[int]
        completed_date_time=None,  # type: Optional[datetime.datetime]
        conversation_thread_id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        due_date_time=None,  # type: Optional[datetime.datetime]
        has_description=None,  # type: Optional[bool]
        order_hint=None,  # type: Optional[str]
        percent_complete=None,  # type: Optional[int]
        plan_id=None,  # type: Optional[str]
        preview_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphPlannerPreviewType"]]
        reference_count=None,  # type: Optional[int]
        start_date_time=None,  # type: Optional[datetime.datetime]
        title=None,  # type: Optional[str]
        bucket_task_board_format=None,  # type: Optional["models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat"]
        progress_task_board_format=None,  # type: Optional["models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat"]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        checklist=None,  # type: Optional[Dict[str, object]]
        description=None,  # type: Optional[str]
        microsoft_graph_planner_preview_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphPlannerPreviewType"]]
        references=None,  # type: Optional[Dict[str, object]]
        id1=None,  # type: Optional[str]
        order_hints_by_assignee=None,  # type: Optional[Dict[str, object]]
        unassigned_order_hint=None,  # type: Optional[str]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property tasks in groups.

        Update the navigation property tasks in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param id: Read-only.
        :type id: str
        :param active_checklist_item_count: Number of checklist items with value set to false,
         representing incomplete items.
        :type active_checklist_item_count: int
        :param applied_categories: plannerAppliedCategories.
        :type applied_categories: dict[str, object]
        :param assignee_priority: Hint used to order items of this type in a list view. The format is
         defined as outlined here.
        :type assignee_priority: str
        :param assignments: plannerAssignments.
        :type assignments: dict[str, object]
        :param bucket_id: Bucket ID to which the task belongs. The bucket needs to be in the plan that
         the task is in. It is 28 characters long and case-sensitive. Format validation is done on the
         service.
        :type bucket_id: str
        :param checklist_item_count: Number of checklist items that are present on the task.
        :type checklist_item_count: int
        :param completed_date_time: Read-only. Date and time at which the 'percentComplete' of the task
         is set to '100'. The Timestamp type represents date and time information using ISO 8601 format
         and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this:
         '2014-01-01T00:00:00Z'.
        :type completed_date_time: ~datetime.datetime
        :param conversation_thread_id: Thread ID of the conversation on the task. This is the ID of the
         conversation thread object created in the group.
        :type conversation_thread_id: str
        :param created_date_time: Read-only. Date and time at which the task is created. The Timestamp
         type represents date and time information using ISO 8601 format and is always in UTC time. For
         example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param due_date_time: Date and time at which the task is due. The Timestamp type represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type due_date_time: ~datetime.datetime
        :param has_description: Read-only. Value is true if the details object of the task has a non-
         empty description and false otherwise.
        :type has_description: bool
        :param order_hint: Hint used to order items of this type in a list view. The format is defined
         as outlined here.
        :type order_hint: str
        :param percent_complete: Percentage of task completion. When set to 100, the task is considered
         completed.
        :type percent_complete: int
        :param plan_id: Plan ID to which the task belongs.
        :type plan_id: str
        :param preview_type:
        :type preview_type: str or ~planner.models.MicrosoftGraphPlannerPreviewType
        :param reference_count: Number of external references that exist on the task.
        :type reference_count: int
        :param start_date_time: Date and time at which the task starts. The Timestamp type represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type start_date_time: ~datetime.datetime
        :param title: Title of the task.
        :type title: str
        :param bucket_task_board_format: plannerBucketTaskBoardTaskFormat.
        :type bucket_task_board_format: ~planner.models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat
        :param progress_task_board_format: plannerProgressTaskBoardTaskFormat.
        :type progress_task_board_format: ~planner.models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param checklist: plannerChecklistItems.
        :type checklist: dict[str, object]
        :param description: Description of the task.
        :type description: str
        :param microsoft_graph_planner_preview_type:
        :type microsoft_graph_planner_preview_type: str or ~planner.models.MicrosoftGraphPlannerPreviewType
        :param references: plannerExternalReferences.
        :type references: dict[str, object]
        :param id1: Read-only.
        :type id1: str
        :param order_hints_by_assignee: plannerOrderHintsByAssignee.
        :type order_hints_by_assignee: dict[str, object]
        :param unassigned_order_hint: Hint value used to order the task on the AssignedTo view of the
         Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary
         does not provide an order hint for the user the task is assigned to. The format is defined as
         outlined here.
        :type unassigned_order_hint: str
        :param application: identity.
        :type application: ~planner.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~planner.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~planner.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~planner.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~planner.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~planner.models.MicrosoftGraphIdentity
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerTask(id=id, active_checklist_item_count=active_checklist_item_count, applied_categories=applied_categories, assignee_priority=assignee_priority, assignments=assignments, bucket_id=bucket_id, checklist_item_count=checklist_item_count, completed_date_time=completed_date_time, conversation_thread_id=conversation_thread_id, created_date_time=created_date_time, due_date_time=due_date_time, has_description=has_description, order_hint=order_hint, percent_complete=percent_complete, plan_id=plan_id, preview_type=preview_type, reference_count=reference_count, start_date_time=start_date_time, title=title, bucket_task_board_format=bucket_task_board_format, progress_task_board_format=progress_task_board_format, id_details_id=microsoft_graph_entity_id, checklist=checklist, description=description, preview_type_details_preview_type=microsoft_graph_planner_preview_type, references=references, id_assigned_to_task_board_format_id=id1, order_hints_by_assignee=order_hints_by_assignee, unassigned_order_hint=unassigned_order_hint, application_created_by_application=application, device_created_by_device=device, user_created_by_user=user, application_completed_by_application=microsoft_graph_identity_application, device_completed_by_device=microsoft_graph_identity_device, user_completed_by_user=microsoft_graph_identity_user)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerTask')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_task.metadata = {'url': '/groups/{group-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}'}  # type: ignore

    def delete_task(
        self,
        group_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property tasks for groups.

        Delete navigation property tasks for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
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
        url = self.delete_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_task.metadata = {'url': '/groups/{group-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}'}  # type: ignore
