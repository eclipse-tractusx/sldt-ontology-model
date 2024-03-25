# Ontology Governance Process

- This document describes the Ontology Governance Process.
- This process is maintained by Catena-X e.V. Semantic Modelling Committee with technical support from the Ontology Modelling Team.
- Based on this process, the Core Ontology and its submodels Domain Ontologies are maintained.
- New ontologies can be developed and existing ontologies can be updated. If necessary, ontologies can be also deprecated.
- Ontologies can be used universally. Therefore, existing ontologies from other sources can be adapted to the Catena-X landscape.
- The ontologies are developed as part of the Tractus-X project and published on w3id.org.

#### **Core Modelling Team**
- T-Systems, Mercedes, ZF

<br/>

<div align="center"  width="100%">
  <img src="images/OGP.jpg" alt="image" width="1200" height="auto" />
</div>

<br/>

#### **Issue Content**
- Typ of Issue (New, Update, Deprecate, Integrate)
- List the use cases where it is needed.
- Description and explanation why it is needed or not
- Reason
    - New Ontology Reason
        - Please describe the new ontology and how it helps you in your Catena-X use case. Please state the business questions to be answered 
        - Query and Data Exapmles 
    - Update Reason
        - Please describe why the current version of the ontology is insufficient to serve the use case and how an update to the ontology could improve the use case 
        - Query and Data examples
    - Deprecate Reason
        - Please describe why the referenced ontology should be deprecated
    - Integration Reason
        - Please describe the relevance and benefits of the ontology.


#### **Model Deprecation Process**
- Criteria 
    - The ontology that should be deprecated exists and is not deprecated already 
    - The respective ontology does not affect existing use cases (aspect is either used in higher versions or replaced by a different aspect)
    - An ontology, which will be deprecated, is not imported into any released ontology
- To Do
    - Move the ontology to the "Deprecated" folder
    - The latest version will remain on W3id.org.
    - Add additional information to w3id.org that it is deprecated and why.

#### **Process to create new Model**
- Criteria
    - The proposed ontology does not exist already
    - The proposed ontology does not extend an existing domain but introduces a completely new domain
    - The proposal references a Catena-X use case
    - Relevant standards are mentioned/linked
    - The business questions to be solved are specified and cannot be answered by existing ontologies
- To Do
    - The new ontologies can be developed by domain experts based on the standard. If necessary, the core ontology team can collaborate.
    - Development of a new ontology in a branch
    - Create MD file

#### **Process to integrate new Model**
- The Integrate process is similar to the Create New Model process. But it's more complicated. This is because different ontologies have different design patterns. Therefore, the ontology modelling team needs to support this process from the start. Changes to the core ontology may be required. This in turn requires extensive analysis to ensure the compatibility of the domain ontologies.

#### **Update Process**
- Criteria
    - The ontology that should be updated exists
    - The referenced use case exists
    - The potential updates are discussed with all stakeholders
- To Do
    - The new ontologies can be updated by domain experts based on the standard. If necessary, the core ontology team can collaborate.
    - Create a new version
    - Update MD File

#### **Review Process**
- The ontology modelling team checks that the criteria in the standards are met:
    - Technical Modelling prerequisites
    - Syntax of Content
    - Understandability of Content
- Write a Review
- Merge the Branch or send it back to Update

#### **Publishing Process**
- Publish the new version in W3id.org
