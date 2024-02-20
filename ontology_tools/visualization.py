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
import graphviz
from rdflib import Graph, SKOS, OWL, RDFS, RDF
#from ontology_tools.settings import ontology_path, refactored_path

# only for rectored ontologies

def getDomainName(cxObject):
    
    cxObject = cxObject.replace('https://w3id.org/catenax/ontology/','').split('#')[0]
    return cxObject

domain_name = "core"

xsd = "http://www.w3.org/2001/XMLSchema#" 
cx_s = 'https://w3id.org/catenax/ontology/core#'

main_ontology = Graph()
main_ontology.parse(  'ontology/' + domain_name + '_ontology.ttl')
counter = 0
colors = ['deepskyblue', 'yellowgreen', 'yellow', 'magenta', 'orange', 'deeppink', 'purple', 'springgreen', 'green', 'blue' , 'red' , 'white',]
dict = {}

dot = graphviz.Digraph(name = domain_name + '_ontology', 
#,'rankdir':'RL'
#'label': domain_name + ' ontology', 'labelloc':'t','rankdir':'RL',
#'width':'0', 'height':'0'
graph_attr = { 'fontsize':'10', 'fontname' : 'Helvetica,Arial,sans-serif', 'layout':'neato', 'overlap':'scalexy', 'splines':'ortho'},  #'splines':'ortho',
node_attr = {'fontsize':'10', 'fontname':'Helvetica,Arial,sans-serif', 'shape':'record', 'fillcolor':'gray95'},
edge_attr = {'fontsize':'10', 'fontname':'Helvetica,Arial,sans-serif', 'arrowsize':'0.3', 'penwidth':'0.3'})


# add node (classes)
for s, p, o in main_ontology.triples((None, None, OWL.Class)):
    
    classDesign =  "<{<b>" + s.__str__().replace(cx_s,'') + "</b> | <i><b> domain:" + getDomainName(s.__str__()) + "</b></i> <br align=\"left\"/>"
    #classDesign = "<{<b>I/O class</b> | <i>This text is normal.</i> <br align=\"left\"/>...<br align=\"left\"/>|+ method<br align=\"left\"/>...<br align=\"left\"/>}>"
    
    for dataType in main_ontology.subjects( RDFS.domain, s):
        if (dataType, RDF.type, OWL.DatatypeProperty) in main_ontology:
            for range in main_ontology.objects(dataType, RDFS.range):
                classDesign = classDesign +  dataType.__str__().replace(cx_s,'') + ":" + range.__str__().replace(xsd,'') + "<br align=\"left\"/>"
    
    classDesign = classDesign + "}>"
    
    dot.node(s.__str__().replace(cx_s,''), label = classDesign , style='filled' ) 


# add node (edges)
for s, p, o in main_ontology.triples((None, None, OWL.ObjectProperty)):
    if not (s,OWL.inverseOf,None) in main_ontology:
        edgelabel = s.__str__().replace(cx_s,'')
    
        if  (None, OWL.inverseOf, s) in main_ontology:
            for inv in main_ontology.subjects( OWL.inverseOf, s):
                edgelabel = edgelabel + ' / \n' + inv.__str__().replace(cx_s,'') + " ➝"

        dot.node(s.__str__().replace(cx_s,''), label=edgelabel, style='filled' ,  fillcolor = 'greenyellow', shape = 'plaintext', fontsize = '8', width='0', height='0' ) 


# add edges
for s, p, o in main_ontology.triples((None, None, OWL.ObjectProperty)):
    if not (s,OWL.inverseOf,None) in main_ontology:
        for s1, p1, o1 in main_ontology.triples((s, RDFS.domain, None)):
            for s2, p2, o2 in main_ontology.triples((s, RDFS.range, None)):
                
                dot.edge(o1.__str__().replace(cx_s,''), s.__str__().replace(cx_s,''),  arrowhead = 'none' ) #label = s.__str__().replace(cx_s,''),
                dot.edge(s.__str__().replace(cx_s,''), o2.__str__().replace(cx_s,''),  ) #label = s.__str__().replace(cx_s,'') 

# add sub classes style=dashed
for s, p, o in main_ontology.triples((None, RDFS.subClassOf, None)):
    dot.edge(s.__str__().replace(cx_s,''), o.__str__().replace(cx_s,''), style='dashed') 

print(dot.source)  
dot.format='svg'
dot.render(directory= 'docs/images', view=True).replace('\\', '/')

#fie_ext = 'jpg'
#temp_img = 'ontology/temp_file'
#my_graph = graphviz.Source(graph_data)
#my_graph.render(temp_img,format=fie_ext, view=False
#dot.render(temp_img,format=fie_ext, view=False)
#dot.format = 'jpg'

#dot.render(directory='ontology/doctest-output')
