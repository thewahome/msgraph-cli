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


def people_user_create_person(client,
                              user_id,
                              id_=None,
                              birthday=None,
                              company_name=None,
                              department=None,
                              display_name=None,
                              given_name=None,
                              im_address=None,
                              is_favorite=None,
                              job_title=None,
                              office_location=None,
                              person_notes=None,
                              person_type=None,
                              phones=None,
                              postal_addresses=None,
                              profession=None,
                              scored_email_addresses=None,
                              surname=None,
                              user_principal_name=None,
                              websites=None,
                              yomi_company=None):
    body = {}
    body['id'] = id_
    body['birthday'] = birthday
    body['company_name'] = company_name
    body['department'] = department
    body['display_name'] = display_name
    body['given_name'] = given_name
    body['im_address'] = im_address
    body['is_favorite'] = is_favorite
    body['job_title'] = job_title
    body['office_location'] = office_location
    body['person_notes'] = person_notes
    body['person_type'] = person_type
    body['phones'] = phones
    body['postal_addresses'] = postal_addresses
    body['profession'] = profession
    body['scored_email_addresses'] = scored_email_addresses
    body['surname'] = surname
    body['user_principal_name'] = user_principal_name
    body['websites'] = websites
    body['yomi_company'] = yomi_company
    return client.create_people(user_id=user_id,
                                body=body)


def people_user_delete_insight(client,
                               user_id,
                               if_match=None):
    return client.delete_insights(user_id=user_id,
                                  if_match=if_match)


def people_user_delete_person(client,
                              user_id,
                              person_id,
                              if_match=None):
    return client.delete_people(user_id=user_id,
                                person_id=person_id,
                                if_match=if_match)


def people_user_list_person(client,
                            user_id,
                            orderby=None,
                            select=None,
                            expand=None):
    return client.list_people(user_id=user_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)


def people_user_show_insight(client,
                             user_id,
                             select=None,
                             expand=None):
    return client.get_insights(user_id=user_id,
                               select=select,
                               expand=expand)


def people_user_show_person(client,
                            user_id,
                            person_id,
                            select=None,
                            expand=None):
    return client.get_people(user_id=user_id,
                             person_id=person_id,
                             select=select,
                             expand=expand)


def people_user_update_insight(client,
                               user_id,
                               id_=None,
                               shared=None,
                               trending=None,
                               used=None):
    body = {}
    body['id'] = id_
    body['shared'] = shared
    body['trending'] = trending
    body['used'] = used
    return client.update_insights(user_id=user_id,
                                  body=body)


def people_user_update_person(client,
                              user_id,
                              person_id,
                              id_=None,
                              birthday=None,
                              company_name=None,
                              department=None,
                              display_name=None,
                              given_name=None,
                              im_address=None,
                              is_favorite=None,
                              job_title=None,
                              office_location=None,
                              person_notes=None,
                              person_type=None,
                              phones=None,
                              postal_addresses=None,
                              profession=None,
                              scored_email_addresses=None,
                              surname=None,
                              user_principal_name=None,
                              websites=None,
                              yomi_company=None):
    body = {}
    body['id'] = id_
    body['birthday'] = birthday
    body['company_name'] = company_name
    body['department'] = department
    body['display_name'] = display_name
    body['given_name'] = given_name
    body['im_address'] = im_address
    body['is_favorite'] = is_favorite
    body['job_title'] = job_title
    body['office_location'] = office_location
    body['person_notes'] = person_notes
    body['person_type'] = person_type
    body['phones'] = phones
    body['postal_addresses'] = postal_addresses
    body['profession'] = profession
    body['scored_email_addresses'] = scored_email_addresses
    body['surname'] = surname
    body['user_principal_name'] = user_principal_name
    body['websites'] = websites
    body['yomi_company'] = yomi_company
    return client.update_people(user_id=user_id,
                                person_id=person_id,
                                body=body)


def people_usersinsight_create_shared(client,
                                      user_id,
                                      id_=None,
                                      resource_reference=None,
                                      resource_visualization=None,
                                      sharing_history=None,
                                      microsoft_graph_entity_id=None,
                                      id1=None,
                                      shared_by=None,
                                      shared_date_time=None,
                                      sharing_reference=None,
                                      sharing_subject=None,
                                      sharing_type=None):
    body = {}
    body['id'] = id_
    body['resource_reference'] = resource_reference
    body['resource_visualization'] = resource_visualization
    body['sharing_history'] = sharing_history
    body['resource'] = {}
    body['resource']['id'] = microsoft_graph_entity_id
    body['last_shared_method'] = {}
    body['last_shared_method']['id'] = id1
    body['last_shared'] = {}
    body['last_shared']['shared_by'] = shared_by
    body['last_shared']['shared_date_time'] = shared_date_time
    body['last_shared']['sharing_reference'] = sharing_reference
    body['last_shared']['sharing_subject'] = sharing_subject
    body['last_shared']['sharing_type'] = sharing_type
    return client.create_shared(user_id=user_id,
                                body=body)


def people_usersinsight_create_trending(client,
                                        user_id,
                                        id_=None,
                                        last_modified_date_time=None,
                                        resource_reference=None,
                                        resource_visualization=None,
                                        weight=None,
                                        microsoft_graph_entity_id=None):
    body = {}
    body['id'] = id_
    body['last_modified_date_time'] = last_modified_date_time
    body['resource_reference'] = resource_reference
    body['resource_visualization'] = resource_visualization
    body['weight'] = weight
    body['resource'] = {}
    body['resource']['id'] = microsoft_graph_entity_id
    return client.create_trending(user_id=user_id,
                                  body=body)


def people_usersinsight_create_used(client,
                                    user_id,
                                    id_=None,
                                    last_used=None,
                                    resource_reference=None,
                                    resource_visualization=None,
                                    microsoft_graph_entity_id=None):
    body = {}
    body['id'] = id_
    body['last_used'] = last_used
    body['resource_reference'] = resource_reference
    body['resource_visualization'] = resource_visualization
    body['resource'] = {}
    body['resource']['id'] = microsoft_graph_entity_id
    return client.create_used(user_id=user_id,
                              body=body)


def people_usersinsight_delete_shared(client,
                                      user_id,
                                      shared_insight_id,
                                      if_match=None):
    return client.delete_shared(user_id=user_id,
                                shared_insight_id=shared_insight_id,
                                if_match=if_match)


def people_usersinsight_delete_trending(client,
                                        user_id,
                                        trending_id,
                                        if_match=None):
    return client.delete_trending(user_id=user_id,
                                  trending_id=trending_id,
                                  if_match=if_match)


def people_usersinsight_delete_used(client,
                                    user_id,
                                    used_insight_id,
                                    if_match=None):
    return client.delete_used(user_id=user_id,
                              used_insight_id=used_insight_id,
                              if_match=if_match)


def people_usersinsight_list_shared(client,
                                    user_id,
                                    orderby=None,
                                    select=None,
                                    expand=None):
    return client.list_shared(user_id=user_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)


def people_usersinsight_list_trending(client,
                                      user_id,
                                      orderby=None,
                                      select=None,
                                      expand=None):
    return client.list_trending(user_id=user_id,
                                orderby=orderby,
                                select=select,
                                expand=expand)


def people_usersinsight_list_used(client,
                                  user_id,
                                  orderby=None,
                                  select=None,
                                  expand=None):
    return client.list_used(user_id=user_id,
                            orderby=orderby,
                            select=select,
                            expand=expand)


def people_usersinsight_show_shared(client,
                                    user_id,
                                    shared_insight_id,
                                    select=None,
                                    expand=None):
    return client.get_shared(user_id=user_id,
                             shared_insight_id=shared_insight_id,
                             select=select,
                             expand=expand)


def people_usersinsight_show_trending(client,
                                      user_id,
                                      trending_id,
                                      select=None,
                                      expand=None):
    return client.get_trending(user_id=user_id,
                               trending_id=trending_id,
                               select=select,
                               expand=expand)


def people_usersinsight_show_used(client,
                                  user_id,
                                  used_insight_id,
                                  select=None,
                                  expand=None):
    return client.get_used(user_id=user_id,
                           used_insight_id=used_insight_id,
                           select=select,
                           expand=expand)


def people_usersinsight_update_shared(client,
                                      user_id,
                                      shared_insight_id,
                                      id_=None,
                                      resource_reference=None,
                                      resource_visualization=None,
                                      sharing_history=None,
                                      microsoft_graph_entity_id=None,
                                      id1=None,
                                      shared_by=None,
                                      shared_date_time=None,
                                      sharing_reference=None,
                                      sharing_subject=None,
                                      sharing_type=None):
    body = {}
    body['id'] = id_
    body['resource_reference'] = resource_reference
    body['resource_visualization'] = resource_visualization
    body['sharing_history'] = sharing_history
    body['resource'] = {}
    body['resource']['id'] = microsoft_graph_entity_id
    body['last_shared_method'] = {}
    body['last_shared_method']['id'] = id1
    body['last_shared'] = {}
    body['last_shared']['shared_by'] = shared_by
    body['last_shared']['shared_date_time'] = shared_date_time
    body['last_shared']['sharing_reference'] = sharing_reference
    body['last_shared']['sharing_subject'] = sharing_subject
    body['last_shared']['sharing_type'] = sharing_type
    return client.update_shared(user_id=user_id,
                                shared_insight_id=shared_insight_id,
                                body=body)


def people_usersinsight_update_trending(client,
                                        user_id,
                                        trending_id,
                                        id_=None,
                                        last_modified_date_time=None,
                                        resource_reference=None,
                                        resource_visualization=None,
                                        weight=None,
                                        microsoft_graph_entity_id=None):
    body = {}
    body['id'] = id_
    body['last_modified_date_time'] = last_modified_date_time
    body['resource_reference'] = resource_reference
    body['resource_visualization'] = resource_visualization
    body['weight'] = weight
    body['resource'] = {}
    body['resource']['id'] = microsoft_graph_entity_id
    return client.update_trending(user_id=user_id,
                                  trending_id=trending_id,
                                  body=body)


def people_usersinsight_update_used(client,
                                    user_id,
                                    used_insight_id,
                                    id_=None,
                                    last_used=None,
                                    resource_reference=None,
                                    resource_visualization=None,
                                    microsoft_graph_entity_id=None):
    body = {}
    body['id'] = id_
    body['last_used'] = last_used
    body['resource_reference'] = resource_reference
    body['resource_visualization'] = resource_visualization
    body['resource'] = {}
    body['resource']['id'] = microsoft_graph_entity_id
    return client.update_used(user_id=user_id,
                              used_insight_id=used_insight_id,
                              body=body)


def people_usersinsightsshared_delete_ref_last_shared_method(client,
                                                             user_id,
                                                             shared_insight_id,
                                                             if_match=None):
    return client.delete_ref_last_shared_method(user_id=user_id,
                                                shared_insight_id=shared_insight_id,
                                                if_match=if_match)


def people_usersinsightsshared_delete_ref_resource(client,
                                                   user_id,
                                                   shared_insight_id,
                                                   if_match=None):
    return client.delete_ref_resource(user_id=user_id,
                                      shared_insight_id=shared_insight_id,
                                      if_match=if_match)


def people_usersinsightsshared_set_ref_last_shared_method(client,
                                                          user_id,
                                                          shared_insight_id,
                                                          body):
    return client.set_ref_last_shared_method(user_id=user_id,
                                             shared_insight_id=shared_insight_id,
                                             body=body)


def people_usersinsightsshared_set_ref_resource(client,
                                                user_id,
                                                shared_insight_id,
                                                body):
    return client.set_ref_resource(user_id=user_id,
                                   shared_insight_id=shared_insight_id,
                                   body=body)


def people_usersinsightsshared_show_last_shared_method(client,
                                                       user_id,
                                                       shared_insight_id,
                                                       select=None,
                                                       expand=None):
    return client.get_last_shared_method(user_id=user_id,
                                         shared_insight_id=shared_insight_id,
                                         select=select,
                                         expand=expand)


def people_usersinsightsshared_show_ref_last_shared_method(client,
                                                           user_id,
                                                           shared_insight_id):
    return client.get_ref_last_shared_method(user_id=user_id,
                                             shared_insight_id=shared_insight_id)


def people_usersinsightsshared_show_ref_resource(client,
                                                 user_id,
                                                 shared_insight_id):
    return client.get_ref_resource(user_id=user_id,
                                   shared_insight_id=shared_insight_id)


def people_usersinsightsshared_show_resource(client,
                                             user_id,
                                             shared_insight_id,
                                             select=None,
                                             expand=None):
    return client.get_resource(user_id=user_id,
                               shared_insight_id=shared_insight_id,
                               select=select,
                               expand=expand)


def people_usersinsightstrending_delete_ref_resource(client,
                                                     user_id,
                                                     trending_id,
                                                     if_match=None):
    return client.delete_ref_resource(user_id=user_id,
                                      trending_id=trending_id,
                                      if_match=if_match)


def people_usersinsightstrending_set_ref_resource(client,
                                                  user_id,
                                                  trending_id,
                                                  body):
    return client.set_ref_resource(user_id=user_id,
                                   trending_id=trending_id,
                                   body=body)


def people_usersinsightstrending_show_ref_resource(client,
                                                   user_id,
                                                   trending_id):
    return client.get_ref_resource(user_id=user_id,
                                   trending_id=trending_id)


def people_usersinsightstrending_show_resource(client,
                                               user_id,
                                               trending_id,
                                               select=None,
                                               expand=None):
    return client.get_resource(user_id=user_id,
                               trending_id=trending_id,
                               select=select,
                               expand=expand)


def people_usersinsightsused_delete_ref_resource(client,
                                                 user_id,
                                                 used_insight_id,
                                                 if_match=None):
    return client.delete_ref_resource(user_id=user_id,
                                      used_insight_id=used_insight_id,
                                      if_match=if_match)


def people_usersinsightsused_set_ref_resource(client,
                                              user_id,
                                              used_insight_id,
                                              body):
    return client.set_ref_resource(user_id=user_id,
                                   used_insight_id=used_insight_id,
                                   body=body)


def people_usersinsightsused_show_ref_resource(client,
                                               user_id,
                                               used_insight_id):
    return client.get_ref_resource(user_id=user_id,
                                   used_insight_id=used_insight_id)


def people_usersinsightsused_show_resource(client,
                                           user_id,
                                           used_insight_id,
                                           select=None,
                                           expand=None):
    return client.get_resource(user_id=user_id,
                               used_insight_id=used_insight_id,
                               select=select,
                               expand=expand)
