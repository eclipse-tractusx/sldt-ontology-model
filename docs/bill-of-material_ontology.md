



# Bill Of Material Ontology


**Title:**  Bill Of Material Ontology

**Description:**  Ontology for bills of material.

**Creator:**  [@drcgjung](https://github.com/drcgjung)

**Contributor:**  [@obalandi](https://github.com/obalandi)

**Date:**  2023-09-08

**Version:**  0.10.3

**Imports:**  file:common_ontology.ttl , file:core_ontology.ttl 

**Link to ontology:**  https://w3id.org/catenax/ontology/bill-of-material  
  
![ontology](images/bill-of-material_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="BillOfMaterial">BillOfMaterial</span>|The Bill Of Material relates qualitatively and quantitatively Assembly Parts to their Components.|[quantity](#quantity) , [quantityMeasure](#quantityMeasure) , [quantityUnit](#quantityUnit) , [validityPeriod](#validityPeriod) , [validityPeriodEnd](#validityPeriodEnd) , [validityPeriodStart](#validityPeriodStart) |[assembler](#assembler) , [assembly](#assembly) , [assemblyConcept](#assemblyConcept) , [component](#component) , [concept](#concept) , [supplier](#supplier) |[ConceptualObject](./core_ontology.md#ConceptualObject) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="quantity">quantity</span>|Describes the quantity of the BOM.|[BillOfMaterial](#BillOfMaterial) |||
|<span id="quantityMeasure">quantityMeasure</span>|The measure of quantity that a component contributes to an assymbly in a bill of material .|[BillOfMaterial](#BillOfMaterial) |xsd:float |[quantity](#quantity) |
|<span id="quantityUnit">quantityUnit</span>|The unit of quantity that a component contributes to an assymbly in a bill of material .|[BillOfMaterial](#BillOfMaterial) |xsd:string |[quantity](#quantity) |
|<span id="validityPeriod">validityPeriod</span>|Describes the validity period.|[BillOfMaterial](#BillOfMaterial) |||
|<span id="validityPeriodEnd">validityPeriodEnd</span>|The end of validity.|[BillOfMaterial](#BillOfMaterial) |xsd:date |[validityPeriod](#validityPeriod) |
|<span id="validityPeriodStart">validityPeriodStart</span>|The start of validity.|[BillOfMaterial](#BillOfMaterial) |xsd:date |[validityPeriod](#validityPeriod) |

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="assembler">assembler</span>|The assembler of the assembly.|[BillOfMaterial](#BillOfMaterial) |[BusinessPartner](./common_ontology.md#BusinessPartner) ||
|<span id="assembly">assembly</span>|Refers the assembly of a bill of material.|[BillOfMaterial](#BillOfMaterial) |[PhysicalObject](./core_ontology.md#PhysicalObject) ||
|<span id="assemblyConcept">assemblyConcept</span>|Refers the assembly concept of a bill of material.|[BillOfMaterial](#BillOfMaterial) |[ConceptualObject](./core_ontology.md#ConceptualObject) ||
|<span id="component">component</span>|Lists the components of a bill of material.|[BillOfMaterial](#BillOfMaterial) |[PhysicalObject](./core_ontology.md#PhysicalObject) ||
|<span id="concept">concept</span>|Lists the concepts of a bill of material.|[BillOfMaterial](#BillOfMaterial) |[ConceptualObject](./core_ontology.md#ConceptualObject) ||
|<span id="hasBom">hasBom</span>|Refers the bill of material of an assembly.|[PhysicalObject](./core_ontology.md#PhysicalObject) |[BillOfMaterial](#BillOfMaterial) ||
|<span id="supplier">supplier</span>|The supplier of the component(s).|[BillOfMaterial](#BillOfMaterial) |[BusinessPartner](./common_ontology.md#BusinessPartner) ||


```python
import Mdutils


mdFile = MdUtils(file_name='Example_Markdown',title='Markdown File Example')
mdFile.create_md_file()
```