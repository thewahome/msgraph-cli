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


def directoryobjects_directoryobjectsdirectoryobject_create_directory_object(client,
                                                                             id_=None,
                                                                             deleted_date_time=None):
    body = {}
    body['id'] = id_
    body['deleted_date_time'] = deleted_date_time
    return client.create_directory_object(body=body)


def directoryobjects_directoryobjectsdirectoryobject_delete_directory_object(client,
                                                                             directory_object_id,
                                                                             if_match=None):
    return client.delete_directory_object(directory_object_id=directory_object_id,
                                          if_match=if_match)


def directoryobjects_directoryobjectsdirectoryobject_list_directory_object(client,
                                                                           orderby=None,
                                                                           select=None,
                                                                           expand=None):
    return client.list_directory_object(orderby=orderby,
                                        select=select,
                                        expand=expand)


def directoryobjects_directoryobjectsdirectoryobject_show_directory_object(client,
                                                                           directory_object_id,
                                                                           select=None,
                                                                           expand=None):
    return client.get_directory_object(directory_object_id=directory_object_id,
                                       select=select,
                                       expand=expand)


def directoryobjects_directoryobjectsdirectoryobject_update_directory_object(client,
                                                                             directory_object_id,
                                                                             id_=None,
                                                                             deleted_date_time=None):
    body = {}
    body['id'] = id_
    body['deleted_date_time'] = deleted_date_time
    return client.update_directory_object(directory_object_id=directory_object_id,
                                          body=body)


def directoryobjects_directoryobject_check_member_group(client,
                                                        directory_object_id,
                                                        group_ids=None):
    body = {}
    body['group_ids'] = group_ids
    return client.check_member_groups(directory_object_id=directory_object_id,
                                      body=body)


def directoryobjects_directoryobject_check_member_object(client,
                                                         directory_object_id,
                                                         ids=None):
    body = {}
    body['ids'] = ids
    return client.check_member_objects(directory_object_id=directory_object_id,
                                       body=body)


def directoryobjects_directoryobject_get_available_extension_property(client,
                                                                      is_synced_from_on_premises=None):
    if is_synced_from_on_premises is None:
        is_synced_from_on_premises = False
    body = {}
    body['is_synced_from_on_premises'] = False if is_synced_from_on_premises is None else is_synced_from_on_premises
    return client.get_available_extension_properties(body=body)


def directoryobjects_directoryobject_get_by_id(client,
                                               ids=None,
                                               types=None):
    body = {}
    body['ids'] = ids
    body['types'] = types
    return client.get_by_ids(body=body)


def directoryobjects_directoryobject_get_member_group(client,
                                                      directory_object_id,
                                                      security_enabled_only=None):
    if security_enabled_only is None:
        security_enabled_only = False
    body = {}
    body['security_enabled_only'] = False if security_enabled_only is None else security_enabled_only
    return client.get_member_groups(directory_object_id=directory_object_id,
                                    body=body)


def directoryobjects_directoryobject_get_member_object(client,
                                                       directory_object_id,
                                                       security_enabled_only=None):
    if security_enabled_only is None:
        security_enabled_only = False
    body = {}
    body['security_enabled_only'] = False if security_enabled_only is None else security_enabled_only
    return client.get_member_objects(directory_object_id=directory_object_id,
                                     body=body)


def directoryobjects_directoryobject_restore(client,
                                             directory_object_id):
    return client.restore(directory_object_id=directory_object_id)


def directoryobjects_directoryobject_validate_property(client,
                                                       entity_type=None,
                                                       display_name=None,
                                                       mail_nickname=None,
                                                       on_behalf_of_user_id=None):
    body = {}
    body['entity_type'] = entity_type
    body['display_name'] = display_name
    body['mail_nickname'] = mail_nickname
    body['on_behalf_of_user_id'] = on_behalf_of_user_id
    return client.validate_properties(body=body)
