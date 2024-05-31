



# Supply Chain Ontology


**Title:**  Supply Chain Ontology

**Description:**  Ontology for supply chains.

**Creator:**  [@drcgjung](https://github.com/drcgjung)

**Contributor:**  [@obalandi](https://github.com/obalandi)

**Date:**  2023-12-12

**Version:**  0.12.0

**Imports:**  file:core_ontology.ttl , file:common_ontology.ttl 

**Link to ontology:**  https://w3id.org/catenax/ontology/supply-chain  


```mermaid
classDiagram 
   class BusinessPartner~common~{
   } 
   class ConceptualObject~core~{
   } 
   class PhysicalObject~core~{
   } 
   class SupplyChain~supply-chain~{
       validityPeriodEnd date
       validityPeriodStart date
   } 
   SupplyChain --> PhysicalObject : good
   SupplyChain --> BusinessPartner : recipient
   SupplyChain --> BusinessPartner : supplier
   SupplyChain --|> ConceptualObject

```  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="SupplyChain">SupplyChain</span>|The Supply Chain relates consumers and a supplier.|[validityPeriod](#validityPeriod) , [validityPeriodEnd](#validityPeriodEnd) , [validityPeriodStart](#validityPeriodStart) |[good](#good) , [recipient](#recipient) , [supplier](#supplier) |[ConceptualObject](./core_ontology.md#ConceptualObject) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="validityPeriod">validityPeriod</span>|Defines the validity period.|[SupplyChain](#SupplyChain) |||
|<span id="validityPeriodEnd">validityPeriodEnd</span>|The end of validity.|[SupplyChain](#SupplyChain) |xsd:date |[validityPeriod](#validityPeriod) |
|<span id="validityPeriodStart">validityPeriodStart</span>|The start of validity.|[SupplyChain](#SupplyChain) |xsd:date |[validityPeriod](#validityPeriod) |

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="good">good</span>|Refers to the goods in the supply chain.|[SupplyChain](#SupplyChain) |[PhysicalObject](./core_ontology.md#PhysicalObject) ||
|<span id="recipient">recipient</span>|Refers to the recipient.|[SupplyChain](#SupplyChain) |[BusinessPartner](./common_ontology.md#BusinessPartner) ||
|<span id="supplier">supplier</span>|Refers to the supplier.|[SupplyChain](#SupplyChain) |[BusinessPartner](./common_ontology.md#BusinessPartner) ||
