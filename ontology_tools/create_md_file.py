# Copyright (c) 2024 T-Systems International GmbH
# Copyright (c) 2024 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
# Copyright (c) 2024 ZF Friedrichshafen AG 
# Copyright (c) 2024 Mercedes-Benz AG 
# Copyright (c) 2024 Contributors to the Catena-X Association
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

import operator
import mdutils
import os
from rdflib import Graph, SKOS, OWL, RDFS, RDF, DC

#Get domain name
def getDomainName(cxObject):
    
    cxObject = cxObject.replace('https://w3id.org/catenax/ontology/','').split('#')[0]
    return cxObject

#Customized name
def customizedName(link:str):
    
   # cx_s = 'https://w3id.org/catenax/ontology/' + domain_name + '#'
    
    if (link.__contains__('http://www.w3.org/2001/XMLSchema#') ) :
            return link.replace('http://www.w3.org/2001/XMLSchema#','')
    
    elif (link.__contains__('https://json-schema.org/draft/2020-12/schema#') ) : 
        return link.replace('https://json-schema.org/draft/2020-12/schema#','')   
        
    elif (link.__contains__('http://www.w3.org/2002/07/owl#') ) : 
        return link.replace('http://www.w3.org/2002/07/owl#','')  
  	
    elif (link.__contains__('http://www.w3.org/2000/01/rdf-schema#') ) : 
        return link.replace('http://www.w3.org/2000/01/rdf-schema#','')
    
    elif (link.__contains__('http://www.w3.org/ns/shacl#') ) : 
        return link.replace('http://www.w3.org/ns/shacl#','')
    
    elif ( link.__contains__('catenax')) :
        return link.replace('https://w3id.org/catenax/ontology/','').split('#')[1]
    else:
       return link

#Creates mermaid visualization
def create_mermaid(domain_name):

    cx_s = 'https://w3id.org/catenax/ontology/' + domain_name + '#'

    #Graph settings
    main_ontology = Graph()
    main_ontology.parse('ontology/' + domain_name + '_ontology.ttl')
    
    mermaid = "classDiagram \n"
    
    #Add node (classes)
    for s, p, o in main_ontology.triples((None, None, OWL.Class)):
        
        className = customizedName(s.__str__().replace(cx_s,''))
        
        mermaid = mermaid + "   class " + className + "~" + getDomainName(s.__str__()) + "~" + "{\n"

        for dataType in main_ontology.subjects( RDFS.domain, s):
            if (dataType, RDF.type, OWL.DatatypeProperty) in main_ontology:
                for range in main_ontology.objects(dataType, RDFS.range):
                    mermaid = mermaid + "       " + dataType.__str__().replace(cx_s,'') + " " + customizedName(range.__str__()) + "\n"
                    
        mermaid = mermaid + "   } \n"
                    
    #Add node (edges)
    for s, p, o in main_ontology.triples((None, None, OWL.ObjectProperty)):
        if not (s,OWL.inverseOf,None) in main_ontology:
            edgelabel = s.__str__().replace(cx_s,'')
        
            if  (None, OWL.inverseOf, s) in main_ontology:
                for inv in main_ontology.subjects( OWL.inverseOf, s):
                    edgelabel = edgelabel + ' / \n' + inv.__str__().replace(cx_s,'') 

    #Add edges
    for s, p, o in main_ontology.triples((None, None, OWL.ObjectProperty)):
        for s1, p1, o1 in main_ontology.triples((s, RDFS.domain, None)):
            for s2, p2, o2 in main_ontology.triples((s, RDFS.range, None)):
                if not (s,OWL.inverseOf,None) in main_ontology:
                    
                    edgelabel = s.__str__().replace(cx_s,'')
                    
                    if (None, OWL.inverseOf, s) in main_ontology:
                        for inv in main_ontology.subjects( OWL.inverseOf, s):
                            edgelabel = edgelabel + '/\\n' + inv.__str__().replace(cx_s,'')
                        mermaid = mermaid + "   " + customizedName(o1.__str__()) + " <--> " + customizedName(o2.__str__()) + " : " + edgelabel + "\n"
                    else:
                        mermaid = mermaid + "   " + customizedName(o1.__str__()) + " --> " + customizedName(o2.__str__()) + " : " + edgelabel+ "\n"
    #Subclass
    for s, p, o in main_ontology.triples((None, RDFS.subClassOf, None)):
        mermaid = mermaid + "   " + customizedName(s.__str__()) + " --|> " + customizedName(o.__str__()) + "\n"

    return mermaid

#Customized link
def customizedLink(domain_name, link:str):
    
    cx_s = 'https://w3id.org/catenax/ontology/' + domain_name + '#'
    
    if (link.__contains__('http://www.w3.org/2001/XMLSchema#') ) :
            return 'xsd:' + link.replace('http://www.w3.org/2001/XMLSchema#','')
    
    elif (link.__contains__('https://json-schema.org/draft/2020-12/schema#') ) : 
        return 'json:' + link.replace('https://json-schema.org/draft/2020-12/schema#','')   
        
    elif (link.__contains__('http://www.w3.org/2002/07/owl#') ) : 
        return 'owl:' + link.replace('http://www.w3.org/2002/07/owl#','')  
    
    elif (link.__contains__('http://www.w3.org/ns/shacl#') ) : 
        return 'owl:' + link.replace('http://www.w3.org/ns/shacl#','')
  	
    elif (link.__contains__('http://www.w3.org/2000/01/rdf-schema#') ) : 
        return 'rdfs:' + link.replace('http://www.w3.org/2000/01/rdf-schema#','')
    elif ( link.__contains__('catenax') &  link.__contains__(domain_name)  ) :
        return "[" + link.replace(cx_s,'') +"](#" + link.replace(cx_s,'') + ")"
    
    elif (link.__contains__('catenax') &  operator.not_(link.__contains__(domain_name))   ) :
        cxObject = link.replace('https://w3id.org/catenax/ontology/','').split('#')[1]
        cxDomain = link.replace('https://w3id.org/catenax/ontology/','').split('#')[0]  
        return '[' + cxObject +'](./' + cxDomain + '_ontology.md#'+ cxObject +')'
    else:
       return link

#Creates md file for ontologies    
def create_md_file_for_ontology(domain_name):
    
    cx_s = 'https://w3id.org/catenax/ontology/' + domain_name + '#'
    main_ontology = Graph()
    main_ontology.parse(  'ontology/' + domain_name + '_ontology.ttl')
    mdFile = mdutils.MdUtils(file_name='docs/' + domain_name + '_ontology')

    # Ontology Information
    for s, p, o in main_ontology.triples((None, None, OWL.Ontology)):

        creator = main_ontology.value(s, DC.creator) if( (s, DC.creator,None) in main_ontology) else "None"
        contributor = main_ontology.value(s, DC.contributor) if( (s, DC.contributor,None) in main_ontology) else "None"
        date = main_ontology.value(s, DC.date) if( (s, DC.date,None) in main_ontology) else "None"
        description = main_ontology.value(s, DC.description) if( (s, DC.description,None) in main_ontology) else "None"
        title = main_ontology.value(s, DC.title) if( (s, DC.title,None) in main_ontology) else "None"
        versionInfo = main_ontology.value(s, OWL.versionInfo) if( (s, OWL.versionInfo,None) in main_ontology) else "None"
        imports = ''
        
        for s, p1, o1 in main_ontology.triples((s, OWL.imports, None)):
            imports = imports + o1.__str__()  + " , "
            
        mdFile.new_header(1, title.__str__())        
        mdFile.new_paragraph("**Title:**  " + title.__str__())
        mdFile.new_paragraph("**Description:**  " + description.__str__())
        mdFile.new_paragraph("**Creator:**  " + creator.__str__())
        mdFile.new_paragraph("**Contributor:**  " + contributor.__str__())
        mdFile.new_paragraph("**Date:**  " + date.__str__())
        mdFile.new_paragraph("**Version:**  " + versionInfo.__str__())
        mdFile.new_paragraph("**Imports:**  " + imports[:-2] )
        mdFile.new_paragraph("**Link to ontology:**  " + cx_s[:-1])

    # Ontology image
    mdFile.new_line()
    #mdFile.new_line(mdFile.new_inline_image(text='ontology', path='images/' + domain_name + '_ontology.gv.svg'))
    
    mermaid = create_mermaid(domain_name)
    mdFile.insert_code(mermaid, language='mermaid')
    
    mdFile.new_line()

    # Classes
    hasValue = False
    for s, p, o in main_ontology.triples((None, None, OWL.Class)):
            if(s.__str__().__contains__(domain_name)):
                hasValue = True
    if (hasValue) :
        
        mdFile.new_header(2, "Classes")
        list_of_strings = ["Name", "Description", "Datatype properties", "Object properties", "Subclass of" ]
        rowCounter = 1
        
        for s, p, o in main_ontology.triples((None, None, OWL.Class)):
            if(s.__str__().__contains__(domain_name)):
                
                #Class name
                className = s.__str__().replace(cx_s,'') 
                className = "<span id=\""+ className +"\">" + className + "</span>"
                
                #description  
                description = main_ontology.value(s, RDFS.comment)

                #properties
                dataProperties = ""
                objectProperties = ""
                for s1, p1, o1 in main_ontology.triples((None, RDFS.domain, s)):
                    
                    if (s1, RDF.type, OWL.DatatypeProperty) in main_ontology :
                        dataProperties = dataProperties +  "[" + s1.__str__().replace(cx_s,'') +"](#" + s1.__str__().replace(cx_s,'') + ") , "
                    
                    if (s1, RDF.type, OWL.ObjectProperty) in main_ontology :
                        objectProperties = objectProperties +  "[" + s1.__str__().replace(cx_s,'') +"](#" + s1.__str__().replace(cx_s,'') + ") , " 
                        
                dataProperties = dataProperties[:-2]
                objectProperties = objectProperties[:-2]
                
                #subClassOf
                subClassOf = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.subClassOf, None)):
                    if not(o1.__str__().__contains__('http://www.w3.org/2002/07/owl#Thing')):
                        subClassOf = subClassOf + customizedLink(domain_name, o1.__str__())  + " , "

                subClassOf = subClassOf[:-2]
                
                
                list_of_strings.extend([className, description , dataProperties , objectProperties, subClassOf])
                
                rowCounter = rowCounter + 1

        mdFile.new_line()
        mdFile.new_table(columns=5, rows=rowCounter, text=list_of_strings, text_align='left')

    # Datatype Properties
    hasValue = False
    for s, p, o in main_ontology.triples((None, None, OWL.DatatypeProperty)):
            if(s.__str__().__contains__(domain_name)):
                hasValue = True
    if (hasValue) :
        
        mdFile.new_header(2, "Data Properties")
        list_of_strings = ["Name", "Description", "Domain", "Range", "Subproperty of"] 
        rowCounter = 1
        
        for s, p, o in main_ontology.triples((None, None, OWL.DatatypeProperty)):
            if(s.__str__().__contains__(domain_name)):
                
                #Property Name
                className = s.__str__().replace(cx_s,'') 
                className = "<span id=\""+ className +"\">" + className + "</span>"
                
                #Description
                description = main_ontology.value(s, RDFS.comment)

                #Domain
                domain = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.domain, None)):
                    domain = domain + customizedLink(domain_name, o1.__str__())  + " , "
                domain = domain[:-2]
                    
                #Range 
                range = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.range, None)):
                    range = range + customizedLink(domain_name, o1.__str__()) + " , "
                range = range[:-2]
                
                #subPropertyOf 
                subPropertyOf = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.subPropertyOf, None)):
                    if not(o1.__str__().__contains__('http://www.w3.org/2002/07/owl#topDataProperty')):
                        subPropertyOf = subPropertyOf + customizedLink(domain_name, o1.__str__())  + " , "
                subPropertyOf = subPropertyOf[:-2]
                

                list_of_strings.extend([className, description , domain, range, subPropertyOf ])
                rowCounter = rowCounter + 1

        mdFile.new_line()
        mdFile.new_table(columns=5, rows=rowCounter, text=list_of_strings, text_align='left')

    # Object Properties
    hasValue = False
    for s, p, o in main_ontology.triples((None, None, OWL.ObjectProperty)):
            if(s.__str__().__contains__(domain_name)):
                hasValue = True
    if (hasValue) :
        
        mdFile.new_header(2, "Object Properties")
        list_of_strings = ["Name", "Descriptions", "Domain", "Range", "Subproperty of"]
        rowCounter = 1
        
        for s, p, o in main_ontology.triples((None, None, OWL.ObjectProperty)):
            if(s.__str__().__contains__(domain_name)):
                
                #ObjectProperty
                className = s.__str__().replace(cx_s,'') 
                className = "<span id=\""+ className +"\">" + className + "</span>"
                
                #Description
                description = main_ontology.value(s, RDFS.comment)

                #Domain
                domain = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.domain, None)):
                    domain = domain + customizedLink(domain_name, o1.__str__()) + " , "
                domain = domain[:-2]
                    
                #Range 
                range = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.range, None)):
                    range = range +  customizedLink(domain_name, o1.__str__()) + " , "
                range = range[:-2]
                
                #SubPropertyOf 
                subPropertyOf = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.subPropertyOf, None)):
                    if not(o1.__str__().__contains__('http://www.w3.org/2002/07/owl#topObjectProperty')):
                        subPropertyOf = subPropertyOf +  customizedLink(domain_name, o1.__str__()) + " , "
                subPropertyOf = subPropertyOf[:-2]
                
                list_of_strings.extend([className, description , domain, range, subPropertyOf ])
                rowCounter = rowCounter + 1

        mdFile.new_line()
        mdFile.new_table(columns=5, rows=rowCounter, text=list_of_strings, text_align='left')
        mdFile.create_md_file()
    
    # Annotation Properties
    hasValue = False
    for s, p, o in main_ontology.triples((None, None, OWL.AnnotationProperty)):
            if(s.__str__().__contains__(domain_name)):
                hasValue = True
    if (hasValue) :
    
        mdFile.new_header(2, "Annotation Properties")
        list_of_strings = ["Name", "Descriptions", "Domain", "Range", "Subproperty of"]
        rowCounter = 1
        
        for s, p, o in main_ontology.triples((None, None, OWL.AnnotationProperty)):
            if(s.__str__().__contains__(domain_name)):
                
                #ObjectProperty
                className = s.__str__().replace(cx_s,'') 
                className = "<span id=\""+ className +"\">" + className + "</span>"
                
                #Description
                description = main_ontology.value(s, RDFS.comment)

                #Domain
                domain = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.domain, None)):
                    domain = domain + customizedLink(domain_name, o1.__str__()) + " , "
                domain = domain[:-2]
                    
                #Range 
                range = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.range, None)):
                    range = range +  customizedLink(domain_name, o1.__str__()) + " , "
                range = range[:-2]
                
                #SubPropertyOf 
                subPropertyOf = ""
                for s1, p1, o1 in main_ontology.triples((s, RDFS.subPropertyOf, None)):
                    if not(o1.__str__().__contains__('http://www.w3.org/2002/07/owl#topObjectProperty')):
                        subPropertyOf = subPropertyOf +  customizedLink(domain_name, o1.__str__()) + " , "
                subPropertyOf = subPropertyOf[:-2]
                
                list_of_strings.extend([className, description , domain, range, subPropertyOf ])
                rowCounter = rowCounter + 1

        mdFile.new_line()
        mdFile.new_table(columns=5, rows=rowCounter, text=list_of_strings, text_align='left')

    mdFile.create_md_file()

#Creates md file for taxonomies   
def create_md_file_for_taxonomy(domain_name): 
        
    cx_s = 'https://w3id.org/catenax/taxonomy#'
    
    main_ontology = Graph()
    main_ontology.parse(  'taxonomy/' + domain_name + '_taxonomy.ttl')
    mdFile = mdutils.MdUtils(file_name='docs/' + domain_name + '_taxonomy')

    # Ontology Information
    for s, p, o in main_ontology.triples((None, None, SKOS.ConceptScheme)):

        creator = main_ontology.value(s, DC.creator) if( (s, DC.creator,None) in main_ontology) else "None"
        contributor = main_ontology.value(s, DC.contributor) if( (s, DC.contributor,None) in main_ontology) else "None"
        date = main_ontology.value(s, DC.date) if( (s, DC.date,None) in main_ontology) else "None"
        description = main_ontology.value(s, DC.description) if( (s, DC.description,None) in main_ontology) else "None"
        title = main_ontology.value(s, DC.title) if( (s, DC.title,None) in main_ontology) else "None"
        versionInfo = main_ontology.value(s, OWL.versionInfo) if( (s, OWL.versionInfo,None) in main_ontology) else "None"
     
            
        mdFile.new_header(1, title.__str__())        
        mdFile.new_paragraph("**Title:**  " + title.__str__())
        mdFile.new_paragraph("**Description:**  " + description.__str__())
        mdFile.new_paragraph("**Creator:**  " + creator.__str__())
        mdFile.new_paragraph("**Contributor:**  " + contributor.__str__())
        mdFile.new_paragraph("**Date:**  " + date.__str__())
        mdFile.new_paragraph("**Version:**  " + versionInfo.__str__())
        mdFile.new_paragraph("**Link to ontology:**  " + cx_s[:-1])

    # Ontology image
    mdFile.new_line()
    
    # Concepts
    mdFile.new_header(2, "Concepts")
    list_of_strings = ["Name", "Label", "Description", "Broader", "Narrower"]
    rowCounter = 1
    
    for s, p, o in main_ontology.triples((None, RDF.type, SKOS.Concept)):
            
        #Class name
        className = s.__str__().replace(cx_s,'') 
        className = "<span id=\""+ className +"\">" + className + "</span>"
        
        #pref label
        prefLabel = main_ontology.value(s, SKOS.prefLabel)
        
        #definition  
        definition = main_ontology.value(s, SKOS.definition)

        #broader
        broader = ""
        for b in main_ontology.objects( s, SKOS.broader):            
            broader = broader +  "[" + b.__str__().replace(cx_s,'') +"](#" + b.__str__().replace(cx_s,'') + ") , "       
        broader = broader[:-2]
        
        #Narrower
        narrower = ""
        for b in main_ontology.objects( s, SKOS.narrower):            
            narrower = narrower +  "[" + b.__str__().replace(cx_s,'') +"](#" + b.__str__().replace(cx_s,'') + ") , "       
        narrower = narrower[:-2]
        
        
        list_of_strings.extend([className, prefLabel, definition , broader , narrower])
        
        rowCounter = rowCounter + 1

    mdFile.new_line()
    mdFile.new_table(columns=5, rows=rowCounter, text=list_of_strings, text_align='left')

    mdFile.create_md_file()  
   
# Fuction Call
listOfontologies = os.listdir('./ontology')

for ontology in listOfontologies:
    if(ontology.__contains__('ontology')):
        domain_name = ontology.replace('_ontology.ttl','')
        create_md_file_for_ontology(domain_name)
        
listOfontologies = os.listdir('./taxonomy')

for taxonomy in listOfontologies:
    if(taxonomy.__contains__('taxonomy')):
        domain_name = taxonomy.replace('_taxonomy.ttl','')
        create_md_file_for_taxonomy(domain_name)