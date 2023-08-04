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