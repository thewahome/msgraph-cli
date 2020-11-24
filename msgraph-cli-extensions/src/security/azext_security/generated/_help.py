# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['security'] = """
    type: group
    short-summary: security
"""

helps['security get-security'] = """
    type: command
    short-summary: "Get Security"
"""

helps['security update-security'] = """
    type: command
    short-summary: "Update Security"
"""

helps['security'] = """
    type: group
    short-summary: security
"""

helps['security delete'] = """
    type: command
    short-summary: "Delete navigation property secureScores for Security"
"""

helps['security create-alert'] = """
    type: command
    short-summary: "Create new navigation property to alerts for Security"
    parameters:
      - name: --cloud-app-states
        short-summary: "Security-related stateful information generated by the provider about the cloud application/s \
related to this alert."
        long-summary: |
            Usage: --cloud-app-states destination-service-ip=XX destination-service-name=XX risk-score=XX

            destination-service-ip: Destination IP Address of the connection to the cloud application/service.
            destination-service-name: Cloud application/service name (for example 'Salesforce', 'DropBox', etc.).
            risk-score: Provider-generated/calculated risk score of the Cloud Application/Service. Recommended value \
range of 0-1, which equates to a percentage.

            Multiple actions can be specified by using more than one --cloud-app-states argument.
      - name: --file-states
        short-summary: "Security-related stateful information generated by the provider about the file(s) related to \
this alert."
        long-summary: |
            Usage: --file-states name=XX path=XX risk-score=XX hash-type=XX hash-value=XX

            name: File name (without path).
            path: Full file path of the file/imageFile.
            risk-score: Provider generated/calculated risk score of the alert file. Recommended value range of 0-1, \
which equates to a percentage.
            hash-value: Value of the file hash.

            Multiple actions can be specified by using more than one --file-states argument.
      - name: --history-states
        long-summary: |
            Usage: --history-states app-id=XX assigned-to=XX comments=XX feedback=XX status=XX updated-date-time=XX \
user=XX


            Multiple actions can be specified by using more than one --history-states argument.
      - name: --host-states
        short-summary: "Security-related stateful information generated by the provider about the host(s) related to \
this alert."
        long-summary: |
            Usage: --host-states fqdn=XX is-azure-ad-joined=XX is-azure-ad-registered=XX \
is-hybrid-azure-domain-joined=XX net-bios-name=XX os=XX private-ip-address=XX public-ip-address=XX risk-score=XX

            fqdn: Host FQDN (Fully Qualified Domain Name) (for example, machine.company.com).
            is-hybrid-azure-domain-joined: True if the host is domain joined to an on-premises Active Directory \
domain.
            net-bios-name: The local host name, without the DNS domain name.
            os: Host Operating System. (For example, Windows10, MacOS, RHEL, etc.).
            private-ip-address: Private (not routable) IPv4 or IPv6 address (see RFC 1918) at the time of the alert.
            public-ip-address: Publicly routable IPv4 or IPv6 address (see RFC 1918) at time of the alert.
            risk-score: Provider-generated/calculated risk score of the host.  Recommended value range of 0-1, which \
equates to a percentage.

            Multiple actions can be specified by using more than one --host-states argument.
      - name: --malware-states
        short-summary: "Threat Intelligence pertaining to malware related to this alert."
        long-summary: |
            Usage: --malware-states category=XX family=XX name=XX severity=XX was-running=XX

            category: Provider-generated malware category (for example, trojan, ransomware, etc.).
            family: Provider-generated malware family (for example, 'wannacry', 'notpetya', etc.).
            name: Provider-generated malware variant name (for example, Trojan:Win32/Powessere.H).
            severity: Provider-determined severity of this malware.
            was-running: Indicates whether the detected file (malware/vulnerability) was running at the time of \
detection or was detected at rest on the disk.

            Multiple actions can be specified by using more than one --malware-states argument.
      - name: --network-connections
        short-summary: "Security-related stateful information generated by the provider about the network \
connection(s) related to this alert."
        long-summary: |
            Usage: --network-connections application-name=XX destination-address=XX destination-domain=XX \
destination-location=XX destination-port=XX destination-url=XX direction=XX domain-registered-date-time=XX \
local-dns-name=XX nat-destination-address=XX nat-destination-port=XX nat-source-address=XX nat-source-port=XX \
protocol=XX risk-score=XX source-address=XX source-location=XX source-port=XX status=XX url-parameters=XX

            application-name: Name of the application managing the network connection (for example, Facebook or SMTP).
            destination-address: Destination IP address (of the network connection).
            destination-domain: Destination domain portion of the destination URL. (for example 'www.contoso.com').
            destination-location: Location (by IP address mapping) associated with the destination of a network \
connection.
            destination-port: Destination port (of the network connection).
            destination-url: Network connection URL/URI string - excluding parameters. (for example \
'www.contoso.com/products/default.html')
            domain-registered-date-time: Date when the destination domain was registered. The Timestamp type \
represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan \
1, 2014 would look like this: '2014-01-01T00:00:00Z'
            local-dns-name: The local DNS name resolution as it appears in the host's local DNS cache (for example, in \
case the 'hosts' file was tampered with).
            nat-destination-address: Network Address Translation destination IP address.
            nat-destination-port: Network Address Translation destination port.
            nat-source-address: Network Address Translation source IP address.
            nat-source-port: Network Address Translation source port.
            risk-score: Provider generated/calculated risk score of the network connection. Recommended value range of \
0-1, which equates to a percentage.
            source-address: Source (i.e. origin) IP address (of the network connection).
            source-location: Location (by IP address mapping) associated with the source of a network connection.
            source-port: Source (i.e. origin) IP port (of the network connection).
            url-parameters: Parameters (suffix) of the destination URL.

            Multiple actions can be specified by using more than one --network-connections argument.
      - name: --registry-key-states
        short-summary: "Security-related stateful information generated by the provider about the registry keys \
related to this alert."
        long-summary: |
            Usage: --registry-key-states hive=XX key=XX old-key=XX old-value-data=XX old-value-name=XX operation=XX \
process-id=XX value-data=XX value-name=XX value-type=XX

            key: Current (i.e. changed) registry key (excludes HIVE).
            old-key: Previous (i.e. before changed) registry key (excludes HIVE).
            old-value-data: Previous (i.e. before changed) registry key value data (contents).
            old-value-name: Previous (i.e. before changed) registry key value name.
            process-id: Process ID (PID) of the process that modified the registry key (process details will appear in \
the alert 'processes' collection).
            value-data: Current (i.e. changed) registry key value data (contents).
            value-name: Current (i.e. changed) registry key value name

            Multiple actions can be specified by using more than one --registry-key-states argument.
      - name: --security-resources
        short-summary: "Resources related to current alert. For example, for some alerts this can have the Azure \
Resource value."
        long-summary: |
            Usage: --security-resources resource=XX resource-type=XX

            resource: Name of the resource that is related to current alert. Required.

            Multiple actions can be specified by using more than one --security-resources argument.
      - name: --triggers
        short-summary: "Security-related information about the specific properties that triggered the alert \
(properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip \
addresses. This field indicates which properties triggered the alert generation."
        long-summary: |
            Usage: --triggers name=XX type=XX value=XX

            name: Name of the property serving as a detection trigger.
            type: Type of the property in the key:value pair for interpretation. For example, String, Boolean, etc.
            value: Value of the property serving as a detection trigger.

            Multiple actions can be specified by using more than one --triggers argument.
      - name: --user-states
        short-summary: "Security-related stateful information generated by the provider about the user accounts \
related to this alert."
        long-summary: |
            Usage: --user-states aad-user-id=XX account-name=XX domain-name=XX email-role=XX is-vpn=XX \
logon-date-time=XX logon-id=XX logon-ip=XX logon-location=XX logon-type=XX on-premises-security-identifier=XX \
risk-score=XX user-account-type=XX user-principal-name=XX

            aad-user-id: AAD User object identifier (GUID) - represents the physical/multi-account user entity.
            account-name: Account name of user account (without Active Directory domain or DNS domain) - (also called \
mailNickName).
            domain-name: NetBIOS/Active Directory domain of user account (that is, domain/account format).
            is-vpn: Indicates whether the user logged on through a VPN.
            logon-date-time: Time at which the sign-in occurred. The Timestamp type represents date and time \
information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like \
this: '2014-01-01T00:00:00Z'.
            logon-id: User sign-in ID.
            logon-ip: IP Address the sign-in request originated from.
            logon-location: Location (by IP address mapping) associated with a user sign-in event by this user.
            on-premises-security-identifier: Active Directory (on-premises) Security Identifier (SID) of the user.
            risk-score: Provider-generated/calculated risk score of the user account. Recommended value range of 0-1, \
which equates to a percentage.
            user-principal-name: User sign-in name - internet format: (user account name)@(user account DNS domain \
name).

            Multiple actions can be specified by using more than one --user-states argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
      - name: --vulnerability-states
        short-summary: "Threat intelligence pertaining to one or more vulnerabilities related to this alert."
        long-summary: |
            Usage: --vulnerability-states cve=XX severity=XX was-running=XX

            cve: Common Vulnerabilities and Exposures (CVE) for the vulnerability.
            severity: Base Common Vulnerability Scoring System (CVSS) severity score for this vulnerability.
            was-running: Indicates whether the detected vulnerability (file) was running at the time of detection or \
was the file detected at rest on the disk.

            Multiple actions can be specified by using more than one --vulnerability-states argument.
"""

helps['security create-secure-score'] = """
    type: command
    short-summary: "Create new navigation property to secureScores for Security"
    parameters:
      - name: --average-comparative-scores
        short-summary: "Average score by different scopes (for example, average by industry, average by seating) and \
control category (Identity, Data, Device, Apps, Infrastructure) within the scope."
        long-summary: |
            Usage: --average-comparative-scores average-score=XX basis=XX

            average-score: Average score within specified basis.
            basis: Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.

            Multiple actions can be specified by using more than one --average-comparative-scores argument.
      - name: --control-scores
        short-summary: "Contains tenant scores for a set of controls."
        long-summary: |
            Usage: --control-scores control-category=XX control-name=XX description=XX score=XX

            control-category: Control action category (Identity, Data, Device, Apps, Infrastructure).
            control-name: Control unique name.
            description: Description of the control.
            score: Tenant achieved score for the control (it varies day by day depending on tenant operations on the \
control).

            Multiple actions can be specified by using more than one --control-scores argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""

helps['security create-secure-score-control-profile'] = """
    type: command
    short-summary: "Create new navigation property to secureScoreControlProfiles for Security"
    parameters:
      - name: --compliance-information
        long-summary: |
            Usage: --compliance-information certification-controls=XX certification-name=XX

            certification-controls: Collection of the certification controls associated with certification
            certification-name: Compliance certification name (for example, ISO 27018:2014, GDPR, FedRAMP, NIST \
800-171)

            Multiple actions can be specified by using more than one --compliance-information argument.
      - name: --control-state-updates
        long-summary: |
            Usage: --control-state-updates assigned-to=XX comment=XX state=XX updated-by=XX updated-date-time=XX

            assigned-to: Assigns the control to the user who will take the action.
            comment: Provides optional comment about the control.
            state: State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
            updated-by: ID of the user who updated tenant state.
            updated-date-time: Time at which the control state was updated.

            Multiple actions can be specified by using more than one --control-state-updates argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""

helps['security get-alert'] = """
    type: command
    short-summary: "Get alerts from Security"
"""

helps['security get-secure-score'] = """
    type: command
    short-summary: "Get secureScores from Security"
"""

helps['security get-secure-score-control-profile'] = """
    type: command
    short-summary: "Get secureScoreControlProfiles from Security"
"""

helps['security list-alert'] = """
    type: command
    short-summary: "Get alerts from Security"
"""

helps['security list-secure-score'] = """
    type: command
    short-summary: "Get secureScores from Security"
"""

helps['security list-secure-score-control-profile'] = """
    type: command
    short-summary: "Get secureScoreControlProfiles from Security"
"""

helps['security update-alert'] = """
    type: command
    short-summary: "Update the navigation property alerts in Security"
    parameters:
      - name: --cloud-app-states
        short-summary: "Security-related stateful information generated by the provider about the cloud application/s \
related to this alert."
        long-summary: |
            Usage: --cloud-app-states destination-service-ip=XX destination-service-name=XX risk-score=XX

            destination-service-ip: Destination IP Address of the connection to the cloud application/service.
            destination-service-name: Cloud application/service name (for example 'Salesforce', 'DropBox', etc.).
            risk-score: Provider-generated/calculated risk score of the Cloud Application/Service. Recommended value \
range of 0-1, which equates to a percentage.

            Multiple actions can be specified by using more than one --cloud-app-states argument.
      - name: --file-states
        short-summary: "Security-related stateful information generated by the provider about the file(s) related to \
this alert."
        long-summary: |
            Usage: --file-states name=XX path=XX risk-score=XX hash-type=XX hash-value=XX

            name: File name (without path).
            path: Full file path of the file/imageFile.
            risk-score: Provider generated/calculated risk score of the alert file. Recommended value range of 0-1, \
which equates to a percentage.
            hash-value: Value of the file hash.

            Multiple actions can be specified by using more than one --file-states argument.
      - name: --history-states
        long-summary: |
            Usage: --history-states app-id=XX assigned-to=XX comments=XX feedback=XX status=XX updated-date-time=XX \
user=XX


            Multiple actions can be specified by using more than one --history-states argument.
      - name: --host-states
        short-summary: "Security-related stateful information generated by the provider about the host(s) related to \
this alert."
        long-summary: |
            Usage: --host-states fqdn=XX is-azure-ad-joined=XX is-azure-ad-registered=XX \
is-hybrid-azure-domain-joined=XX net-bios-name=XX os=XX private-ip-address=XX public-ip-address=XX risk-score=XX

            fqdn: Host FQDN (Fully Qualified Domain Name) (for example, machine.company.com).
            is-hybrid-azure-domain-joined: True if the host is domain joined to an on-premises Active Directory \
domain.
            net-bios-name: The local host name, without the DNS domain name.
            os: Host Operating System. (For example, Windows10, MacOS, RHEL, etc.).
            private-ip-address: Private (not routable) IPv4 or IPv6 address (see RFC 1918) at the time of the alert.
            public-ip-address: Publicly routable IPv4 or IPv6 address (see RFC 1918) at time of the alert.
            risk-score: Provider-generated/calculated risk score of the host.  Recommended value range of 0-1, which \
equates to a percentage.

            Multiple actions can be specified by using more than one --host-states argument.
      - name: --malware-states
        short-summary: "Threat Intelligence pertaining to malware related to this alert."
        long-summary: |
            Usage: --malware-states category=XX family=XX name=XX severity=XX was-running=XX

            category: Provider-generated malware category (for example, trojan, ransomware, etc.).
            family: Provider-generated malware family (for example, 'wannacry', 'notpetya', etc.).
            name: Provider-generated malware variant name (for example, Trojan:Win32/Powessere.H).
            severity: Provider-determined severity of this malware.
            was-running: Indicates whether the detected file (malware/vulnerability) was running at the time of \
detection or was detected at rest on the disk.

            Multiple actions can be specified by using more than one --malware-states argument.
      - name: --network-connections
        short-summary: "Security-related stateful information generated by the provider about the network \
connection(s) related to this alert."
        long-summary: |
            Usage: --network-connections application-name=XX destination-address=XX destination-domain=XX \
destination-location=XX destination-port=XX destination-url=XX direction=XX domain-registered-date-time=XX \
local-dns-name=XX nat-destination-address=XX nat-destination-port=XX nat-source-address=XX nat-source-port=XX \
protocol=XX risk-score=XX source-address=XX source-location=XX source-port=XX status=XX url-parameters=XX

            application-name: Name of the application managing the network connection (for example, Facebook or SMTP).
            destination-address: Destination IP address (of the network connection).
            destination-domain: Destination domain portion of the destination URL. (for example 'www.contoso.com').
            destination-location: Location (by IP address mapping) associated with the destination of a network \
connection.
            destination-port: Destination port (of the network connection).
            destination-url: Network connection URL/URI string - excluding parameters. (for example \
'www.contoso.com/products/default.html')
            domain-registered-date-time: Date when the destination domain was registered. The Timestamp type \
represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan \
1, 2014 would look like this: '2014-01-01T00:00:00Z'
            local-dns-name: The local DNS name resolution as it appears in the host's local DNS cache (for example, in \
case the 'hosts' file was tampered with).
            nat-destination-address: Network Address Translation destination IP address.
            nat-destination-port: Network Address Translation destination port.
            nat-source-address: Network Address Translation source IP address.
            nat-source-port: Network Address Translation source port.
            risk-score: Provider generated/calculated risk score of the network connection. Recommended value range of \
0-1, which equates to a percentage.
            source-address: Source (i.e. origin) IP address (of the network connection).
            source-location: Location (by IP address mapping) associated with the source of a network connection.
            source-port: Source (i.e. origin) IP port (of the network connection).
            url-parameters: Parameters (suffix) of the destination URL.

            Multiple actions can be specified by using more than one --network-connections argument.
      - name: --registry-key-states
        short-summary: "Security-related stateful information generated by the provider about the registry keys \
related to this alert."
        long-summary: |
            Usage: --registry-key-states hive=XX key=XX old-key=XX old-value-data=XX old-value-name=XX operation=XX \
process-id=XX value-data=XX value-name=XX value-type=XX

            key: Current (i.e. changed) registry key (excludes HIVE).
            old-key: Previous (i.e. before changed) registry key (excludes HIVE).
            old-value-data: Previous (i.e. before changed) registry key value data (contents).
            old-value-name: Previous (i.e. before changed) registry key value name.
            process-id: Process ID (PID) of the process that modified the registry key (process details will appear in \
the alert 'processes' collection).
            value-data: Current (i.e. changed) registry key value data (contents).
            value-name: Current (i.e. changed) registry key value name

            Multiple actions can be specified by using more than one --registry-key-states argument.
      - name: --security-resources
        short-summary: "Resources related to current alert. For example, for some alerts this can have the Azure \
Resource value."
        long-summary: |
            Usage: --security-resources resource=XX resource-type=XX

            resource: Name of the resource that is related to current alert. Required.

            Multiple actions can be specified by using more than one --security-resources argument.
      - name: --triggers
        short-summary: "Security-related information about the specific properties that triggered the alert \
(properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip \
addresses. This field indicates which properties triggered the alert generation."
        long-summary: |
            Usage: --triggers name=XX type=XX value=XX

            name: Name of the property serving as a detection trigger.
            type: Type of the property in the key:value pair for interpretation. For example, String, Boolean, etc.
            value: Value of the property serving as a detection trigger.

            Multiple actions can be specified by using more than one --triggers argument.
      - name: --user-states
        short-summary: "Security-related stateful information generated by the provider about the user accounts \
related to this alert."
        long-summary: |
            Usage: --user-states aad-user-id=XX account-name=XX domain-name=XX email-role=XX is-vpn=XX \
logon-date-time=XX logon-id=XX logon-ip=XX logon-location=XX logon-type=XX on-premises-security-identifier=XX \
risk-score=XX user-account-type=XX user-principal-name=XX

            aad-user-id: AAD User object identifier (GUID) - represents the physical/multi-account user entity.
            account-name: Account name of user account (without Active Directory domain or DNS domain) - (also called \
mailNickName).
            domain-name: NetBIOS/Active Directory domain of user account (that is, domain/account format).
            is-vpn: Indicates whether the user logged on through a VPN.
            logon-date-time: Time at which the sign-in occurred. The Timestamp type represents date and time \
information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like \
this: '2014-01-01T00:00:00Z'.
            logon-id: User sign-in ID.
            logon-ip: IP Address the sign-in request originated from.
            logon-location: Location (by IP address mapping) associated with a user sign-in event by this user.
            on-premises-security-identifier: Active Directory (on-premises) Security Identifier (SID) of the user.
            risk-score: Provider-generated/calculated risk score of the user account. Recommended value range of 0-1, \
which equates to a percentage.
            user-principal-name: User sign-in name - internet format: (user account name)@(user account DNS domain \
name).

            Multiple actions can be specified by using more than one --user-states argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
      - name: --vulnerability-states
        short-summary: "Threat intelligence pertaining to one or more vulnerabilities related to this alert."
        long-summary: |
            Usage: --vulnerability-states cve=XX severity=XX was-running=XX

            cve: Common Vulnerabilities and Exposures (CVE) for the vulnerability.
            severity: Base Common Vulnerability Scoring System (CVSS) severity score for this vulnerability.
            was-running: Indicates whether the detected vulnerability (file) was running at the time of detection or \
was the file detected at rest on the disk.

            Multiple actions can be specified by using more than one --vulnerability-states argument.
"""

helps['security update-secure-score'] = """
    type: command
    short-summary: "Update the navigation property secureScores in Security"
    parameters:
      - name: --average-comparative-scores
        short-summary: "Average score by different scopes (for example, average by industry, average by seating) and \
control category (Identity, Data, Device, Apps, Infrastructure) within the scope."
        long-summary: |
            Usage: --average-comparative-scores average-score=XX basis=XX

            average-score: Average score within specified basis.
            basis: Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.

            Multiple actions can be specified by using more than one --average-comparative-scores argument.
      - name: --control-scores
        short-summary: "Contains tenant scores for a set of controls."
        long-summary: |
            Usage: --control-scores control-category=XX control-name=XX description=XX score=XX

            control-category: Control action category (Identity, Data, Device, Apps, Infrastructure).
            control-name: Control unique name.
            description: Description of the control.
            score: Tenant achieved score for the control (it varies day by day depending on tenant operations on the \
control).

            Multiple actions can be specified by using more than one --control-scores argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""

helps['security update-secure-score-control-profile'] = """
    type: command
    short-summary: "Update the navigation property secureScoreControlProfiles in Security"
    parameters:
      - name: --compliance-information
        long-summary: |
            Usage: --compliance-information certification-controls=XX certification-name=XX

            certification-controls: Collection of the certification controls associated with certification
            certification-name: Compliance certification name (for example, ISO 27018:2014, GDPR, FedRAMP, NIST \
800-171)

            Multiple actions can be specified by using more than one --compliance-information argument.
      - name: --control-state-updates
        long-summary: |
            Usage: --control-state-updates assigned-to=XX comment=XX state=XX updated-by=XX updated-date-time=XX

            assigned-to: Assigns the control to the user who will take the action.
            comment: Provides optional comment about the control.
            state: State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
            updated-by: ID of the user who updated tenant state.
            updated-date-time: Time at which the control state was updated.

            Multiple actions can be specified by using more than one --control-state-updates argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""
