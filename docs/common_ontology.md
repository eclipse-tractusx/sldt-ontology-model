



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
|<span id="DataspaceConnector">DataspaceConnector</span>|Dataspace Connector is an interface based on the Eclipse Dataspace Connector technology. A Dataspace Connector makes various assets available through contracts. A contract describes with which policy which asset can be provided.|[url](#url) |[offers](#offers) ||
|<span id="FunctionAsset">FunctionAsset</span>|This subclass of Asset allows performing calculations on asset.|||[Asset](#Asset) |
|<span id="GraphAsset">GraphAsset</span>|This subclass of Asset allows arbitrary data queries to be executed on assets.|||[Asset](#Asset) |
|<span id="SkillAsset">SkillAsset</span>|This subclass of Asset allows only the execution of predefined data queries on assets.|||[Asset](#Asset) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="contentType">contentType</span>|This property describes in which format the data will be output, i.e. XML or JSON.|[Asset](#Asset) |xml:string ||
|<span id="description">description</span>|This property contains description of asset.|[Asset](#Asset) |xml:string ||
|<span id="id">id</span>|This property contains unique identifier of Bussiness Partner/Connector/Asset.|owl:Thing |xml:string ||
|<span id="isFederated">isFederated</span>|If this property is set to true, it means that this connector will federate with other connectors.|[Asset](#Asset) |xml:boolean ||
|<span id="name">name</span>|This property contains name of asset.|[Asset](#Asset) |xml:string ||
|<span id="implementsProtocol">implementsProtocol</span>|This property refers to the network protocol implemented by the asset.|[Asset](#Asset) |xml:string ||
|<span id="url">url</span>|None|[DataspaceConnector](#DataspaceConnector) |xml:anyURI ||
|<span id="authenticationInformation">authenticationInformation</span>|Base property for all authentication informations.|[AuthenticatedResource](#AuthenticatedResource) |xml:string ||
|<span id="authenticationCode">authenticationCode</span>|An authentication code under which authentication information are transmitted.|||[authenticationInformation](#authenticationInformation) |
|<span id="authenticationKey">authenticationKey</span>|An authentication key which encodes some authentication proof.|||[authenticationInformation](#authenticationInformation) |
|<span id="version">version</span>|This property contains version of asset.|[Asset](#Asset) |xml:string ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="hasDataspaceConnector">hasDataspaceConnector</span>|This property describes which connectors belong to which business partners.|[BusinessPartner](#BusinessPartner) |[DataspaceConnector](#DataspaceConnector) ||
|<span id="offers">offers</span>|This property refers to the offered assets.|[DataspaceConnector](#DataspaceConnector) |[Asset](#Asset) ||
|<span id="publishedUnderContract">publishedUnderContract</span>|This property refers to the contract associated with the asset.|[Asset](#Asset) |||
