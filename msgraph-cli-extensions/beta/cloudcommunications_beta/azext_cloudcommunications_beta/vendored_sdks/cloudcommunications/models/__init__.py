# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import collectionofaudioroutinggroup
    from ._models_py3 import collectionofcall
    from ._models_py3 import collectionofcallrecord
    from ._models_py3 import collectionofcommsoperation
    from ._models_py3 import collectionofonlinemeeting
    from ._models_py3 import collectionofonlinemeeting0
    from ._models_py3 import collectionofparticipant
    from ._models_py3 import collectionofpresence
    from ._models_py3 import collectionofsegment
    from ._models_py3 import collectionofsession
    from ._models_py3 import microsoftgraphaudioconferencing
    from ._models_py3 import microsoftgraphaudioroutinggroup
    from ._models_py3 import microsoftgraphcall
    from ._models_py3 import microsoftgraphcallmediastate
    from ._models_py3 import microsoftgraphcallrecordscallrecord
    from ._models_py3 import microsoftgraphcallrecordsdeviceinfo
    from ._models_py3 import microsoftgraphcallrecordsendpoint
    from ._models_py3 import microsoftgraphcallrecordsfailureinfo
    from ._models_py3 import microsoftgraphcallrecordsmedia
    from ._models_py3 import microsoftgraphcallrecordsmediastream
    from ._models_py3 import microsoftgraphcallrecordsnetworkinfo
    from ._models_py3 import microsoftgraphcallrecordssegment
    from ._models_py3 import microsoftgraphcallrecordssession
    from ._models_py3 import microsoftgraphcallrecordsuseragent
    from ._models_py3 import microsoftgraphcallroute
    from ._models_py3 import microsoftgraphcalltranscriptioninfo
    from ._models_py3 import microsoftgraphcancelmediaprocessingoperation
    from ._models_py3 import microsoftgraphchatinfo
    from ._models_py3 import microsoftgraphcloudcommunications
    from ._models_py3 import microsoftgraphcommsoperation
    from ._models_py3 import microsoftgraphentity
    from ._models_py3 import microsoftgraphidentity
    from ._models_py3 import microsoftgraphidentityset
    from ._models_py3 import microsoftgraphincomingcontext
    from ._models_py3 import microsoftgraphinvitationparticipantinfo
    from ._models_py3 import microsoftgraphinviteparticipantsoperation
    from ._models_py3 import microsoftgraphitembody
    from ._models_py3 import microsoftgraphlobbybypasssettings
    from ._models_py3 import microsoftgraphmediaconfig
    from ._models_py3 import microsoftgraphmediastream
    from ._models_py3 import microsoftgraphmeetingcapability
    from ._models_py3 import microsoftgraphmeetinginfo
    from ._models_py3 import microsoftgraphmeetingparticipantinfo
    from ._models_py3 import microsoftgraphmeetingparticipants
    from ._models_py3 import microsoftgraphmuteparticipantoperation
    from ._models_py3 import microsoftgraphmuteparticipantsoperation
    from ._models_py3 import microsoftgraphonlinemeeting
    from ._models_py3 import microsoftgraphparticipant
    from ._models_py3 import microsoftgraphparticipantinfo
    from ._models_py3 import microsoftgraphplaypromptoperation
    from ._models_py3 import microsoftgraphpresence
    from ._models_py3 import microsoftgraphrecordinginfo
    from ._models_py3 import microsoftgraphrecordoperation
    from ._models_py3 import microsoftgraphresultinfo
    from ._models_py3 import microsoftgraphsubscribetotoneoperation
    from ._models_py3 import microsoftgraphteleconferencedevicemediaquality
    from ._models_py3 import microsoftgraphteleconferencedevicequality
    from ._models_py3 import microsoftgraphtoneinfo
    from ._models_py3 import microsoftgraphunmuteparticipantoperation
    from ._models_py3 import microsoftgraphupdaterecordingstatusoperation
    from ._models_py3 import odataerror
    from ._models_py3 import odataerrordetail
    from ._models_py3 import odataerrormain
    from ._models_py3 import paths10wpgkzcommunicationsmicrosoftgraphgetpresencesbyuseridpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths13zt223communicationscallscallidmicrosoftgraphmutepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths14wb7kqcommunicationscallscallidmicrosoftgraphrecordresponsepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths183gi8ucommunicationscallscallidmicrosoftgraphredirectpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths1bh76wacommunicationscallscallidparticipantsmicrosoftgraphinvitepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths1gzqcv2communicationscallscallidmicrosoftgraphplaypromptpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths1jbdsmacommunicationscallsmicrosoftgraphlogteleconferencedevicequalitypostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths1mdqe66communicationscallscallidmicrosoftgraphrecordpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths1pc6sxrcommunicationsonlinemeetingsmicrosoftgraphcreateorgetpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths1x7bvttcommunicationscallscallidmicrosoftgraphunmutepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths4qrghdcommunicationscallscallidmicrosoftgraphrejectpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import paths4zbm7lcommunicationscallscallidmicrosoftgraphtransferpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathseipedycommunicationscallscallidmicrosoftgraphupdaterecordingstatuspostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathskpvac3communicationscallscallidparticipantsmicrosoftgraphmuteallpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathsoj95zpcommunicationscallscallidmicrosoftgraphchangescreensharingrolepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathsqvpqn4communicationscallscallidmicrosoftgraphanswerpostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathstobgxocommunicationscallscallidparticipantsparticipantidmicrosoftgraphmutepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathsxyl6wicommunicationscallscallidmicrosoftgraphsubscribetotonepostrequestbodycontentapplicationjsonschema
    from ._models_py3 import pathsyp37fjcommunicationscallscallidmicrosoftgraphcancelmediaprocessingpostrequestbodycontentapplicationjsonschema
except (SyntaxError, ImportError):
    from ._models import collectionofaudioroutinggroup  # type: ignore
    from ._models import collectionofcall  # type: ignore
    from ._models import collectionofcallrecord  # type: ignore
    from ._models import collectionofcommsoperation  # type: ignore
    from ._models import collectionofonlinemeeting  # type: ignore
    from ._models import collectionofonlinemeeting0  # type: ignore
    from ._models import collectionofparticipant  # type: ignore
    from ._models import collectionofpresence  # type: ignore
    from ._models import collectionofsegment  # type: ignore
    from ._models import collectionofsession  # type: ignore
    from ._models import microsoftgraphaudioconferencing  # type: ignore
    from ._models import microsoftgraphaudioroutinggroup  # type: ignore
    from ._models import microsoftgraphcall  # type: ignore
    from ._models import microsoftgraphcallmediastate  # type: ignore
    from ._models import microsoftgraphcallrecordscallrecord  # type: ignore
    from ._models import microsoftgraphcallrecordsdeviceinfo  # type: ignore
    from ._models import microsoftgraphcallrecordsendpoint  # type: ignore
    from ._models import microsoftgraphcallrecordsfailureinfo  # type: ignore
    from ._models import microsoftgraphcallrecordsmedia  # type: ignore
    from ._models import microsoftgraphcallrecordsmediastream  # type: ignore
    from ._models import microsoftgraphcallrecordsnetworkinfo  # type: ignore
    from ._models import microsoftgraphcallrecordssegment  # type: ignore
    from ._models import microsoftgraphcallrecordssession  # type: ignore
    from ._models import microsoftgraphcallrecordsuseragent  # type: ignore
    from ._models import microsoftgraphcallroute  # type: ignore
    from ._models import microsoftgraphcalltranscriptioninfo  # type: ignore
    from ._models import microsoftgraphcancelmediaprocessingoperation  # type: ignore
    from ._models import microsoftgraphchatinfo  # type: ignore
    from ._models import microsoftgraphcloudcommunications  # type: ignore
    from ._models import microsoftgraphcommsoperation  # type: ignore
    from ._models import microsoftgraphentity  # type: ignore
    from ._models import microsoftgraphidentity  # type: ignore
    from ._models import microsoftgraphidentityset  # type: ignore
    from ._models import microsoftgraphincomingcontext  # type: ignore
    from ._models import microsoftgraphinvitationparticipantinfo  # type: ignore
    from ._models import microsoftgraphinviteparticipantsoperation  # type: ignore
    from ._models import microsoftgraphitembody  # type: ignore
    from ._models import microsoftgraphlobbybypasssettings  # type: ignore
    from ._models import microsoftgraphmediaconfig  # type: ignore
    from ._models import microsoftgraphmediastream  # type: ignore
    from ._models import microsoftgraphmeetingcapability  # type: ignore
    from ._models import microsoftgraphmeetinginfo  # type: ignore
    from ._models import microsoftgraphmeetingparticipantinfo  # type: ignore
    from ._models import microsoftgraphmeetingparticipants  # type: ignore
    from ._models import microsoftgraphmuteparticipantoperation  # type: ignore
    from ._models import microsoftgraphmuteparticipantsoperation  # type: ignore
    from ._models import microsoftgraphonlinemeeting  # type: ignore
    from ._models import microsoftgraphparticipant  # type: ignore
    from ._models import microsoftgraphparticipantinfo  # type: ignore
    from ._models import microsoftgraphplaypromptoperation  # type: ignore
    from ._models import microsoftgraphpresence  # type: ignore
    from ._models import microsoftgraphrecordinginfo  # type: ignore
    from ._models import microsoftgraphrecordoperation  # type: ignore
    from ._models import microsoftgraphresultinfo  # type: ignore
    from ._models import microsoftgraphsubscribetotoneoperation  # type: ignore
    from ._models import microsoftgraphteleconferencedevicemediaquality  # type: ignore
    from ._models import microsoftgraphteleconferencedevicequality  # type: ignore
    from ._models import microsoftgraphtoneinfo  # type: ignore
    from ._models import microsoftgraphunmuteparticipantoperation  # type: ignore
    from ._models import microsoftgraphupdaterecordingstatusoperation  # type: ignore
    from ._models import odataerror  # type: ignore
    from ._models import odataerrordetail  # type: ignore
    from ._models import odataerrormain  # type: ignore
    from ._models import paths10wpgkzcommunicationsmicrosoftgraphgetpresencesbyuseridpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths13zt223communicationscallscallidmicrosoftgraphmutepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths14wb7kqcommunicationscallscallidmicrosoftgraphrecordresponsepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths183gi8ucommunicationscallscallidmicrosoftgraphredirectpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths1bh76wacommunicationscallscallidparticipantsmicrosoftgraphinvitepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths1gzqcv2communicationscallscallidmicrosoftgraphplaypromptpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths1jbdsmacommunicationscallsmicrosoftgraphlogteleconferencedevicequalitypostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths1mdqe66communicationscallscallidmicrosoftgraphrecordpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths1pc6sxrcommunicationsonlinemeetingsmicrosoftgraphcreateorgetpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths1x7bvttcommunicationscallscallidmicrosoftgraphunmutepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths4qrghdcommunicationscallscallidmicrosoftgraphrejectpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import paths4zbm7lcommunicationscallscallidmicrosoftgraphtransferpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathseipedycommunicationscallscallidmicrosoftgraphupdaterecordingstatuspostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathskpvac3communicationscallscallidparticipantsmicrosoftgraphmuteallpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathsoj95zpcommunicationscallscallidmicrosoftgraphchangescreensharingrolepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathsqvpqn4communicationscallscallidmicrosoftgraphanswerpostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathstobgxocommunicationscallscallidparticipantsparticipantidmicrosoftgraphmutepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathsxyl6wicommunicationscallscallidmicrosoftgraphsubscribetotonepostrequestbodycontentapplicationjsonschema  # type: ignore
    from ._models import pathsyp37fjcommunicationscallscallidmicrosoftgraphcancelmediaprocessingpostrequestbodycontentapplicationjsonschema  # type: ignore

from ._cloud_communications_enums import (
    Enum32,
    Enum34,
    Enum35,
    Enum37,
    Enum39,
    Enum40,
    Enum41,
    Enum42,
    Enum43,
    Enum44,
    Enum45,
    Enum46,
    Enum47,
    Enum48,
    Enum49,
    Enum55,
    Enum56,
    Enum57,
    Enum58,
    Enum59,
    Enum60,
    Enum61,
    Enum62,
    Enum63,
    Enum64,
    Enum65,
    Enum66,
    Enum67,
    Enum68,
    Enum69,
    Enum70,
    Get0itemsitem,
    Get1itemsitem,
    Get2itemsitem,
    Get3itemsitem,
    Get5itemsitem,
    Get6itemsitem,
    Get7itemsitem,
    Get8itemsitem,
    Microsoftgraphaccesslevel,
    Microsoftgraphautoadmitteduserstype,
    Microsoftgraphbodytype,
    Microsoftgraphcalldirection,
    Microsoftgraphcalldisposition,
    Microsoftgraphcallrecordscalltype,
    Microsoftgraphcallrecordsfailurestage,
    Microsoftgraphcallrecordsmediastreamdirection,
    Microsoftgraphcallrecordsmodality,
    Microsoftgraphcallrecordsnetworkconnectiontype,
    Microsoftgraphcallrecordswifiband,
    Microsoftgraphcallrecordswifiradiotype,
    Microsoftgraphcallstate,
    Microsoftgraphcalltranscriptionstate,
    Microsoftgraphendpointtype,
    Microsoftgraphlobbybypassscope,
    Microsoftgraphmediadirection,
    Microsoftgraphmediastate,
    Microsoftgraphmeetingcapabilities,
    Microsoftgraphmodality,
    Microsoftgraphonlinemeetingpresenters,
    Microsoftgraphonlinemeetingrole,
    Microsoftgraphoperationstatus,
    Microsoftgraphplaypromptcompletionreason,
    Microsoftgraphrecordcompletionreason,
    Microsoftgraphrecordingstatus,
    Microsoftgraphrejectreason,
    Microsoftgraphroutingmode,
    Microsoftgraphroutingpolicy,
    Microsoftgraphroutingtype,
    Microsoftgraphscreensharingrole,
    Microsoftgraphtone,
)

__all__ = [
    'collectionofaudioroutinggroup',
    'collectionofcall',
    'collectionofcallrecord',
    'collectionofcommsoperation',
    'collectionofonlinemeeting',
    'collectionofonlinemeeting0',
    'collectionofparticipant',
    'collectionofpresence',
    'collectionofsegment',
    'collectionofsession',
    'microsoftgraphaudioconferencing',
    'microsoftgraphaudioroutinggroup',
    'microsoftgraphcall',
    'microsoftgraphcallmediastate',
    'microsoftgraphcallrecordscallrecord',
    'microsoftgraphcallrecordsdeviceinfo',
    'microsoftgraphcallrecordsendpoint',
    'microsoftgraphcallrecordsfailureinfo',
    'microsoftgraphcallrecordsmedia',
    'microsoftgraphcallrecordsmediastream',
    'microsoftgraphcallrecordsnetworkinfo',
    'microsoftgraphcallrecordssegment',
    'microsoftgraphcallrecordssession',
    'microsoftgraphcallrecordsuseragent',
    'microsoftgraphcallroute',
    'microsoftgraphcalltranscriptioninfo',
    'microsoftgraphcancelmediaprocessingoperation',
    'microsoftgraphchatinfo',
    'microsoftgraphcloudcommunications',
    'microsoftgraphcommsoperation',
    'microsoftgraphentity',
    'microsoftgraphidentity',
    'microsoftgraphidentityset',
    'microsoftgraphincomingcontext',
    'microsoftgraphinvitationparticipantinfo',
    'microsoftgraphinviteparticipantsoperation',
    'microsoftgraphitembody',
    'microsoftgraphlobbybypasssettings',
    'microsoftgraphmediaconfig',
    'microsoftgraphmediastream',
    'microsoftgraphmeetingcapability',
    'microsoftgraphmeetinginfo',
    'microsoftgraphmeetingparticipantinfo',
    'microsoftgraphmeetingparticipants',
    'microsoftgraphmuteparticipantoperation',
    'microsoftgraphmuteparticipantsoperation',
    'microsoftgraphonlinemeeting',
    'microsoftgraphparticipant',
    'microsoftgraphparticipantinfo',
    'microsoftgraphplaypromptoperation',
    'microsoftgraphpresence',
    'microsoftgraphrecordinginfo',
    'microsoftgraphrecordoperation',
    'microsoftgraphresultinfo',
    'microsoftgraphsubscribetotoneoperation',
    'microsoftgraphteleconferencedevicemediaquality',
    'microsoftgraphteleconferencedevicequality',
    'microsoftgraphtoneinfo',
    'microsoftgraphunmuteparticipantoperation',
    'microsoftgraphupdaterecordingstatusoperation',
    'odataerror',
    'odataerrordetail',
    'odataerrormain',
    'paths10wpgkzcommunicationsmicrosoftgraphgetpresencesbyuseridpostrequestbodycontentapplicationjsonschema',
    'paths13zt223communicationscallscallidmicrosoftgraphmutepostrequestbodycontentapplicationjsonschema',
    'paths14wb7kqcommunicationscallscallidmicrosoftgraphrecordresponsepostrequestbodycontentapplicationjsonschema',
    'paths183gi8ucommunicationscallscallidmicrosoftgraphredirectpostrequestbodycontentapplicationjsonschema',
    'paths1bh76wacommunicationscallscallidparticipantsmicrosoftgraphinvitepostrequestbodycontentapplicationjsonschema',
    'paths1gzqcv2communicationscallscallidmicrosoftgraphplaypromptpostrequestbodycontentapplicationjsonschema',
    'paths1jbdsmacommunicationscallsmicrosoftgraphlogteleconferencedevicequalitypostrequestbodycontentapplicationjsonschema',
    'paths1mdqe66communicationscallscallidmicrosoftgraphrecordpostrequestbodycontentapplicationjsonschema',
    'paths1pc6sxrcommunicationsonlinemeetingsmicrosoftgraphcreateorgetpostrequestbodycontentapplicationjsonschema',
    'paths1x7bvttcommunicationscallscallidmicrosoftgraphunmutepostrequestbodycontentapplicationjsonschema',
    'paths4qrghdcommunicationscallscallidmicrosoftgraphrejectpostrequestbodycontentapplicationjsonschema',
    'paths4zbm7lcommunicationscallscallidmicrosoftgraphtransferpostrequestbodycontentapplicationjsonschema',
    'pathseipedycommunicationscallscallidmicrosoftgraphupdaterecordingstatuspostrequestbodycontentapplicationjsonschema',
    'pathskpvac3communicationscallscallidparticipantsmicrosoftgraphmuteallpostrequestbodycontentapplicationjsonschema',
    'pathsoj95zpcommunicationscallscallidmicrosoftgraphchangescreensharingrolepostrequestbodycontentapplicationjsonschema',
    'pathsqvpqn4communicationscallscallidmicrosoftgraphanswerpostrequestbodycontentapplicationjsonschema',
    'pathstobgxocommunicationscallscallidparticipantsparticipantidmicrosoftgraphmutepostrequestbodycontentapplicationjsonschema',
    'pathsxyl6wicommunicationscallscallidmicrosoftgraphsubscribetotonepostrequestbodycontentapplicationjsonschema',
    'pathsyp37fjcommunicationscallscallidmicrosoftgraphcancelmediaprocessingpostrequestbodycontentapplicationjsonschema',
    'Enum32',
    'Enum34',
    'Enum35',
    'Enum37',
    'Enum39',
    'Enum40',
    'Enum41',
    'Enum42',
    'Enum43',
    'Enum44',
    'Enum45',
    'Enum46',
    'Enum47',
    'Enum48',
    'Enum49',
    'Enum55',
    'Enum56',
    'Enum57',
    'Enum58',
    'Enum59',
    'Enum60',
    'Enum61',
    'Enum62',
    'Enum63',
    'Enum64',
    'Enum65',
    'Enum66',
    'Enum67',
    'Enum68',
    'Enum69',
    'Enum70',
    'Get0itemsitem',
    'Get1itemsitem',
    'Get2itemsitem',
    'Get3itemsitem',
    'Get5itemsitem',
    'Get6itemsitem',
    'Get7itemsitem',
    'Get8itemsitem',
    'Microsoftgraphaccesslevel',
    'Microsoftgraphautoadmitteduserstype',
    'Microsoftgraphbodytype',
    'Microsoftgraphcalldirection',
    'Microsoftgraphcalldisposition',
    'Microsoftgraphcallrecordscalltype',
    'Microsoftgraphcallrecordsfailurestage',
    'Microsoftgraphcallrecordsmediastreamdirection',
    'Microsoftgraphcallrecordsmodality',
    'Microsoftgraphcallrecordsnetworkconnectiontype',
    'Microsoftgraphcallrecordswifiband',
    'Microsoftgraphcallrecordswifiradiotype',
    'Microsoftgraphcallstate',
    'Microsoftgraphcalltranscriptionstate',
    'Microsoftgraphendpointtype',
    'Microsoftgraphlobbybypassscope',
    'Microsoftgraphmediadirection',
    'Microsoftgraphmediastate',
    'Microsoftgraphmeetingcapabilities',
    'Microsoftgraphmodality',
    'Microsoftgraphonlinemeetingpresenters',
    'Microsoftgraphonlinemeetingrole',
    'Microsoftgraphoperationstatus',
    'Microsoftgraphplaypromptcompletionreason',
    'Microsoftgraphrecordcompletionreason',
    'Microsoftgraphrecordingstatus',
    'Microsoftgraphrejectreason',
    'Microsoftgraphroutingmode',
    'Microsoftgraphroutingpolicy',
    'Microsoftgraphroutingtype',
    'Microsoftgraphscreensharingrole',
    'Microsoftgraphtone',
]
