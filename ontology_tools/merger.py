
import os
from rdflib import Graph, SKOS, OWL, RDFS, RDF, DC, URIRef, Literal, XSD
#from ontology_tools.settings import ontology_path, refactored_path


# Main ontology information
main_ontology = Graph()
main_ontology.bind("dc", DC)

catenax_ontology = URIRef("https://w3id.org/catenax/ontology")


main_ontology.add((catenax_ontology, RDF.type, OWL.Ontology))
main_ontology.add((catenax_ontology, DC.contributor, Literal("Catena-X Knowledge Agents Team") ))
main_ontology.add((catenax_ontology, DC.date, Literal("2023-08-04", datatype = XSD.string))) # ^^xsd:date
main_ontology.add((catenax_ontology, DC.description, Literal("Catena-X Ontology for the Autmotive Industry.") ))
main_ontology.add((catenax_ontology, DC.title, Literal("Catena-X Ontology") ))

# Files 
files = os.listdir('ontology')

for file in files:

    domain_ontology = Graph()
    domain_ontology.parse('ontology/' + file)
    
    #Remove Ontology Information
    for s, p, o in domain_ontology.triples((None, None, OWL.Ontology)):
        domain_ontology.remove((s, None, None))
    
    main_ontology = main_ontology + domain_ontology

main_ontology.serialize(destination="created_ontology.ttl")
