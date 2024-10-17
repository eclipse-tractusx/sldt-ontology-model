###############################################################
# Copyright (c) 2024 T-Systems International GmbH
# Copyright (c) 2024 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
# Copyright (c) 2024 ZF Friedrichshafen AG 
# Copyright (c) 2024 Mercedes-Benz AG 
# Copyright (c) 2024 Catena-X Association
# Copyright (c) 2022 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
###############################################################

import os
from rdflib import Graph, RDF, OWL, URIRef, DC, Literal

#This function merges ontologies.
def merge_ontologies(*domain_name):
    
    # Main ontology information
    main_ontology = Graph()
    
    main = URIRef("https://w3id.org/catenax/ontology")
    main_ontology.add((main, RDF.type, OWL.Ontology))
    main_ontology.add((main, DC.title, Literal("Catena-X Main Ontology")))
    main_ontology.add((main, DC.description, Literal("The main ontology is a merge of domain ontologies and is created automatically, see Domain Ontologies for details.")))

    for file in domain_name:

        domain_ontology = Graph()
        domain_ontology.parse('ontology/' + file + "_ontology.ttl")
        ont = URIRef("https://w3id.org/catenax/ontology/" + file)

        for s, p, o in domain_ontology.triples((ont, None, None)):
            domain_ontology.remove((s, p, o))
                
        main_ontology = main_ontology + domain_ontology

    main_ontology.serialize(destination="ontology.ttl")

#This function merges taxonomies  
def merge_taxonomies():
    # Main ontology information
    main_taxo = Graph()
    
    # Files 
    files = os.listdir('taxonomy')

    for file in files:

        domain_taxo = Graph()
        domain_taxo.parse('taxonomy/' + file)    
        main_taxo = main_taxo + domain_taxo

    main_taxo.serialize(destination="taxonomy.ttl")

merge_ontologies('behaviour', 'bill-of-material', 'common', 'core', 'function', 'reliability', 'supply-chain', 'vehicle')

merge_taxonomies()