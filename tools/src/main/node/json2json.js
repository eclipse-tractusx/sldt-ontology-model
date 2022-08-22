//
// Tool to split a DTC service json into data jsons
// See copyright notice in the top folder
// See authors file in the top folder
// See license file in the top folder
//
const fs = require('fs');

var bpnl = "BPNL00000003COJN";
var input = '../../dataspace/agents/provisioning/resources/dtc_codes.json';
var inputText=fs.readFileSync(input, 'utf8');
var dtcs=JSON.parse(inputText);

var output1 = '../../dataspace/agents/provisioning/resources/dtc_codes_meta.json';
var output2 = '../../dataspace/agents/provisioning/resources/dtc_codes_content.json';
var output3 = '../../dataspace/agents/provisioning/resources/dtc_codes_part.json';

var write = function(path,obj) {
    fs.writeFileSync(path,JSON.stringify(obj),'utf8');
}

dtcs.meta.bpnl=bpnl;

write(output1,[dtcs.meta]);

var contentLength=dtcs.content.length;
var identifiers=[];
var parts=[];

write('INSERT INTO "dtc"."content" ("bpnl","number","id","code","description","possible_causes","created_at","lock_version") VALUES',true);
for(var count=0;count<contentLength;count++) {
    var dtc = dtcs.content[count];
    dtc.bpnl=bpnl;
    for(var pcount=0;pcount<dtc.parts.length;pcount++) {
        var part=dtc.parts[pcount].part;
        if(identifiers.indexOf(part.entityGuid)<0) {
            part.bpnl=bpnl;
            parts.push(part);
            identifiers.push(part.entityGuid);
        }
    }
}
write(output2,dtcs.content);
write(output3,parts);

