# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class Enum10(str, Enum):

    id = "id"
    teams_app_id = "teamsAppId"
    display_name = "displayName"
    version = "version"

class Enum6(str, Enum):

    id = "id"
    teams_app = "teamsApp"
    teams_app_definition = "teamsAppDefinition"

class Enum8(str, Enum):

    id = "id"
    external_id = "externalId"
    name = "name"
    display_name = "displayName"
    distribution_method = "distributionMethod"
    app_definitions = "appDefinitions"

class Enum9(str, Enum):

    asterisk = "*"
    app_definitions = "appDefinitions"

class Get1ItemsItem(str, Enum):

    id = "id"
    installed_apps = "installedApps"

class Get2ItemsItem(str, Enum):

    asterisk = "*"
    installed_apps = "installedApps"

class Get3ItemsItem(str, Enum):

    asterisk = "*"
    teams_app = "teamsApp"
    teams_app_definition = "teamsAppDefinition"

class Get6ItemsItem(str, Enum):

    id = "id"
    id_desc = "id desc"

class Get7ItemsItem(str, Enum):

    id = "id"
    teams_app = "teamsApp"
    teams_app_definition = "teamsAppDefinition"

class Get8ItemsItem(str, Enum):

    asterisk = "*"
    teams_app = "teamsApp"
    teams_app_definition = "teamsAppDefinition"

class MicrosoftGraphTeamsAppDistributionMethod(str, Enum):

    store = "store"
    organization = "organization"
    sideloaded = "sideloaded"
    unknown_future_value = "unknownFutureValue"
