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
import pandas as pd
from rdflib import Graph, URIRef, Literal
from ontology_tools.settings import cx_url, cx_file, mapping_path

def convert_ontology_to_csv():

    # read ontology
    graph = Graph()
    graph.parse(cx_file)

    # query classes with attributes
    query = """
    SELECT DISTINCT ?ontology ?class ?attribute ?data_type WHERE {
        ?bn owl:someValuesFrom ?data_type ;
            owl:onProperty ?attribute .
        ?attribute rdf:type owl:DatatypeProperty .
        ?class rdfs:subClassOf ?bn;
            rdfs:isDefinedBy ?ontology .
    }
    ORDER BY ?ontology ?class ?attribute
    """
    r = graph.query(query)
    r.serialize(mapping_path+'/cx_ontology_attribute.csv', format='csv')

    # query classes with relations
    query = """
    SELECT DISTINCT ?ontology ?class ?relation ?object WHERE {
        ?bn owl:someValuesFrom ?object ;
            owl:onProperty ?relation .
        ?relation rdf:type owl:ObjectProperty .
        ?class rdfs:subClassOf ?bn;
            rdfs:isDefinedBy ?ontology .
    }
    ORDER BY ?ontology ?class ?relation
    """
    r = graph.query(query)
    r.serialize(mapping_path+'/cx_ontology_relation.csv', format='csv')

    # concat attributes & relations
    df = pd.concat([
        pd.read_csv(mapping_path+'/cx_ontology_attribute.csv'),
        pd.read_csv(mapping_path + '/cx_ontology_relation.csv')
        ])

    # add prefixes
    for col in df.columns:
        df[col] = df[col].str.replace(cx_url, 'cx:', regex=False)
        df[col] = df[col].str.replace('http://www.w3.org/2002/07/owl#', 'owl:', regex=False)
    df['ontology'] = df['ontology'].str.replace('https://raw.githubusercontent.com/catenax-ng/product-knowledge/main/ontology/', '', regex=False)
    df['ontology'] = df['ontology'].str.replace('.ttl', '', regex=False).str.title().str.replace('_',  '')
    df['data_type'] = df['data_type'].str.replace('http://www.w3.org/2001/XMLSchema#', 'xsd:', regex=False)

    # write csv
    df = df.sort_values(['class', 'attribute'])
    out_file = mapping_path+'/cx_ontology.csv'
    print('# writing:', out_file)
    df.to_csv(out_file, index=False)