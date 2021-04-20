# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVITYDATETIME = "activityDateTime"
    ACTIVITYDISPLAYNAME = "activityDisplayName"
    ADDITIONALDETAILS = "additionalDetails"
    CATEGORY = "category"
    CORRELATIONID = "correlationId"
    INITIATEDBY = "initiatedBy"
    LOGGEDBYSERVICE = "loggedByService"
    OPERATIONTYPE = "operationType"
    RESULT = "result"
    RESULTREASON = "resultReason"
    TARGETRESOURCES = "targetResources"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    APPDISPLAYNAME = "appDisplayName"
    APPDISPLAYNAMEDESC = "appDisplayName desc"
    APPID = "appId"
    APPIDDESC = "appId desc"
    APPLIEDCONDITIONALACCESSPOLICIES = "appliedConditionalAccessPolicies"
    APPLIEDCONDITIONALACCESSPOLICIESDESC = "appliedConditionalAccessPolicies desc"
    CLIENTAPPUSED = "clientAppUsed"
    CLIENTAPPUSEDDESC = "clientAppUsed desc"
    CONDITIONALACCESSSTATUS = "conditionalAccessStatus"
    CONDITIONALACCESSSTATUSDESC = "conditionalAccessStatus desc"
    CORRELATIONID = "correlationId"
    CORRELATIONIDDESC = "correlationId desc"
    CREATEDDATETIME = "createdDateTime"
    CREATEDDATETIMEDESC = "createdDateTime desc"
    DEVICEDETAIL = "deviceDetail"
    DEVICEDETAILDESC = "deviceDetail desc"
    IPADDRESS = "ipAddress"
    IPADDRESSDESC = "ipAddress desc"
    ISINTERACTIVE = "isInteractive"
    ISINTERACTIVEDESC = "isInteractive desc"
    LOCATION = "location"
    LOCATIONDESC = "location desc"
    RESOURCEDISPLAYNAME = "resourceDisplayName"
    RESOURCEDISPLAYNAMEDESC = "resourceDisplayName desc"
    RESOURCEID = "resourceId"
    RESOURCEIDDESC = "resourceId desc"
    RISKDETAIL = "riskDetail"
    RISKDETAILDESC = "riskDetail desc"
    RISKEVENTTYPES = "riskEventTypes"
    RISKEVENTTYPESDESC = "riskEventTypes desc"
    RISKEVENTTYPESV2 = "riskEventTypes_v2"
    RISKEVENTTYPESV2DESC = "riskEventTypes_v2 desc"
    RISKLEVELAGGREGATED = "riskLevelAggregated"
    RISKLEVELAGGREGATEDDESC = "riskLevelAggregated desc"
    RISKLEVELDURINGSIGNIN = "riskLevelDuringSignIn"
    RISKLEVELDURINGSIGNINDESC = "riskLevelDuringSignIn desc"
    RISKSTATE = "riskState"
    RISKSTATEDESC = "riskState desc"
    STATUS = "status"
    STATUSDESC = "status desc"
    USERDISPLAYNAME = "userDisplayName"
    USERDISPLAYNAMEDESC = "userDisplayName desc"
    USERID = "userId"
    USERIDDESC = "userId desc"
    USERPRINCIPALNAME = "userPrincipalName"
    USERPRINCIPALNAMEDESC = "userPrincipalName desc"
    TARGETTENANTID = "targetTenantId"
    TARGETTENANTIDDESC = "targetTenantId desc"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPDISPLAYNAME = "appDisplayName"
    APPID = "appId"
    APPLIEDCONDITIONALACCESSPOLICIES = "appliedConditionalAccessPolicies"
    CLIENTAPPUSED = "clientAppUsed"
    CONDITIONALACCESSSTATUS = "conditionalAccessStatus"
    CORRELATIONID = "correlationId"
    CREATEDDATETIME = "createdDateTime"
    DEVICEDETAIL = "deviceDetail"
    IPADDRESS = "ipAddress"
    ISINTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCEDISPLAYNAME = "resourceDisplayName"
    RESOURCEID = "resourceId"
    RISKDETAIL = "riskDetail"
    RISKEVENTTYPES = "riskEventTypes"
    RISKEVENTTYPESV2 = "riskEventTypes_v2"
    RISKLEVELAGGREGATED = "riskLevelAggregated"
    RISKLEVELDURINGSIGNIN = "riskLevelDuringSignIn"
    RISKSTATE = "riskState"
    STATUS = "status"
    USERDISPLAYNAME = "userDisplayName"
    USERID = "userId"
    USERPRINCIPALNAME = "userPrincipalName"
    TARGETTENANTID = "targetTenantId"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPDISPLAYNAME = "appDisplayName"
    APPID = "appId"
    APPLIEDCONDITIONALACCESSPOLICIES = "appliedConditionalAccessPolicies"
    CLIENTAPPUSED = "clientAppUsed"
    CONDITIONALACCESSSTATUS = "conditionalAccessStatus"
    CORRELATIONID = "correlationId"
    CREATEDDATETIME = "createdDateTime"
    DEVICEDETAIL = "deviceDetail"
    IPADDRESS = "ipAddress"
    ISINTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCEDISPLAYNAME = "resourceDisplayName"
    RESOURCEID = "resourceId"
    RISKDETAIL = "riskDetail"
    RISKEVENTTYPES = "riskEventTypes"
    RISKEVENTTYPESV2 = "riskEventTypes_v2"
    RISKLEVELAGGREGATED = "riskLevelAggregated"
    RISKLEVELDURINGSIGNIN = "riskLevelDuringSignIn"
    RISKSTATE = "riskState"
    STATUS = "status"
    USERDISPLAYNAME = "userDisplayName"
    USERID = "userId"
    USERPRINCIPALNAME = "userPrincipalName"
    TARGETTENANTID = "targetTenantId"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    APPDISPLAYNAME = "appDisplayName"
    APPDISPLAYNAMEDESC = "appDisplayName desc"
    APPID = "appId"
    APPIDDESC = "appId desc"
    APPLIEDCONDITIONALACCESSPOLICIES = "appliedConditionalAccessPolicies"
    APPLIEDCONDITIONALACCESSPOLICIESDESC = "appliedConditionalAccessPolicies desc"
    CLIENTAPPUSED = "clientAppUsed"
    CLIENTAPPUSEDDESC = "clientAppUsed desc"
    CONDITIONALACCESSSTATUS = "conditionalAccessStatus"
    CONDITIONALACCESSSTATUSDESC = "conditionalAccessStatus desc"
    CORRELATIONID = "correlationId"
    CORRELATIONIDDESC = "correlationId desc"
    CREATEDDATETIME = "createdDateTime"
    CREATEDDATETIMEDESC = "createdDateTime desc"
    DEVICEDETAIL = "deviceDetail"
    DEVICEDETAILDESC = "deviceDetail desc"
    IPADDRESS = "ipAddress"
    IPADDRESSDESC = "ipAddress desc"
    ISINTERACTIVE = "isInteractive"
    ISINTERACTIVEDESC = "isInteractive desc"
    LOCATION = "location"
    LOCATIONDESC = "location desc"
    RESOURCEDISPLAYNAME = "resourceDisplayName"
    RESOURCEDISPLAYNAMEDESC = "resourceDisplayName desc"
    RESOURCEID = "resourceId"
    RESOURCEIDDESC = "resourceId desc"
    RISKDETAIL = "riskDetail"
    RISKDETAILDESC = "riskDetail desc"
    RISKEVENTTYPES = "riskEventTypes"
    RISKEVENTTYPESDESC = "riskEventTypes desc"
    RISKEVENTTYPESV2 = "riskEventTypes_v2"
    RISKEVENTTYPESV2DESC = "riskEventTypes_v2 desc"
    RISKLEVELAGGREGATED = "riskLevelAggregated"
    RISKLEVELAGGREGATEDDESC = "riskLevelAggregated desc"
    RISKLEVELDURINGSIGNIN = "riskLevelDuringSignIn"
    RISKLEVELDURINGSIGNINDESC = "riskLevelDuringSignIn desc"
    RISKSTATE = "riskState"
    RISKSTATEDESC = "riskState desc"
    STATUS = "status"
    STATUSDESC = "status desc"
    USERDISPLAYNAME = "userDisplayName"
    USERDISPLAYNAMEDESC = "userDisplayName desc"
    USERID = "userId"
    USERIDDESC = "userId desc"
    USERPRINCIPALNAME = "userPrincipalName"
    USERPRINCIPALNAMEDESC = "userPrincipalName desc"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPDISPLAYNAME = "appDisplayName"
    APPID = "appId"
    APPLIEDCONDITIONALACCESSPOLICIES = "appliedConditionalAccessPolicies"
    CLIENTAPPUSED = "clientAppUsed"
    CONDITIONALACCESSSTATUS = "conditionalAccessStatus"
    CORRELATIONID = "correlationId"
    CREATEDDATETIME = "createdDateTime"
    DEVICEDETAIL = "deviceDetail"
    IPADDRESS = "ipAddress"
    ISINTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCEDISPLAYNAME = "resourceDisplayName"
    RESOURCEID = "resourceId"
    RISKDETAIL = "riskDetail"
    RISKEVENTTYPES = "riskEventTypes"
    RISKEVENTTYPESV2 = "riskEventTypes_v2"
    RISKLEVELAGGREGATED = "riskLevelAggregated"
    RISKLEVELDURINGSIGNIN = "riskLevelDuringSignIn"
    RISKSTATE = "riskState"
    STATUS = "status"
    USERDISPLAYNAME = "userDisplayName"
    USERID = "userId"
    USERPRINCIPALNAME = "userPrincipalName"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPDISPLAYNAME = "appDisplayName"
    APPID = "appId"
    APPLIEDCONDITIONALACCESSPOLICIES = "appliedConditionalAccessPolicies"
    CLIENTAPPUSED = "clientAppUsed"
    CONDITIONALACCESSSTATUS = "conditionalAccessStatus"
    CORRELATIONID = "correlationId"
    CREATEDDATETIME = "createdDateTime"
    DEVICEDETAIL = "deviceDetail"
    IPADDRESS = "ipAddress"
    ISINTERACTIVE = "isInteractive"
    LOCATION = "location"
    RESOURCEDISPLAYNAME = "resourceDisplayName"
    RESOURCEID = "resourceId"
    RISKDETAIL = "riskDetail"
    RISKEVENTTYPES = "riskEventTypes"
    RISKEVENTTYPESV2 = "riskEventTypes_v2"
    RISKLEVELAGGREGATED = "riskLevelAggregated"
    RISKLEVELDURINGSIGNIN = "riskLevelDuringSignIn"
    RISKSTATE = "riskState"
    STATUS = "status"
    USERDISPLAYNAME = "userDisplayName"
    USERID = "userId"
    USERPRINCIPALNAME = "userPrincipalName"

class Get0itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DIRECTORYAUDITS = "directoryAudits"
    RESTRICTEDSIGNINS = "restrictedSignIns"
    SIGNINS = "signIns"

class Get1itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DIRECTORYAUDITS = "directoryAudits"
    RESTRICTEDSIGNINS = "restrictedSignIns"
    SIGNINS = "signIns"

class Get5itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    ACTIVITYDATETIME = "activityDateTime"
    ACTIVITYDATETIMEDESC = "activityDateTime desc"
    ACTIVITYDISPLAYNAME = "activityDisplayName"
    ACTIVITYDISPLAYNAMEDESC = "activityDisplayName desc"
    ADDITIONALDETAILS = "additionalDetails"
    ADDITIONALDETAILSDESC = "additionalDetails desc"
    CATEGORY = "category"
    CATEGORYDESC = "category desc"
    CORRELATIONID = "correlationId"
    CORRELATIONIDDESC = "correlationId desc"
    INITIATEDBY = "initiatedBy"
    INITIATEDBYDESC = "initiatedBy desc"
    LOGGEDBYSERVICE = "loggedByService"
    LOGGEDBYSERVICEDESC = "loggedByService desc"
    OPERATIONTYPE = "operationType"
    OPERATIONTYPEDESC = "operationType desc"
    RESULT = "result"
    RESULTDESC = "result desc"
    RESULTREASON = "resultReason"
    RESULTREASONDESC = "resultReason desc"
    TARGETRESOURCES = "targetResources"
    TARGETRESOURCESDESC = "targetResources desc"

class Get6itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVITYDATETIME = "activityDateTime"
    ACTIVITYDISPLAYNAME = "activityDisplayName"
    ADDITIONALDETAILS = "additionalDetails"
    CATEGORY = "category"
    CORRELATIONID = "correlationId"
    INITIATEDBY = "initiatedBy"
    LOGGEDBYSERVICE = "loggedByService"
    OPERATIONTYPE = "operationType"
    RESULT = "result"
    RESULTREASON = "resultReason"
    TARGETRESOURCES = "targetResources"

class Microsoftgraphappliedconditionalaccesspolicyresult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCESS = "success"
    FAILURE = "failure"
    NOTAPPLIED = "notApplied"
    NOTENABLED = "notEnabled"
    UNKNOWN = "unknown"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphconditionalaccessstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCESS = "success"
    FAILURE = "failure"
    NOTAPPLIED = "notApplied"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphgrouptype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNIFIEDGROUPS = "unifiedGroups"
    AZUREAD = "azureAD"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphoperationresult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCESS = "success"
    FAILURE = "failure"
    TIMEOUT = "timeout"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphriskdetail(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ADMINGENERATEDTEMPORARYPASSWORD = "adminGeneratedTemporaryPassword"
    USERPERFORMEDSECUREDPASSWORDCHANGE = "userPerformedSecuredPasswordChange"
    USERPERFORMEDSECUREDPASSWORDRESET = "userPerformedSecuredPasswordReset"
    ADMINCONFIRMEDSIGNINSAFE = "adminConfirmedSigninSafe"
    AICONFIRMEDSIGNINSAFE = "aiConfirmedSigninSafe"
    USERPASSEDMFADRIVENBYRISKBASEDPOLICY = "userPassedMFADrivenByRiskBasedPolicy"
    ADMINDISMISSEDALLRISKFORUSER = "adminDismissedAllRiskForUser"
    ADMINCONFIRMEDSIGNINCOMPROMISED = "adminConfirmedSigninCompromised"
    HIDDEN = "hidden"
    ADMINCONFIRMEDUSERCOMPROMISED = "adminConfirmedUserCompromised"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphriskeventtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNLIKELYTRAVEL = "unlikelyTravel"
    ANONYMIZEDIPADDRESS = "anonymizedIPAddress"
    MALICIOUSIPADDRESS = "maliciousIPAddress"
    UNFAMILIARFEATURES = "unfamiliarFeatures"
    MALWAREINFECTEDIPADDRESS = "malwareInfectedIPAddress"
    SUSPICIOUSIPADDRESS = "suspiciousIPAddress"
    LEAKEDCREDENTIALS = "leakedCredentials"
    INVESTIGATIONSTHREATINTELLIGENCE = "investigationsThreatIntelligence"
    GENERIC = "generic"
    ADMINCONFIRMEDUSERCOMPROMISED = "adminConfirmedUserCompromised"
    MCASIMPOSSIBLETRAVEL = "mcasImpossibleTravel"
    MCASSUSPICIOUSINBOXMANIPULATIONRULES = "mcasSuspiciousInboxManipulationRules"
    INVESTIGATIONSTHREATINTELLIGENCESIGNINLINKED = "investigationsThreatIntelligenceSigninLinked"
    MALICIOUSIPADDRESSVALIDCREDENTIALSBLOCKEDIP = "maliciousIPAddressValidCredentialsBlockedIP"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphrisklevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    HIDDEN = "hidden"
    NONE = "none"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphriskstate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    CONFIRMEDSAFE = "confirmedSafe"
    REMEDIATED = "remediated"
    DISMISSED = "dismissed"
    ATRISK = "atRisk"
    CONFIRMEDCOMPROMISED = "confirmedCompromised"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"
