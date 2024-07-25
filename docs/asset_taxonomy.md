# Asset Taxonomy

**Title:**  Asset Taxonomy

**Description:**  This taxonomy represents and contains concepts of the asset.

**Creator:**  [@arnoweiss](https://github.com/arnoweiss)

**Contributor:**  None

**Date:**  2024-01-01

**Version:**  0.1.0

**Link to ontology:**  https://w3id.org/catenax/taxonomy  

## Concepts
  

|Name|Label|Description|Broader|Narrower|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Asset">Asset</span>|Asset|The Asset concept describes the provision via a repository of a specific set of data for a specific purpose. It is defined by its public API.|[ConceptionalObject](#ConceptionalObject) ||
|<span id="DigitalTwinRegistry">DigitalTwinRegistry</span>|Digital Twin Registry|The Digital Twin Registry (DTR) is the union of the Catena-X-selected subsets of the Asset Administration Shell Registry and Discovery APIs.|[Asset](#Asset) ||
|<span id="Submodel">Submodel</span>|Submodel|The Submodel API serves aspects of a Digital Twin according to the Asset Administration Shell standard.|[Asset](#Asset) ||
|<span id="ReceiveQualityInvestigationNotification">ReceiveQualityInvestigationNotification</span>|Receive Quality Investigation Notification|API to receive quality investigation notifications|[Asset](#Asset) ||
|<span id="ReceiveQualityAlertNotification">ReceiveQualityAlertNotification</span>|Receive Quality Alert Notification|API to receive quality alert notifications|[Asset](#Asset) ||
|<span id="UpdateQualityInvestigationNotification">UpdateQualityInvestigationNotification</span>|Update Quality Investigation Notification|API to update quality investigation notifications|[Asset](#Asset) ||
|<span id="UpdateQualityAlertNotification">UpdateQualityAlertNotification</span>|Update Quality Alert Notification|API to update quality Alert notifications|[Asset](#Asset) ||
|<span id="ResolveQualityInvestigationNotification">ResolveQualityInvestigationNotification</span>|Resolve Quality Investigation Notification|API to update quality investigation notifications|[Asset](#Asset) ||
|<span id="ResolveQualityAlertNotification">ResolveQualityAlertNotification</span>|Resolve Quality Alert Notification|API to resolve quality Alert notifications|[Asset](#Asset) ||
|<span id="ReceiveUniqueIdPushNotification">ReceiveUniqueIdPushNotification</span>|Receive Unique ID Push Notification|API to receive Unique Id Push notifications|[Asset](#Asset) ||
|<span id="UniqueIdPushConnectToParentNotification">UniqueIdPushConnectToParentNotification</span>|Unique ID Push Connect-to-Parent Notification|API to receive a Unique ID Push notification to connect a digital twin with its parent digital twin (bottom-up notification)|[Asset](#Asset) ||
|<span id="UniqueIdPushConnectToChildNotification">UniqueIdPushConnectToChildNotification</span>|Unique ID Push Connect-to-Child Notification|API to receive a Unique ID Push notification to connect a digital twin with its child digital twin (top-down notification)|[Asset](#Asset) ||
|<span id="PcfExchange">PcfExchange</span>|PCF Exchange API|API to exchange data on Product Carbon Footprints|[Asset](#Asset) ||
|<span id="GraphAsset">GraphAsset</span>|Graph Asset|This subconcept of Asset allows arbitrary data queries to be executed on assets.|[Asset](#Asset) ||
|<span id="SkillAsset">SkillAsset</span>|Skill Asset|This subconcept of Asset allows only the execution of predefined data queries on assets.|[Asset](#Asset) ||
|<span id="QualityAsset">QualityAsset</span>|Quality Asset|This subconcept of Asset signifies that a data offer is associated with the Quality use-case. Assets and data offers are further specified by the dcat:conformsTo property.|[Asset](#Asset) ||
|<span id="DcmMaterialDemand">DcmMaterialDemand</span>|Receive Material Demand DCM|API to receive a Material Demand in DCM context|[Asset](#Asset) ||
|<span id="DcmWeekBasedMaterialDemand">DcmWeekBasedMaterialDemand</span>|Receive Week Based Material Demand DCM|API to receive a Week Based Material Demand in DCM context|[Asset](#Asset) ||
|<span id="DcmWeekBasedCapacityGroup">DcmWeekBasedCapacityGroup</span>|Receive Week Based Capacity Group DCM|API to receive a Week Based Capacity Group in DCM context|[Asset](#Asset) ||
|<span id="DcmIdBasedRequestForUpdate">DcmIdBasedRequestForUpdate</span>|Receive ID Based Request for Update DCM|API to receive an ID Based Request for Update in DCM context|[Asset](#Asset) ||
|<span id="DcmIdBasedComment">DcmIdBasedComment</span>|Receive ID Based Comment for DCM|API to receive an ID Based Comment in DCM context|[Asset](#Asset) ||

## NOTICE

This work is licensed under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

- Copyright (c) 2024 T-Systems International GmbH
- Copyright (c) 2024 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
- Copyright (c) 2024 ZF Friedrichshafen AG 
- Copyright (c) 2024 Mercedes-Benz AG 
- Copyright (c) 2024 SAP AG
- Copyright (c) 2024 Catena-X Association
- Copyright (c) 2024 Contributors to the Eclipse Foundation
