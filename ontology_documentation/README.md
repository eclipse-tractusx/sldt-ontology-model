
# Ontology Architecture
In [Catena-X](https://catena-x.net/) we want to build a federated virtual knowledge graph for the
[automotive industry](https://en.wikipedia.org/wiki/Automotive_industry) in order to enable data access across companies.

## Fundamental Principles
1. Maximise Semantics 
2. Reduce Complexity
3. Minimise Redundancy 

[Semantics](https://en.wikipedia.org/wiki/Semantics) is the **understanding of the meaning** of the data by the data producer and consumer. 
The main goal is to **bridge the semantic gap** between data producers and consumers.
See also [FAIR data](https://en.wikipedia.org/wiki/FAIR_data).
We follow the data-centric architecture, i.e. we start with data first and then comes the applications.

## Semantic Standards
We use the following [semantic web](https://en.wikipedia.org/wiki/Semantic_Web)
[W3C](https://de.wikipedia.org/wiki/World_Wide_Web_Consortium) standards:
* [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework) /
[RDFS](https://en.wikipedia.org/wiki/RDF_Schema) /
[OWL](https://de.wikipedia.org/wiki/Web_Ontology_Language) for ontology [modelling](https://en.wikipedia.org/wiki/Data_modeling),
* [SKOS](https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System) for [data dictionary](https://en.wikipedia.org/wiki/Data_dictionary) ([glossary](https://en.wikipedia.org/wiki/Glossary) and [thesaurus](https://en.wikipedia.org/wiki/Thesaurus)),
* [turtle](https://en.wikipedia.org/wiki/Turtle_(syntax)) as [file format](https://en.wikipedia.org/wiki/File_format) in [unicode](https://en.wikipedia.org/wiki/Unicode) for storing ontologies,
* [SPARQL](https://en.wikipedia.org/wiki/SPARQL) for [querying](https://en.wikipedia.org/wiki/Query_language),
* [R2RML](https://www.w3.org/TR/r2rml/) / [RML](https://rml.io/specs/rml/) / OBDA for [data mapping](https://en.wikipedia.org/wiki/Data_mapping) between an ontology and a [database schema](https://en.wikipedia.org/wiki/Database_schema),
* [Ontop](https://ontop-vkg.org/) for [data virtualisation](https://en.wikipedia.org/wiki/Data_virtualization),
* [SHACL](https://en.wikipedia.org/wiki/SHACL) for constraints,
* [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) for identifiers.

# Basic Concepts
### Basic Elements
#### Identifier
In the semantic web (RDF/OWL) every element of an ontology (classes, relations, attributes) or
knowledge graph (individuals) is represented as a [resource](https://en.wikipedia.org/wiki/Web_resource) and has an 
**unique identifier** in form of an [Uniform Resource Identifier (URI)](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier).
An URI is also known as a web address or internet link.

#### Namespace
A [namespace](https://en.wikipedia.org/wiki/Namespace) is the base URL for identifiers and we use prefix **cx**
and separator **#** to abbreviate the URI
https://raw.githubusercontent.com/catenax-ng/product-knowledge/main/ontology/cx_ontology.ttl#.
The ontology files can be directly accessed from the internet, e.g.
[cx_ontlogy.ttl](https://raw.githubusercontent.com/catenax-ng/product-knowledge/main/ontology/cx_ontology.ttl) in github.
Furthermore, we use following namespaces for the W3C standards:

| **prefix** | namespace                               |
|------------|-----------------------------------------|
| **owl**    | <http://www.w3.org/2002/07/owl#>        |
| **rdfs**   | <http://www.w3.org/2000/01/rdf-schema#> |
| **skos**   | <http://www.w3.org/2004/02/skos/core#>  |
| **xsd**    | <http://www.w3.org/2001/XMLSchema#>     |

#### Literal
A [literal](https://en.wikipedia.org/wiki/Literal_(computer_programming)) is a
[typed](https://en.wikipedia.org/wiki/Primitive_data_type) data value, e.g. string or integer.
The data types are based on [XML schema](https://en.wikipedia.org/wiki/XML_Schema_(W3C)) in OWL.
* foaf:Person foaf:name **"Max Mustermann"**

### Ontology
An ontology is a [semantic data model](https://en.wikipedia.org/wiki/Semantic_data_model) that consists of classes,
relations, attributes. It corresponds to a
[logical data model](https://en.wikipedia.org/wiki/Logical_schema) or
[entity-relationship model (ERM)](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) of a
[relational database (RDB)](https://en.wikipedia.org/wiki/Relational_database).

| simple         | **OWL**              | **OOP**     | **UML**     | **RDB** | **ERM**           | CS     |
|----------------|----------------------|-------------|-------------|---------|-------------------|--------|
| **class**      | owl:Class            | class       | class       | table   | entity type       |        |
| **relation**   | owl:ObjectProrperty  | association | association | key     | relationship type |        |
| **attribute**  | owl:DatatypeProperty | field       | attribute   | column  | attribute type    | field  |
| **individual** | individual           | instance    | object      | row     | entity            | record |

#### Ontology Domain
The **scope** of a domain-specific ontology is called **domain**. This can encompass:
* field, subject, topic, specialty, discipline, expertise
* [subject-matter](https://en.wikipedia.org/wiki/Subject-matter_expert), [knowledge domain](https://en.wikipedia.org/wiki/Domain_knowledge)

#### Ontology Layers
Three model layers:
* [conceptual data model](https://en.wikipedia.org/wiki/Conceptual_schema)
* [logical data model](https://en.wikipedia.org/wiki/Logical_schema)
* [physical data model](https://en.wikipedia.org/wiki/Physical_schema)

### Individual
### Class
### Relation
* association, 
* composition (part-of), 
* aggregation (has-a), 
* inheritance (is-a)

#### Domain of a Relation

#### Range of a Relation

### Attribute

### Triple
A triple is statement consisting of **subject**-**predicate**-**object** that is defined by [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework).
It is the basic unit of a [triplestore](https://en.wikipedia.org/wiki/Triplestore).

### Knowledge Graph
A [knowledge graph](https://en.wikipedia.org/wiki/Knowledge_graph) is a
[graph-structured database](https://en.wikipedia.org/wiki/Graph_database)
where knowledge is represented in the ontology and individuals.
There are two types of KGs: RDF ([Neptune](https://en.wikipedia.org/wiki/Amazon_Neptune), RDFox, AnzoGraph)
and LPG ([Neo4j](https://de.wikipedia.org/wiki/Neo4j), [Tinkerpop](https://tinkerpop.apache.org/)). We use RDF.

#### Data virtualization
[data virtualization](https://en.wikipedia.org/wiki/Data_virtualization) vs [materialisation](https://en.wikipedia.org/wiki/Materialized_view)

#### Federation
[federation](https://en.wikipedia.org/wiki/Federated_database_system)

# Ontology Modelling Standards

## Language
* bilingual (en, de)
* use generic terms for identifiers (domain-independent)
* use business terms for prefLabel (domain-specific)
* specify always annotations fully (definition, example, synonyms)

## Naming Convention
Ontology modelling is an iterative, continuous development process. It is always subject to potential changes in the
future. Therefore, we always start with a MVP ontology and extend it later on, i.e. an agile working model fits here well.
A semantic model is only useful, when it is used by someone (application integration).

| **convention**  |  **identifier**  |   **name_en**  |    **name_de**    |
|-----------------|:----------------:|:--------------:|:-----------------:|
| **language**        | English          | English        | German            |
| **readability**     | machine-readable | human-readable | human-readable    |
| **terms**           | generic terms    | business terms | business terms    |
| **character range** | [A-z0-9]         | [A-z0-9 -]     | [A-z0-9 -ÄäÖöÜüß] |
| **separator**       | none             | whitespace     | whitespace        |
| **class case**      | PascalCase       | Title Case     | Title Case        |
| **relation case**   | camelCase        | lower case     | lower case        |
| **attribute case**  | camelCase        | Title Case     | Title Case        |
| **acronyms**        | no               | yes            | yes               |

## Ontology Table Schema
| **simple_name** | **rdf_name**       |
|--------------------|-----------------------|
|   type             |   rdf:type            |
|   identifier       |                       |
|   parents          |   rdfs:subClassOf     |
|   relation_from    |   rdfs:domain         |
|   relation_to      |   rdfs:range          |
|   name_en          |   skos:prefLabel@en   |
|   name_de          |   skos:prefLabel@de   |
|   definition_en    |   skos:definition@en  |
|   example_en       |   skos:example@en     |
|   note_en          |   skos:note@en        |
|   synonyms_en      |   skos:altLabel@en    |
|   synonyms_de      |   skos:altLabel@de    |
|   links            |   rdfs:seeAlso        |

# Advanced Topics

## Ontology Scoping
* modular, reusable, non-redundant

### Business Question

## Open-world assumption
[Open-world assumption](https://en.wikipedia.org/wiki/Open-world_assumption)

## Ontology Metadata
Annotations

## Ontology Merging

#### Individual Identifier
* class + '_' + primary_key
* mapping -> template

## Collision
[name collision](https://en.wikipedia.org/wiki/Name_collision)

## Data Normalisation
[Normalisation](https://en.wikipedia.org/wiki/Database_normalization) is necessary to minimise the redudnancy.

## Decisions
### Instances or Subclasses
* cx:VehiclePlant cx:isOfType cx:PlantType_VehiclePlant
* cx:VehiclePlant owl:subClassOf cx:Plant

### Generic or Specific Relation Names

### Instances or Attributes
* cx:Vehicle cx:hasColor cx:Color_Blue
* cx:Vehicle cx:hasColor "blue"

### Generic or Specific Attributes
* plant + id
* plant + plant_id

### Number of allowed Datatypes
* string, integer
* string, int, integer, ...

### Everything is a Concept
* cx:Vehicle rdf:type owl:Class; skos:Concept

### Link vs. Use External Ontologies
* cx:Person owl:equivalentClass foaf:Person

### Single vs. Multiple Namespaces
* cx vs. cx, cx-vehicle, cx-common

### Open vs. Closed Compound Words
* data set vs. dataset

### Hyphenation
* E-mail vs. Email