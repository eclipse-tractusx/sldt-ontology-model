



# Common Ontology


**Title:**  Common Ontology

**Description:**  The common ontology describes the Dataspace connectors in detail. On the one hand, this includes the information from which Catena-X business partner the connectors are deployed. On the other hand, with which contracts which assets provide the connectors.

**Creator:**  [@ZazraltMagic](https://github.com/ZazraltMagic)

**Contributor:**  [@drcgjung](https://github.com/drcgjung) , [@obalandi](https://github.com/obalandi)

**Date:**  2023-05-23

**Version:**  1.9.4

**Imports:**  file:core_ontology.ttl

**Link to ontology:**  https://w3id.org/catenax/ontology/common  
  
![ontology](images/common_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Application">Application</span>|An application defines a coded software that fulfills a specific purpose.||||
|<span id="Asset">Asset</span>|The Asset class describes the provision via a repository of a specific set of data for a specific purpose.|[contentType](#contentType) , [description](#description) , [id](#id) , [name](#name) , [version](#version) , [implementsProtocol](#implementsProtocol) , [publishedUnderContract](#publishedUnderContract) , [satisfiesRole](#satisfiesRole) , [isFederated](#isFederated) , [http://www.w3.org/ns/shacl#shapesGraph](#http://www.w3.org/ns/shacl#shapesGraph) , [authenticationInformation](#authenticationInformation) , [authenticationCode](#authenticationCode) , [authenticationKey](#authenticationKey) , [distributionMode](#distributionMode) ||[Application](#Application) |
|<span id="BusinessPartner">BusinessPartner</span>|A Business Partner is a legal entity that is part of the Catena-X network or that stands in a relevant relation to a Catena-X Business Partner.||[hasDataspaceConnector](#hasDataspaceConnector) |[Actor](./core_ontology.md#Actor) |
|<span id="DataspaceConnector">DataspaceConnector</span>|Dataspace Connector is an interface based on the Eclipse Dataspace Connector technology. A Dataspace Connector makes various assets available through contracts. A contract describes with which policy which asset can be provided.|[url](#url) |[offers](#offers) |[Application](#Application) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="contentType">contentType</span>|This property describes in which format the data will be output, i.e. XML or JSON.|[Asset](#Asset) |xsd:string ||
|<span id="description">description</span>|This property contains description of asset.|[Asset](#Asset) |xsd:string ||
|<span id="id">id</span>|This property contains unique identifier of Bussiness Partner/Connector/Asset.|[Asset](#Asset) |xsd:string ||
|<span id="name">name</span>|This property contains name of asset.|[Asset](#Asset) |xsd:string ||
|<span id="version">version</span>|Version of the asset.|[Asset](#Asset) |xsd:string ||
|<span id="implementsProtocol">implementsProtocol</span>|This property refers to the network protocol implemented by the asset.|[Asset](#Asset) |xsd:string ||
|<span id="publishedUnderContract">publishedUnderContract</span>|This property refers to the contract associated with the asset.|[Asset](#Asset) |xsd:string ||
|<span id="satisfiesRole">satisfiesRole</span>|Use Case Role IRI.|[Asset](#Asset) |xsd:anyURI ||
|<span id="isFederated">isFederated</span>|If this property is set to true, it means that this connector will federate with other connectors.|[Asset](#Asset) |xsd:boolean ||
|<span id="url">url</span>||[DataspaceConnector](#DataspaceConnector) |xsd:anyURI ||
|<span id="authenticationInformation">authenticationInformation</span>|Base property for all authentication informations.|[Asset](#Asset) |xsd:string ||
|<span id="authenticationCode">authenticationCode</span>|An authentication code under which authentication information are transmitted.|[Asset](#Asset) |xsd:string |[authenticationInformation](#authenticationInformation) |
|<span id="authenticationKey">authenticationKey</span>|An authentication key which encodes some authentication proof.|[Asset](#Asset) |xsd:string |[authenticationInformation](#authenticationInformation) |
|<span id="distributionMode">distributionMode</span>|The skill may only be invoked local to the computing environment of the provider.|[Asset](#Asset) |xsd:string ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="hasDataspaceConnector">hasDataspaceConnector</span>|This property describes which connectors belong to which business partners.|[BusinessPartner](#BusinessPartner) |[DataspaceConnector](#DataspaceConnector) ||
|<span id="offers">offers</span>|This property refers to the offered assets.|[DataspaceConnector](#DataspaceConnector) |[Asset](#Asset) ||
