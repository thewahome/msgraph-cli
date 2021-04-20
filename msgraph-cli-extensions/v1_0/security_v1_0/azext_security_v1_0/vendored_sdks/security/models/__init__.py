# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import collectionofalert
    from ._models_py3 import collectionofsecurescore
    from ._models_py3 import collectionofsecurescorecontrolprofile
    from ._models_py3 import microsoftgraphalert
    from ._models_py3 import microsoftgraphalerthistorystate
    from ._models_py3 import microsoftgraphalerttrigger
    from ._models_py3 import microsoftgraphaveragecomparativescore
    from ._models_py3 import microsoftgraphcertificationcontrol
    from ._models_py3 import microsoftgraphcloudappsecuritystate
    from ._models_py3 import microsoftgraphcomplianceinformation
    from ._models_py3 import microsoftgraphcontrolscore
    from ._models_py3 import microsoftgraphentity
    from ._models_py3 import microsoftgraphfilehash
    from ._models_py3 import microsoftgraphfilesecuritystate
    from ._models_py3 import microsoftgraphhostsecuritystate
    from ._models_py3 import microsoftgraphmalwarestate
    from ._models_py3 import microsoftgraphnetworkconnection
    from ._models_py3 import microsoftgraphprocess
    from ._models_py3 import microsoftgraphregistrykeystate
    from ._models_py3 import microsoftgraphsecurescore
    from ._models_py3 import microsoftgraphsecurescorecontrolprofile
    from ._models_py3 import microsoftgraphsecurescorecontrolstateupdate
    from ._models_py3 import microsoftgraphsecurity
    from ._models_py3 import microsoftgraphsecurityresource
    from ._models_py3 import microsoftgraphsecurityvendorinformation
    from ._models_py3 import microsoftgraphusersecuritystate
    from ._models_py3 import microsoftgraphvulnerabilitystate
    from ._models_py3 import odataerror
    from ._models_py3 import odataerrordetail
    from ._models_py3 import odataerrormain
except (SyntaxError, ImportError):
    from ._models import collectionofalert  # type: ignore
    from ._models import collectionofsecurescore  # type: ignore
    from ._models import collectionofsecurescorecontrolprofile  # type: ignore
    from ._models import microsoftgraphalert  # type: ignore
    from ._models import microsoftgraphalerthistorystate  # type: ignore
    from ._models import microsoftgraphalerttrigger  # type: ignore
    from ._models import microsoftgraphaveragecomparativescore  # type: ignore
    from ._models import microsoftgraphcertificationcontrol  # type: ignore
    from ._models import microsoftgraphcloudappsecuritystate  # type: ignore
    from ._models import microsoftgraphcomplianceinformation  # type: ignore
    from ._models import microsoftgraphcontrolscore  # type: ignore
    from ._models import microsoftgraphentity  # type: ignore
    from ._models import microsoftgraphfilehash  # type: ignore
    from ._models import microsoftgraphfilesecuritystate  # type: ignore
    from ._models import microsoftgraphhostsecuritystate  # type: ignore
    from ._models import microsoftgraphmalwarestate  # type: ignore
    from ._models import microsoftgraphnetworkconnection  # type: ignore
    from ._models import microsoftgraphprocess  # type: ignore
    from ._models import microsoftgraphregistrykeystate  # type: ignore
    from ._models import microsoftgraphsecurescore  # type: ignore
    from ._models import microsoftgraphsecurescorecontrolprofile  # type: ignore
    from ._models import microsoftgraphsecurescorecontrolstateupdate  # type: ignore
    from ._models import microsoftgraphsecurity  # type: ignore
    from ._models import microsoftgraphsecurityresource  # type: ignore
    from ._models import microsoftgraphsecurityvendorinformation  # type: ignore
    from ._models import microsoftgraphusersecuritystate  # type: ignore
    from ._models import microsoftgraphvulnerabilitystate  # type: ignore
    from ._models import odataerror  # type: ignore
    from ._models import odataerrordetail  # type: ignore
    from ._models import odataerrormain  # type: ignore

from ._security_enums import (
    Enum19,
    Enum20,
    Enum21,
    Enum22,
    Enum23,
    Enum24,
    Enum25,
    Get0itemsitem,
    Get1itemsitem,
    Get5itemsitem,
    Get6itemsitem,
    Microsoftgraphalertfeedback,
    Microsoftgraphalertseverity,
    Microsoftgraphalertstatus,
    Microsoftgraphconnectiondirection,
    Microsoftgraphconnectionstatus,
    Microsoftgraphemailrole,
    Microsoftgraphfilehashtype,
    Microsoftgraphlogontype,
    Microsoftgraphprocessintegritylevel,
    Microsoftgraphregistryhive,
    Microsoftgraphregistryoperation,
    Microsoftgraphregistryvaluetype,
    Microsoftgraphsecuritynetworkprotocol,
    Microsoftgraphsecurityresourcetype,
    Microsoftgraphuseraccountsecuritytype,
)

__all__ = [
    'collectionofalert',
    'collectionofsecurescore',
    'collectionofsecurescorecontrolprofile',
    'microsoftgraphalert',
    'microsoftgraphalerthistorystate',
    'microsoftgraphalerttrigger',
    'microsoftgraphaveragecomparativescore',
    'microsoftgraphcertificationcontrol',
    'microsoftgraphcloudappsecuritystate',
    'microsoftgraphcomplianceinformation',
    'microsoftgraphcontrolscore',
    'microsoftgraphentity',
    'microsoftgraphfilehash',
    'microsoftgraphfilesecuritystate',
    'microsoftgraphhostsecuritystate',
    'microsoftgraphmalwarestate',
    'microsoftgraphnetworkconnection',
    'microsoftgraphprocess',
    'microsoftgraphregistrykeystate',
    'microsoftgraphsecurescore',
    'microsoftgraphsecurescorecontrolprofile',
    'microsoftgraphsecurescorecontrolstateupdate',
    'microsoftgraphsecurity',
    'microsoftgraphsecurityresource',
    'microsoftgraphsecurityvendorinformation',
    'microsoftgraphusersecuritystate',
    'microsoftgraphvulnerabilitystate',
    'odataerror',
    'odataerrordetail',
    'odataerrormain',
    'Enum19',
    'Enum20',
    'Enum21',
    'Enum22',
    'Enum23',
    'Enum24',
    'Enum25',
    'Get0itemsitem',
    'Get1itemsitem',
    'Get5itemsitem',
    'Get6itemsitem',
    'Microsoftgraphalertfeedback',
    'Microsoftgraphalertseverity',
    'Microsoftgraphalertstatus',
    'Microsoftgraphconnectiondirection',
    'Microsoftgraphconnectionstatus',
    'Microsoftgraphemailrole',
    'Microsoftgraphfilehashtype',
    'Microsoftgraphlogontype',
    'Microsoftgraphprocessintegritylevel',
    'Microsoftgraphregistryhive',
    'Microsoftgraphregistryoperation',
    'Microsoftgraphregistryvaluetype',
    'Microsoftgraphsecuritynetworkprotocol',
    'Microsoftgraphsecurityresourcetype',
    'Microsoftgraphuseraccountsecuritytype',
]
