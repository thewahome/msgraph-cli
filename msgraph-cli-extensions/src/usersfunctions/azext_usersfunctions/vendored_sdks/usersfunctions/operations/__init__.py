# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._user_activity_operations import UserActivityOperations
from ._user_calendar_calendar_view_calendar_operations import UserCalendarCalendarViewCalendarOperations
from ._user_calendar_calendar_view_instance_operations import UserCalendarCalendarViewInstanceOperations
from ._user_calendar_calendar_view_operations import UserCalendarCalendarViewOperations
from ._user_calendar_event_calendar_operations import UserCalendarEventCalendarOperations
from ._user_calendar_event_instance_operations import UserCalendarEventInstanceOperations
from ._user_calendar_event_operations import UserCalendarEventOperations
from ._user_calendar_operations import UserCalendarOperations
from ._user_calendar_group_calendar_calendar_view_calendar_operations import UserCalendarGroupCalendarCalendarViewCalendarOperations
from ._user_calendar_group_calendar_calendar_view_instance_operations import UserCalendarGroupCalendarCalendarViewInstanceOperations
from ._user_calendar_group_calendar_calendar_view_operations import UserCalendarGroupCalendarCalendarViewOperations
from ._user_calendar_group_calendar_event_calendar_operations import UserCalendarGroupCalendarEventCalendarOperations
from ._user_calendar_group_calendar_event_instance_operations import UserCalendarGroupCalendarEventInstanceOperations
from ._user_calendar_group_calendar_event_operations import UserCalendarGroupCalendarEventOperations
from ._user_calendar_group_calendar_operations import UserCalendarGroupCalendarOperations
from ._user_calendar_calendar_view_calendar_operations import UserCalendarCalendarViewCalendarOperations
from ._user_calendar_calendar_view_instance_operations import UserCalendarCalendarViewInstanceOperations
from ._user_calendar_calendar_view_operations import UserCalendarCalendarViewOperations
from ._user_calendar_event_calendar_operations import UserCalendarEventCalendarOperations
from ._user_calendar_event_instance_operations import UserCalendarEventInstanceOperations
from ._user_calendar_event_operations import UserCalendarEventOperations
from ._user_calendar_operations import UserCalendarOperations
from ._user_calendar_view_calendar_calendar_view_operations import UserCalendarViewCalendarCalendarViewOperations
from ._user_calendar_view_calendar_event_operations import UserCalendarViewCalendarEventOperations
from ._user_calendar_view_calendar_operations import UserCalendarViewCalendarOperations
from ._user_calendar_view_instance_operations import UserCalendarViewInstanceOperations
from ._user_calendar_view_operations import UserCalendarViewOperations
from ._user_contact_folder_child_folder_operations import UserContactFolderChildFolderOperations
from ._user_contact_folder_contact_operations import UserContactFolderContactOperations
from ._user_contact_folder_operations import UserContactFolderOperations
from ._user_contact_operations import UserContactOperations
from ._user_event_calendar_calendar_view_operations import UserEventCalendarCalendarViewOperations
from ._user_event_calendar_event_operations import UserEventCalendarEventOperations
from ._user_event_calendar_operations import UserEventCalendarOperations
from ._user_event_instance_operations import UserEventInstanceOperations
from ._user_event_operations import UserEventOperations
from ._user_mail_folder_child_folder_operations import UserMailFolderChildFolderOperations
from ._user_mail_folder_message_operations import UserMailFolderMessageOperations
from ._user_mail_folder_operations import UserMailFolderOperations
from ._user_managed_app_registration_operations import UserManagedAppRegistrationOperations
from ._user_message_operations import UserMessageOperations
from ._user_operations import UserOperations
from ._user_onenote_notebook_section_group_section_page_operations import UserOnenoteNotebookSectionGroupSectionPageOperations
from ._user_onenote_notebook_section_page_operations import UserOnenoteNotebookSectionPageOperations
from ._user_onenote_notebook_operations import UserOnenoteNotebookOperations
from ._user_onenote_page_operations import UserOnenotePageOperations
from ._user_onenote_page_parent_notebook_section_group_section_page_operations import UserOnenotePageParentNotebookSectionGroupSectionPageOperations
from ._user_onenote_page_parent_notebook_section_page_operations import UserOnenotePageParentNotebookSectionPageOperations
from ._user_onenote_page_parent_section_page_operations import UserOnenotePageParentSectionPageOperations
from ._user_onenote_section_group_parent_notebook_section_page_operations import UserOnenoteSectionGroupParentNotebookSectionPageOperations
from ._user_onenote_section_group_section_page_operations import UserOnenoteSectionGroupSectionPageOperations
from ._user_onenote_section_page_operations import UserOnenoteSectionPageOperations
from ._user_outlook_operations import UserOutlookOperations
from ._user_todo_list_task_operations import UserTodoListTaskOperations
from ._user_todo_list_operations import UserTodoListOperations

__all__ = [
    'UserActivityOperations',
    'UserCalendarCalendarViewCalendarOperations',
    'UserCalendarCalendarViewInstanceOperations',
    'UserCalendarCalendarViewOperations',
    'UserCalendarEventCalendarOperations',
    'UserCalendarEventInstanceOperations',
    'UserCalendarEventOperations',
    'UserCalendarOperations',
    'UserCalendarGroupCalendarCalendarViewCalendarOperations',
    'UserCalendarGroupCalendarCalendarViewInstanceOperations',
    'UserCalendarGroupCalendarCalendarViewOperations',
    'UserCalendarGroupCalendarEventCalendarOperations',
    'UserCalendarGroupCalendarEventInstanceOperations',
    'UserCalendarGroupCalendarEventOperations',
    'UserCalendarGroupCalendarOperations',
    'UserCalendarCalendarViewCalendarOperations',
    'UserCalendarCalendarViewInstanceOperations',
    'UserCalendarCalendarViewOperations',
    'UserCalendarEventCalendarOperations',
    'UserCalendarEventInstanceOperations',
    'UserCalendarEventOperations',
    'UserCalendarOperations',
    'UserCalendarViewCalendarCalendarViewOperations',
    'UserCalendarViewCalendarEventOperations',
    'UserCalendarViewCalendarOperations',
    'UserCalendarViewInstanceOperations',
    'UserCalendarViewOperations',
    'UserContactFolderChildFolderOperations',
    'UserContactFolderContactOperations',
    'UserContactFolderOperations',
    'UserContactOperations',
    'UserEventCalendarCalendarViewOperations',
    'UserEventCalendarEventOperations',
    'UserEventCalendarOperations',
    'UserEventInstanceOperations',
    'UserEventOperations',
    'UserMailFolderChildFolderOperations',
    'UserMailFolderMessageOperations',
    'UserMailFolderOperations',
    'UserManagedAppRegistrationOperations',
    'UserMessageOperations',
    'UserOperations',
    'UserOnenoteNotebookSectionGroupSectionPageOperations',
    'UserOnenoteNotebookSectionPageOperations',
    'UserOnenoteNotebookOperations',
    'UserOnenotePageOperations',
    'UserOnenotePageParentNotebookSectionGroupSectionPageOperations',
    'UserOnenotePageParentNotebookSectionPageOperations',
    'UserOnenotePageParentSectionPageOperations',
    'UserOnenoteSectionGroupParentNotebookSectionPageOperations',
    'UserOnenoteSectionGroupSectionPageOperations',
    'UserOnenoteSectionPageOperations',
    'UserOutlookOperations',
    'UserTodoListTaskOperations',
    'UserTodoListOperations',
]
