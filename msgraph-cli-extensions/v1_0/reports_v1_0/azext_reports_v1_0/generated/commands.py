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
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType
from azext_reports_v1_0.generated._client_factory import (
    cf_auditlogsauditlogroot,
    cf_auditlog,
    cf_reportsreportroot,
    cf_report,
)


reports_v1_0_auditlogsauditlogroot = CliCommandType(
    operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._auditlogsauditlogroot_operations#auditlogsauditlogrootOperations.{}',
    client_factory=cf_auditlogsauditlogroot,
)


reports_v1_0_auditlog = CliCommandType(
    operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._auditlogs_operations#auditlogsOperations.{}',
    client_factory=cf_auditlog,
)


reports_v1_0_reportsreportroot = CliCommandType(
    operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._reportsreportroot_operations#reportsreportrootOperations.{}',
    client_factory=cf_reportsreportroot,
)


reports_v1_0_report = CliCommandType(
    operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._reports_operations#reportsOperations.{}',
    client_factory=cf_report,
)


def load_command_table(self, _):

    with self.command_group(
        'reports auditlogsauditlogroot', reports_v1_0_auditlogsauditlogroot, client_factory=cf_auditlogsauditlogroot
    ) as g:
        g.custom_command('show-audit-log-root', 'reports_auditlogsauditlogroot_show_audit_log_root')
        g.custom_command('update-audit-log-root', 'reports_auditlogsauditlogroot_update_audit_log_root')

    with self.command_group('reports auditlog', reports_v1_0_auditlog, client_factory=cf_auditlog) as g:
        g.custom_command('create-directory-audit', 'reports_auditlog_create_directory_audit')
        g.custom_command('create-restricted-sign-in', 'reports_auditlog_create_restricted_sign_in')
        g.custom_command('create-sign-in', 'reports_auditlog_create_sign_in')
        g.custom_command('delete-directory-audit', 'reports_auditlog_delete_directory_audit')
        g.custom_command('delete-restricted-sign-in', 'reports_auditlog_delete_restricted_sign_in')
        g.custom_command('delete-sign-in', 'reports_auditlog_delete_sign_in')
        g.custom_command('list-directory-audit', 'reports_auditlog_list_directory_audit')
        g.custom_command('list-restricted-sign-in', 'reports_auditlog_list_restricted_sign_in')
        g.custom_command('list-sign-in', 'reports_auditlog_list_sign_in')
        g.custom_command('show-directory-audit', 'reports_auditlog_show_directory_audit')
        g.custom_command('show-restricted-sign-in', 'reports_auditlog_show_restricted_sign_in')
        g.custom_command('show-sign-in', 'reports_auditlog_show_sign_in')
        g.custom_command('update-directory-audit', 'reports_auditlog_update_directory_audit')
        g.custom_command('update-restricted-sign-in', 'reports_auditlog_update_restricted_sign_in')
        g.custom_command('update-sign-in', 'reports_auditlog_update_sign_in')

    with self.command_group(
        'reports reportsreportroot', reports_v1_0_reportsreportroot, client_factory=cf_reportsreportroot
    ) as g:
        g.custom_command('show-report-root', 'reports_reportsreportroot_show_report_root')
        g.custom_command('update-report-root', 'reports_reportsreportroot_update_report_root')

    with self.command_group('reports report', reports_v1_0_report, client_factory=cf_report) as g:
        g.custom_command('device-configuration-device-activity', 'reports_report_device_configuration_device_activity')
        g.custom_command('device-configuration-user-activity', 'reports_report_device_configuration_user_activity')
        g.custom_command(
            'managed-device-enrollment-failure-details027-e',
            'reports_report_managed_device_enrollment_failure_details027_e',
        )
        g.custom_command(
            'managed-device-enrollment-failure-details2-b3-d',
            'reports_report_managed_device_enrollment_failure_details2_b3_d',
        )
        g.custom_command(
            'managed-device-enrollment-top-failure-afd1', 'reports_report_managed_device_enrollment_top_failure_afd1'
        )
        g.custom_command(
            'managed-device-enrollment-top-failures4669', 'reports_report_managed_device_enrollment_top_failures4669'
        )
        g.custom_command('show-email-activity-count', 'reports_report_show_email_activity_count')
        g.custom_command('show-email-activity-user-count', 'reports_report_show_email_activity_user_count')
        g.custom_command('show-email-activity-user-detail-ddb2', 'reports_report_show_email_activity_user_detail_ddb2')
        g.custom_command('show-email-activity-user-detail-fe32', 'reports_report_show_email_activity_user_detail_fe32')
        g.custom_command('show-email-app-usage-app-user-count', 'reports_report_show_email_app_usage_app_user_count')
        g.custom_command('show-email-app-usage-user-count', 'reports_report_show_email_app_usage_user_count')
        g.custom_command(
            'show-email-app-usage-user-detail546-b', 'reports_report_show_email_app_usage_user_detail546_b'
        )
        g.custom_command(
            'show-email-app-usage-user-detail62-ec', 'reports_report_show_email_app_usage_user_detail62_ec'
        )
        g.custom_command(
            'show-email-app-usage-version-user-count', 'reports_report_show_email_app_usage_version_user_count'
        )
        g.custom_command('show-mailbox-usage-detail', 'reports_report_show_mailbox_usage_detail')
        g.custom_command('show-mailbox-usage-mailbox-count', 'reports_report_show_mailbox_usage_mailbox_count')
        g.custom_command(
            'show-mailbox-usage-quota-status-mailbox-count',
            'reports_report_show_mailbox_usage_quota_status_mailbox_count',
        )
        g.custom_command('show-mailbox-usage-storage', 'reports_report_show_mailbox_usage_storage')
        g.custom_command('show-office365-activation-count', 'reports_report_show_office365_activation_count')
        g.custom_command('show-office365-activation-user-count', 'reports_report_show_office365_activation_user_count')
        g.custom_command(
            'show-office365-activation-user-detail', 'reports_report_show_office365_activation_user_detail'
        )
        g.custom_command('show-office365-active-user-count', 'reports_report_show_office365_active_user_count')
        g.custom_command(
            'show-office365-active-user-detail-d389', 'reports_report_show_office365_active_user_detail_d389'
        )
        g.custom_command(
            'show-office365-active-user-detail68-ad', 'reports_report_show_office365_active_user_detail68_ad'
        )
        g.custom_command('show-office365-group-activity-count', 'reports_report_show_office365_group_activity_count')
        g.custom_command(
            'show-office365-group-activity-detail38-f6', 'reports_report_show_office365_group_activity_detail38_f6'
        )
        g.custom_command(
            'show-office365-group-activity-detail81-cc', 'reports_report_show_office365_group_activity_detail81_cc'
        )
        g.custom_command(
            'show-office365-group-activity-file-count', 'reports_report_show_office365_group_activity_file_count'
        )
        g.custom_command(
            'show-office365-group-activity-group-count', 'reports_report_show_office365_group_activity_group_count'
        )
        g.custom_command(
            'show-office365-group-activity-storage', 'reports_report_show_office365_group_activity_storage'
        )
        g.custom_command('show-office365-service-user-count', 'reports_report_show_office365_service_user_count')
        g.custom_command('show-one-drive-activity-file-count', 'reports_report_show_one_drive_activity_file_count')
        g.custom_command('show-one-drive-activity-user-count', 'reports_report_show_one_drive_activity_user_count')
        g.custom_command(
            'show-one-drive-activity-user-detail-c424', 'reports_report_show_one_drive_activity_user_detail_c424'
        )
        g.custom_command(
            'show-one-drive-activity-user-detail05-f1', 'reports_report_show_one_drive_activity_user_detail05_f1'
        )
        g.custom_command('show-one-drive-usage-account-count', 'reports_report_show_one_drive_usage_account_count')
        g.custom_command(
            'show-one-drive-usage-account-detail-dd7-f', 'reports_report_show_one_drive_usage_account_detail_dd7_f'
        )
        g.custom_command(
            'show-one-drive-usage-account-detail-e827', 'reports_report_show_one_drive_usage_account_detail_e827'
        )
        g.custom_command('show-one-drive-usage-file-count', 'reports_report_show_one_drive_usage_file_count')
        g.custom_command('show-one-drive-usage-storage', 'reports_report_show_one_drive_usage_storage')
        g.custom_command('show-share-point-activity-file-count', 'reports_report_show_share_point_activity_file_count')
        g.custom_command('show-share-point-activity-page', 'reports_report_show_share_point_activity_page')
        g.custom_command('show-share-point-activity-user-count', 'reports_report_show_share_point_activity_user_count')
        g.custom_command(
            'show-share-point-activity-user-detail-b778', 'reports_report_show_share_point_activity_user_detail_b778'
        )
        g.custom_command(
            'show-share-point-activity-user-detail-f3-be', 'reports_report_show_share_point_activity_user_detail_f3_be'
        )
        g.custom_command(
            'show-share-point-site-usage-detail-d27-a', 'reports_report_show_share_point_site_usage_detail_d27_a'
        )
        g.custom_command(
            'show-share-point-site-usage-detail204-b', 'reports_report_show_share_point_site_usage_detail204_b'
        )
        g.custom_command(
            'show-share-point-site-usage-file-count', 'reports_report_show_share_point_site_usage_file_count'
        )
        g.custom_command('show-share-point-site-usage-page', 'reports_report_show_share_point_site_usage_page')
        g.custom_command(
            'show-share-point-site-usage-site-count', 'reports_report_show_share_point_site_usage_site_count'
        )
        g.custom_command('show-share-point-site-usage-storage', 'reports_report_show_share_point_site_usage_storage')
        g.custom_command(
            'show-skype-for-business-activity-count', 'reports_report_show_skype_for_business_activity_count'
        )
        g.custom_command(
            'show-skype-for-business-activity-user-count', 'reports_report_show_skype_for_business_activity_user_count'
        )
        g.custom_command(
            'show-skype-for-business-activity-user-detail-e4-c9',
            'reports_report_show_skype_for_business_activity_user_detail_e4_c9',
        )
        g.custom_command(
            'show-skype-for-business-activity-user-detail744-e',
            'reports_report_show_skype_for_business_activity_user_detail744_e',
        )
        g.custom_command(
            'show-skype-for-business-device-usage-distribution-user-count',
            'reports_report_show_skype_for_business_device_usage_distribution_user_count',
        )
        g.custom_command(
            'show-skype-for-business-device-usage-user-count',
            'reports_report_show_skype_for_business_device_usage_user_count',
        )
        g.custom_command(
            'show-skype-for-business-device-usage-user-detail-a692',
            'reports_report_show_skype_for_business_device_usage_user_detail_a692',
        )
        g.custom_command(
            'show-skype-for-business-device-usage-user-detail-e753',
            'reports_report_show_skype_for_business_device_usage_user_detail_e753',
        )
        g.custom_command(
            'show-skype-for-business-organizer-activity-count',
            'reports_report_show_skype_for_business_organizer_activity_count',
        )
        g.custom_command(
            'show-skype-for-business-organizer-activity-minute-count',
            'reports_report_show_skype_for_business_organizer_activity_minute_count',
        )
        g.custom_command(
            'show-skype-for-business-organizer-activity-user-count',
            'reports_report_show_skype_for_business_organizer_activity_user_count',
        )
        g.custom_command(
            'show-skype-for-business-participant-activity-count',
            'reports_report_show_skype_for_business_participant_activity_count',
        )
        g.custom_command(
            'show-skype-for-business-participant-activity-minute-count',
            'reports_report_show_skype_for_business_participant_activity_minute_count',
        )
        g.custom_command(
            'show-skype-for-business-participant-activity-user-count',
            'reports_report_show_skype_for_business_participant_activity_user_count',
        )
        g.custom_command(
            'show-skype-for-business-peer-to-peer-activity-count',
            'reports_report_show_skype_for_business_peer_to_peer_activity_count',
        )
        g.custom_command(
            'show-skype-for-business-peer-to-peer-activity-minute-count',
            'reports_report_show_skype_for_business_peer_to_peer_activity_minute_count',
        )
        g.custom_command(
            'show-skype-for-business-peer-to-peer-activity-user-count',
            'reports_report_show_skype_for_business_peer_to_peer_activity_user_count',
        )
        g.custom_command(
            'show-team-device-usage-distribution-user-count',
            'reports_report_show_team_device_usage_distribution_user_count',
        )
        g.custom_command('show-team-device-usage-user-count', 'reports_report_show_team_device_usage_user_count')
        g.custom_command(
            'show-team-device-usage-user-detail7148', 'reports_report_show_team_device_usage_user_detail7148'
        )
        g.custom_command(
            'show-team-device-usage-user-detail7565', 'reports_report_show_team_device_usage_user_detail7565'
        )
        g.custom_command('show-team-user-activity-count', 'reports_report_show_team_user_activity_count')
        g.custom_command('show-team-user-activity-user-count', 'reports_report_show_team_user_activity_user_count')
        g.custom_command(
            'show-team-user-activity-user-detail-a3-f1', 'reports_report_show_team_user_activity_user_detail_a3_f1'
        )
        g.custom_command(
            'show-team-user-activity-user-detail-eb13', 'reports_report_show_team_user_activity_user_detail_eb13'
        )
        g.custom_command('show-yammer-activity-count', 'reports_report_show_yammer_activity_count')
        g.custom_command('show-yammer-activity-user-count', 'reports_report_show_yammer_activity_user_count')
        g.custom_command(
            'show-yammer-activity-user-detail-ac30', 'reports_report_show_yammer_activity_user_detail_ac30'
        )
        g.custom_command(
            'show-yammer-activity-user-detail15-a5', 'reports_report_show_yammer_activity_user_detail15_a5'
        )
        g.custom_command(
            'show-yammer-device-usage-distribution-user-count',
            'reports_report_show_yammer_device_usage_distribution_user_count',
        )
        g.custom_command('show-yammer-device-usage-user-count', 'reports_report_show_yammer_device_usage_user_count')
        g.custom_command(
            'show-yammer-device-usage-user-detail-cfad', 'reports_report_show_yammer_device_usage_user_detail_cfad'
        )
        g.custom_command(
            'show-yammer-device-usage-user-detail-d0-ac', 'reports_report_show_yammer_device_usage_user_detail_d0_ac'
        )
        g.custom_command('show-yammer-group-activity-count', 'reports_report_show_yammer_group_activity_count')
        g.custom_command(
            'show-yammer-group-activity-detail-da9-a', 'reports_report_show_yammer_group_activity_detail_da9_a'
        )
        g.custom_command(
            'show-yammer-group-activity-detail0-d7-d', 'reports_report_show_yammer_group_activity_detail0_d7_d'
        )
        g.custom_command(
            'show-yammer-group-activity-group-count', 'reports_report_show_yammer_group_activity_group_count'
        )

    with self.command_group('reports_v1_0', is_experimental=True):
        pass
