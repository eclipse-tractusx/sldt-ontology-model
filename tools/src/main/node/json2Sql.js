const fs = require('fs');

var bpnl = "BPNL00000003COJN";
var input = '../../dataspace/agents/provisioning/resources/dtc_codes.json';
var inputText=fs.readFileSync(input, 'utf8');
var dtcs=JSON.parse(inputText);

var output = '../../dataspace/agents/provisioning/resources/dtc.sql';

var write = function(text, append) {
    if(append) {
        fs.appendFileSync(output,"\n",'utf8');
        fs.appendFileSync(output,text,'utf8');
    } else {
        fs.writeFileSync(output,text,'utf8');
    }
};

write('DROP SCHEMA IF EXISTS "dtc" CASCADE;',false);
write('CREATE SCHEMA "dtc";',true);
write('',true);

write('CREATE TABLE "dtc"."meta" (',true);
write('  "bpnl" varchar(17) NOT NULL,',true);
write('  "first" BOOLEAN NOT NULL,',true);
write('  "last" BOOLEAN NOT NULL,',true);
write('  "number" INT NOT NULL,',true);
write('  "number_of_elements" INT NOT NULL,',true);
write('  "size" INT NOT NULL,',true);
write('  "total_elements" INT NOT NULL,',true);
write('  "total_pages" INT NOT NULL,',true);
write('  PRIMARY KEY ("bpnl", "number")',true);
write(');',true);


var meta=dtcs.meta;

write('INSERT INTO "dtc"."meta" ("bpnl","first","last","number","number_of_elements","size","total_elements","total_pages") VALUES',true);
write(`  ('${bpnl}',${meta.first},${meta.last},${meta.number},${meta.number_of_elements},${meta.size},${meta.total_elements},${meta.total_pages});`,true);
write('',true);


write('CREATE TABLE "dtc"."content" (',true);
write('  "bpnl" varchar(17) NOT NULL,',true);
write('  "number" INT NOT NULL,',true);
write('  "id" VARCHAR(64) NOT NULL PRIMARY KEY,',true);
write('  "code" VARCHAR(10) NOT NULL,',true);
write('  "description" VARCHAR(256) NOT NULL,',true);
write('  "possible_causes" VARCHAR(256) NOT NULL,',true);
write('  "make" VARCHAR(256) NULL,',true);
write('  "created_at" VARCHAR(64) NOT NULL,',true);
write('  "updated_at" VARCHAR(64) NULL,',true);
write('  "lock_version" INT NOT NULL',true);
write(');',true);
write('ALTER TABLE "dtc"."content" ADD FOREIGN KEY ("bpnl","number") REFERENCES "dtc"."meta"("bpnl","number");',true);

var content=dtcs.content;
var contentLength=content.length;

write('INSERT INTO "dtc"."content" ("bpnl","number","id","code","description","possible_causes","created_at","lock_version") VALUES',true);
for(var count=0;count<contentLength;count++) {
    var separator=",";
    if(count==contentLength-1) {
        separator=";";
    }
    var dtc=content[count];
    write(`  ('${bpnl}',${meta.number},'${dtc.id}','${dtc.code}','${dtc.description}','${dtc.possible_causes}','${dtc.created_at}',${dtc.lock_version})${separator}`,true);
}
write('',true);


write('CREATE TABLE "dtc"."part" (',true);
write('  "bpnl" varchar(17) NOT NULL,',true);
write('  "number" INT NOT NULL,',true);
write('  "entityGuid" VARCHAR(64) NOT NULL PRIMARY KEY,',true);
write('  "enDenomination" VARCHAR(256) NOT NULL,',true);
write('  "classification" VARCHAR(256) NOT NULL,',true);
write('  "category" VARCHAR(256) NOT NULL,',true);
write('  "enDaClass" VARCHAR(256) NOT NULL',true);
write(');',true);
write('ALTER TABLE "dtc"."part" ADD FOREIGN KEY ("bpnl","number") REFERENCES "dtc"."meta"("bpnl","number");',true);

var identifiers=[];

var separator=" ";
write('INSERT INTO "dtc"."part" ("bpnl","number","entityGuid","enDenomination","classification","category","enDaClass") VALUES',true);
for(var count=0;count<contentLength;count++) {
    var dtc=content[count];
    var parts=dtc.parts;
    for(var pcount=0;pcount<parts.length;pcount++) {
        var part=parts[pcount];
        if(identifiers.indexOf(part.part.entityGuid)<0) {
            write(`${separator}('${bpnl}',${meta.number},'${part.part.entityGuid}','${part.part.enDenomination}','${part.part.classification}','${part.part.category}','${part.part.enDaClass}')`,true);
            separator=",";
            identifiers.push(part.part.entityGuid);
        }
    }
}
write(';',true);

write('CREATE TABLE "dtc"."content_part" (',true);
write('  "part_entityGuid" VARCHAR(64) NOT NULL,',true);
write('  "dtc_id" VARCHAR(64) NOT NULL',true);
write(');',true);
write('ALTER TABLE "dtc"."content_part" ADD FOREIGN KEY ("dtc_id") REFERENCES "dtc"."content"("id");',true);
write('ALTER TABLE "dtc"."content_part" ADD FOREIGN KEY ("part_entityGuid") REFERENCES "dtc"."part"("entityGuid");',true);

write('INSERT INTO "dtc"."content_part" ("part_entityGuid","dtc_id") VALUES',true);
separator=" ";
for(var count=0;count<contentLength;count++) {
    var dtc=content[count];
    var parts=dtc.parts;
    for(var pcount=0;pcount<parts.length;pcount++) {
        var part=parts[pcount];
        write(`${separator}('${part.part.entityGuid}','${dtc.id}')`,true);
        var separator=",";
    }
}
write(';',true);


