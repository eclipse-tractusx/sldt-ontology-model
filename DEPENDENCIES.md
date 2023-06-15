# Dependencies of Tractus-X Knowledge Agents Ontology

The following is a simple type of single-level Software-BOM for all official open source products of Tractus-X Knowledge Agents. 

* Component - The specific sub-component of the Epic/Product (* for all)
* Library/Module - The library or module that the Product/Component is depending on
* Stage - The kind of dependency 
  * Compile - The library is needed to compile the source code of the component into the target artifact (runtime)
  * Test - The library is needed to test the target artifact
  * Packaging - The library is needed to test the target artifact before, while and/or after packaging it
  * Runtime - The library is shipped as a part of the target artifact (runtime)
  * Provided - The library is not shipped as a part of the target artifact, but needed in it runtime
  * All - The library is needed at all Stages
* Version - the version of the library that the component is dependant upon
* License - the license identifier
* Comment - any further remarks on the kind of dependency

| Component | Library/Module  | Version | Stage | License | Comment |
| -- | --- | --- | --- | --- | ---| 
| * | * | [Apache Maven](https://maven.apache.org) | >=3.8 | Compile + Test + Packaging | Apache License 2.0 |     |
| * | * | Docker Engine | >=20.10.17 | Packaging + Provided | Apache License 2.0 |     |
| * | * | [kubernetes](https://kubernetes.io/de/)/[helm](https://helm.sh/) | >=1.20/3.9 | Provided | Apache License 2.0 |     |
| * | * | [Python](https://www.python.org/) | >=3.9 | Test + Packaging + Provided | Zero Clause BSD |     |
| Tools | [OWLApi](https://github.com/owlcs/owlapi) | >=5.1 | Compile + Test + Packaging | LGPL and Apache License |     |
| Tools | [OWL2VOWL](https://github.com/VisualDataWeb/OWL2VOWL) | >=0.3.7 | Compile + Test + Packaging | MIT License |     |
| Tools | [SLF4J](https://www.slf4j.org) | >=2.0.0 | Compile + Test + Packaging | MIT |     |
| Tools | [Junit Jupiter](https://junit.org) | >=5 | Test | MIT |     |
| Tools | [NodeJS](https://nodejs.org/en/) | >=14 | Compile + Packaging | MIT (Main) + Various Extensions | Only for Json2Sql|
| Tools | [Jackson](https://github.com/FasterXML/jackson) | >=2.12.6 | Compile + Test + Packaging | Apache License 2.0 |     |
| Tools | [RDFlib](https://rdflib.readthedocs.io/en/stable/) | >=6.2 | Compile + Test + Packaging | BSD-3 |     |
