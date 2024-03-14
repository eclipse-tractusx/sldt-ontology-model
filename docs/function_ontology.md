



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
|<span id="argumentName">argumentName</span>|Determines the name or index of the function argument.|[Argument](#Argument) |xml:string ||
|<span id="batch">batch</span>|Determines maximal batch size for function invocations. Default is '1' which means that each invocation is done separately|[Function](#Function) |xml:long ||
|<span id="callbackProperty">callbackProperty</span>|Determines a (set of) paths in the input document and the output response under which the callback address (see <https://w3id.org/catenax/ontology/function#callbackAddress>) and the referring callback id will be transmitted.|[Function](#Function) , [Result](#Result) |xml:string ||
|<span id="dataType">dataType</span>|Determines the data type of an argument or return value.|[Argument](#Argument) , [ReturnValue](#ReturnValue) |||
|<span id="default">default</span>|Determines a default for the given argument which is taken if this is a mandatory argument (see <https://w3id.org/catenax/ontology/function#mandatory>)|[Argument](#Argument) |xml:anyType ||
|<span id="inputProperty">inputProperty</span>|Determines a path/name in the input document under which all input arguments are encoded. Default is '.'|[Function](#Function) |xml:string ||
|<span id="invocationIdProperty">invocationIdProperty</span>|Determines a (set of) paths in the input document under which the IRI of the invocation (instance of Function) will be transmitted.|[Function](#Function) |xml:string ||
|<span id="invocationMethod">invocationMethod</span>|Determines the invocation method of the function in case that the target service provides several possibilities.|[Function](#Function) |xml:string ||
|<span id="outputProperty">outputProperty</span>|Determines a path/name in the output response under which all output arguments are encoded. Default is '.'|[Result](#Result) |xml:string ||
|<span id="priority">priority</span>|Determines the priority with which the argument is processed. Default is '10'|[Argument](#Argument) |xml:integer ||
|<span id="resultIdProperty">resultIdProperty</span>|Determines a path in the output response under which the IRI of the result component will be transmitted.|[Result](#Result) |xml:string ||
|<span id="targetUri">targetUri</span>|The target URI of the function should resolve to some existing service (URL).|[Function](#Function) |xml:string ||
|<span id="valuePath">valuePath</span>|Determines a path in the output response under which a return value is transmitted.|[ReturnValue](#ReturnValue) |xml:string ||

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="input">input</span>|Describes the arguments of a function.|[Function](#Function) |[Argument](#Argument) ||
|<span id="output">output</span>|None|[Result](#Result) |[ReturnValue](#ReturnValue) ||
|<span id="result">result</span>|Describes the result of a function.|[Function](#Function) |[Result](#Result) ||
