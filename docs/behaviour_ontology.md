



# Behaviour Ontology


**Title:**  Behaviour Ontology

**Description:**  The Behaviour Ontology is an implementation of the Function Ontology for behaviour predictions. It contains prognosis functions for specific vehicle parts.

**Creator:**  [@drcgjung](https://github.com/drcgjung)

**Contributor:**  [@obalandi](https://github.com/obalandi)

**Date:**  2023-07-04

**Version:**  1.9.5

**Imports:**  file:function_ontology.ttl , file:vehicle_ontology.ttl 

**Link to ontology:**  https://w3id.org/catenax/ontology/behaviour  


```mermaid
classDiagram 
   class Object~https://json-schema.org/draft/2020-12/schema~{
   } 
   class HealthIndication~behaviour~{
       HealthIndicationArgument anyType
       adaptionValueList string
       adaptionValueMileage string
       adaptionValueOperatingTime string
       adaptionValueTimestamp string
       adaptionValueVersion string
       classifiedLoadCollectiveChannels string
       classifiedLoadCollectiveClasses string
       classifiedLoadCollectiveComponentDescription string
       classifiedLoadCollectiveCountingMethod string
       classifiedLoadCollectiveCountingUnit string
       classifiedLoadCollectiveCountingValue string
       classifiedLoadCollectiveCounts string
       classifiedLoadCollectiveProjectDescription string
       requestComponentId string
   } 
   class HealthIndicatorResult~behaviour~{
       healthIndicatorValues Object
       indicatorVersion string
       responseComponentId string
   } 
   class PrognosisFunction~behaviour~{
       bodyClasses Object
       bodyCountsList Object
       headerChannels Object
       countingMethod string
       countingUnit string
       countingValue string
       observationType anyURI
   } 
   class RemainingUsefulLife~behaviour~{
       metadata Object
       notification Object
       RemainingUsefulLifeArgument anyType
       classification string
       recipient anyURI
       recipientConnector anyURI
       sender anyURI
       senderConnector anyURI
       severity string
       status string
       statusDate dateTime
       statusMileage int
       statusOperatingHours float
       targetDate dateTime
       timeStamp dateTime
   } 
   class RemainingUsefulLifeResult~behaviour~{
       remainingOperatingHours float
       remainingRunningDistance int
   } 
   class Function~function~{
   } 
   class Result~function~{
   } 
   class Part~vehicle~{
   } 
   PrognosisFunction --> Object : bodyClasses
   PrognosisFunction --> Object : bodyCountsList
   RemainingUsefulLife --> Part : component
   PrognosisFunction --> Object : headerChannels
   HealthIndicatorResult --> Object : healthIndicatorValues
   RemainingUsefulLife --> Object : metadata
   RemainingUsefulLife --> Object : notification
   HealthIndication --|> PrognosisFunction
   RemainingUsefulLife --|> PrognosisFunction
   HealthIndicatorResult --|> Result
   RemainingUsefulLifeResult --|> Result
   PrognosisFunction --|> Function

```  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="HealthIndication">HealthIndication</span>|Health Indication is an evaluation function operating on batches of load collectives and adaptive values.|[HealthIndicationArgument](#HealthIndicationArgument) , [adaptionValueList](#adaptionValueList) , [adaptionValueMileage](#adaptionValueMileage) , [adaptionValueOperatingTime](#adaptionValueOperatingTime) , [adaptionValueTimestamp](#adaptionValueTimestamp) , [adaptionValueVersion](#adaptionValueVersion) , [classifiedLoadCollectiveChannels](#classifiedLoadCollectiveChannels) , [classifiedLoadCollectiveClasses](#classifiedLoadCollectiveClasses) , [classifiedLoadCollectiveComponentDescription](#classifiedLoadCollectiveComponentDescription) , [classifiedLoadCollectiveCountingMethod](#classifiedLoadCollectiveCountingMethod) , [classifiedLoadCollectiveCountingUnit](#classifiedLoadCollectiveCountingUnit) , [classifiedLoadCollectiveCountingValue](#classifiedLoadCollectiveCountingValue) , [classifiedLoadCollectiveCounts](#classifiedLoadCollectiveCounts) , [classifiedLoadCollectiveProjectDescription](#classifiedLoadCollectiveProjectDescription) , [requestComponentId](#requestComponentId) ||[PrognosisFunction](#PrognosisFunction) |
|<span id="HealthIndicatorResult">HealthIndicatorResult</span>|Health Indicator is part of a indicator batch.|[healthIndicatorValues](#healthIndicatorValues) , [indicatorVersion](#indicatorVersion) , [responseComponentId](#responseComponentId) |[healthIndicatorValues](#healthIndicatorValues) |[Result](./function_ontology.md#Result) |
|<span id="PrognosisFunction">PrognosisFunction</span>|Super class of prognosis functions.|[bodyClasses](#bodyClasses) , [bodyCountsList](#bodyCountsList) , [headerChannels](#headerChannels) , [countingMethod](#countingMethod) , [countingUnit](#countingUnit) , [countingValue](#countingValue) , [observationType](#observationType) , [prognosisFunctionArgument](#prognosisFunctionArgument) |[bodyClasses](#bodyClasses) , [bodyCountsList](#bodyCountsList) , [headerChannels](#headerChannels) |[Function](./function_ontology.md#Function) |
|<span id="RemainingUsefulLife">RemainingUsefulLife</span>|Remaining Useful Life is a Prediction of the Estimated Mileage/Runtime until a Breakdown.|[metadata](#metadata) , [notification](#notification) , [RemainingUsefulLifeArgument](#RemainingUsefulLifeArgument) , [classification](#classification) , [recipient](#recipient) , [recipientConnector](#recipientConnector) , [sender](#sender) , [senderConnector](#senderConnector) , [severity](#severity) , [status](#status) , [statusDate](#statusDate) , [statusMileage](#statusMileage) , [statusOperatingHours](#statusOperatingHours) , [targetDate](#targetDate) , [timeStamp](#timeStamp) |[component](#component) , [metadata](#metadata) , [notification](#notification) |[PrognosisFunction](#PrognosisFunction) |
|<span id="RemainingUsefulLifeResult">RemainingUsefulLifeResult</span>|The asynchronous notification response.|[remainingOperatingHours](#remainingOperatingHours) , [remainingRunningDistance](#remainingRunningDistance) ||[Result](./function_ontology.md#Result) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="HealthIndicationArgument">HealthIndicationArgument</span>|Super property of health indication function arguments.|[HealthIndication](#HealthIndication) |xsd:anyType |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="RemainingUsefulLifeArgument">RemainingUsefulLifeArgument</span>|Super property of remaining useful life function arguments.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:anyType |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="adaptionValueList">adaptionValueList</span>|A Health Indicator Adaption needs an array of adaption values.|[HealthIndication](#HealthIndication) |xsd:string |[HealthIndicationArgument](#HealthIndicationArgument) |
|<span id="adaptionValueMileage">adaptionValueMileage</span>|A Health Indicator Adaption needs a mileage of the embedding vehicle.|[HealthIndication](#HealthIndication) |xsd:string |[HealthIndicationArgument](#HealthIndicationArgument) |
|<span id="adaptionValueOperatingTime">adaptionValueOperatingTime</span>|A Health Indicator Adaption needs an operating time of the embedding vehicle.|[HealthIndication](#HealthIndication) |xsd:string |[HealthIndicationArgument](#HealthIndicationArgument) |
|<span id="adaptionValueTimestamp">adaptionValueTimestamp</span>|A Health Indicator Adaption needs a timestamp.|[HealthIndication](#HealthIndication) |xsd:string |[HealthIndicationArgument](#HealthIndicationArgument) |
|<span id="adaptionValueVersion">adaptionValueVersion</span>|A Health Indicator Adaption needs a version.|[HealthIndication](#HealthIndication) |xsd:string |[HealthIndicationArgument](#HealthIndicationArgument) |
|<span id="bodyClasses">bodyClasses</span>|Classes of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="bodyCountsList">bodyCountsList</span>|Counts List of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classification">classification</span>|Classification of the notification.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveChannels">classifiedLoadCollectiveChannels</span>|A Load Collective has descriptors for all channels.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveClasses">classifiedLoadCollectiveClasses</span>|A Load Collective has a body with the class indices.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveComponentDescription">classifiedLoadCollectiveComponentDescription</span>|A Load Collective has a component description.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveCountingMethod">classifiedLoadCollectiveCountingMethod</span>|A Load Collective has a method for the counting dimension.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveCountingUnit">classifiedLoadCollectiveCountingUnit</span>|A Load Collective has a unit for the counting dimension.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveCountingValue">classifiedLoadCollectiveCountingValue</span>|A Load Collective has a value for the counting dimension.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveCounts">classifiedLoadCollectiveCounts</span>|A Load Collective has a body with the raw measurements.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="classifiedLoadCollectiveProjectDescription">classifiedLoadCollectiveProjectDescription</span>|A Load Collective has a project description.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="countingMethod">countingMethod</span>|Counting Method of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="countingUnit">countingUnit</span>|Counting Unit of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="countingValue">countingValue</span>|Counting Value Name of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="headerChannels">headerChannels</span>|Channels of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="healthIndicatorValues">healthIndicatorValues</span>|Health Indicator Values are percentages.|[HealthIndicatorResult](#HealthIndicatorResult) |json:Object |[returnValue](./function_ontology.md#returnValue) |
|<span id="indicatorVersion">indicatorVersion</span>|Version of the health indicator prognosis.|[HealthIndicatorResult](#HealthIndicatorResult) |xsd:string |[returnValue](./function_ontology.md#returnValue) |
|<span id="metadata">metadata</span>|Additional Metadata of the Loadspectrum.|[RemainingUsefulLife](#RemainingUsefulLife) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="notification">notification</span>|An optional notification output template.|[RemainingUsefulLife](#RemainingUsefulLife) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="observationType">observationType</span>|None|[PrognosisFunction](#PrognosisFunction) |xsd:anyURI |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="prognosisFunctionArgument">prognosisFunctionArgument</span>|Prognosis Function Argument|[PrognosisFunction](#PrognosisFunction) |||
|<span id="recipient">recipient</span>|Recipient of the notification as a BPN.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:anyURI |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="recipientConnector">recipientConnector</span>|Recipient Address of the notification as a URL.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:anyURI |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="remainingOperatingHours">remainingOperatingHours</span>|Predicted Operating Hours of Remaining Useful Life Response|[RemainingUsefulLifeResult](#RemainingUsefulLifeResult) |xsd:float |[returnValue](./function_ontology.md#returnValue) |
|<span id="remainingRunningDistance">remainingRunningDistance</span>|Predicted Distance of Remaining Useful Life Response|[RemainingUsefulLifeResult](#RemainingUsefulLifeResult) |xsd:int |[returnValue](./function_ontology.md#returnValue) |
|<span id="requestComponentId">requestComponentId</span>|A Health Indicator Input relates to a component.|[HealthIndication](#HealthIndication) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="responseComponentId">responseComponentId</span>|Component Id of the health indicator prognosis.|[HealthIndicatorResult](#HealthIndicatorResult) |xsd:string |[returnValue](./function_ontology.md#returnValue) |
|<span id="sender">sender</span>|Sender of the notification as a BPN.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:anyURI |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="senderConnector">senderConnector</span>|Sender Address of the notification as a URL.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:anyURI |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="severity">severity</span>|Severity of the notification.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="status">status</span>|Status of the notification.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:string |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="statusDate">statusDate</span>|Time of Recording.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:dateTime |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="statusMileage">statusMileage</span>|Mileage of Component at Time of Recording.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:int |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="statusOperatingHours">statusOperatingHours</span>|Operating Hours of Target Component at Time of Recording.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:float |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="targetDate">targetDate</span>|Target Date of the notification.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:dateTime |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="timeStamp">timeStamp</span>|Timestamp of the notification.|[RemainingUsefulLife](#RemainingUsefulLife) |xsd:dateTime |[prognosisFunctionArgument](#prognosisFunctionArgument) |

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="bodyClasses">bodyClasses</span>|Classes of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="bodyCountsList">bodyCountsList</span>|Counts List of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="component">component</span>|Component of the Predicition.|[RemainingUsefulLife](#RemainingUsefulLife) |[Part](./vehicle_ontology.md#Part) ||
|<span id="headerChannels">headerChannels</span>|Channels of Load Spectrum.|[PrognosisFunction](#PrognosisFunction) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="healthIndicatorValues">healthIndicatorValues</span>|Health Indicator Values are percentages.|[HealthIndicatorResult](#HealthIndicatorResult) |json:Object |[returnValue](./function_ontology.md#returnValue) |
|<span id="metadata">metadata</span>|Additional Metadata of the Loadspectrum.|[RemainingUsefulLife](#RemainingUsefulLife) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |
|<span id="notification">notification</span>|An optional notification output template.|[RemainingUsefulLife](#RemainingUsefulLife) |json:Object |[prognosisFunctionArgument](#prognosisFunctionArgument) |

## NOTICE

This work is licensed under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

- Copyright (c) 2024 T-Systems International GmbH
- Copyright (c) 2024 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
- Copyright (c) 2024 ZF Friedrichshafen AG 
- Copyright (c) 2024 Mercedes-Benz AG 
- Copyright (c) 2024 SAP AG
- Copyright (c) 2024 Catena-X Association
- Copyright (c) 2024 Contributors to the Eclipse Foundation
