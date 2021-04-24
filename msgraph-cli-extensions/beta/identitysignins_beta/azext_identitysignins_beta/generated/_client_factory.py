# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_identitysignins_beta_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_identitysignins_beta.vendored_sdks.identitysignins import IdentitySignIns
    return get_mgmt_service_client(cli_ctx,
                                   IdentitySignIns,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_data_policy_operation_data_policy_operation(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).data_policy_operations_data_policy_operation


def cf_identity(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).identity


def cf_identity_conditional_access(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).identity_conditional_access


def cf_identity_provider_identity_provider(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).identity_providers_identity_provider


def cf_identity_provider(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).identity_providers


def cf_information_protection_information_protection(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_information_protection


def cf_information_protection(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection


def cf_information_protection_data_loss_prevention_policy(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_data_loss_prevention_policies


def cf_information_protection_policy(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_policy


def cf_information_protection_policy_label(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_policy_labels


def cf_information_protection_sensitivity_label(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_sensitivity_labels


def cf_information_protection_sensitivity_label_sublabel(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_sensitivity_labels_sublabels


def cf_information_protection_threat_assessment_request(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).information_protection_threat_assessment_requests


def cf_invitation_invitation(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).invitations_invitation


def cf_invitation(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).invitations


def cf_oauth2permission_grant_oauth2permission_grant(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).oauth2_permission_grants_oauth2_permission_grant


def cf_oauth2permission_grant(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).oauth2_permission_grants


def cf_organization(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).organization


def cf_policy_policy_root(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).policies_policy_root


def cf_policy(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).policies


def cf_policy_permission_grant_policy(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).policies_permission_grant_policies


def cf_risk_detection_risk_detection(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).risk_detections_risk_detection


def cf_risky_user_risky_user(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).risky_users_risky_user


def cf_risky_user(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).risky_users


def cf_trust_framework_trust_framework(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).trust_framework_trust_framework


def cf_trust_framework(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).trust_framework


def cf_trust_framework_key_set(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).trust_framework_key_sets


def cf_user(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).users


def cf_user_authentication(cli_ctx, *_):
    return cf_identitysignins_beta_cl(cli_ctx).users_authentication
