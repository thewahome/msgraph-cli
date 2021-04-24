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


def search_external_external_show_external(client,
                                           select=None,
                                           expand=None):
    return client.get_external(select=select,
                               expand=expand)


def search_external_external_update_external(client,
                                             connections=None):
    body = {}
    body['connections'] = connections
    return client.update_external(body=body)


def search_external_create_connection(client,
                                      id_=None,
                                      configuration=None,
                                      description=None,
                                      name=None,
                                      state=None,
                                      groups=None,
                                      items=None,
                                      operations=None,
                                      microsoft_graph_entity_id=None,
                                      base_type=None,
                                      properties=None):
    body = {}
    body['id'] = id_
    body['configuration'] = configuration
    body['description'] = description
    body['name'] = name
    body['state'] = state
    body['groups'] = groups
    body['items'] = items
    body['operations'] = operations
    body['schema'] = {}
    body['schema']['id'] = microsoft_graph_entity_id
    body['schema']['base_type'] = base_type
    body['schema']['properties'] = properties
    return client.create_connections(body=body)


def search_external_delete_connection(client,
                                      external_connection_id,
                                      if_match=None):
    return client.delete_connections(external_connection_id=external_connection_id,
                                     if_match=if_match)


def search_external_list_connection(client,
                                    orderby=None,
                                    select=None,
                                    expand=None):
    return client.list_connections(orderby=orderby,
                                   select=select,
                                   expand=expand)


def search_external_show_connection(client,
                                    external_connection_id,
                                    select=None,
                                    expand=None):
    return client.get_connections(external_connection_id=external_connection_id,
                                  select=select,
                                  expand=expand)


def search_external_update_connection(client,
                                      external_connection_id,
                                      id_=None,
                                      configuration=None,
                                      description=None,
                                      name=None,
                                      state=None,
                                      groups=None,
                                      items=None,
                                      operations=None,
                                      microsoft_graph_entity_id=None,
                                      base_type=None,
                                      properties=None):
    body = {}
    body['id'] = id_
    body['configuration'] = configuration
    body['description'] = description
    body['name'] = name
    body['state'] = state
    body['groups'] = groups
    body['items'] = items
    body['operations'] = operations
    body['schema'] = {}
    body['schema']['id'] = microsoft_graph_entity_id
    body['schema']['base_type'] = base_type
    body['schema']['properties'] = properties
    return client.update_connections(external_connection_id=external_connection_id,
                                     body=body)


def search_search_entity_show_search_entity(client,
                                            select=None,
                                            expand=None):
    return client.get_search_entity(select=select,
                                    expand=expand)


def search_search_entity_update_search_entity(client,
                                              id_=None):
    body = {}
    body['id'] = id_
    return client.update_search_entity(body=body)


def search_search_query(client,
                        requests=None):
    body = {}
    body['requests'] = requests
    return client.query(body=body)
