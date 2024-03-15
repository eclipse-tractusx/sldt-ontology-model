



# Reliability Ontology


**Title:**  Reliability Ontology

**Description:**  Ontology for reliability.

**Creator:**  Zazralt Magic

**Contributor:**  Jörg Schulz, Rolf Bosse, Oguzhan Balandi 

**Date:**  2023-02-21

**Version:**  1.9.4

**Imports:**  file:core_ontology.ttl

**Link to ontology:**  https://w3id.org/catenax/ontology/reliability  
  
![ontology](images/reliability_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Analysis">Analysis</span>|None|[mileageOfVehicle](#mileageOfVehicle) , [operatingHoursOfPart](#operatingHoursOfPart) , [operatingHoursOfVehicle](#operatingHoursOfVehicle) |[analysedObject](#analysedObject) , [analysedPart](#analysedPart) , [analysedVehicle](#analysedVehicle) , [result](#result) |[Activity](./core_ontology.md#Activity) |
|<span id="AnalysisResult">AnalysisResult</span>|None|||[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="LoadSpectrum">LoadSpectrum</span>|None|[datetime](#datetime) , [description](#description) , [endDatetime](#endDatetime) , [id](#id) , [name](#name) , [type](#type) |[channel](#channel) , [class](#class) , [hasValues](#hasValues) |[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumAnalysis">LoadSpectrumAnalysis</span>|None|||[OnBoardTelematics](#OnBoardTelematics) |
|<span id="LoadSpectrumChannel">LoadSpectrumChannel</span>|None|[lowerLimit](#lowerLimit) , [name](#name) , [numberOfBins](#numberOfBins) , [type](#type) , [unit](#unit) , [upperLimit](#upperLimit) ||[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumClass">LoadSpectrumClass</span>|None|||[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumValues">LoadSpectrumValues</span>|None|[countingValue](#countingValue) , [countingMethod](#countingMethod) , [countingUnit](#countingUnit) , [index](#index) ||[AnalysisResult](#AnalysisResult) |
|<span id="OnBoardTelematics">OnBoardTelematics</span>|None|||[Analysis](#Analysis) |
|<span id="TelematicsResult">TelematicsResult</span>|None|||[AnalysisResult](#AnalysisResult) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="channels">channels</span>|None||json:Object ||
|<span id="countingValue">countingValue</span>|None|[LoadSpectrumValues](#LoadSpectrumValues) |xsd:string ||
|<span id="countingMethod">countingMethod</span>|None|[LoadSpectrumValues](#LoadSpectrumValues) |xsd:string ||
|<span id="countingUnit">countingUnit</span>|None|[LoadSpectrumValues](#LoadSpectrumValues) |xsd:string ||
|<span id="datetime">datetime</span>|None|[LoadSpectrum](#LoadSpectrum) |xsd:dateTime ||
|<span id="description">description</span>|None|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="endDatetime">endDatetime</span>|None|[LoadSpectrum](#LoadSpectrum) |xsd:dateTime ||
|<span id="id">id</span>|None|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="index">index</span>|None|[LoadSpectrumValues](#LoadSpectrumValues) |xsd:string ||
|<span id="lowerLimit">lowerLimit</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:float ||
|<span id="mileageOfVehicle">mileageOfVehicle</span>|None|[Analysis](#Analysis) |xsd:integer ||
|<span id="name">name</span>|None|[LoadSpectrum](#LoadSpectrum) , [LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="numberOfBins">numberOfBins</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:integer ||
|<span id="operatingHoursOfPart">operatingHoursOfPart</span>|None|[Analysis](#Analysis) |xsd:float ||
|<span id="operatingHoursOfVehicle">operatingHoursOfVehicle</span>|None|[Analysis](#Analysis) |xsd:float ||
|<span id="type">type</span>|None|[LoadSpectrum](#LoadSpectrum) , [LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="unit">unit</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="upperLimit">upperLimit</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:float ||
|<span id="values">values</span>|None||json:Object ||
|<span id="classes">classes</span>|None||json:Object ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="analysedObject">analysedObject</span>|None|[Analysis](#Analysis) |[PhysicalObject](./core_ontology.md#PhysicalObject) |[refersToPhysicalObject](./core_ontology.md#refersToPhysicalObject) |
|<span id="analysedPart">analysedPart</span>|None|[Analysis](#Analysis) |[Part](./vehicle_ontology.md#Part) |[analysedObject](#analysedObject) |
|<span id="analysedVehicle">analysedVehicle</span>|None|[Analysis](#Analysis) |[Vehicle](./vehicle_ontology.md#Vehicle) |[analysedObject](#analysedObject) |
|<span id="channel">channel</span>|None|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumChannel](#LoadSpectrumChannel) ||
|<span id="class">class</span>|None|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumClass](#LoadSpectrumClass) ||
|<span id="result">result</span>|None|[Analysis](#Analysis) |[AnalysisResult](#AnalysisResult) |[refersToConceptualObject](./core_ontology.md#refersToConceptualObject) |
|<span id="hasValues">hasValues</span>|None|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumValues](#LoadSpectrumValues) ||
