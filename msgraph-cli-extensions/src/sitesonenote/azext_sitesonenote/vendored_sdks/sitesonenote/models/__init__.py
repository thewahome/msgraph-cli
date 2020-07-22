# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CollectionOfNotebook
    from ._models_py3 import CollectionOfOnenoteOperation
    from ._models_py3 import CollectionOfOnenotePage
    from ._models_py3 import CollectionOfOnenotePage0
    from ._models_py3 import CollectionOfOnenotePage1
    from ._models_py3 import CollectionOfOnenotePage2
    from ._models_py3 import CollectionOfOnenotePage3
    from ._models_py3 import CollectionOfOnenotePage4
    from ._models_py3 import CollectionOfOnenotePage5
    from ._models_py3 import CollectionOfOnenotePage6
    from ._models_py3 import CollectionOfOnenotePage7
    from ._models_py3 import CollectionOfOnenoteResource
    from ._models_py3 import CollectionOfOnenoteSection
    from ._models_py3 import CollectionOfOnenoteSection0
    from ._models_py3 import CollectionOfOnenoteSection1
    from ._models_py3 import CollectionOfOnenoteSection10
    from ._models_py3 import CollectionOfOnenoteSection11
    from ._models_py3 import CollectionOfOnenoteSection12
    from ._models_py3 import CollectionOfOnenoteSection13
    from ._models_py3 import CollectionOfOnenoteSection14
    from ._models_py3 import CollectionOfOnenoteSection15
    from ._models_py3 import CollectionOfOnenoteSection16
    from ._models_py3 import CollectionOfOnenoteSection17
    from ._models_py3 import CollectionOfOnenoteSection18
    from ._models_py3 import CollectionOfOnenoteSection19
    from ._models_py3 import CollectionOfOnenoteSection2
    from ._models_py3 import CollectionOfOnenoteSection3
    from ._models_py3 import CollectionOfOnenoteSection4
    from ._models_py3 import CollectionOfOnenoteSection5
    from ._models_py3 import CollectionOfOnenoteSection6
    from ._models_py3 import CollectionOfOnenoteSection7
    from ._models_py3 import CollectionOfOnenoteSection8
    from ._models_py3 import CollectionOfOnenoteSection9
    from ._models_py3 import CollectionOfSectionGroup
    from ._models_py3 import CollectionOfSectionGroup0
    from ._models_py3 import CollectionOfSectionGroup1
    from ._models_py3 import CollectionOfSectionGroup10
    from ._models_py3 import CollectionOfSectionGroup11
    from ._models_py3 import CollectionOfSectionGroup12
    from ._models_py3 import CollectionOfSectionGroup13
    from ._models_py3 import CollectionOfSectionGroup14
    from ._models_py3 import CollectionOfSectionGroup15
    from ._models_py3 import CollectionOfSectionGroup16
    from ._models_py3 import CollectionOfSectionGroup17
    from ._models_py3 import CollectionOfSectionGroup18
    from ._models_py3 import CollectionOfSectionGroup19
    from ._models_py3 import CollectionOfSectionGroup2
    from ._models_py3 import CollectionOfSectionGroup3
    from ._models_py3 import CollectionOfSectionGroup4
    from ._models_py3 import CollectionOfSectionGroup5
    from ._models_py3 import CollectionOfSectionGroup6
    from ._models_py3 import CollectionOfSectionGroup7
    from ._models_py3 import CollectionOfSectionGroup8
    from ._models_py3 import CollectionOfSectionGroup9
    from ._models_py3 import MicrosoftGraphEntity
    from ._models_py3 import MicrosoftGraphExternalLink
    from ._models_py3 import MicrosoftGraphIdentity
    from ._models_py3 import MicrosoftGraphNotebook
    from ._models_py3 import MicrosoftGraphOnenote
    from ._models_py3 import MicrosoftGraphOnenoteEntityBaseModel
    from ._models_py3 import MicrosoftGraphOnenoteEntityHierarchyModel
    from ._models_py3 import MicrosoftGraphOnenoteEntitySchemaObjectModel
    from ._models_py3 import MicrosoftGraphOnenoteOperation
    from ._models_py3 import MicrosoftGraphOnenoteOperationError
    from ._models_py3 import MicrosoftGraphOnenotePage
    from ._models_py3 import MicrosoftGraphOnenoteResource
    from ._models_py3 import MicrosoftGraphOnenoteSection
    from ._models_py3 import MicrosoftGraphOperation
    from ._models_py3 import MicrosoftGraphPageLinks
    from ._models_py3 import MicrosoftGraphSectionGroup
    from ._models_py3 import OdataError
    from ._models_py3 import OdataErrorDetail
    from ._models_py3 import OdataErrorMain
except (SyntaxError, ImportError):
    from ._models import CollectionOfNotebook  # type: ignore
    from ._models import CollectionOfOnenoteOperation  # type: ignore
    from ._models import CollectionOfOnenotePage  # type: ignore
    from ._models import CollectionOfOnenotePage0  # type: ignore
    from ._models import CollectionOfOnenotePage1  # type: ignore
    from ._models import CollectionOfOnenotePage2  # type: ignore
    from ._models import CollectionOfOnenotePage3  # type: ignore
    from ._models import CollectionOfOnenotePage4  # type: ignore
    from ._models import CollectionOfOnenotePage5  # type: ignore
    from ._models import CollectionOfOnenotePage6  # type: ignore
    from ._models import CollectionOfOnenotePage7  # type: ignore
    from ._models import CollectionOfOnenoteResource  # type: ignore
    from ._models import CollectionOfOnenoteSection  # type: ignore
    from ._models import CollectionOfOnenoteSection0  # type: ignore
    from ._models import CollectionOfOnenoteSection1  # type: ignore
    from ._models import CollectionOfOnenoteSection10  # type: ignore
    from ._models import CollectionOfOnenoteSection11  # type: ignore
    from ._models import CollectionOfOnenoteSection12  # type: ignore
    from ._models import CollectionOfOnenoteSection13  # type: ignore
    from ._models import CollectionOfOnenoteSection14  # type: ignore
    from ._models import CollectionOfOnenoteSection15  # type: ignore
    from ._models import CollectionOfOnenoteSection16  # type: ignore
    from ._models import CollectionOfOnenoteSection17  # type: ignore
    from ._models import CollectionOfOnenoteSection18  # type: ignore
    from ._models import CollectionOfOnenoteSection19  # type: ignore
    from ._models import CollectionOfOnenoteSection2  # type: ignore
    from ._models import CollectionOfOnenoteSection3  # type: ignore
    from ._models import CollectionOfOnenoteSection4  # type: ignore
    from ._models import CollectionOfOnenoteSection5  # type: ignore
    from ._models import CollectionOfOnenoteSection6  # type: ignore
    from ._models import CollectionOfOnenoteSection7  # type: ignore
    from ._models import CollectionOfOnenoteSection8  # type: ignore
    from ._models import CollectionOfOnenoteSection9  # type: ignore
    from ._models import CollectionOfSectionGroup  # type: ignore
    from ._models import CollectionOfSectionGroup0  # type: ignore
    from ._models import CollectionOfSectionGroup1  # type: ignore
    from ._models import CollectionOfSectionGroup10  # type: ignore
    from ._models import CollectionOfSectionGroup11  # type: ignore
    from ._models import CollectionOfSectionGroup12  # type: ignore
    from ._models import CollectionOfSectionGroup13  # type: ignore
    from ._models import CollectionOfSectionGroup14  # type: ignore
    from ._models import CollectionOfSectionGroup15  # type: ignore
    from ._models import CollectionOfSectionGroup16  # type: ignore
    from ._models import CollectionOfSectionGroup17  # type: ignore
    from ._models import CollectionOfSectionGroup18  # type: ignore
    from ._models import CollectionOfSectionGroup19  # type: ignore
    from ._models import CollectionOfSectionGroup2  # type: ignore
    from ._models import CollectionOfSectionGroup3  # type: ignore
    from ._models import CollectionOfSectionGroup4  # type: ignore
    from ._models import CollectionOfSectionGroup5  # type: ignore
    from ._models import CollectionOfSectionGroup6  # type: ignore
    from ._models import CollectionOfSectionGroup7  # type: ignore
    from ._models import CollectionOfSectionGroup8  # type: ignore
    from ._models import CollectionOfSectionGroup9  # type: ignore
    from ._models import MicrosoftGraphEntity  # type: ignore
    from ._models import MicrosoftGraphExternalLink  # type: ignore
    from ._models import MicrosoftGraphIdentity  # type: ignore
    from ._models import MicrosoftGraphNotebook  # type: ignore
    from ._models import MicrosoftGraphOnenote  # type: ignore
    from ._models import MicrosoftGraphOnenoteEntityBaseModel  # type: ignore
    from ._models import MicrosoftGraphOnenoteEntityHierarchyModel  # type: ignore
    from ._models import MicrosoftGraphOnenoteEntitySchemaObjectModel  # type: ignore
    from ._models import MicrosoftGraphOnenoteOperation  # type: ignore
    from ._models import MicrosoftGraphOnenoteOperationError  # type: ignore
    from ._models import MicrosoftGraphOnenotePage  # type: ignore
    from ._models import MicrosoftGraphOnenoteResource  # type: ignore
    from ._models import MicrosoftGraphOnenoteSection  # type: ignore
    from ._models import MicrosoftGraphOperation  # type: ignore
    from ._models import MicrosoftGraphPageLinks  # type: ignore
    from ._models import MicrosoftGraphSectionGroup  # type: ignore
    from ._models import OdataError  # type: ignore
    from ._models import OdataErrorDetail  # type: ignore
    from ._models import OdataErrorMain  # type: ignore

from ._sites_one_note_enums import (
    Enum10,
    Enum100,
    Enum101,
    Enum102,
    Enum103,
    Enum104,
    Enum105,
    Enum106,
    Enum107,
    Enum108,
    Enum109,
    Enum110,
    Enum111,
    Enum112,
    Enum113,
    Enum114,
    Enum115,
    Enum116,
    Enum117,
    Enum118,
    Enum119,
    Enum12,
    Enum120,
    Enum121,
    Enum122,
    Enum123,
    Enum124,
    Enum125,
    Enum126,
    Enum127,
    Enum128,
    Enum129,
    Enum130,
    Enum131,
    Enum132,
    Enum133,
    Enum134,
    Enum135,
    Enum136,
    Enum137,
    Enum138,
    Enum139,
    Enum14,
    Enum140,
    Enum141,
    Enum142,
    Enum143,
    Enum144,
    Enum145,
    Enum146,
    Enum147,
    Enum148,
    Enum149,
    Enum15,
    Enum150,
    Enum151,
    Enum152,
    Enum153,
    Enum154,
    Enum155,
    Enum156,
    Enum157,
    Enum158,
    Enum159,
    Enum16,
    Enum160,
    Enum161,
    Enum162,
    Enum163,
    Enum164,
    Enum165,
    Enum166,
    Enum167,
    Enum168,
    Enum169,
    Enum17,
    Enum170,
    Enum171,
    Enum172,
    Enum173,
    Enum174,
    Enum175,
    Enum176,
    Enum177,
    Enum178,
    Enum179,
    Enum18,
    Enum180,
    Enum181,
    Enum182,
    Enum183,
    Enum184,
    Enum185,
    Enum186,
    Enum187,
    Enum188,
    Enum189,
    Enum19,
    Enum190,
    Enum191,
    Enum192,
    Enum193,
    Enum194,
    Enum195,
    Enum196,
    Enum197,
    Enum198,
    Enum199,
    Enum200,
    Enum201,
    Enum202,
    Enum203,
    Enum204,
    Enum205,
    Enum206,
    Enum207,
    Enum208,
    Enum209,
    Enum21,
    Enum210,
    Enum211,
    Enum212,
    Enum213,
    Enum214,
    Enum215,
    Enum216,
    Enum217,
    Enum218,
    Enum219,
    Enum220,
    Enum221,
    Enum222,
    Enum223,
    Enum224,
    Enum225,
    Enum226,
    Enum227,
    Enum228,
    Enum229,
    Enum23,
    Enum230,
    Enum231,
    Enum232,
    Enum233,
    Enum234,
    Enum235,
    Enum236,
    Enum237,
    Enum238,
    Enum239,
    Enum24,
    Enum240,
    Enum241,
    Enum242,
    Enum243,
    Enum244,
    Enum245,
    Enum246,
    Enum247,
    Enum248,
    Enum249,
    Enum25,
    Enum250,
    Enum251,
    Enum252,
    Enum253,
    Enum254,
    Enum255,
    Enum256,
    Enum257,
    Enum258,
    Enum259,
    Enum26,
    Enum260,
    Enum261,
    Enum262,
    Enum263,
    Enum264,
    Enum265,
    Enum266,
    Enum267,
    Enum268,
    Enum269,
    Enum27,
    Enum270,
    Enum271,
    Enum272,
    Enum273,
    Enum274,
    Enum275,
    Enum276,
    Enum277,
    Enum278,
    Enum279,
    Enum28,
    Enum280,
    Enum281,
    Enum282,
    Enum283,
    Enum284,
    Enum285,
    Enum286,
    Enum287,
    Enum288,
    Enum289,
    Enum29,
    Enum290,
    Enum291,
    Enum292,
    Enum293,
    Enum294,
    Enum295,
    Enum296,
    Enum297,
    Enum298,
    Enum299,
    Enum300,
    Enum301,
    Enum302,
    Enum303,
    Enum304,
    Enum305,
    Enum306,
    Enum307,
    Enum308,
    Enum309,
    Enum31,
    Enum310,
    Enum311,
    Enum312,
    Enum313,
    Enum314,
    Enum315,
    Enum316,
    Enum317,
    Enum318,
    Enum319,
    Enum32,
    Enum320,
    Enum321,
    Enum322,
    Enum323,
    Enum324,
    Enum325,
    Enum326,
    Enum327,
    Enum328,
    Enum329,
    Enum33,
    Enum330,
    Enum331,
    Enum332,
    Enum333,
    Enum334,
    Enum335,
    Enum336,
    Enum337,
    Enum338,
    Enum339,
    Enum34,
    Enum340,
    Enum341,
    Enum342,
    Enum343,
    Enum344,
    Enum345,
    Enum346,
    Enum347,
    Enum348,
    Enum349,
    Enum35,
    Enum350,
    Enum351,
    Enum352,
    Enum353,
    Enum354,
    Enum355,
    Enum356,
    Enum357,
    Enum358,
    Enum359,
    Enum36,
    Enum360,
    Enum361,
    Enum362,
    Enum363,
    Enum364,
    Enum365,
    Enum37,
    Enum38,
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
    Enum50,
    Enum51,
    Enum52,
    Enum53,
    Enum54,
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
    Enum7,
    Enum70,
    Enum71,
    Enum72,
    Enum73,
    Enum74,
    Enum75,
    Enum76,
    Enum77,
    Enum78,
    Enum79,
    Enum80,
    Enum81,
    Enum82,
    Enum83,
    Enum84,
    Enum85,
    Enum86,
    Enum87,
    Enum88,
    Enum89,
    Enum9,
    Enum90,
    Enum91,
    Enum92,
    Enum93,
    Enum94,
    Enum95,
    Enum96,
    Enum97,
    Enum98,
    Enum99,
    Get10ItemsItem,
    Get11ItemsItem,
    Get1ItemsItem,
    Get2ItemsItem,
    Get3ItemsItem,
    Get4ItemsItem,
    Get5ItemsItem,
    Get6ItemsItem,
    Get7ItemsItem,
    Get8ItemsItem,
    Get9ItemsItem,
    MicrosoftGraphOnenoteUserRole,
    MicrosoftGraphOperationStatus,
)

__all__ = [
    'CollectionOfNotebook',
    'CollectionOfOnenoteOperation',
    'CollectionOfOnenotePage',
    'CollectionOfOnenotePage0',
    'CollectionOfOnenotePage1',
    'CollectionOfOnenotePage2',
    'CollectionOfOnenotePage3',
    'CollectionOfOnenotePage4',
    'CollectionOfOnenotePage5',
    'CollectionOfOnenotePage6',
    'CollectionOfOnenotePage7',
    'CollectionOfOnenoteResource',
    'CollectionOfOnenoteSection',
    'CollectionOfOnenoteSection0',
    'CollectionOfOnenoteSection1',
    'CollectionOfOnenoteSection10',
    'CollectionOfOnenoteSection11',
    'CollectionOfOnenoteSection12',
    'CollectionOfOnenoteSection13',
    'CollectionOfOnenoteSection14',
    'CollectionOfOnenoteSection15',
    'CollectionOfOnenoteSection16',
    'CollectionOfOnenoteSection17',
    'CollectionOfOnenoteSection18',
    'CollectionOfOnenoteSection19',
    'CollectionOfOnenoteSection2',
    'CollectionOfOnenoteSection3',
    'CollectionOfOnenoteSection4',
    'CollectionOfOnenoteSection5',
    'CollectionOfOnenoteSection6',
    'CollectionOfOnenoteSection7',
    'CollectionOfOnenoteSection8',
    'CollectionOfOnenoteSection9',
    'CollectionOfSectionGroup',
    'CollectionOfSectionGroup0',
    'CollectionOfSectionGroup1',
    'CollectionOfSectionGroup10',
    'CollectionOfSectionGroup11',
    'CollectionOfSectionGroup12',
    'CollectionOfSectionGroup13',
    'CollectionOfSectionGroup14',
    'CollectionOfSectionGroup15',
    'CollectionOfSectionGroup16',
    'CollectionOfSectionGroup17',
    'CollectionOfSectionGroup18',
    'CollectionOfSectionGroup19',
    'CollectionOfSectionGroup2',
    'CollectionOfSectionGroup3',
    'CollectionOfSectionGroup4',
    'CollectionOfSectionGroup5',
    'CollectionOfSectionGroup6',
    'CollectionOfSectionGroup7',
    'CollectionOfSectionGroup8',
    'CollectionOfSectionGroup9',
    'MicrosoftGraphEntity',
    'MicrosoftGraphExternalLink',
    'MicrosoftGraphIdentity',
    'MicrosoftGraphNotebook',
    'MicrosoftGraphOnenote',
    'MicrosoftGraphOnenoteEntityBaseModel',
    'MicrosoftGraphOnenoteEntityHierarchyModel',
    'MicrosoftGraphOnenoteEntitySchemaObjectModel',
    'MicrosoftGraphOnenoteOperation',
    'MicrosoftGraphOnenoteOperationError',
    'MicrosoftGraphOnenotePage',
    'MicrosoftGraphOnenoteResource',
    'MicrosoftGraphOnenoteSection',
    'MicrosoftGraphOperation',
    'MicrosoftGraphPageLinks',
    'MicrosoftGraphSectionGroup',
    'OdataError',
    'OdataErrorDetail',
    'OdataErrorMain',
    'Enum10',
    'Enum100',
    'Enum101',
    'Enum102',
    'Enum103',
    'Enum104',
    'Enum105',
    'Enum106',
    'Enum107',
    'Enum108',
    'Enum109',
    'Enum110',
    'Enum111',
    'Enum112',
    'Enum113',
    'Enum114',
    'Enum115',
    'Enum116',
    'Enum117',
    'Enum118',
    'Enum119',
    'Enum12',
    'Enum120',
    'Enum121',
    'Enum122',
    'Enum123',
    'Enum124',
    'Enum125',
    'Enum126',
    'Enum127',
    'Enum128',
    'Enum129',
    'Enum130',
    'Enum131',
    'Enum132',
    'Enum133',
    'Enum134',
    'Enum135',
    'Enum136',
    'Enum137',
    'Enum138',
    'Enum139',
    'Enum14',
    'Enum140',
    'Enum141',
    'Enum142',
    'Enum143',
    'Enum144',
    'Enum145',
    'Enum146',
    'Enum147',
    'Enum148',
    'Enum149',
    'Enum15',
    'Enum150',
    'Enum151',
    'Enum152',
    'Enum153',
    'Enum154',
    'Enum155',
    'Enum156',
    'Enum157',
    'Enum158',
    'Enum159',
    'Enum16',
    'Enum160',
    'Enum161',
    'Enum162',
    'Enum163',
    'Enum164',
    'Enum165',
    'Enum166',
    'Enum167',
    'Enum168',
    'Enum169',
    'Enum17',
    'Enum170',
    'Enum171',
    'Enum172',
    'Enum173',
    'Enum174',
    'Enum175',
    'Enum176',
    'Enum177',
    'Enum178',
    'Enum179',
    'Enum18',
    'Enum180',
    'Enum181',
    'Enum182',
    'Enum183',
    'Enum184',
    'Enum185',
    'Enum186',
    'Enum187',
    'Enum188',
    'Enum189',
    'Enum19',
    'Enum190',
    'Enum191',
    'Enum192',
    'Enum193',
    'Enum194',
    'Enum195',
    'Enum196',
    'Enum197',
    'Enum198',
    'Enum199',
    'Enum200',
    'Enum201',
    'Enum202',
    'Enum203',
    'Enum204',
    'Enum205',
    'Enum206',
    'Enum207',
    'Enum208',
    'Enum209',
    'Enum21',
    'Enum210',
    'Enum211',
    'Enum212',
    'Enum213',
    'Enum214',
    'Enum215',
    'Enum216',
    'Enum217',
    'Enum218',
    'Enum219',
    'Enum220',
    'Enum221',
    'Enum222',
    'Enum223',
    'Enum224',
    'Enum225',
    'Enum226',
    'Enum227',
    'Enum228',
    'Enum229',
    'Enum23',
    'Enum230',
    'Enum231',
    'Enum232',
    'Enum233',
    'Enum234',
    'Enum235',
    'Enum236',
    'Enum237',
    'Enum238',
    'Enum239',
    'Enum24',
    'Enum240',
    'Enum241',
    'Enum242',
    'Enum243',
    'Enum244',
    'Enum245',
    'Enum246',
    'Enum247',
    'Enum248',
    'Enum249',
    'Enum25',
    'Enum250',
    'Enum251',
    'Enum252',
    'Enum253',
    'Enum254',
    'Enum255',
    'Enum256',
    'Enum257',
    'Enum258',
    'Enum259',
    'Enum26',
    'Enum260',
    'Enum261',
    'Enum262',
    'Enum263',
    'Enum264',
    'Enum265',
    'Enum266',
    'Enum267',
    'Enum268',
    'Enum269',
    'Enum27',
    'Enum270',
    'Enum271',
    'Enum272',
    'Enum273',
    'Enum274',
    'Enum275',
    'Enum276',
    'Enum277',
    'Enum278',
    'Enum279',
    'Enum28',
    'Enum280',
    'Enum281',
    'Enum282',
    'Enum283',
    'Enum284',
    'Enum285',
    'Enum286',
    'Enum287',
    'Enum288',
    'Enum289',
    'Enum29',
    'Enum290',
    'Enum291',
    'Enum292',
    'Enum293',
    'Enum294',
    'Enum295',
    'Enum296',
    'Enum297',
    'Enum298',
    'Enum299',
    'Enum300',
    'Enum301',
    'Enum302',
    'Enum303',
    'Enum304',
    'Enum305',
    'Enum306',
    'Enum307',
    'Enum308',
    'Enum309',
    'Enum31',
    'Enum310',
    'Enum311',
    'Enum312',
    'Enum313',
    'Enum314',
    'Enum315',
    'Enum316',
    'Enum317',
    'Enum318',
    'Enum319',
    'Enum32',
    'Enum320',
    'Enum321',
    'Enum322',
    'Enum323',
    'Enum324',
    'Enum325',
    'Enum326',
    'Enum327',
    'Enum328',
    'Enum329',
    'Enum33',
    'Enum330',
    'Enum331',
    'Enum332',
    'Enum333',
    'Enum334',
    'Enum335',
    'Enum336',
    'Enum337',
    'Enum338',
    'Enum339',
    'Enum34',
    'Enum340',
    'Enum341',
    'Enum342',
    'Enum343',
    'Enum344',
    'Enum345',
    'Enum346',
    'Enum347',
    'Enum348',
    'Enum349',
    'Enum35',
    'Enum350',
    'Enum351',
    'Enum352',
    'Enum353',
    'Enum354',
    'Enum355',
    'Enum356',
    'Enum357',
    'Enum358',
    'Enum359',
    'Enum36',
    'Enum360',
    'Enum361',
    'Enum362',
    'Enum363',
    'Enum364',
    'Enum365',
    'Enum37',
    'Enum38',
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
    'Enum50',
    'Enum51',
    'Enum52',
    'Enum53',
    'Enum54',
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
    'Enum7',
    'Enum70',
    'Enum71',
    'Enum72',
    'Enum73',
    'Enum74',
    'Enum75',
    'Enum76',
    'Enum77',
    'Enum78',
    'Enum79',
    'Enum80',
    'Enum81',
    'Enum82',
    'Enum83',
    'Enum84',
    'Enum85',
    'Enum86',
    'Enum87',
    'Enum88',
    'Enum89',
    'Enum9',
    'Enum90',
    'Enum91',
    'Enum92',
    'Enum93',
    'Enum94',
    'Enum95',
    'Enum96',
    'Enum97',
    'Enum98',
    'Enum99',
    'Get10ItemsItem',
    'Get11ItemsItem',
    'Get1ItemsItem',
    'Get2ItemsItem',
    'Get3ItemsItem',
    'Get4ItemsItem',
    'Get5ItemsItem',
    'Get6ItemsItem',
    'Get7ItemsItem',
    'Get8ItemsItem',
    'Get9ItemsItem',
    'MicrosoftGraphOnenoteUserRole',
    'MicrosoftGraphOperationStatus',
]
