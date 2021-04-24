# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def crossdeviceexperiences_user_create_activity(client,
                                                user_id,
                                                id_=None,
                                                activation_url=None,
                                                activity_source_host=None,
                                                app_activity_id=None,
                                                app_display_name=None,
                                                content_info=None,
                                                content_url=None,
                                                created_date_time=None,
                                                expiration_date_time=None,
                                                fallback_url=None,
                                                last_modified_date_time=None,
                                                status=None,
                                                user_timezone=None,
                                                history_items=None,
                                                attribution=None,
                                                background_color=None,
                                                content=None,
                                                description=None,
                                                display_text=None):
    body = {}
    body['id'] = id_
    body['activation_url'] = activation_url
    body['activity_source_host'] = activity_source_host
    body['app_activity_id'] = app_activity_id
    body['app_display_name'] = app_display_name
    body['content_info'] = content_info
    body['content_url'] = content_url
    body['created_date_time'] = created_date_time
    body['expiration_date_time'] = expiration_date_time
    body['fallback_url'] = fallback_url
    body['last_modified_date_time'] = last_modified_date_time
    body['status'] = status
    body['user_timezone'] = user_timezone
    body['history_items'] = history_items
    body['visual_elements'] = {}
    body['visual_elements']['attribution'] = attribution
    body['visual_elements']['background_color'] = background_color
    body['visual_elements']['content'] = content
    body['visual_elements']['description'] = description
    body['visual_elements']['display_text'] = display_text
    return client.create_activities(user_id=user_id,
                                    body=body)


def crossdeviceexperiences_user_create_device(client,
                                              user_id,
                                              id_=None,
                                              deleted_date_time=None,
                                              account_enabled=None,
                                              alternative_security_ids=None,
                                              approximate_last_sign_in_date_time=None,
                                              compliance_expiration_date_time=None,
                                              device_category=None,
                                              device_id=None,
                                              device_metadata=None,
                                              device_ownership=None,
                                              device_version=None,
                                              display_name=None,
                                              domain_name=None,
                                              enrollment_profile_name=None,
                                              enrollment_type=None,
                                              extension_attributes=None,
                                              is_compliant=None,
                                              is_managed=None,
                                              is_rooted=None,
                                              management_type=None,
                                              on_premises_last_sync_date_time=None,
                                              on_premises_sync_enabled=None,
                                              operating_system=None,
                                              operating_system_version=None,
                                              physical_ids=None,
                                              profile_type=None,
                                              registration_date_time=None,
                                              system_labels=None,
                                              trust_type=None,
                                              kind=None,
                                              manufacturer=None,
                                              model=None,
                                              name=None,
                                              platform=None,
                                              status=None,
                                              member_of=None,
                                              registered_owners=None,
                                              registered_users=None,
                                              transitive_member_of=None,
                                              extensions=None,
                                              commands=None):
    body = {}
    body['id'] = id_
    body['deleted_date_time'] = deleted_date_time
    body['account_enabled'] = account_enabled
    body['alternative_security_ids'] = alternative_security_ids
    body['approximate_last_sign_in_date_time'] = approximate_last_sign_in_date_time
    body['compliance_expiration_date_time'] = compliance_expiration_date_time
    body['device_category'] = device_category
    body['device_id'] = device_id
    body['device_metadata'] = device_metadata
    body['device_ownership'] = device_ownership
    body['device_version'] = device_version
    body['display_name'] = display_name
    body['domain_name'] = domain_name
    body['enrollment_profile_name'] = enrollment_profile_name
    body['enrollment_type'] = enrollment_type
    body['extension_attributes'] = extension_attributes
    body['is_compliant'] = is_compliant
    body['is_managed'] = is_managed
    body['is_rooted'] = is_rooted
    body['management_type'] = management_type
    body['on_premises_last_sync_date_time'] = on_premises_last_sync_date_time
    body['on_premises_sync_enabled'] = on_premises_sync_enabled
    body['operating_system'] = operating_system
    body['operating_system_version'] = operating_system_version
    body['physical_ids'] = physical_ids
    body['profile_type'] = profile_type
    body['registration_date_time'] = registration_date_time
    body['system_labels'] = system_labels
    body['trust_type'] = trust_type
    body['kind'] = kind
    body['manufacturer'] = manufacturer
    body['model'] = model
    body['name'] = name
    body['platform'] = platform
    body['status'] = status
    body['member_of'] = member_of
    body['registered_owners'] = registered_owners
    body['registered_users'] = registered_users
    body['transitive_member_of'] = transitive_member_of
    body['extensions'] = extensions
    body['commands'] = commands
    return client.create_devices(user_id=user_id,
                                 body=body)


def crossdeviceexperiences_user_delete_activity(client,
                                                user_id,
                                                user_activity_id,
                                                if_match=None):
    return client.delete_activities(user_id=user_id,
                                    user_activity_id=user_activity_id,
                                    if_match=if_match)


def crossdeviceexperiences_user_delete_device(client,
                                              user_id,
                                              device_id,
                                              if_match=None):
    return client.delete_devices(user_id=user_id,
                                 device_id=device_id,
                                 if_match=if_match)


def crossdeviceexperiences_user_list_activity(client,
                                              user_id,
                                              orderby=None,
                                              select=None,
                                              expand=None):
    return client.list_activities(user_id=user_id,
                                  orderby=orderby,
                                  select=select,
                                  expand=expand)


def crossdeviceexperiences_user_list_device(client,
                                            user_id,
                                            orderby=None,
                                            select=None,
                                            expand=None):
    return client.list_devices(user_id=user_id,
                               orderby=orderby,
                               select=select,
                               expand=expand)


def crossdeviceexperiences_user_show_activity(client,
                                              user_id,
                                              user_activity_id,
                                              select=None,
                                              expand=None):
    return client.get_activities(user_id=user_id,
                                 user_activity_id=user_activity_id,
                                 select=select,
                                 expand=expand)


def crossdeviceexperiences_user_show_device(client,
                                            user_id,
                                            device_id,
                                            select=None,
                                            expand=None):
    return client.get_devices(user_id=user_id,
                              device_id=device_id,
                              select=select,
                              expand=expand)


def crossdeviceexperiences_user_update_activity(client,
                                                user_id,
                                                user_activity_id,
                                                id_=None,
                                                activation_url=None,
                                                activity_source_host=None,
                                                app_activity_id=None,
                                                app_display_name=None,
                                                content_info=None,
                                                content_url=None,
                                                created_date_time=None,
                                                expiration_date_time=None,
                                                fallback_url=None,
                                                last_modified_date_time=None,
                                                status=None,
                                                user_timezone=None,
                                                history_items=None,
                                                attribution=None,
                                                background_color=None,
                                                content=None,
                                                description=None,
                                                display_text=None):
    body = {}
    body['id'] = id_
    body['activation_url'] = activation_url
    body['activity_source_host'] = activity_source_host
    body['app_activity_id'] = app_activity_id
    body['app_display_name'] = app_display_name
    body['content_info'] = content_info
    body['content_url'] = content_url
    body['created_date_time'] = created_date_time
    body['expiration_date_time'] = expiration_date_time
    body['fallback_url'] = fallback_url
    body['last_modified_date_time'] = last_modified_date_time
    body['status'] = status
    body['user_timezone'] = user_timezone
    body['history_items'] = history_items
    body['visual_elements'] = {}
    body['visual_elements']['attribution'] = attribution
    body['visual_elements']['background_color'] = background_color
    body['visual_elements']['content'] = content
    body['visual_elements']['description'] = description
    body['visual_elements']['display_text'] = display_text
    return client.update_activities(user_id=user_id,
                                    user_activity_id=user_activity_id,
                                    body=body)


def crossdeviceexperiences_user_update_device(client,
                                              user_id,
                                              device_id,
                                              id_=None,
                                              deleted_date_time=None,
                                              account_enabled=None,
                                              alternative_security_ids=None,
                                              approximate_last_sign_in_date_time=None,
                                              compliance_expiration_date_time=None,
                                              device_category=None,
                                              microsoft_graph_device_id=None,
                                              device_metadata=None,
                                              device_ownership=None,
                                              device_version=None,
                                              display_name=None,
                                              domain_name=None,
                                              enrollment_profile_name=None,
                                              enrollment_type=None,
                                              extension_attributes=None,
                                              is_compliant=None,
                                              is_managed=None,
                                              is_rooted=None,
                                              management_type=None,
                                              on_premises_last_sync_date_time=None,
                                              on_premises_sync_enabled=None,
                                              operating_system=None,
                                              operating_system_version=None,
                                              physical_ids=None,
                                              profile_type=None,
                                              registration_date_time=None,
                                              system_labels=None,
                                              trust_type=None,
                                              kind=None,
                                              manufacturer=None,
                                              model=None,
                                              name=None,
                                              platform=None,
                                              status=None,
                                              member_of=None,
                                              registered_owners=None,
                                              registered_users=None,
                                              transitive_member_of=None,
                                              extensions=None,
                                              commands=None):
    body = {}
    body['id'] = id_
    body['deleted_date_time'] = deleted_date_time
    body['account_enabled'] = account_enabled
    body['alternative_security_ids'] = alternative_security_ids
    body['approximate_last_sign_in_date_time'] = approximate_last_sign_in_date_time
    body['compliance_expiration_date_time'] = compliance_expiration_date_time
    body['device_category'] = device_category
    body['device_id'] = microsoft_graph_device_id
    body['device_metadata'] = device_metadata
    body['device_ownership'] = device_ownership
    body['device_version'] = device_version
    body['display_name'] = display_name
    body['domain_name'] = domain_name
    body['enrollment_profile_name'] = enrollment_profile_name
    body['enrollment_type'] = enrollment_type
    body['extension_attributes'] = extension_attributes
    body['is_compliant'] = is_compliant
    body['is_managed'] = is_managed
    body['is_rooted'] = is_rooted
    body['management_type'] = management_type
    body['on_premises_last_sync_date_time'] = on_premises_last_sync_date_time
    body['on_premises_sync_enabled'] = on_premises_sync_enabled
    body['operating_system'] = operating_system
    body['operating_system_version'] = operating_system_version
    body['physical_ids'] = physical_ids
    body['profile_type'] = profile_type
    body['registration_date_time'] = registration_date_time
    body['system_labels'] = system_labels
    body['trust_type'] = trust_type
    body['kind'] = kind
    body['manufacturer'] = manufacturer
    body['model'] = model
    body['name'] = name
    body['platform'] = platform
    body['status'] = status
    body['member_of'] = member_of
    body['registered_owners'] = registered_owners
    body['registered_users'] = registered_users
    body['transitive_member_of'] = transitive_member_of
    body['extensions'] = extensions
    body['commands'] = commands
    return client.update_devices(user_id=user_id,
                                 device_id=device_id,
                                 body=body)


def crossdeviceexperiences_user_activity_create_history_item(client,
                                                             user_id,
                                                             user_activity_id,
                                                             id_=None,
                                                             active_duration_seconds=None,
                                                             created_date_time=None,
                                                             expiration_date_time=None,
                                                             last_active_date_time=None,
                                                             last_modified_date_time=None,
                                                             started_date_time=None,
                                                             status=None,
                                                             user_timezone=None,
                                                             activity=None):
    body = {}
    body['id'] = id_
    body['active_duration_seconds'] = active_duration_seconds
    body['created_date_time'] = created_date_time
    body['expiration_date_time'] = expiration_date_time
    body['last_active_date_time'] = last_active_date_time
    body['last_modified_date_time'] = last_modified_date_time
    body['started_date_time'] = started_date_time
    body['status'] = status
    body['user_timezone'] = user_timezone
    body['activity'] = activity
    return client.create_history_items(user_id=user_id,
                                       user_activity_id=user_activity_id,
                                       body=body)


def crossdeviceexperiences_user_activity_delete_history_item(client,
                                                             user_id,
                                                             user_activity_id,
                                                             activity_history_item_id,
                                                             if_match=None):
    return client.delete_history_items(user_id=user_id,
                                       user_activity_id=user_activity_id,
                                       activity_history_item_id=activity_history_item_id,
                                       if_match=if_match)


def crossdeviceexperiences_user_activity_list_history_item(client,
                                                           user_id,
                                                           user_activity_id,
                                                           orderby=None,
                                                           select=None,
                                                           expand=None):
    return client.list_history_items(user_id=user_id,
                                     user_activity_id=user_activity_id,
                                     orderby=orderby,
                                     select=select,
                                     expand=expand)


def crossdeviceexperiences_user_activity_show_history_item(client,
                                                           user_id,
                                                           user_activity_id,
                                                           activity_history_item_id,
                                                           select=None,
                                                           expand=None):
    return client.get_history_items(user_id=user_id,
                                    user_activity_id=user_activity_id,
                                    activity_history_item_id=activity_history_item_id,
                                    select=select,
                                    expand=expand)


def crossdeviceexperiences_user_activity_update_history_item(client,
                                                             user_id,
                                                             user_activity_id,
                                                             activity_history_item_id,
                                                             id_=None,
                                                             active_duration_seconds=None,
                                                             created_date_time=None,
                                                             expiration_date_time=None,
                                                             last_active_date_time=None,
                                                             last_modified_date_time=None,
                                                             started_date_time=None,
                                                             status=None,
                                                             user_timezone=None,
                                                             activity=None):
    body = {}
    body['id'] = id_
    body['active_duration_seconds'] = active_duration_seconds
    body['created_date_time'] = created_date_time
    body['expiration_date_time'] = expiration_date_time
    body['last_active_date_time'] = last_active_date_time
    body['last_modified_date_time'] = last_modified_date_time
    body['started_date_time'] = started_date_time
    body['status'] = status
    body['user_timezone'] = user_timezone
    body['activity'] = activity
    return client.update_history_items(user_id=user_id,
                                       user_activity_id=user_activity_id,
                                       activity_history_item_id=activity_history_item_id,
                                       body=body)


def crossdeviceexperiences_user_activity_history_item_delete_ref_activity(client,
                                                                          user_id,
                                                                          user_activity_id,
                                                                          activity_history_item_id,
                                                                          if_match=None):
    return client.delete_ref_activity(user_id=user_id,
                                      user_activity_id=user_activity_id,
                                      activity_history_item_id=activity_history_item_id,
                                      if_match=if_match)


def crossdeviceexperiences_user_activity_history_item_set_ref_activity(client,
                                                                       user_id,
                                                                       user_activity_id,
                                                                       activity_history_item_id,
                                                                       body):
    return client.set_ref_activity(user_id=user_id,
                                   user_activity_id=user_activity_id,
                                   activity_history_item_id=activity_history_item_id,
                                   body=body)


def crossdeviceexperiences_user_activity_history_item_show_activity(client,
                                                                    user_id,
                                                                    user_activity_id,
                                                                    activity_history_item_id,
                                                                    select=None,
                                                                    expand=None):
    return client.get_activity(user_id=user_id,
                               user_activity_id=user_activity_id,
                               activity_history_item_id=activity_history_item_id,
                               select=select,
                               expand=expand)


def crossdeviceexperiences_user_activity_history_item_show_ref_activity(client,
                                                                        user_id,
                                                                        user_activity_id,
                                                                        activity_history_item_id):
    return client.get_ref_activity(user_id=user_id,
                                   user_activity_id=user_activity_id,
                                   activity_history_item_id=activity_history_item_id)
