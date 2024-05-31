



# Catena-X Taxonomy


**Title:**  Catena-X Taxonomy

**Description:**  This taxonomy represents and contains all of the concepts that are used in the Catena-X ontologies.

**Creator:**  [@obalandi](https://github.com/obalandi)

**Contributor:**  None

**Date:**  2023-05-05

**Version:**  0.1.0

**Link to ontology:**  https://w3id.org/catenax/taxonomy  

## Concepts
  

|Name|Label|Description|Broader|Narrower|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Thing">Thing</span>|Thing|The top concept of all the Catena X concepts.||[Place](#Place) , [PhysicalObject](#PhysicalObject) , [ConceptualObject](#ConceptualObject) , [Actor](#Actor) , [Activity](#Activity) |
|<span id="Place">Place</span>|Place|The Place is determined by reference to the position of objects such as buildings, cities, or special geographic markers.|[Thing](#Thing) ||
|<span id="PhysicalObject">PhysicalObject</span>|Physical Object|This concept includes objects of a material nature, which are documentation units and have physical boundaries.|[Thing](#Thing) |[Vehicle](#Vehicle) , [Part](#Part) |
|<span id="Part">Part</span>|Part|A part in the automotive context is a component of a vehicle. Parts may have sub-parts that perform specific sub-functions.|[PhysicalObject](#PhysicalObject) ||
|<span id="Vehicle">Vehicle</span>|Vehicle|A vehicle is a motor-powered road vehicle that transports people or cargo .|[PhysicalObject](#PhysicalObject) ||
|<span id="ConceptualObject">ConceptualObject</span>|Conceptional Object|This concept includes non-material products, human-produced data related to physical objects. The production of such information may have been supported by the use of technical tools.|[Thing](#Thing) |[Result](#Result) , [Address](#Address) , [Application](#Application) , [SupplyChain](#SupplyChain) , [BillOfMaterial](#BillOfMaterial) |
|<span id="BillOfMaterial">BillOfMaterial</span>|Bill Of Material|The Bill Of Material relates qualitatively and quantitatively Assembly Parts to their Components.|[ConceptualObject](#ConceptualObject) ||
|<span id="SupplyChain">SupplyChain</span>|Supply Chain|The Supply Chain relates consumers and a supplier.|[ConceptualObject](#ConceptualObject) ||
|<span id="ErrorCause">ErrorCause</span>|Error Cause|An analysis result can indicate possible and current error causes. |[ConceptualObject](#ConceptualObject) ||
|<span id="Result">Result</span>|Result|Specific conceptual outcomes of an activity or application.|[ConceptualObject](#ConceptualObject) ||
|<span id="AnalysisResult">AnalysisResult</span>|Analysis Result|Results of the analysis activity.|[Result](#Result) |[DiagnosticTroubleCode](#DiagnosticTroubleCode) , [LoadSpectrum](#LoadSpectrum) |
|<span id="LoadSpectrum">LoadSpectrum</span>|Load Spectrum|Load spectrum is a multi dimensional histogram that contains the state history of a set of vehicle parts, i.e. how a vehicle was driven, for a given time period.|[AnalysisResult](#AnalysisResult) ||
|<span id="Clutch">Clutch</span>|Clutch|Load spectrum of a vehicle clutch.|[LoadSpectrum](#LoadSpectrum) ||
|<span id="GearSet">GearSet</span>|GearSet|Load spectrum of a vehicle gear with respect to performance.|[LoadSpectrum](#LoadSpectrum) ||
|<span id="GearOil">GearOil</span>|GearOil|Load spectrum of a vehicle gear with respect to heat.|[LoadSpectrum](#LoadSpectrum) ||
|<span id="DiagnosticTroubleCode">DiagnosticTroubleCode</span>|Diagnostic Trouble Code|Diagnostic Trouble Code, is a code used to diagnose malfunctions in a vehicle.|[AnalysisResult](#AnalysisResult) ||
|<span id="Address">Address</span>|Address|The address describes the legal address of places.|[ConceptualObject](#ConceptualObject) ||
|<span id="Application">Application</span>|Application|An application defines a coded software that fulfills a specific purpose.|[ConceptualObject](#ConceptualObject) |[Asset](#Asset) , [Function](#Function) , [DataspaceConnector](#DataspaceConnector) |
|<span id="Function">Function</span>|Function|A function defines a calculation that is called through an API.|[Application](#Application) |[PrognosisFunction](#PrognosisFunction) |
|<span id="PrognosisFunction">PrognosisFunction</span>|Prognosis Function|In the automotive industry, a prognosis is a prediction of the probable failure of an operational function.|[Function](#Function) |[HealthIndication](#HealthIndication) , [RemainingUsefulLife](#RemainingUsefulLife) |
|<span id="HealthIndication">HealthIndication</span>|Health Indication|Health Indication is an evaluation function operating on batches of load collectives and adaptive values.|[PrognosisFunction](#PrognosisFunction) ||
|<span id="RemainingUsefulLife">RemainingUsefulLife</span>|Remaining Useful Life|Remaining Useful Life is a Prediction of the Estimated Mileage/Runtime until a Breakdown.|[PrognosisFunction](#PrognosisFunction) ||
|<span id="DataspaceConnector">DataspaceConnector</span>|Dataspace Connector|Dataspace Connector is an interface based on the Eclipse Dataspace Connector technology. A Dataspace Connector makes various assets available through contracts. A contract describes with which policy which asset can be provided.|[Application](#Application) ||
|<span id="Actor">Actor</span>|Actor|The actor  comprises organization or people, either individually or in groups, who have the potential to perform intentional actions of kinds for which someone may be held responsible.|[Thing](#Thing) |[BusinessPartner](#BusinessPartner) , [AnalysisDevice](#AnalysisDevice) |
|<span id="AnalysisDevice">AnalysisDevice</span>|Analysis Device|An analysis device, e.g. a diagnostic device, reads or calculates certain analysis results.|[Actor](#Actor) ||
|<span id="BusinessPartner">BusinessPartner</span>|Business Partner|A Business Partner is a legal entity that is part of the Catena-X network or that stands in a relevant relation to a Catena-X Business Partner.|[Actor](#Actor) ||
|<span id="Activity">Activity</span>|Activity|This class comprises actions intentionally carried out by instances of Actor that result in changes of state in physical and conceptual objects.|[Thing](#Thing) |[Analysis](#Analysis) |
|<span id="Analysis">Analysis</span>|Analysis|An analysis is an activity that includes all types of reliability and quality analyses.|[Activity](#Activity) |[Diagnosis](#Diagnosis) |
|<span id="LoadSpectrumAnalysis">LoadSpectrumAnalysis</span>|Load Spectrum Analysis|Load spectrum analysis is an analysis that calculates load spectrum values for a vehicle part.|[Analysis](#Analysis) ||
|<span id="Diagnosis">Diagnosis</span>|Diagnosis|Vehicle diagnosis is the identification of a problem or the cause and location of a problem.|[Analysis](#Analysis) ||
