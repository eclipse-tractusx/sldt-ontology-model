# Catena-X Ontology 

This repository hosts semantic models and tools with a focus on the self-description and catalogue capabilities of the 
[Catena-X Knowledge Agents](https://catenax-ng.github.io/product-knowledge/docs/adoption-view/CX-0084-Federated_Queries_In_Data_Spaces_v1.0.0) standard. 

They may be used in conjunction with the [Tractus-X Extensions for the Eclipse Dataspace Components](https://github.com/catenax-ng/product-agents-edc) and 
[Tractus-X Binding Agent Implementations](https://github.com/catenax-ng/product-agents) for dataspace-wide validation, discovery, type inference and binding definitions.

* See the [copyright notice](COPYRIGHT.md)
* See the [authors file](AUTHORS.md)
* See the [license file](LICENSE.md)
* See the [code of conduct](CODE_OF_CONDUCT.md)
* See the [contribution guidelines](CONTRIBUTING.md)
* See the [dependencies and their licenses](DEPENDENCIES.md)

## What's inside?

The Catena-X Ontology is not aimed at being a world model. 
Instead it is aimed as an integrative framework with a focus on Automotive Manufacturing.

Therefore, our focus lies on defining practical [domain](ontology)/[use case](ontology_use_case) ontology files (and tools to process/merge them into broader contexts).
Each domain ontology file is written in a format named [Turtle (TTL)](https://www.w3.org/TeamSubmission/turtle/).

Following the [Resource Description Framework (RDF)](https://en.wikipedia.org/wiki/Resource_Description_Framework), these files defines 
- semantic concepts (classes of entities/nodes, where a node can have multiple classes)
- properties (attributes of entities using primitive node types) and 
- relations/predicates (which are links between nodes where the source node is called subject and the target node is called the object) 

All definitions in a file should belong to the same namespace (which is the technical key of the domain) and should be using a common nickname (prefix)
that is also the name of the file. Each commit/branch/release tag coincides with a *version* of the respective ontology. Therefore, namespaces and 
versions are different types of IRIs, the former being represented by URNs the latter by URLs.

Domain ontologies can refer to concepts of other domains/prefixes by importing concrete versions.
Relations are usually defined in those concepts/domain which cannot exist without the relation.

## Contents

- [Ontology Tools](tools)
- [Ontology Tools (Python)](ontology_tools)
- [Documentation](ontology_documentation)
- [Example Data Bindings](ontology_mapping)
- [Catena-X Merged Ontology](ontology.ttl)
- [Catena-X Taxonomy](taxonomy.ttl)
- [Catena-X Domain Ontologies](ontology)
- [Catena-X Use Case Ontologies](ontology_use_case)
- [Former Way of Defining Ontologies (Deprecated)](ontology_tables)
- [Renderings of Catena-X Ontologies (for use in UX components)](vowl)

## How to use it

### Prepare

A suitable [conda](https://conda.io/) environment named `knowledgeagents` can be created
and activated with:

```
conda env create -f environment.yaml
conda activate knowledgeagents
```

### Ontology Create

Creating a new ontology excel source can be done by invoking

```
python 
>>> import ontology_tools.create_ontology as co
>>>  co.create_ontology_table('test','Schorsch','1.0.0')
```

### Ontology Merge

Creating a merged ontology out of several domain ontologies may be done by invoking

```
python -m ontology_tools.merge_ontology ontology/*_ontology.ttl 
```

### Use Case Create

Creating a new use case excel source can be done by invoking

```
python 
>>> import ontology_tools.create_use_case as cu
>>> cu.create_use_case_template('behaviour_twin')
```

The excel template can then be edited to annotate the required classes, attributes and relations by the stakeholders of the use case.

Deriving a new use case ontology can then be done 

```
python 
>>> import ontology_tools.create_use_case as cu
>>> cu.create_use_case_ontology('behaviour_twin')
```
