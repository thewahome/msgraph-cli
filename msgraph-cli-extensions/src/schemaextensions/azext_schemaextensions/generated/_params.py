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

from azext_schemaextensions.action import AddProperties


def load_arguments(self, _):

    with self.argument_context('schemaextensions delete') as c:
        c.argument('schema_extension_id', type=str, help='key: id of schemaExtension')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('schemaextensions create-schema-extension') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('description', type=str, help='Description for the schema extension.')
        c.argument('owner', type=str, help='The appId of the application that is the owner of the schema extension. '
                   'This property can be supplied on creation, to set the owner.  If not supplied, then the calling '
                   'application\'s appId will be set as the owner. In either case, the signed-in user must be the '
                   'owner of the application. Once set, this property is read-only and cannot be changed.')
        c.argument('properties', action=AddProperties, nargs='*', help='The collection of property names and types '
                   'that make up the schema extension definition.')
        c.argument('status', type=str, help='The lifecycle state of the schema extension. Possible states are '
                   'InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. Schema '
                   'extensions provides more information on the possible state transitions and behaviors.')
        c.argument('target_types', nargs='*', help='Set of Microsoft Graph types (that can support extensions) that '
                   'the schema extension can be applied to. Select from contact, device, event, group, message, '
                   'organization, post, or user.')

    with self.argument_context('schemaextensions get-schema-extension') as c:
        c.argument('schema_extension_id', type=str, help='key: id of schemaExtension')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('schemaextensions list-schema-extension') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('schemaextensions update-schema-extension') as c:
        c.argument('schema_extension_id', type=str, help='key: id of schemaExtension')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('description', type=str, help='Description for the schema extension.')
        c.argument('owner', type=str, help='The appId of the application that is the owner of the schema extension. '
                   'This property can be supplied on creation, to set the owner.  If not supplied, then the calling '
                   'application\'s appId will be set as the owner. In either case, the signed-in user must be the '
                   'owner of the application. Once set, this property is read-only and cannot be changed.')
        c.argument('properties', action=AddProperties, nargs='*', help='The collection of property names and types '
                   'that make up the schema extension definition.')
        c.argument('status', type=str, help='The lifecycle state of the schema extension. Possible states are '
                   'InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. Schema '
                   'extensions provides more information on the possible state transitions and behaviors.')
        c.argument('target_types', nargs='*', help='Set of Microsoft Graph types (that can support extensions) that '
                   'the schema extension can be applied to. Select from contact, device, event, group, message, '
                   'organization, post, or user.')
