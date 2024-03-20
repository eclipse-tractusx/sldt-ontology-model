import operator
import mdutils
import os
from rdflib import Graph, SKOS, OWL, RDFS, RDF, DC

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
    

def create_md_file_for_domain(domain_name):
    
    cx_s = 'https://w3id.org/catenax/ontology/' + domain_name + '#'
    main_ontology = Graph()
    main_ontology.parse(  'ontology/' + domain_name + '_ontology.ttl')
    mdFile = mdutils.MdUtils(file_name='docs/' + domain_name + '_ontology')

    # Ontology Information
    for s, p, o in main_ontology.triples((None, None, OWL.Ontology)):

        creator = main_ontology.value(s, DC.creator) if( (s, DC.creator,None) in main_ontology) else "None"
        contributor = main_ontology.value(s, DC.contributor) if( (s, DC.contributor,None) in main_ontology) else "None"
        date = main_ontology.value(s, DC.date) if( (s, DC.creator,None) in main_ontology) else "None"
        description = main_ontology.value(s, DC.description) if( (s, DC.creator,None) in main_ontology) else "None"
        title = main_ontology.value(s, DC.title) if( (s, DC.creator,None) in main_ontology) else "None"
        versionInfo = main_ontology.value(s, OWL.versionInfo) if( (s, DC.creator,None) in main_ontology) else "None"
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
    mdFile.new_line(mdFile.new_inline_image(text='ontology', path='images/' + domain_name + '_ontology.gv.svg'))
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

#create_md_file_for_domain('core')
#create_md_file_for_domain('function')
#create_md_file_for_domain('behaviour')
   
# Fuction Call
listOfontologies = os.listdir('./ontology')

for ontology in listOfontologies:
    if(ontology.__contains__('ontology')):
        domain_name = ontology.replace('_ontology.ttl','')
        create_md_file_for_domain(domain_name)