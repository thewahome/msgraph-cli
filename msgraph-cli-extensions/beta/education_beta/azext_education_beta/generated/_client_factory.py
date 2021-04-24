# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_education_beta_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_education_beta.vendored_sdks.education import Education
    return get_mgmt_service_client(cli_ctx,
                                   Education,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_education_education_root(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_education_root


def cf_education(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education


def cf_education_class(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_classes


def cf_education_class_assignment(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_classes_assignments


def cf_education_class_assignment_submission(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_classes_assignments_submissions


def cf_education_class_member(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_classes_members


def cf_education_class_school(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_classes_schools


def cf_education_class_teacher(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_classes_teachers


def cf_education_me(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_me


def cf_education_me_assignment(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_me_assignments


def cf_education_me_assignment_submission(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_me_assignments_submissions


def cf_education_me_class(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_me_classes


def cf_education_me_school(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_me_schools


def cf_education_me_taught_class(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_me_taught_classes


def cf_education_school(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_schools


def cf_education_school_class(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_schools_classes


def cf_education_school_user(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_schools_users


def cf_education_synchronization_profile(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_synchronization_profiles


def cf_education_user(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_users


def cf_education_user_assignment(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_users_assignments


def cf_education_user_assignment_submission(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_users_assignments_submissions


def cf_education_user_class(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_users_classes


def cf_education_user_school(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_users_schools


def cf_education_user_taught_class(cli_ctx, *_):
    return cf_education_beta_cl(cli_ctx).education_users_taught_classes
