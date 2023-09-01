# Copyright (c) 2022,2023 T-Systems International GmbH
# Copyright (c) 2022,2023 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
# Copyright (c) 2022,2023 ZF Friedrichshafen AG 
# Copyright (c) 2022,2023 Mercedes-Benz AG 
# Copyright (c) 2022,2023 Contributors to the Catena-X Association
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
import os
from rdflib.namespace import RDF, RDFS, OWL, DC
from rdflib import Graph, URIRef, Literal
from datetime import date
import sys
from ontology_tools.settings import cx, cx_ontology, cx_url, cx_file, mapping_path

def merge_ontology(path='.', folder = '.', file_out = 'ontology.ttl', files = None):

    # get file list
    if (files is None):
        files = os.listdir(folder)

    files.sort()

    # start
    g = Graph()
    for file in files:
        if ((not file.startswith('.')) & file.endswith('_ontology.ttl') ) & (file != file_out):
            ttl_file = path+'/'+file
            if os.path.exists(ttl_file):
                # read & merge ontology
                graph = Graph().parse(ttl_file)
                # remove ontology annotations
                if (None, RDF['type'], OWL['Ontology']) in graph:
                    ontology = graph.value(None, RDF.type, OWL.Ontology)
                    graph = graph.remove((ontology, None, None))
                print('# merging: ', ttl_file)
                for member in graph.subjects(RDF.type,None,True):
                    graph.add((member,RDFS.isDefinedBy,URIRef(cx_url+file)))
                g = g + graph

    # add meta data
    ontology_iri = 'ontology'
    g = g.add((cx_ontology[ontology_iri], RDF.type, OWL.Ontology))
    g = g.add((cx_ontology[ontology_iri], DC.title, Literal('Catena-X Ontology')))
    g = g.add((cx_ontology[ontology_iri], DC.date, Literal(date.today())))
    g = g.add((cx_ontology[ontology_iri], DC.creator, Literal('Catena-X Knowledge Agents Team')))
    g = g.add((cx_ontology[ontology_iri], DC.description, Literal('Catena-X Ontology for the Autmotive Industry.')))
    #for file in files:
    #        if ((not file.startswith('.')) & file.endswith('_ontology.ttl') ) & (file != file_out):
    #            g = g.add((cx_ontology[ontology_iri], OWL.imports, URIRef(cx_url+file)))

     #g = g.add((cx[ontology_iri], RDFS.seeAlso, URIRef('https://github.com/catenax-ng/product-knowledge/blob/main/ontology/')))

    # write
    print('# writing: ', folder+'/'+file_out)
    g.serialize(destination=folder+'/'+file_out, format='turtle')

if __name__ == '__main__':
  merge_ontology(files=sys.argv[1:])