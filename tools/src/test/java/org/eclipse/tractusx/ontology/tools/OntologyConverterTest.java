// Copyright (c) 2022,2023 T-Systems International GmbH
// Copyright (c) 2022,2023 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
// Copyright (c) 2022,2023 ZF Friedrichshafen AG 
// Copyright (c) 2022,2023 Mercedes-Benz AG 
// Copyright (c) 2022,2023 Contributors to the Catena-X Association
//
// See the NOTICE file(s) distributed with this work for additional
// information regarding copyright ownership.
//
// This program and the accompanying materials are made available under the
// terms of the Apache License, Version 2.0 which is available at
// https://www.apache.org/licenses/LICENSE-2.0.
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.
//
// SPDX-License-Identifier: Apache-2.0
package org.eclipse.tractusx.ontology.tools;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import de.uni_stuttgart.vis.vowl.owl2vowl.export.types.BackupExporter;
import org.junit.jupiter.api.Test;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyManager;

import java.io.File;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for the vowl converter
 */
public class OntologyConverterTest {

    /** ontology manager */
    OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
    ObjectMapper jsonMapper=new ObjectMapper();

    /**
     * read the CX ontology, merge it and understand it as an xml document
     */
    @Test
    public void testRestrictions() throws Exception {
        OWLOntology ontology=manager.loadOntologyFromOntologyDocument(new File("src/test/resources/restrictions_ontology.ttl"));
        OntologyConverter converter=new OntologyConverter(ontology);
        converter.clearLoadingMsg();
        BackupExporter exporter = new BackupExporter();
        try {
            converter.export(exporter);
        } catch (Exception var3) {
            throw new IllegalStateException(var3);
        }
        String json=exporter.getConvertedJson();
        JsonNode value= jsonMapper.readTree(json);
        // two classes: Process, Action and 1 Type string
        assertEquals(3,((ArrayNode) value.get("class")).size(),"Correct class size");
        // two classes: Process and Action and 1 Type string
        assertEquals(3,((ArrayNode) value.get("classAttribute")).size(),"Correct classAttribute size");
        // two properties: disjointness and someValues
        assertEquals(3,((ArrayNode) value.get("property")).size(),"Correct property size");
        // two properties: disjointness and someValues
        assertEquals(3,((ArrayNode) value.get("propertyAttribute")).size(),"Correct propertyAttribute size");
    }

    /**
     * read the CX ontology, merge it and understand it as an xml document
     */
    @Test
    public void testUnions() throws Exception {
        OWLOntology ontology=manager.loadOntologyFromOntologyDocument(new File("src/test/resources/unions_ontology.ttl"));
        OntologyConverter converter=new OntologyConverter(ontology);
        converter.clearLoadingMsg();
        BackupExporter exporter = new BackupExporter();
        try {
            converter.export(exporter);
        } catch (Exception var3) {
            throw new IllegalStateException(var3);
        }
        String json=exporter.getConvertedJson();
        JsonNode value= jsonMapper.readTree(json);
        // two classes: Process, Action and 2 anonymous unions
        assertEquals(4,((ArrayNode) value.get("class")).size(),"Correct class size");
        assertEquals(4,((ArrayNode) value.get("classAttribute")).size(),"Correct classAttribute size");
        // 6 concrete rels
        assertEquals(6,((ArrayNode) value.get("property")).size(),"Correct property size");
        assertEquals(6,((ArrayNode) value.get("propertyAttribute")).size(),"Correct propertyAttribute size");
    }
}
