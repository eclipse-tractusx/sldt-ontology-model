import os
from rdflib import Graph

#This function merges ontologies.
def merge_ontologies(*domain_name):
    
    # Main ontology information
    main_ontology = Graph()

    for file in domain_name:

        domain_ontology = Graph()
        domain_ontology.parse('ontology/' + file + "_ontology.ttl")
                
        main_ontology = main_ontology + domain_ontology

    main_ontology.serialize(destination="created_ontology.ttl")

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

    main_taxo.serialize(destination="created_taxonomy.ttl")

merge_ontologies('core', 'common')

merge_taxonomies()