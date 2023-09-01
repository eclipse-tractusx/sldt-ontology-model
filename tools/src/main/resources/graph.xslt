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
  version="1.0">
  <xsl:output method="text" encoding="UTF-8"  omit-xml-declaration="yes" indent="no" media-type="application/json" />

  <xsl:template match="/rdf:RDF">
{ 
    "nodes":[<xsl:for-each select="owl:Class">
      { "data": { "id": "<xsl:value-of select="@rdf:about"/>", "type":"class", "category": "<xsl:value-of select="rdfs:isDefinedBy/@rdf:resource"/>", "label": "<xsl:value-of select="skos:prefLabel"/>" } } ,
    </xsl:for-each><xsl:for-each select="owl:NamedIndividual">
      { "data": { "id": "<xsl:value-of select="@rdf:about"/>", "type":"object", "category": "<xsl:value-of select="../owl:Class[@rdf:about=current()/rdf:type/@rdf:resource]/rdfs:isDefinedBy/@rdf:resource"/>", "label": "<xsl:value-of select="skos:prefLabel"/>" } }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>
  </xsl:for-each>],
    "edges":[<xsl:for-each select="owl:ObjectProperty">
      { "data": { "source": "<xsl:value-of select="rdfs:domain/@rdf:resource"/>", "type":"relation", "target": "<xsl:value-of select="rdfs:range/@rdf:resource"/>", "category": "<xsl:value-of select="rdfs:isDefinedBy/@rdf:resource"/>", "label": "<xsl:value-of select="skos:prefLabel"/>" } } ,
    </xsl:for-each><xsl:for-each select="owl:Class/rdfs:subClassOf">
      { "data": { "source": "<xsl:value-of select="../@rdf:about"/>", "type":"subclass", "target": "<xsl:value-of select="@rdf:resource"/>", "category": "<xsl:value-of select="../rdfs:isDefinedBy/@rdf:resource"/>", "label": "subclass" } } ,
    </xsl:for-each><xsl:for-each select="owl:NamedIndividual/rdf:type">
    { "data": { "source": "<xsl:value-of select="../@rdf:about"/>", "type":"instance", "target": "<xsl:value-of select="@rdf:resource"/>", "category": "<xsl:value-of select="../../owl:Class[@rdf:about=current()/@rdf:resource]/rdfs:isDefinedBy/@rdf:resource"/>", "label": "type" } } <xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>
  </xsl:for-each>]
}
  </xsl:template>

</xsl:stylesheet>