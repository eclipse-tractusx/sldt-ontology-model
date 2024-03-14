



# Common Ontology


**Title:**  Common Ontology

**Description:**  The common ontology describes the Dataspace connectors in detail. On the one hand, this includes the information from which Catena-X business partner the connectors are deployed. On the other hand, with which contracts which assets provide the connectors.

**Creator:**  Zazralt Magic

**Contributor:**  Oguzhan Balandi

**Date:**  2023-05-23

**Version:**  1.9.4

**Imports:**  None

**Link to ontology:**  https://w3id.org/catenax/ontology/common  
  
![ontology](images/common_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Asset">Asset</span>|None|[contentType](#contentType) , [description](#description) , [isFederated](#isFederated) , [name](#name) , [implementsProtocol](#implementsProtocol) , [version](#version) |[publishedUnderContract](#publishedUnderContract) , [http://www.w3.org/ns/shacl#shapesGraph](#http://www.w3.org/ns/shacl#shapesGraph) ||
|<span id="BusinessPartner">BusinessPartner</span>|None||[hasDataspaceConnector](#hasDataspaceConnector) ||
|<span id="DataspaceConnector">DataspaceConnector</span>|None|[url](#url) |[offers](#offers) ||
|<span id="FunctionAsset">FunctionAsset</span>|None|||[Asset](#Asset) |
|<span id="GraphAsset">GraphAsset</span>|None|||[Asset](#Asset) |
|<span id="SkillAsset">SkillAsset</span>|None|||[Asset](#Asset) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="contentType">contentType</span>|None|[Asset](#Asset) |xml:string ||
|<span id="description">description</span>|None|[Asset](#Asset) |xml:string ||
|<span id="id">id</span>|None|owl:Thing |xml:string ||
|<span id="isFederated">isFederated</span>|None|[Asset](#Asset) |xml:boolean ||
|<span id="name">name</span>|None|[Asset](#Asset) |xml:string ||
|<span id="implementsProtocol">implementsProtocol</span>|None|[Asset](#Asset) |xml:string ||
|<span id="url">url</span>|None|[DataspaceConnector](#DataspaceConnector) |xml:anyURI ||
|<span id="authenticationInformation">authenticationInformation</span>|None|[AuthenticatedResource](#AuthenticatedResource) |xml:string ||
|<span id="authenticationCode">authenticationCode</span>|None|||[authenticationInformation](#authenticationInformation) |
|<span id="authenticationKey">authenticationKey</span>|None|||[authenticationInformation](#authenticationInformation) |
|<span id="version">version</span>|None|[Asset](#Asset) |xml:string ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="hasDataspaceConnector">hasDataspaceConnector</span>|None|[BusinessPartner](#BusinessPartner) |[DataspaceConnector](#DataspaceConnector) ||
|<span id="offers">offers</span>|None|[DataspaceConnector](#DataspaceConnector) |[Asset](#Asset) ||
|<span id="publishedUnderContract">publishedUnderContract</span>|None|[Asset](#Asset) |||
