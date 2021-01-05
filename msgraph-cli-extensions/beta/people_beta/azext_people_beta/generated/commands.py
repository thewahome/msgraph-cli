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

    from azext_people_beta.generated._client_factory import cf_user
    people_beta_user = CliCommandType(
        operations_tmpl='azext_people_beta.vendored_sdks.people.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('people', people_beta_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'people_delete', confirmation=True)
        g.custom_command('create-person', 'people_create_person')
        g.custom_command('get-analytic', 'people_get_analytic')
        g.custom_command('get-person', 'people_get_person')
        g.custom_command('get-profile', 'people_get_profile')
        g.custom_command('list-person', 'people_list_person')
        g.custom_command('update-analytic', 'people_update_analytic')
        g.custom_command('update-person', 'people_update_person')
        g.custom_command('update-profile', 'people_update_profile')

    from azext_people_beta.generated._client_factory import cf_user_analytic
    people_beta_user_analytic = CliCommandType(
        operations_tmpl='azext_people_beta.vendored_sdks.people.operations._user_analytic_operations#UserAnalyticOperat'
        'ions.{}',
        client_factory=cf_user_analytic)
    with self.command_group('people', people_beta_user_analytic, client_factory=cf_user_analytic) as g:
        g.custom_command('delete', 'people_delete', confirmation=True)
        g.custom_command('create-activity-statistics', 'people_create_activity_statistics')
        g.custom_command('get-activity-statistics', 'people_get_activity_statistics')
        g.custom_command('list-activity-statistics', 'people_list_activity_statistics')
        g.custom_command('update-activity-statistics', 'people_update_activity_statistics')

    from azext_people_beta.generated._client_factory import cf_user_profile
    people_beta_user_profile = CliCommandType(
        operations_tmpl='azext_people_beta.vendored_sdks.people.operations._user_profile_operations#UserProfileOperatio'
        'ns.{}',
        client_factory=cf_user_profile)
    with self.command_group('people', people_beta_user_profile, client_factory=cf_user_profile) as g:
        g.custom_command('delete', 'people_delete', confirmation=True)
        g.custom_command('create-account', 'people_create_account')
        g.custom_command('create-address', 'people_create_address')
        g.custom_command('create-anniversary', 'people_create_anniversary')
        g.custom_command('create-award', 'people_create_award')
        g.custom_command('create-certification', 'people_create_certification')
        g.custom_command('create-educational-activity', 'people_create_educational_activity')
        g.custom_command('create-email', 'people_create_email')
        g.custom_command('create-interest', 'people_create_interest')
        g.custom_command('create-language', 'people_create_language')
        g.custom_command('create-name', 'people_create_name')
        g.custom_command('create-note', 'people_create_note')
        g.custom_command('create-patent', 'people_create_patent')
        g.custom_command('create-phone', 'people_create_phone')
        g.custom_command('create-position', 'people_create_position')
        g.custom_command('create-project', 'people_create_project')
        g.custom_command('create-publication', 'people_create_publication')
        g.custom_command('create-skill', 'people_create_skill')
        g.custom_command('create-web-account', 'people_create_web_account')
        g.custom_command('create-website', 'people_create_website')
        g.custom_command('get-account', 'people_get_account')
        g.custom_command('get-address', 'people_get_address')
        g.custom_command('get-anniversary', 'people_get_anniversary')
        g.custom_command('get-award', 'people_get_award')
        g.custom_command('get-certification', 'people_get_certification')
        g.custom_command('get-educational-activity', 'people_get_educational_activity')
        g.custom_command('get-email', 'people_get_email')
        g.custom_command('get-interest', 'people_get_interest')
        g.custom_command('get-language', 'people_get_language')
        g.custom_command('get-name', 'people_get_name')
        g.custom_command('get-note', 'people_get_note')
        g.custom_command('get-patent', 'people_get_patent')
        g.custom_command('get-phone', 'people_get_phone')
        g.custom_command('get-position', 'people_get_position')
        g.custom_command('get-project', 'people_get_project')
        g.custom_command('get-publication', 'people_get_publication')
        g.custom_command('get-skill', 'people_get_skill')
        g.custom_command('get-web-account', 'people_get_web_account')
        g.custom_command('get-website', 'people_get_website')
        g.custom_command('list-account', 'people_list_account')
        g.custom_command('list-address', 'people_list_address')
        g.custom_command('list-anniversary', 'people_list_anniversary')
        g.custom_command('list-award', 'people_list_award')
        g.custom_command('list-certification', 'people_list_certification')
        g.custom_command('list-educational-activity', 'people_list_educational_activity')
        g.custom_command('list-email', 'people_list_email')
        g.custom_command('list-interest', 'people_list_interest')
        g.custom_command('list-language', 'people_list_language')
        g.custom_command('list-name', 'people_list_name')
        g.custom_command('list-note', 'people_list_note')
        g.custom_command('list-patent', 'people_list_patent')
        g.custom_command('list-phone', 'people_list_phone')
        g.custom_command('list-position', 'people_list_position')
        g.custom_command('list-project', 'people_list_project')
        g.custom_command('list-publication', 'people_list_publication')
        g.custom_command('list-skill', 'people_list_skill')
        g.custom_command('list-web-account', 'people_list_web_account')
        g.custom_command('list-website', 'people_list_website')
        g.custom_command('update-account', 'people_update_account')
        g.custom_command('update-address', 'people_update_address')
        g.custom_command('update-anniversary', 'people_update_anniversary')
        g.custom_command('update-award', 'people_update_award')
        g.custom_command('update-certification', 'people_update_certification')
        g.custom_command('update-educational-activity', 'people_update_educational_activity')
        g.custom_command('update-email', 'people_update_email')
        g.custom_command('update-interest', 'people_update_interest')
        g.custom_command('update-language', 'people_update_language')
        g.custom_command('update-name', 'people_update_name')
        g.custom_command('update-note', 'people_update_note')
        g.custom_command('update-patent', 'people_update_patent')
        g.custom_command('update-phone', 'people_update_phone')
        g.custom_command('update-position', 'people_update_position')
        g.custom_command('update-project', 'people_update_project')
        g.custom_command('update-publication', 'people_update_publication')
        g.custom_command('update-skill', 'people_update_skill')
        g.custom_command('update-web-account', 'people_update_web_account')
        g.custom_command('update-website', 'people_update_website')
