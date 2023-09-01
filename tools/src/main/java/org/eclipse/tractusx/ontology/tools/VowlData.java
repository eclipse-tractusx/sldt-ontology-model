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

import de.uni_stuttgart.vis.vowl.owl2vowl.model.entities.AbstractEntity;
import de.uni_stuttgart.vis.vowl.owl2vowl.model.entities.nodes.datatypes.DatatypeReference;
import de.uni_stuttgart.vis.vowl.owl2vowl.model.entities.properties.VowlDatatypeProperty;
import de.uni_stuttgart.vis.vowl.owl2vowl.model.entities.properties.VowlObjectProperty;
import org.semanticweb.owlapi.model.IRI;

import java.util.Map;
import java.util.Set;
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

    /** filters entities based on redundancies */
    public boolean filter(Map<IRI, AbstractEntity> entities, AbstractEntity entity) {
        if (entity instanceof VowlObjectProperty && entity.getType().equals("owl:objectProperty")) {
            return ((VowlObjectProperty) entity).getDomains().size() != 1;
        } else if (entity instanceof VowlDatatypeProperty && entity.getType().equals("owl:datatypeProperty")) {
            return ((VowlDatatypeProperty) entity).getDomains().size() != 1;
        } else if (entity instanceof DatatypeReference && entity.getType().equals("rdfs:Datatype")) {
            Set<IRI> allIngoing=((DatatypeReference) entity).getInGoingProperties();
            return allIngoing.size() == 0 ||
                    allIngoing.stream().anyMatch(iri -> filter(entities, entities.get(iri)));
        }
        return true;
    }

    /**
     * filters the entities when in export mode
     * @return map of entities with object properties filtered
     */
    @Override
    public Map<IRI, AbstractEntity> getEntityMap() {
        Map<IRI, AbstractEntity> entities=super.getEntityMap();
        if(isExport) {
            // filter the entities for pure objectProperties with a single domain
            final Map<IRI, AbstractEntity> previousEntities=entities;
            entities=entities.entrySet().stream().filter( entityEntry -> filter(previousEntities,entityEntry.getValue())).collect(Collectors.toMap(Map.Entry::getKey,Map.Entry::getValue));
        }
        return entities;
    }

}
