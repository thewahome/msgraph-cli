# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_usersfunctions_v1_0_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_usersfunctions_v1_0.vendored_sdks.usersfunctions import UsersFunctions
    return get_mgmt_service_client(cli_ctx,
                                   UsersFunctions,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_usersactivity(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersactivities


def cf_userscalendarviewcalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarcalendarviewcalendar


def cf_userscalendarviewinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarcalendarviewinstances


def cf_userscalendarview(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarcalendarview


def cf_userscalendareventscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendareventscalendar


def cf_userscalendareventsinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendareventsinstances


def cf_userscalendarevent(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarevents


def cf_userscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendar


def cf_userscalendargroupscalendarscalendarviewcalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarviewcalendar


def cf_userscalendargroupscalendarscalendarviewinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarviewinstances


def cf_userscalendargroupscalendarscalendarview(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarview


def cf_userscalendargroupscalendarseventscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendarseventscalendar


def cf_userscalendargroupscalendarseventsinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendarseventsinstances


def cf_userscalendargroupscalendarsevent(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendarsevents


def cf_userscalendargroupscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendargroupscalendars


def cf_userscalendarscalendarviewcalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarscalendarviewcalendar


def cf_userscalendarscalendarviewinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarscalendarviewinstances


def cf_userscalendarscalendarview(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarscalendarview


def cf_userscalendarseventscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarseventscalendar


def cf_userscalendarseventsinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarseventsinstances


def cf_userscalendarsevent(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarsevents


def cf_userscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendars


def cf_userscalendarviewcalendarview(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarviewcalendarcalendarview


def cf_userscalendarviewcalendarevent(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarviewcalendarevents


def cf_userscalendarviewcalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarviewcalendar


def cf_userscalendarviewinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarviewinstances


def cf_userscalendarview(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscalendarview


def cf_userscontactfolderschildfolder(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscontactfolderschildfolders


def cf_userscontactfolderscontact(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscontactfolderscontacts


def cf_userscontactfolder(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscontactfolders


def cf_userscontact(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userscontacts


def cf_userseventscalendarview(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userseventscalendarcalendarview


def cf_userseventscalendarevent(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userseventscalendarevents


def cf_userseventscalendar(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userseventscalendar


def cf_userseventsinstance(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).userseventsinstances


def cf_usersevent(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersevents


def cf_usersmailfolderschildfolder(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersmailfolderschildfolders


def cf_usersmailfoldersmessage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersmailfoldersmessages


def cf_usersmailfolder(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersmailfolders


def cf_usersmanagedappregistration(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersmanagedappregistrations


def cf_usersmessage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersmessages


def cf_user(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).users


def cf_usersonenotenotebookssectiongroupssectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupssectionspages


def cf_usersonenotenotebookssectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotenotebookssectionspages


def cf_usersonenotenotebook(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotenotebooks


def cf_usersonenotepage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotepages


def cf_usersonenotepagesparentnotebooksectiongroupssectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectiongroupssectionspages


def cf_usersonenotepagesparentnotebooksectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectionspages


def cf_usersonenotepagesparentsectionpage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionpages


def cf_usersonenotesectiongroupsparentnotebooksectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebooksectionspages


def cf_usersonenotesectiongroupssectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionspages


def cf_usersonenotesectionspage(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersonenotesectionspages


def cf_usersoutlook(cli_ctx, *_):
    return cf_usersfunctions_v1_0_cl(cli_ctx).usersoutlook
