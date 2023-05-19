# path settings
ontology_path = 'ontology'
refactored_path = 'ontology/ontology_refactored'
tables_path = 'ontology/ontology_tables'
numbers_path = 'ontology/ontology_numbers'
tools_path = 'ontology/ontology_tools'
mapping_path = 'ontology/ontology_mapping'
use_case_path = 'ontology/ontology_use_case'

# namespace settigns
from rdflib import Namespace
cx_url = 'https://raw.github.com/eclipse-tractusx/ontology/main/'
cx_ontology = Namespace("https://catena-x.net/product-knowledge/")
cx = Namespace("https://catena-x.net/product-knowledge/ontology#")
cx_file = ontology_path + '/ontology.ttl'