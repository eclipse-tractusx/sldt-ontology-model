



# Function Ontology


**Title:**  Function Ontology

**Description:**  Ontology for function invocations.

**Creator:**  Christoph Jung

**Contributor:**  Oguzhan Balandi

**Date:**  2023-06-29

**Version:**  1.9.4

**Imports:**  file:common_ontology.ttl

**Link to ontology:**  https://w3id.org/catenax/ontology/function  
  
![ontology](images/function_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="Argument">Argument</span>|None|[argumentName](#argumentName) , [dataType](#dataType) , [default](#default) , [priority](#priority) ||[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="Function">Function</span>|None|[batch](#batch) , [callbackProperty](#callbackProperty) , [inputProperty](#inputProperty) , [invocationIdProperty](#invocationIdProperty) , [invocationMethod](#invocationMethod) , [targetUri](#targetUri) |[input](#input) , [result](#result) |[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="Result">Result</span>|None|[callbackProperty](#callbackProperty) , [outputProperty](#outputProperty) , [resultIdProperty](#resultIdProperty) |[output](#output) |[ConceptualObject](./core_ontology.md#ConceptualObject) |
|<span id="ReturnValue">ReturnValue</span>|None|[dataType](#dataType) , [valuePath](#valuePath) ||[ConceptualObject](./core_ontology.md#ConceptualObject) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="argumentName">argumentName</span>|None|[Argument](#Argument) |xml:string ||
|<span id="batch">batch</span>|None|[Function](#Function) |xml:long ||
|<span id="callbackProperty">callbackProperty</span>|None|[Function](#Function) , [Result](#Result) |xml:string ||
|<span id="dataType">dataType</span>|None|[Argument](#Argument) , [ReturnValue](#ReturnValue) |||
|<span id="default">default</span>|None|[Argument](#Argument) |xml:anyType ||
|<span id="inputProperty">inputProperty</span>|None|[Function](#Function) |xml:string ||
|<span id="invocationIdProperty">invocationIdProperty</span>|None|[Function](#Function) |xml:string ||
|<span id="invocationMethod">invocationMethod</span>|None|[Function](#Function) |xml:string ||
|<span id="outputProperty">outputProperty</span>|None|[Result](#Result) |xml:string ||
|<span id="priority">priority</span>|None|[Argument](#Argument) |xml:integer ||
|<span id="resultIdProperty">resultIdProperty</span>|None|[Result](#Result) |xml:string ||
|<span id="targetUri">targetUri</span>|None|[Function](#Function) |xml:string ||
|<span id="valuePath">valuePath</span>|None|[ReturnValue](#ReturnValue) |xml:string ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="input">input</span>|None|[Function](#Function) |[Argument](#Argument) ||
|<span id="output">output</span>|None|[Result](#Result) |[ReturnValue](#ReturnValue) ||
|<span id="result">result</span>|None|[Function](#Function) |[Result](#Result) ||
