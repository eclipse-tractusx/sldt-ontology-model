



# Reliability Ontology


**Title:**  Reliability Ontology

**Description:**  None

**Creator:**  [@ZazraltMagic](https://github.com/ZazraltMagic)

**Contributor:**  [@Joerg-Schulz](https://github.com/Joerg-Schulz), [@bosserf](https://github.com/bosserf), [@obalandi](https://github.com/obalandi), [@drcgjung](https://github.com/drcgjung)

**Date:**  2023-02-21

**Version:**  1.11.0

**Imports:**  file:core_ontology.ttl , file:vehicle_ontology.ttl 

**Link to ontology:**  https://w3id.org/catenax/ontology/reliability  


```mermaid
classDiagram 
   class Activity~core~{
   } 
   class Actor~core~{
   } 
   class PhysicalObject~core~{
   } 
   class ConceptualObject~core~{
   } 
   class Part~vehicle~{
   } 
   class Vehicle~vehicle~{
   } 
   class Analysis~reliability~{
       mileageOfVehicle integer
       operatingHoursOfPart float
       operatingHoursOfVehicle float
   } 
   class AnalysisDevice~reliability~{
   } 
   class AnalysisResult~reliability~{
   } 
   class Diagnosis~reliability~{
   } 
   class DiagnosticTroubleCode~reliability~{
       diagnosticTroubleCodeId string
       diagnosticTroubleCodeName string
   } 
   class ErrorCause~reliability~{
   } 
   class LoadSpectrum~reliability~{
       datetime dateTime
       description string
       endDatetime dateTime
       id string
       name string
       type string
   } 
   class LoadSpectrumAnalysis~reliability~{
   } 
   class LoadSpectrumChannel~reliability~{
       lowerLimit float
       numberOfBins integer
       type string
       unit string
       upperLimit float
   } 
   class LoadSpectrumClass~reliability~{
   } 
   class LoadSpectrumValue~reliability~{
       countingMethod string
       countingUnit string
       countingValue string
       index string
   } 
   DiagnosticTroubleCode --> ErrorCause : actualCause
   Analysis --> PhysicalObject : analysedObject
   Analysis --> Part : analysedPart
   Analysis --> Vehicle : analysedVehicle
   AnalysisDevice --> Analysis : performs
   LoadSpectrum --> LoadSpectrumChannel : channel
   LoadSpectrum --> LoadSpectrumClass : class
   Diagnosis --> DiagnosticTroubleCode : hasDiagnosticTroubleCode
   DiagnosticTroubleCode --> ErrorCause : possibleCause
   Analysis --> AnalysisResult : result
   LoadSpectrum --> LoadSpectrumValue : value
   Analysis --|> Activity
   AnalysisDevice --|> Actor
   AnalysisResult --|> ConceptualObject
   ErrorCause --|> ConceptualObject
   Diagnosis --|> Analysis
   LoadSpectrumAnalysis --|> Analysis
   DiagnosticTroubleCode --|> AnalysisResult
   LoadSpectrum --|> AnalysisResult
   LoadSpectrumChannel --|> AnalysisResult
   LoadSpectrumClass --|> AnalysisResult
   LoadSpectrumValue --|> AnalysisResult

```  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Analysis">Analysis</span>|An analysis is an activity that includes all types of reliability and quality analyses.|[mileageOfVehicle](#mileageOfVehicle) , [operatingHoursOfPart](#operatingHoursOfPart) , [operatingHoursOfVehicle](#operatingHoursOfVehicle) |[analysedObject](#analysedObject) , [analysedPart](#analysedPart) , [analysedVehicle](#analysedVehicle) , [result](#result) |[Activity](./core_ontology.md#Activity) |
|<span id="AnalysisDevice">AnalysisDevice</span>|An analysis device, e.g. a diagnostic device, reads or calculates certain analysis results.||[performs](#performs) |[Actor](./core_ontology.md#Actor) |
|<span id="AnalysisResult">AnalysisResult</span>|Results of the analysis activity.|||[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="Diagnosis">Diagnosis</span>|Vehicle diagnosis is the identification of a problem or the cause and location of a problem.||[hasDiagnosticTroubleCode](#hasDiagnosticTroubleCode) |[Analysis](#Analysis) |
|<span id="DiagnosticTroubleCode">DiagnosticTroubleCode</span>|Diagnostic Trouble Code, is a code used to diagnose malfunctions in a vehicle.|[diagnosticTroubleCodeId](#diagnosticTroubleCodeId) , [diagnosticTroubleCodeName](#diagnosticTroubleCodeName) |[actualCause](#actualCause) , [possibleCause](#possibleCause) |[AnalysisResult](#AnalysisResult) |
|<span id="ErrorCause">ErrorCause</span>|An analysis result can indicate possible and current error causes.  Example: Temperature values above a certain limit indicate overheating.|||[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="LoadSpectrum">LoadSpectrum</span>|Load spectrum is a 2d histogram that contains the load history of a vehicle, i.e. how a vehicle was used, for a given time period.|[datetime](#datetime) , [description](#description) , [endDatetime](#endDatetime) , [id](#id) , [name](#name) , [type](#type) |[channel](#channel) , [class](#class) , [value](#value) |[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumAnalysis">LoadSpectrumAnalysis</span>|Load spectrum analysis is an analysis that calculates load spectrum values for a vehicle part.|||[Analysis](#Analysis) |
|<span id="LoadSpectrumChannel">LoadSpectrumChannel</span>|The channel contains information about the axis of the 1d or 2d histogram.|[lowerLimit](#lowerLimit) , [numberOfBins](#numberOfBins) , [type](#type) , [unit](#unit) , [upperLimit](#upperLimit) ||[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumClass">LoadSpectrumClass</span>|The class contains information about the quantization states related to an axis.|||[AnalysisResult](#AnalysisResult) |
|<span id="LoadSpectrumValue">LoadSpectrumValue</span>|The values contains a list or a matrix with count values of the histogram.|[countingMethod](#countingMethod) , [countingUnit](#countingUnit) , [countingValue](#countingValue) , [index](#index) ||[AnalysisResult](#AnalysisResult) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="countingMethod">countingMethod</span>|Counting method of Load spectrum.|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="countingUnit">countingUnit</span>|Counting unit of load spectrum.|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="countingValue">countingValue</span>|Counting value of load spectrum.|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="datetime">datetime</span>|Start of the measurement of load spectrum.|[LoadSpectrum](#LoadSpectrum) |xsd:dateTime ||
|<span id="description">description</span>|Details about the load spectrum: who, what, where, when, how?|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="diagnosticTroubleCodeId">diagnosticTroubleCodeId</span>|Id of diagnostic trouble code.|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |xsd:string ||
|<span id="diagnosticTroubleCodeName">diagnosticTroubleCodeName</span>|Name of diagnostic trouble code.|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |xsd:string |[name](#name) |
|<span id="endDatetime">endDatetime</span>|End of the measurement of load spectrum.|[LoadSpectrum](#LoadSpectrum) |xsd:dateTime ||
|<span id="id">id</span>|Id of load spectrum.|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="index">index</span>|Index of load spectrum values.|[LoadSpectrumValue](#LoadSpectrumValue) |xsd:string ||
|<span id="lowerLimit">lowerLimit</span>|Lower limit of load spectrum channel.|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:float ||
|<span id="mileageOfVehicle">mileageOfVehicle</span>|Mileage of analysed vehicle.|[Analysis](#Analysis) |xsd:integer ||
|<span id="name">name</span>|Name of load spectrum|[LoadSpectrum](#LoadSpectrum) |xsd:string ||
|<span id="numberOfBins">numberOfBins</span>|Bins number of load spectrum channel.|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:integer ||
|<span id="operatingHoursOfPart">operatingHoursOfPart</span>|Operating hours Of analysed part.|[Analysis](#Analysis) |xsd:float ||
|<span id="operatingHoursOfVehicle">operatingHoursOfVehicle</span>|Operating hours Of  vehicle.|[Analysis](#Analysis) |xsd:float ||
|<span id="type">type</span>|Type of load spectrum.|[LoadSpectrum](#LoadSpectrum) , [LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="unit">unit</span>|Unit of load spectrum.|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:string ||
|<span id="upperLimit">upperLimit</span>|Upper limit of load spectrum.|[LoadSpectrumChannel](#LoadSpectrumChannel) |xsd:float ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="actualCause">actualCause</span>|Refers to the actual error cause.|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |[ErrorCause](#ErrorCause) ||
|<span id="analysedObject">analysedObject</span>|Refers to analysed object.|[Analysis](#Analysis) |[PhysicalObject](./core_ontology.md#PhysicalObject) |[refersToPhysicalObject](./core_ontology.md#refersToPhysicalObject) |
|<span id="analysedPart">analysedPart</span>|Refers to the analysed part.|[Analysis](#Analysis) |[Part](./vehicle_ontology.md#Part) |[analysedObject](#analysedObject) |
|<span id="analysedVehicle">analysedVehicle</span>|Refers to the analysed vehicle.|[Analysis](#Analysis) |[Vehicle](./vehicle_ontology.md#Vehicle) |[analysedObject](#analysedObject) |
|<span id="performs">performs</span>|A device performs an analysis.|[AnalysisDevice](#AnalysisDevice) |[Analysis](#Analysis) ||
|<span id="channel">channel</span>|Refers to load spectrum channel.|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumChannel](#LoadSpectrumChannel) ||
|<span id="class">class</span>|Refers to load spectrum class.|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumClass](#LoadSpectrumClass) ||
|<span id="hasDiagnosticTroubleCode">hasDiagnosticTroubleCode</span>|Refers to diagnostic trouble code.|[Diagnosis](#Diagnosis) |[DiagnosticTroubleCode](#DiagnosticTroubleCode) ||
|<span id="possibleCause">possibleCause</span>|Refers to possible cause.|[DiagnosticTroubleCode](#DiagnosticTroubleCode) |[ErrorCause](#ErrorCause) ||
|<span id="result">result</span>|Refers to analysis result.|[Analysis](#Analysis) |[AnalysisResult](#AnalysisResult) |[refersToConceptualObject](./core_ontology.md#refersToConceptualObject) |
|<span id="value">value</span>|Refers to load spectrum value.|[LoadSpectrum](#LoadSpectrum) |[LoadSpectrumValue](#LoadSpectrumValue) ||
