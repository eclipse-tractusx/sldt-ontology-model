



# Core Ontology


**Title:**  Core Ontology

**Description:**  The Catena-X core ontology contains main domain-independent classes, attributes and relations.

**Creator:**  [@obalandi](https://github.com/obalandi)

**Contributor:**  None

**Date:**  2023-05-05

**Version:**  1.9.4

**Imports:**  None

**Link to ontology:**  https://w3id.org/catenax/ontology/core  
  
![ontology](images/core_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Activity">Activity</span>|None|[endDateTime](#endDateTime) , [id](#id) , [name](#name) , [startDateTime](#startDateTime) |[hasParticipant](#hasParticipant) , [refersToConceptualObject](#refersToConceptualObject) , [refersToPhysicalObject](#refersToPhysicalObject) , [takesPlaceAt](#takesPlaceAt) ||
|<span id="Actor">Actor</span>|This class comprises organization or people, either individually or in groups, who have the potential to perform intentional actions of kinds for which someone may be held responsible.|[id](#id) , [name](#name) |[participatesIn](#participatesIn) , [relatedToPlace](#relatedToPlace) ||
|<span id="Address">Address</span>|None|[street](#street) , [houseNumber](#houseNumber) , [postalCode](#postalCode) , [city](#city) , [country](#country) ||[ConceptualObject](#ConceptualObject) |
|<span id="ConceptualObject">ConceptualObject</span>|This class includes non-material products, human-produced data related to physical objects. The production of such information may have been supported by the use of technical tools.|[id](#id) , [name](#name) |[describesPhysicalObject](#describesPhysicalObject) , [involvedIn](#involvedIn) ||
|<span id="PhysicalObject">PhysicalObject</span>|This class includes objects of a material nature, which are documentation units and have physical boundaries.|[id](#id) , [name](#name) |[describedByConceptualObject](#describedByConceptualObject) , [involvedIn](#involvedIn) ||
|<span id="Place">Place</span>|None|[id](#id) , [name](#name) |[hasAddress](#hasAddress) , [hosts](#hosts) ||

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="endDateTime">endDateTime</span>|None|[Activity](#Activity) |xml:dateTime ||
|<span id="id">id</span>|None|[Activity](#Activity) , [Place](#Place) , [Actor](#Actor) , [ConceptualObject](#ConceptualObject) , [PhysicalObject](#PhysicalObject) |xml:string ||
|<span id="name">name</span>|None|[Activity](#Activity) , [Place](#Place) , [Actor](#Actor) , [ConceptualObject](#ConceptualObject) , [PhysicalObject](#PhysicalObject) |xml:string ||
|<span id="role">role</span>|None|owl:Thing |xml:string ||
|<span id="startDateTime">startDateTime</span>|None|[Activity](#Activity) |xml:dateTime ||
|<span id="street">street</span>|None|[Address](#Address) |xml:string ||
|<span id="houseNumber">houseNumber</span>|None|[Address](#Address) |xml:int ||
|<span id="postalCode">postalCode</span>|None|[Address](#Address) |xml:string ||
|<span id="city">city</span>|None|[Address](#Address) |xml:string ||
|<span id="country">country</span>|None|[Address](#Address) |xml:string ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="hasAddress">hasAddress</span>|None|[Place](#Place) |[Address](#Address) ||
|<span id="describedByConceptualObject">describedByConceptualObject</span>|Inverse of 'describes physical object' property.|[PhysicalObject](#PhysicalObject) |[ConceptualObject](#ConceptualObject) ||
|<span id="describesPhysicalObject">describesPhysicalObject</span>|None|[ConceptualObject](#ConceptualObject) |[PhysicalObject](#PhysicalObject) ||
|<span id="hasParticipant">hasParticipant</span>|None|[Activity](#Activity) |[Actor](#Actor) ||
|<span id="hosts">hosts</span>|None|[Place](#Place) |[Activity](#Activity) ||
|<span id="involvedIn">involvedIn</span>|None|[ConceptualObject](#ConceptualObject) , [PhysicalObject](#PhysicalObject) |[Activity](#Activity) ||
|<span id="participatesIn">participatesIn</span>|None|[Actor](#Actor) |[Activity](#Activity) ||
|<span id="refersToConceptualObject">refersToConceptualObject</span>|None|[Activity](#Activity) |[ConceptualObject](#ConceptualObject) ||
|<span id="refersToPhysicalObject">refersToPhysicalObject</span>|None|[Activity](#Activity) |[PhysicalObject](#PhysicalObject) ||
|<span id="relatedToPlace">relatedToPlace</span>|None|[Actor](#Actor) |[Place](#Place) ||
|<span id="takesPlaceAt">takesPlaceAt</span>|None|[Activity](#Activity) |[Place](#Place) ||
