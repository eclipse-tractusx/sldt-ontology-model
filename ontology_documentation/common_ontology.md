# Common Ontology

The common ontology describes the Dataspace connectors in detail. On the one hand, this includes the information from which Catena-X business partner the connectors are deployed. On the other hand, with which contracts which assets provide the connectors. All this information is provided in the Catena-X main repository so that the connectors are findable.

![core ontology](images/catenaX_common_ontology.jpg)

### Business Partner

* **Description:**
A Business Partner is a legal entity that is part of the Catena-X network or that stands in a relevant relation to a Catena-X Business Partner.

* **Properties:**	
    * **id:** This property contains unique identifier of business partner.
    * **has dataspace connector:** This property describes which connectors belong to which business partners.

### Dataspace Connector
* **Description:**
Dataspace Connector is an interface based on the Eclipse Dataspace Connector technology. A Dataspace Connector makes various assets available through contracts. A contract describes with which policy which asset can be provided.

* **Properties:**	
    * **id:** This property contains unique identifier of dataspace connector.
    * **url:** This property refers to the URL of the dataspace connectors. A connector can offers multiple assets through one URL. 
    * **offers:** This property refers to the offered assets.

### Asset
* **Description:**
The Asset class describes the provision via a repository of a specific set of data for a specific purpose.

* **Properties:**	
    * **id:** This property contains unique identifier of asset. 
    * **name:**  This property contains name of asset. 
    * **description:** This property contains description of asset.
    * **version:** This property contains version of asset.
    * **protocol:** This property refers to the used protocol.
    * **content type:** This property describes in which format the data will be output, i.e. XML or JSON.
    * **shape graph:** This property refes to SHACL file, in which the RDF data Contraints are defined. In particular, the structure of the identifiers.
    * **rdfs:isDefinedBy:** This property refers to the ontology of the RDF data provided.
    * **is federated:** If this property is set to true, it means that this connector will federate with other connectors.

* **SubClasses:**	
    * **Graph Asset:** This subclass of Asset allows arbitrary data queries to be executed on assets. 
    * **Skill Asset:** This subclass of Asset allows only the execution of predefined data queries on assets. 
    * **Function Asset:** This subclass of Asset allows performing calculations on asset. 
