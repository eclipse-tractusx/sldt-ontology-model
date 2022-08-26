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

import java.io.BufferedOutputStream;
import java.io.BufferedWriter;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintStream;
import java.io.Writer;
import java.util.ArrayList;

import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;

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
   public void run(String[] args) throws Exception {
      ArrayList<String> remainingArgs=new ArrayList<String>();
      PrintStream outStream = System.out;
      String styleSheet=null;
      try {
         for(int count=0;count<args.length;count++) {
            if("-styleSheet".equals(args[count])) {
               styleSheet=args[++count];
            } else {
               remainingArgs.add(args[count]);
            }
         }
         ByteArrayOutputStream bos=new ByteArrayOutputStream();
         run(remainingArgs.toArray(new String[remainingArgs.size()]),bos);
         if(styleSheet!=null) {
            StreamSource sheet = new javax.xml.transform.stream.StreamSource(styleSheet);
            TransformerFactory factory=TransformerFactory.newInstance();
            Transformer transformer=factory.newTransformer(sheet);
            ByteArrayInputStream bis=new ByteArrayInputStream(bos.toByteArray());
            bos=new ByteArrayOutputStream();
            transformer.transform(new StreamSource(bis), new StreamResult(bos));
         }
         outStream.println(new String(bos.toByteArray()));
         outStream.flush();
      } finally {
         if(outStream!=System.out) {
            outStream.close();
         }
      }
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
      
      OWLOntology newOntology = manager.createOntology(IRI.create("https://github.com/catenax-ng/product-knowledge"),imports,false);
      newOntology.getOWLOntologyManager().saveOntology(newOntology, out);
   }

   /** main entry */
   public static void main(String[] args) throws Exception {
      new OntologyMerger().run(args);
   }

}


