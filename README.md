<!--
 * Copyright (c) 2022,2023 Contributors to the Catena-X Association
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Apache License, Version 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
-->

# Ontology Models to realize federated query in Catena-X 

- This repository hosts ontologies based on the [CX - 0067 Ontology Models to realize federated query in Catena-X v.1.1.0](https://catena-x.net/de/standard-library) standard to realize [Knowledge Agent](https://eclipse-tractusx.github.io/docs-kits/kits/knowledge-agents/adoption-view/intro) applications.
- The Catena-X Ontology and its initial Catena-X Taxonomy are not intended to be a world model. Instead, it is intended to be an integrative framework with a focus on automotive manufacturing. Therefore, our focus is on defining practical domain ontologies. All definitions in a domain ontology should belong to the same namespace (which is the technical key of the domain) and should use a common prefix. Domain ontologies can refer to classes of other domains by importing concrete versions.
- The Catena-X taxonomy contains all concepts used in domain ontologies. Furthermore, the defined concepts are not only used in the knowledge agent approach, but are also made available to all Catena-X applications.
</br>

<div align="center"  width="100%">
  <img src="images/ontologies.png" alt="image" width="900" height="auto" />
</div>

## Ontology Development & Governance Process

- The ontologies can be developed based on the ontology governance process.
- The ontologies are developed using the [protégé editor](https://protege.stanford.edu/). Therefore, we prefer to use this editor.
- After the development of a new ontology is finished, the documentation is automatically generated as a Markdown file and stored in the repository. In addition, the ontologies are published at [w3id.org Catena-X](https://w3id.org/catenax). This also allows access to all versions.
- You can download the protégé editor, import the core ontology and start modeling!

## Provisioning of Ontology and Taxanomy

- The ontologies/taxonomies are provided as individual domain files and are simultaneously available as a merged Catena-X ontology/taxonomy in the root directory.

## Implemented Ontologies

Main ontologies:

- [Core Ontology](docs/core_ontology.md)
- [Common Ontology](docs/common_ontology.md)
- [Function Ontology](docs/function_ontology.md)

Domain ontologies:
- [Bill of Material](docs/bill-of-material_ontology.md)
- [Behaviour](docs/behaviour_ontology.md)
- [Supply Chain Ontology](docs/supply-chain_ontology.md)
- [Reliability](docs/reliability_ontology.md)
- [Vehicle Ontology](docs/vehicle_ontology.md)

Taxonomy:
- [Core Taxonomy](docs/core_taxonomy.md)
- [Asset Taxonomy](docs/asset_taxonomy.md)

## Related Information

* See the [Authors file](AUTHORS.md)
* See the [License file](LICENSE)
* See the [Code of conduct](CODE_OF_CONDUCT.md)
* See the [Contribution guidelines](CONTRIBUTING.md)
* See the [Dependencies and their licenses](NOTICE.md)
* See the [Security disclaimer](SECURITY.md)
* See the [Changelog](CHANGELOG.md)

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
