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
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from ontology_tools.settings import cx_url, cx_file, mapping_path
from ontology_tools.write_formatted_excel import write_formatted_excel

def create_mapping_table(mapping_name = 'name', mapping_classes = ['vehicle']):

    # read ontology as table
    df = pd.read_csv(mapping_path+'/cx_ontology.csv')

    # filter by classes
    class_list = ['cx:'+c.title().replace(' ', '') for c in mapping_classes]
    sel = df['class'].isin(class_list)# | df['object'].isin(class_list)
    df = df[sel]

    #df = df.sort_values(['attribute'])
    df['type'] = ''
    df.loc[(df['attribute'].notna()), 'type'] = 'attribute'
    df.loc[(df['relation'].notna()), 'type'] = 'relation'

    #+mapping_name.title().replace(' ', '').replace('_', '')
    df['map'] = df['class']+'TripleMap'
    df['target_map'] = df['object']+'TripleMap'
    df = df.drop(columns=['ontology', 'object'])

    # add columns
    columns = ['table_name', 'table_type', 'table_path', 'column', 'foreign_key', 'primary_key']
    for col in columns:
        df[col] = ''
    df_template = pd.read_csv(mapping_path+'/_mapping_template.csv', sep=';')
    df = pd.concat([df_template, df])

    # write csv file
    # csv_file = mapping_path+'/'+mapping_name.lower().replace(' ', '_')+'_mapping.csv'
    # print('# writing: ', csv_file)
    # df.to_csv(csv_file, index=False)

    xlsx_file = mapping_path+'/'+mapping_name.lower().replace(' ', '_')+'_mapping.xlsx'
    print('# writing: ', xlsx_file)
    #df.to_excel(xlsx_file, index=False)
    write_formatted_excel(df, xlsx_file)