//
// Tool to merge ontologies into single file
// See copyright notice in the top folder
// See authors file in the top folder
// See license file in the top folder
//
package io.catenax.knowledge.tools;

import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.util.OWLOntologyMerger;
import org.semanticweb.owlapi.apibinding.OWLManager;
import java.io.FileInputStream;
import java.io.OutputStream;
import java.util.ArrayList;

/**
 * Command line tool to merge several ontology files into
 * a single one.
 */
public class OntologyMerger {
   /** ontology manager */
   OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
   /** the ontology merger tool */
   OWLOntologyMerger ontologyMerger = new OWLOntologyMerger(manager);

   /** 
    * run the merge command on the given files and output the result to the console  
    * @param files a set of filenames
    */
   public void run(String[] files) throws Exception {
      run(files,System.out);
   }

   /** 
    * run the merge command on the given files with the given output stream
    */
   public void run(String[] args, OutputStream out) throws Exception {
      ArrayList<OWLOntology> imports=new ArrayList();

      for(int count=0;count<args.length;count++) {
         try(FileInputStream fi=new FileInputStream(args[count])) {
            imports.add(manager.loadOntologyFromOntologyDocument(fi));
         }
      }
      
      OWLOntology newOntology = manager.createOntology(IRI.create("https://github.com/catenax-ng/product-knowledge"),imports,true);
      newOntology.getOWLOntologyManager().saveOntology(newOntology, out);
   }

   /** main entry */
   public static void main(String[] args) throws Exception {
      new OntologyMerger().run(args);
   }

}


