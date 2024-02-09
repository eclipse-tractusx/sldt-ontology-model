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
const JG = require('./JG');
const moment = require('./moment');

/*
 * read the former testdata
 */
var testDataContainer=JG.readFile('tools/src/main/resources/CX_Testdata_v1.5.1-AsPlanned.json');
var testData = testDataContainer['https://catenax.io/schema/TestDataContainer/1.0.0'];
var testHeader = testData[0];
var plainObject=testHeader.PlainObject[0];
var UIDPOOL = JSON.parse(plainObject.UIDPOOL.replaceAll("'",'"'));
var testObjects = testData.slice(1);
var twins={};
for(twinId in testObjects) {
    var twin=testObjects[twinId];
    twins[twin.catenaXId]=twin;
}

/* manipulate test data */
for(var id in twins){
    twin=twins[id];
    var childs=0;
    var bom=twin["urn:bamm:io.catenax.single_level_bom_as_planned:2.0.0#SingleLevelBomAsPlanned"];
    if(bom != undefined && bom.length>0) {
        childs=bom[0].childItems.length;
    }
    var part=twin["urn:bamm:io.catenax.part_as_planned:1.0.1#PartAsPlanned"];
    var materialName=JG.loremIpsum({units: 'words', count: 1});
    var materialClass=JG.materialClass();
    var materialComponents = JG.repeat(1,childs+1, function() {
      return {
          "aggregateState" : JG.random("solid", "liquid", "gasenous"),
          "weight" : JG.floating(1, 1000, 3),
          "materialName" : JG.loremIpsum({units: 'words', count: 1}),
          "recycledContent" : JG.floating(1, 1000, 3),
          "materialClass" : JG.materialClass(),
          "materialAbbreviation" : JG.objectId()
          };
       });
    if(part!= undefined && part.length>0) {
      if(part[0].partTypeInformation.nameAtManufacturer.includes('Cathode')) {
        materialName='Automotive Cell Cathode Material';
        materialClass='CathodeMaterial_LithiumNickelManganeseCobaltOxides';
      }
      if(part[0].partTypeInformation.nameAtManufacturer.includes('Natural Rubber')) {
        materialName= 'Natural Rubber Class 5';
        materialClass= 'OrganicMaterial_Rubber';
      }
      if(part[0].partTypeInformation.nameAtManufacturer.includes('Tire')) {
        materialName = 'Wheel Rubber';
        materialClass = 'PolymerMaterial';
        materialComponents = [ {
           "aggregateState" : "solid",
           "weight" : "3.2",
           "materialName" : "Natural Rubber Class 5",
           "recycledContent" : "0.2",
           "materialClass" : "OrganicMaterial_Rubber",
           "materialAbbreviation" : "NR"
         } ];
      }
    }      
    twin["urn:bamm:io.catenax.material_for_recycling:1.1.0#MaterialForRecycling"] = [ {
        "materialName" : materialName,
        "materialClass" : materialClass,
        "component" : materialComponents
      } ];
}

/** Recollect and write */
testObjects=[];
for(var id in twins){
    testObjects.push(twins[id]);
}

for(let i = 0; i < 0; i++) {
    var clones={};
    for(var id in twins) {
        clones[id]=`urn:uuid:${JG.guid()}`;
        UIDPOOL.push(clones[id]);
    }
    for(var id in twins) {
        var twin=JSON.parse(JSON.stringify(twins[id]));
        twin.catenaXId=clones[id];
        for(var aas in twin["https://catenax.io/schema/AAS/3.0"]) {
          aas.globalAssetId.value[0]=clones[id];
          aas.id=`urn:uuid:${JG.guid()}`;
        }
        for(var aspect in twin["urn:bamm:io.catenax.part_as_planned:1.0.1#PartAsPlanned"]) {
          aspect.catenaXId=clones[id];
          aspect.partTypeInformation.manufacturerPartId=aspect.partTypeInformation.manufacturerPartId+i;
          aspect.partTypeInformation.nameAtManufacturer=aspect.partTypeInformation.nameAtManufacturer+i;
        }
        for(var aspect in twin["urn:bamm:io.catenax.part_site_information_as_planned:1.0.0#PartSiteInformationAsPlanned"]) {
          aspect.catenaXId=clones[id];
        }
        for(var aspect in twin["urn:bamm:io.catenax.single_level_bom_as_planned:2.0.0#SingleLevelBomAsPlanned"]) {
          aspect.catenaXId=clones[id];
          for(var childId in aspect.childItems) {
            var child=aspect.childItems[childId];
            child.childCatenaXId=clones[child.childCatenaXId];
          }
        }
        for(var aspect in twin["urn:bamm:io.catenax.single_level_usage_as_planned:1.1.0#SingleLevelUsageAsPlanned"]) {
          aspect.catenaXId=clones[id];
          for(var parentId in aspect.parentParts) {
            var parent=aspect.parentParts[parentId];
            parent.parentCatenaXId=clones[parent.parentCatenaXId];
          }
        }
        testObjects.push(twin);
    }
}

plainObject.UIDPOOL=JSON.stringify(UIDPOOL).replaceAll('"',"'");
testObjects.unshift(testHeader);
testDataContainer={};
testDataContainer['https://catenax.io/schema/TestDataContainer/1.0.0']=testObjects;
JG.writeFile('tools/src/test/resources/CX_Testdata_v1.5.2-SNAPSHOT-AsPlanned.json',testDataContainer);


