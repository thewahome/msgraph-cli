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


def education_educationroot_show_education_root(client,
                                                select=None,
                                                expand=None):
    return client.get_education_root(select=select,
                                     expand=expand)


def education_educationroot_update_education_root(client,
                                                  id_=None,
                                                  classes=None,
                                                  me=None,
                                                  schools=None,
                                                  users=None):
    body = {}
    body['id'] = id_
    body['classes'] = classes
    body['me'] = me
    body['schools'] = schools
    body['users'] = users
    return client.update_education_root(body=body)


def education_education_create_class(client,
                                     id_=None,
                                     class_code=None,
                                     description=None,
                                     display_name=None,
                                     external_id=None,
                                     external_name=None,
                                     external_source=None,
                                     mail_nickname=None,
                                     term=None,
                                     group=None,
                                     members=None,
                                     schools=None,
                                     teachers=None,
                                     application=None,
                                     device=None,
                                     user=None):
    body = {}
    body['id'] = id_
    body['class_code'] = class_code
    body['description'] = description
    body['display_name'] = display_name
    body['external_id'] = external_id
    body['external_name'] = external_name
    body['external_source'] = external_source
    body['mail_nickname'] = mail_nickname
    body['term'] = term
    body['group'] = group
    body['members'] = members
    body['schools'] = schools
    body['teachers'] = teachers
    body['created_by'] = {}
    body['created_by']['application'] = application
    body['created_by']['device'] = device
    body['created_by']['user'] = user
    return client.create_classes(body=body)


def education_education_create_school(client,
                                      id_=None,
                                      description=None,
                                      display_name=None,
                                      external_source=None,
                                      address=None,
                                      external_id=None,
                                      external_principal_id=None,
                                      fax=None,
                                      highest_grade=None,
                                      lowest_grade=None,
                                      phone=None,
                                      principal_email=None,
                                      principal_name=None,
                                      school_number=None,
                                      classes=None,
                                      users=None,
                                      application=None,
                                      device=None,
                                      user=None):
    body = {}
    body['id'] = id_
    body['description'] = description
    body['display_name'] = display_name
    body['external_source'] = external_source
    body['address'] = address
    body['external_id'] = external_id
    body['external_principal_id'] = external_principal_id
    body['fax'] = fax
    body['highest_grade'] = highest_grade
    body['lowest_grade'] = lowest_grade
    body['phone'] = phone
    body['principal_email'] = principal_email
    body['principal_name'] = principal_name
    body['school_number'] = school_number
    body['classes'] = classes
    body['users'] = users
    body['created_by'] = {}
    body['created_by']['application'] = application
    body['created_by']['device'] = device
    body['created_by']['user'] = user
    return client.create_schools(body=body)


def education_education_create_user(client,
                                    body):
    return client.create_users(body=body)


def education_education_delete_class(client,
                                     education_class_id,
                                     if_match=None):
    return client.delete_classes(education_class_id=education_class_id,
                                 if_match=if_match)


def education_education_delete_me(client,
                                  if_match=None):
    return client.delete_me(if_match=if_match)


def education_education_delete_school(client,
                                      education_school_id,
                                      if_match=None):
    return client.delete_schools(education_school_id=education_school_id,
                                 if_match=if_match)


def education_education_delete_user(client,
                                    education_user_id,
                                    if_match=None):
    return client.delete_users(education_user_id=education_user_id,
                               if_match=if_match)


def education_education_list_class(client,
                                   orderby=None,
                                   select=None,
                                   expand=None):
    return client.list_classes(orderby=orderby,
                               select=select,
                               expand=expand)


def education_education_list_school(client,
                                    orderby=None,
                                    select=None,
                                    expand=None):
    return client.list_schools(orderby=orderby,
                               select=select,
                               expand=expand)


def education_education_list_user(client,
                                  orderby=None,
                                  select=None,
                                  expand=None):
    return client.list_users(orderby=orderby,
                             select=select,
                             expand=expand)


def education_education_show_class(client,
                                   education_class_id,
                                   select=None,
                                   expand=None):
    return client.get_classes(education_class_id=education_class_id,
                              select=select,
                              expand=expand)


def education_education_show_me(client,
                                select=None,
                                expand=None):
    return client.get_me(select=select,
                         expand=expand)


def education_education_show_school(client,
                                    education_school_id,
                                    select=None,
                                    expand=None):
    return client.get_schools(education_school_id=education_school_id,
                              select=select,
                              expand=expand)


def education_education_show_user(client,
                                  education_user_id,
                                  select=None,
                                  expand=None):
    return client.get_users(education_user_id=education_user_id,
                            select=select,
                            expand=expand)


def education_education_update_class(client,
                                     education_class_id,
                                     id_=None,
                                     class_code=None,
                                     description=None,
                                     display_name=None,
                                     external_id=None,
                                     external_name=None,
                                     external_source=None,
                                     mail_nickname=None,
                                     term=None,
                                     group=None,
                                     members=None,
                                     schools=None,
                                     teachers=None,
                                     application=None,
                                     device=None,
                                     user=None):
    body = {}
    body['id'] = id_
    body['class_code'] = class_code
    body['description'] = description
    body['display_name'] = display_name
    body['external_id'] = external_id
    body['external_name'] = external_name
    body['external_source'] = external_source
    body['mail_nickname'] = mail_nickname
    body['term'] = term
    body['group'] = group
    body['members'] = members
    body['schools'] = schools
    body['teachers'] = teachers
    body['created_by'] = {}
    body['created_by']['application'] = application
    body['created_by']['device'] = device
    body['created_by']['user'] = user
    return client.update_classes(education_class_id=education_class_id,
                                 body=body)


def education_education_update_me(client,
                                  body):
    return client.update_me(body=body)


def education_education_update_school(client,
                                      education_school_id,
                                      id_=None,
                                      description=None,
                                      display_name=None,
                                      external_source=None,
                                      address=None,
                                      external_id=None,
                                      external_principal_id=None,
                                      fax=None,
                                      highest_grade=None,
                                      lowest_grade=None,
                                      phone=None,
                                      principal_email=None,
                                      principal_name=None,
                                      school_number=None,
                                      classes=None,
                                      users=None,
                                      application=None,
                                      device=None,
                                      user=None):
    body = {}
    body['id'] = id_
    body['description'] = description
    body['display_name'] = display_name
    body['external_source'] = external_source
    body['address'] = address
    body['external_id'] = external_id
    body['external_principal_id'] = external_principal_id
    body['fax'] = fax
    body['highest_grade'] = highest_grade
    body['lowest_grade'] = lowest_grade
    body['phone'] = phone
    body['principal_email'] = principal_email
    body['principal_name'] = principal_name
    body['school_number'] = school_number
    body['classes'] = classes
    body['users'] = users
    body['created_by'] = {}
    body['created_by']['application'] = application
    body['created_by']['device'] = device
    body['created_by']['user'] = user
    return client.update_schools(education_school_id=education_school_id,
                                 body=body)


def education_education_update_user(client,
                                    education_user_id,
                                    body):
    return client.update_users(education_user_id=education_user_id,
                               body=body)


def education_educationclass_create_ref_member(client,
                                               education_class_id,
                                               body):
    return client.create_ref_members(education_class_id=education_class_id,
                                     body=body)


def education_educationclass_create_ref_school(client,
                                               education_class_id,
                                               body):
    return client.create_ref_schools(education_class_id=education_class_id,
                                     body=body)


def education_educationclass_create_ref_teacher(client,
                                                education_class_id,
                                                body):
    return client.create_ref_teachers(education_class_id=education_class_id,
                                      body=body)


def education_educationclass_delete_ref_group(client,
                                              education_class_id,
                                              if_match=None):
    return client.delete_ref_group(education_class_id=education_class_id,
                                   if_match=if_match)


def education_educationclass_list_member(client,
                                         education_class_id,
                                         orderby=None,
                                         select=None,
                                         expand=None):
    return client.list_members(education_class_id=education_class_id,
                               orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationclass_list_ref_member(client,
                                             education_class_id,
                                             orderby=None):
    return client.list_ref_members(education_class_id=education_class_id,
                                   orderby=orderby)


def education_educationclass_list_ref_school(client,
                                             education_class_id,
                                             orderby=None):
    return client.list_ref_schools(education_class_id=education_class_id,
                                   orderby=orderby)


def education_educationclass_list_ref_teacher(client,
                                              education_class_id,
                                              orderby=None):
    return client.list_ref_teachers(education_class_id=education_class_id,
                                    orderby=orderby)


def education_educationclass_list_school(client,
                                         education_class_id,
                                         orderby=None,
                                         select=None,
                                         expand=None):
    return client.list_schools(education_class_id=education_class_id,
                               orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationclass_list_teacher(client,
                                          education_class_id,
                                          orderby=None,
                                          select=None,
                                          expand=None):
    return client.list_teachers(education_class_id=education_class_id,
                                orderby=orderby,
                                select=select,
                                expand=expand)


def education_educationclass_set_ref_group(client,
                                           education_class_id,
                                           body):
    return client.set_ref_group(education_class_id=education_class_id,
                                body=body)


def education_educationclass_show_group(client,
                                        education_class_id,
                                        select=None,
                                        expand=None):
    return client.get_group(education_class_id=education_class_id,
                            select=select,
                            expand=expand)


def education_educationclass_show_ref_group(client,
                                            education_class_id):
    return client.get_ref_group(education_class_id=education_class_id)


def education_educationme_create_ref_class(client,
                                           body):
    return client.create_ref_classes(body=body)


def education_educationme_create_ref_school(client,
                                            body):
    return client.create_ref_schools(body=body)


def education_educationme_delete_ref_user(client,
                                          if_match=None):
    return client.delete_ref_user(if_match=if_match)


def education_educationme_list_class(client,
                                     orderby=None,
                                     select=None,
                                     expand=None):
    return client.list_classes(orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationme_list_ref_class(client,
                                         orderby=None):
    return client.list_ref_classes(orderby=orderby)


def education_educationme_list_ref_school(client,
                                          orderby=None):
    return client.list_ref_schools(orderby=orderby)


def education_educationme_list_school(client,
                                      orderby=None,
                                      select=None,
                                      expand=None):
    return client.list_schools(orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationme_set_ref_user(client,
                                       body):
    return client.set_ref_user(body=body)


def education_educationme_show_ref_user(client):
    return client.get_ref_user()


def education_educationme_show_user(client,
                                    select=None,
                                    expand=None):
    return client.get_user(select=select,
                           expand=expand)


def education_educationschool_create_ref_class(client,
                                               education_school_id,
                                               body):
    return client.create_ref_classes(education_school_id=education_school_id,
                                     body=body)


def education_educationschool_create_ref_user(client,
                                              education_school_id,
                                              body):
    return client.create_ref_users(education_school_id=education_school_id,
                                   body=body)


def education_educationschool_list_class(client,
                                         education_school_id,
                                         orderby=None,
                                         select=None,
                                         expand=None):
    return client.list_classes(education_school_id=education_school_id,
                               orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationschool_list_ref_class(client,
                                             education_school_id,
                                             orderby=None):
    return client.list_ref_classes(education_school_id=education_school_id,
                                   orderby=orderby)


def education_educationschool_list_ref_user(client,
                                            education_school_id,
                                            orderby=None):
    return client.list_ref_users(education_school_id=education_school_id,
                                 orderby=orderby)


def education_educationschool_list_user(client,
                                        education_school_id,
                                        orderby=None,
                                        select=None,
                                        expand=None):
    return client.list_users(education_school_id=education_school_id,
                             orderby=orderby,
                             select=select,
                             expand=expand)


def education_educationuser_create_ref_class(client,
                                             education_user_id,
                                             body):
    return client.create_ref_classes(education_user_id=education_user_id,
                                     body=body)


def education_educationuser_create_ref_school(client,
                                              education_user_id,
                                              body):
    return client.create_ref_schools(education_user_id=education_user_id,
                                     body=body)


def education_educationuser_delete_ref_user(client,
                                            education_user_id,
                                            if_match=None):
    return client.delete_ref_user(education_user_id=education_user_id,
                                  if_match=if_match)


def education_educationuser_list_class(client,
                                       education_user_id,
                                       orderby=None,
                                       select=None,
                                       expand=None):
    return client.list_classes(education_user_id=education_user_id,
                               orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationuser_list_ref_class(client,
                                           education_user_id,
                                           orderby=None):
    return client.list_ref_classes(education_user_id=education_user_id,
                                   orderby=orderby)


def education_educationuser_list_ref_school(client,
                                            education_user_id,
                                            orderby=None):
    return client.list_ref_schools(education_user_id=education_user_id,
                                   orderby=orderby)


def education_educationuser_list_school(client,
                                        education_user_id,
                                        orderby=None,
                                        select=None,
                                        expand=None):
    return client.list_schools(education_user_id=education_user_id,
                               orderby=orderby,
                               select=select,
                               expand=expand)


def education_educationuser_set_ref_user(client,
                                         education_user_id,
                                         body):
    return client.set_ref_user(education_user_id=education_user_id,
                               body=body)


def education_educationuser_show_ref_user(client,
                                          education_user_id):
    return client.get_ref_user(education_user_id=education_user_id)


def education_educationuser_show_user(client,
                                      education_user_id,
                                      select=None,
                                      expand=None):
    return client.get_user(education_user_id=education_user_id,
                           select=select,
                           expand=expand)
