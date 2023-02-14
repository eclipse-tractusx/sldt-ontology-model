//
// Catena-X Ontology Tools
// See copyright notice in the top folder
// See authors file in the top folder
// See license file in the top folder
//
package io.catenax.knowledge.tools;

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
    public void testConverter() throws Exception {
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
}
