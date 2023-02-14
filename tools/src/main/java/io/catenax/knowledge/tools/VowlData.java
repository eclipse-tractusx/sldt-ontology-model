//
// Catena-X Ontology Tools
// See copyright notice in the top folder
// See authors file in the top folder
// See license file in the top folder
//
package io.catenax.knowledge.tools;

import de.uni_stuttgart.vis.vowl.owl2vowl.model.entities.AbstractEntity;
import de.uni_stuttgart.vis.vowl.owl2vowl.model.entities.properties.VowlObjectProperty;
import org.semanticweb.owlapi.model.IRI;

import java.util.Map;
import java.util.stream.Collectors;

/**
 * A modified vowl data model which suppresses redundant
 * object properties which have only a single domain and are
 * expected to have a someValue constraint on the subClass relation anyway.
 */
public class VowlData extends de.uni_stuttgart.vis.vowl.owl2vowl.model.data.VowlData {

    /**
     * flag whether we are still building or exporting
     */
    protected boolean isExport=false;

    /**
     * @return export flag
     */
    public boolean isExport() {
        return isExport;
    }

    /**
     * set
     * @param export flag
     */
    public void setExport(boolean export) {
        isExport = export;
    }

    /**
     * filters the entities when in export mode
     * @return map of entities with object properties filtered
     */
    public Map<IRI, AbstractEntity> getEntityMap() {
        Map<IRI, AbstractEntity> entities=super.getEntityMap();
        if(isExport) {
            // filter the entities for pure objectProperties with a single domain
            entities=entities.entrySet().stream().filter( entity ->
                    (!(entity.getValue() instanceof VowlObjectProperty) || !(((VowlObjectProperty) entity.getValue()).getType().equals("owl:objectProperty")) || ((VowlObjectProperty) entity.getValue()).getDomains().size()>1)).
                    collect(Collectors.toMap(entity->entity.getKey(),entity->entity.getValue()));
        }
        return entities;
    }

}
