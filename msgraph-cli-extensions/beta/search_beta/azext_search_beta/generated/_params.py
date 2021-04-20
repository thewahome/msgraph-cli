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
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_enum_type
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_search_beta.action import (
    AddConfiguration,
    AddProperties
)


def load_arguments(self, _):

    with self.argument_context('search external show-external') as c:
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('search external update-external') as c:
        c.argument('connections', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')

    with self.argument_context('search external create-connection') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('configuration', action=AddConfiguration, nargs='+', help='configuration')
        c.argument('description', type=str, help='')
        c.argument('name', type=str, help='')
        c.argument('state', arg_type=get_enum_type(['draft', 'ready', 'obsolete', 'limitExceeded',
                                                    'unknownFutureValue']), help='')
        c.argument('groups', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('items', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('operations', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('microsoft_graph_entity_id', type=str, help='Read-only.', arg_group='Schema')
        c.argument('base_type', type=str, help='', arg_group='Schema')
        c.argument('properties', action=AddProperties, nargs='+', help='', arg_group='Schema')

    with self.argument_context('search external delete-connection') as c:
        c.argument('external_connection_id', type=str, help='key: id of externalConnection')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('search external list-connection') as c:
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('search external show-connection') as c:
        c.argument('external_connection_id', type=str, help='key: id of externalConnection')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('search external update-connection') as c:
        c.argument('external_connection_id', type=str, help='key: id of externalConnection')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('configuration', action=AddConfiguration, nargs='+', help='configuration')
        c.argument('description', type=str, help='')
        c.argument('name', type=str, help='')
        c.argument('state', arg_type=get_enum_type(['draft', 'ready', 'obsolete', 'limitExceeded',
                                                    'unknownFutureValue']), help='')
        c.argument('groups', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('items', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('operations', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('microsoft_graph_entity_id', type=str, help='Read-only.', arg_group='Schema')
        c.argument('base_type', type=str, help='', arg_group='Schema')
        c.argument('properties', action=AddProperties, nargs='+', help='', arg_group='Schema')

    with self.argument_context('search searchentity show-search-entity') as c:
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('search searchentity update-search-entity') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')

    with self.argument_context('search search query') as c:
        c.argument('requests', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
