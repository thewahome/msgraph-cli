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
from azext_bookings_beta.generated._client_factory import (
    cf_bookingbusinessesbookingbusiness,
    cf_bookingbusiness,
    cf_bookingbusinessesappointment,
    cf_bookingbusinessescalendarview,
    cf_bookingcurrenciesbookingcurrency,
)


bookings_beta_bookingbusinessesbookingbusiness = CliCommandType(
    operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._bookingbusinessesbookingbusiness_operations#bookingbusinessesbookingbusinessOperations.{}',
    client_factory=cf_bookingbusinessesbookingbusiness,
)


bookings_beta_bookingbusiness = CliCommandType(
    operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._bookingbusinesses_operations#bookingbusinessesOperations.{}',
    client_factory=cf_bookingbusiness,
)


bookings_beta_bookingbusinessesappointment = CliCommandType(
    operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._bookingbusinessesappointments_operations#bookingbusinessesappointmentsOperations.{}',
    client_factory=cf_bookingbusinessesappointment,
)


bookings_beta_bookingbusinessescalendarview = CliCommandType(
    operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._bookingbusinessescalendarview_operations#bookingbusinessescalendarviewOperations.{}',
    client_factory=cf_bookingbusinessescalendarview,
)


bookings_beta_bookingcurrenciesbookingcurrency = CliCommandType(
    operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._bookingcurrenciesbookingcurrency_operations#bookingcurrenciesbookingcurrencyOperations.{}',
    client_factory=cf_bookingcurrenciesbookingcurrency,
)


def load_command_table(self, _):

    with self.command_group(
        'bookings bookingbusinessesbookingbusiness',
        bookings_beta_bookingbusinessesbookingbusiness,
        client_factory=cf_bookingbusinessesbookingbusiness,
    ) as g:
        g.custom_command('create-booking-business', 'bookings_bookingbusinessesbookingbusiness_create_booking_business')
        g.custom_command('delete-booking-business', 'bookings_bookingbusinessesbookingbusiness_delete_booking_business')
        g.custom_command('list-booking-business', 'bookings_bookingbusinessesbookingbusiness_list_booking_business')
        g.custom_command('show-booking-business', 'bookings_bookingbusinessesbookingbusiness_show_booking_business')
        g.custom_command('update-booking-business', 'bookings_bookingbusinessesbookingbusiness_update_booking_business')

    with self.command_group(
        'bookings bookingbusiness', bookings_beta_bookingbusiness, client_factory=cf_bookingbusiness
    ) as g:
        g.custom_command('create-appointment', 'bookings_bookingbusiness_create_appointment')
        g.custom_command('create-calendar-view', 'bookings_bookingbusiness_create_calendar_view')
        g.custom_command('create-customer', 'bookings_bookingbusiness_create_customer')
        g.custom_command('create-service', 'bookings_bookingbusiness_create_service')
        g.custom_command('create-staff-member', 'bookings_bookingbusiness_create_staff_member')
        g.custom_command('delete-appointment', 'bookings_bookingbusiness_delete_appointment')
        g.custom_command('delete-calendar-view', 'bookings_bookingbusiness_delete_calendar_view')
        g.custom_command('delete-customer', 'bookings_bookingbusiness_delete_customer')
        g.custom_command('delete-service', 'bookings_bookingbusiness_delete_service')
        g.custom_command('delete-staff-member', 'bookings_bookingbusiness_delete_staff_member')
        g.custom_command('list-appointment', 'bookings_bookingbusiness_list_appointment')
        g.custom_command('list-calendar-view', 'bookings_bookingbusiness_list_calendar_view')
        g.custom_command('list-customer', 'bookings_bookingbusiness_list_customer')
        g.custom_command('list-service', 'bookings_bookingbusiness_list_service')
        g.custom_command('list-staff-member', 'bookings_bookingbusiness_list_staff_member')
        g.custom_command('publish', 'bookings_bookingbusiness_publish')
        g.custom_command('show-appointment', 'bookings_bookingbusiness_show_appointment')
        g.custom_command('show-calendar-view', 'bookings_bookingbusiness_show_calendar_view')
        g.custom_command('show-customer', 'bookings_bookingbusiness_show_customer')
        g.custom_command('show-service', 'bookings_bookingbusiness_show_service')
        g.custom_command('show-staff-member', 'bookings_bookingbusiness_show_staff_member')
        g.custom_command('unpublish', 'bookings_bookingbusiness_unpublish')
        g.custom_command('update-appointment', 'bookings_bookingbusiness_update_appointment')
        g.custom_command('update-calendar-view', 'bookings_bookingbusiness_update_calendar_view')
        g.custom_command('update-customer', 'bookings_bookingbusiness_update_customer')
        g.custom_command('update-service', 'bookings_bookingbusiness_update_service')
        g.custom_command('update-staff-member', 'bookings_bookingbusiness_update_staff_member')

    with self.command_group(
        'bookings bookingbusinessesappointment',
        bookings_beta_bookingbusinessesappointment,
        client_factory=cf_bookingbusinessesappointment,
    ) as g:
        g.custom_command('cancel', 'bookings_bookingbusinessesappointment_cancel')

    with self.command_group(
        'bookings bookingbusinessescalendarview',
        bookings_beta_bookingbusinessescalendarview,
        client_factory=cf_bookingbusinessescalendarview,
    ) as g:
        g.custom_command('cancel', 'bookings_bookingbusinessescalendarview_cancel')

    with self.command_group(
        'bookings bookingcurrenciesbookingcurrency',
        bookings_beta_bookingcurrenciesbookingcurrency,
        client_factory=cf_bookingcurrenciesbookingcurrency,
    ) as g:
        g.custom_command('create-booking-currency', 'bookings_bookingcurrenciesbookingcurrency_create_booking_currency')
        g.custom_command('delete-booking-currency', 'bookings_bookingcurrenciesbookingcurrency_delete_booking_currency')
        g.custom_command('list-booking-currency', 'bookings_bookingcurrenciesbookingcurrency_list_booking_currency')
        g.custom_command('show-booking-currency', 'bookings_bookingcurrenciesbookingcurrency_show_booking_currency')
        g.custom_command('update-booking-currency', 'bookings_bookingcurrenciesbookingcurrency_update_booking_currency')

    with self.command_group('bookings_beta', is_experimental=True):
        pass
