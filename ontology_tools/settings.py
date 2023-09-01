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
# path settings
ontology_path = '.'
refactored_path = 'ontology_refactored'
tables_path = 'ontology_tables'
numbers_path = 'ontology_numbers'
tools_path = 'ontology_tools'
mapping_path = 'ontology_mapping'
use_case_path = 'ontology_use_case'

# namespace settigns
from rdflib import Namespace
cx_url = 'file:'
cx_ontology = Namespace("https://w3id.org/catenax/")
cx = Namespace("https://w3id.org/catenax/ontology")
cx_file = ontology_path + '/ontology.ttl'