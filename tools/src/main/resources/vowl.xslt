<?xml version="1.0" encoding="UTF-8" ?>
<!--
 * Copyright (c) 2022,2023 Contributors to the Catena-X Association
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Apache License, Version 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
-->
<xsl:stylesheet 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
  xmlns:owl="http://www.w3.org/2002/07/owl#" 
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  version="1.0">
  <xsl:output method="text" encoding="UTF-8"  omit-xml-declaration="yes" indent="no" media-type="application/json" />
  <xsl:key name="language" match="*/skos:prefLabel" use="@xml:lang" />
  <xsl:key name="types" match="*/rdfs:range" use="@rdf:resource" />
  <xsl:template match="/rdf:RDF"><xml:text>
{
  "namespace": [
  ],
  "header": {
    "languages": [
      <xsl:for-each select=".//skos:prefLabel[generate-id() = generate-id(key('language',@xml:lang)[1])]">
       <xml:text>"</xml:text><xsl:value-of select="./@xml:lang"/><xml:text>"</xml:text><xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>
     </xsl:for-each>
    ],
    "title": {
      "en": "Catena-X Ontology"
    },
    "iri": "<xsl:value-of select="./owl:Ontology/@rdf:about"/>",
    "version": "0.5.5-SNAPSHOT",
    "author": [
      "Catena-X Consortium"
    ],
    "description": {
      "en": "The Catena-X Ontology is the merged representation of all Catena-X domain ontologies."
    }
  },
  "metrics": {
    "classCount": <xsl:value-of select="count(./owl:Class)"/>,
    "datatypeCount": <xsl:value-of select="count(./rdfs:Datatype)"/>,
    "objectPropertyCount": <xsl:value-of select="count(./owl:ObjectProperty)"/>,
    "datatypePropertyCount": <xsl:value-of select="count(./owl:DatatypeProperty)"/>,
    "propertyCount": <xsl:value-of select="count(./owl:ObjectProperty)+count(./owl:DatatypeProperty)"/>,
    "nodeCount": <xsl:value-of select="count(./*)"/>,
    "axiomCount": <xsl:value-of select="count(.//*)"/>,
    "individualCount": <xsl:value-of select="count(./owl:NamedIndividual)"/> 
  },
  "class": [
     <xsl:for-each select="./owl:Class"><xml:text>
    {
      "id": "</xml:text><xsl:value-of select="generate-id()"/><xml:text>",
      "type": "owl:Class"
    }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if></xml:text>
    </xsl:for-each>
    <xsl:for-each select=".//rdfs:range[generate-id()=generate-id(key('type',@rdf:about)[1])]"><xml:text>
    {
      "id": "</xml:text><xsl:value-of select="generate-id()"/><xml:text>",
      "type": "rdfs:Datatype"
    }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if></xml:text>
    </xsl:for-each>
  ],
  "classAttribute": [
     <xsl:for-each select="./owl:Class"><xml:text>
   {
      "id": "</xml:text><xsl:value-of select="generate-id()"/><xml:text>",
      "label": "</xml:text><xsl:value-of select="./skos:prefLabel[@xml:lang='en']"/><xml:text>",
      "iri": "</xml:text><xsl:value-of select="./@rdf:about"/><xml:text>",
      "individuals": [
        </xml:text><xsl:for-each select="../owl:NamedIndividual[rdf:type/@rdf:resource=current()/@rdf:about]"><xml:text>
        {
          "iri": "</xml:text><xsl:value-of select="./@rdf:about"/><xml:text>",
          "labels": {
            </xml:text><xsl:for-each select="./skos:prefLabel"><xml:text>
            "</xml:text><xsl:value-of select="./@xml:lang"/><xml:text>": "</xml:text><xsl:value-of select="text()"/><xml:text>"<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if></xml:text>
            </xsl:for-each><xml:text>
          },
          "annotations": {
          }
        }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if></xml:text>
        </xsl:for-each><xml:text>
      ],
      "attributes": [
        "external"
      ]
    }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if></xml:text>
    </xsl:for-each>
  ],
  "datatype": [
    {
     <xsl:for-each select="./owl:Class"><xml:text>
    {
      "id": "</xml:text><xsl:value-of select="./@rdf:about"/><xml:text>",
      "type": "</xml:text><xsl:value-of select="./@rdf:about"/><xml:text>"
    }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if></xml:text>
    </xsl:for-each>
    }
  ],
  "datatypeAttribute": [
  ],
  "property": [
    {
      "id": ""
    }
  ],
  "propertyAttribute": [
    {
      "id": "",
      "domain": "",
      "range": "",
      "inverse": "",
      "label": {
        "language": "label"
      },
      "type": "",
      "comment": "",
      "cardinality": "",
      "minCardinality": "",
      "maxCardinality": "",
      "subproperty": [
        ""
      ],
      "equivalent": [
        ""
      ],
      "attributes": [
        "deprecated",
        "external",
        "datatype",
        "object",
        "rdf",
        "transitive",
        "functional",
        "inverse functional",
        "symmetric"
      ]
    }
  ]
}</xml:text>
  </xsl:template>

</xsl:stylesheet>
