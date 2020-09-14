# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_groupsplanner.generated._client_factory import cf_group
    groupsplanner_group = CliCommandType(
        operations_tmpl='azext_groupsplanner.vendored_sdks.groupsplanner.operations._group_operations#GroupOperations.{'
        '}',
        client_factory=cf_group)
    with self.command_group('groupsplanner', groupsplanner_group, client_factory=cf_group) as g:
        g.custom_command('get-planner', 'groupsplanner_get_planner')
        g.custom_command('update-planner', 'groupsplanner_update_planner')

    from azext_groupsplanner.generated._client_factory import cf_group_planner
    groupsplanner_group_planner = CliCommandType(
        operations_tmpl='azext_groupsplanner.vendored_sdks.groupsplanner.operations._group_planner_operations#GroupPlan'
        'nerOperations.{}',
        client_factory=cf_group_planner)
    with self.command_group('groupsplanner', groupsplanner_group_planner, client_factory=cf_group_planner) as g:
        g.custom_command('create-plan', 'groupsplanner_create_plan')
        g.custom_command('get-plan', 'groupsplanner_get_plan')
        g.custom_command('list-plan', 'groupsplanner_list_plan')
        g.custom_command('update-plan', 'groupsplanner_update_plan')

    from azext_groupsplanner.generated._client_factory import cf_group_planner_plan
    groupsplanner_group_planner_plan = CliCommandType(
        operations_tmpl='azext_groupsplanner.vendored_sdks.groupsplanner.operations._group_planner_plan_operations#Grou'
        'pPlannerPlanOperations.{}',
        client_factory=cf_group_planner_plan)
    with self.command_group('groupsplanner', groupsplanner_group_planner_plan,
                            client_factory=cf_group_planner_plan) as g:
        g.custom_command('create-bucket', 'groupsplanner_create_bucket')
        g.custom_command('create-task', 'groupsplanner_create_task')
        g.custom_command('get-bucket', 'groupsplanner_get_bucket')
        g.custom_command('get-detail', 'groupsplanner_get_detail')
        g.custom_command('get-task', 'groupsplanner_get_task')
        g.custom_command('list-bucket', 'groupsplanner_list_bucket')
        g.custom_command('list-task', 'groupsplanner_list_task')
        g.custom_command('update-bucket', 'groupsplanner_update_bucket')
        g.custom_command('update-detail', 'groupsplanner_update_detail')
        g.custom_command('update-task', 'groupsplanner_update_task')

    from azext_groupsplanner.generated._client_factory import cf_group_planner_plan_bucket
    groupsplanner_group_planner_plan_bucket = CliCommandType(
        operations_tmpl='azext_groupsplanner.vendored_sdks.groupsplanner.operations._group_planner_plan_bucket_operatio'
        'ns#GroupPlannerPlanBucketOperations.{}',
        client_factory=cf_group_planner_plan_bucket)
    with self.command_group('groupsplanner', groupsplanner_group_planner_plan_bucket,
                            client_factory=cf_group_planner_plan_bucket) as g:
        g.custom_command('create-task', 'groupsplanner_create_task')
        g.custom_command('get-task', 'groupsplanner_get_task')
        g.custom_command('list-task', 'groupsplanner_list_task')
        g.custom_command('update-task', 'groupsplanner_update_task')

    from azext_groupsplanner.generated._client_factory import cf_group_planner_plan_bucket_task
    groupsplanner_group_planner_plan_bucket_task = CliCommandType(
        operations_tmpl='azext_groupsplanner.vendored_sdks.groupsplanner.operations._group_planner_plan_bucket_task_ope'
        'rations#GroupPlannerPlanBucketTaskOperations.{}',
        client_factory=cf_group_planner_plan_bucket_task)
    with self.command_group('groupsplanner', groupsplanner_group_planner_plan_bucket_task,
                            client_factory=cf_group_planner_plan_bucket_task) as g:
        g.custom_command('get-assigned-to-task-board-format', 'groupsplanner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'groupsplanner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'groupsplanner_get_detail')
        g.custom_command('get-progress-task-board-format', 'groupsplanner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'groupsplanner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'groupsplanner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'groupsplanner_update_detail')
        g.custom_command('update-progress-task-board-format', 'groupsplanner_update_progress_task_board_format')

    from azext_groupsplanner.generated._client_factory import cf_group_planner_plan_task
    groupsplanner_group_planner_plan_task = CliCommandType(
        operations_tmpl='azext_groupsplanner.vendored_sdks.groupsplanner.operations._group_planner_plan_task_operations'
        '#GroupPlannerPlanTaskOperations.{}',
        client_factory=cf_group_planner_plan_task)
    with self.command_group('groupsplanner', groupsplanner_group_planner_plan_task,
                            client_factory=cf_group_planner_plan_task) as g:
        g.custom_command('get-assigned-to-task-board-format', 'groupsplanner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'groupsplanner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'groupsplanner_get_detail')
        g.custom_command('get-progress-task-board-format', 'groupsplanner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'groupsplanner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'groupsplanner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'groupsplanner_update_detail')
        g.custom_command('update-progress-task-board-format', 'groupsplanner_update_progress_task_board_format')
