



# Reliability Ontology


**Title:**  Reliability Ontology

**Description:**  None

**Creator:**  [@ZazraltMagic](https://github.com/ZazraltMagic)

**Contributor:**  [@Joerg-Schulz](https://github.com/Joerg-Schulz), [@bosserf](https://github.com/bosserf), [@obalandi](https://github.com/obalandi), [@drcgjung](https://github.com/drcgjung)

**Date:**  2023-02-21

**Version:**  1.9.4

**Imports:**  file:core_ontology.ttl , file:vehicle_ontology.ttl 

**Link to ontology:**  https://w3id.org/catenax/ontology/reliability  
  
![ontology](images/reliability_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Analysis">Analysis</span>|An analysis is an activity that includes all types of reliability and quality analyses.|[mileageOfVehicle](#mileageOfVehicle) , [operatingHoursOfPart](#operatingHoursOfPart) , [operatingHoursOfVehicle](#operatingHoursOfVehicle) |[analysedObject](#analysedObject) , [analysedPart](#analysedPart) , [analysedVehicle](#analysedVehicle) , [result](#result) |[Activity](./core_ontology.md#Activity) |
|<span id="AnalysisDevice">AnalysisDevice</span>|An analysis device, e.g. a diagnostic device, reads or calculates certain analysis results.||[carryOut](#carryOut) |[Actor](./core_ontology.md#Actor) |
|<span id="AnalysisResult">AnalysisResult</span>|Results of the analysis activity.|||[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="Diagnosis">Diagnosis</span>|Vehicle diagnosis is the identification of a problem or the cause and location of a problem.||[hasDiagnosticTroubleCode](#hasDiagnosticTroubleCode) |[Analysis](#Analysis) |
|<span id="DiagnosticTroubleCode">DiagnosticTroubleCode</span>|None|[diagnosticTroubleCodeId](#diagnosticTroubleCodeId) , [diagnosticTroubleCodeName](#diagnosticTroubleCodeName) |[actualCause](#actualCause) , [possibleCause](#possibleCause) |[AnalysisResult](#AnalysisResult) |
|<span id="ErrorCause">ErrorCause</span>|An analysis result can indicate possible and current error causes.  Example: Temperature values above a certain limit indicate overheating.|||[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="LoadSpectrum">LoadSpectrum</span>|Load spectrum is a 2d histogram that contains the load history of a vehicle, i.e. how a vehicle was used, for a given time period.|[datetime](#datetime) , [description](#description) , [endDatetime](#endDatetime) , [id](#id) , [name](#name) , [type](#type) |[channel](#channel) , [class](#class) , [value](#value) |[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumAnalysis">LoadSpectrumAnalysis</span>|Load spectrum analysis is an analysis that calculates load spectrum values for a vehicle part.|||[Analysis](#Analysis) |
|<span id="LoadSpectrumChannel">LoadSpectrumChannel</span>|The channel contains information about the axis of the 1d or 2d histogram.|[lowerLimit](#lowerLimit) , [name](#name) , [numberOfBins](#numberOfBins) , [type](#type) , [unit](#unit) , [upperLimit](#upperLimit) ||[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumClass">LoadSpectrumClass</span>|The class contains information about the quantization states related to an axis.|||[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumValue">LoadSpectrumValue</span>|The values contains a list or a matrix with count values of the histogram.|[countingMethod](#countingMethod) , [countingUnit](#countingUnit) , [countingValue](#countingValue) , [index](#index) ||[AnalysisResult](#AnalysisResult) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="countingMethod">countingMethod</span>|None|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="countingUnit">countingUnit</span>|None|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="countingValue">countingValue</span>|None|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="datetime">datetime</span>|start of the measurement of load spectrum|[LoadSpectrum](#LoadSpectrum) |xsd:dateTime ||
|<span id="description">description</span>|details about the load spectrum: who, what, where, when, how?|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="diagnosticTroubleCodeId">diagnosticTroubleCodeId</span>|None|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |xsd:string ||
|<span id="diagnosticTroubleCodeName">diagnosticTroubleCodeName</span>|None|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |xsd:string |[name](#name) |
|<span id="endDatetime">endDatetime</span>|end of the measurement of load spectrum|[LoadSpectrum](#LoadSpectrum) |xsd:dateTime ||
|<span id="id">id</span>|None|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="index">index</span>|None|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="lowerLimit">lowerLimit</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:float ||
|<span id="mileageOfVehicle">mileageOfVehicle</span>|None|[Analysis](#Analysis) |xsd:integer ||
|<span id="name">name</span>|None|[LoadSpectrum](#LoadSpectrum) , [LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="numberOfBins">numberOfBins</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:integer ||
|<span id="operatingHoursOfPart">operatingHoursOfPart</span>|None|[Analysis](#Analysis) |xsd:float ||
|<span id="operatingHoursOfVehicle">operatingHoursOfVehicle</span>|None|[Analysis](#Analysis) |xsd:float ||
|<span id="type">type</span>|None|[LoadSpectrum](#LoadSpectrum) , [LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="unit">unit</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="upperLimit">upperLimit</span>|None|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:float ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="actualCause">actualCause</span>|None|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |[ErrorCause](#ErrorCause) ||
|<span id="analysedObject">analysedObject</span>|None|[Analysis](#Analysis) |[PhysicalObject](./core_ontology.md#PhysicalObject) |[refersToPhysicalObject](./core_ontology.md#refersToPhysicalObject) |
|<span id="analysedPart">analysedPart</span>|None|[Analysis](#Analysis) |[Part](./vehicle_ontology.md#Part) |[analysedObject](#analysedObject) |
|<span id="analysedVehicle">analysedVehicle</span>|None|[Analysis](#Analysis) |[Vehicle](./vehicle_ontology.md#Vehicle) |[analysedObject](#analysedObject) |
|<span id="carryOut">carryOut</span>|None|[AnalysisDevice](#AnalysisDevice) |[Analysis](#Analysis) ||
|<span id="channel">channel</span>|None|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumChannel](#LoadSpectrumChannel) ||
|<span id="class">class</span>|None|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumClass](#LoadSpectrumClass) ||
|<span id="hasDiagnosticTroubleCode">hasDiagnosticTroubleCode</span>|None|[Diagnosis](#Diagnosis) |[DiagnosticTroubleCode](#DiagnosticTroubleCode) ||
|<span id="possibleCause">possibleCause</span>|None|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |[ErrorCause](#ErrorCause) ||
|<span id="result">result</span>|None|[Analysis](#Analysis) |[AnalysisResult](#AnalysisResult) |[refersToConceptualObject](./core_ontology.md#refersToConceptualObject) |
|<span id="value">value</span>|None|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumValue](#LoadSpectrumValue) ||
