package org.yzy.test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.queryParser.ParseException;
import org.apache.lucene.queryParser.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.store.LockObtainFailedException;
import org.apache.lucene.util.Version;



public class HelloLucene {


	// ��������
	public void index(){
		IndexWriter writer = null;
		try {
			//1.����Directory
			//Directory directory = new RAMDirectory(); //�������ڴ���
			//Directory directory = FSDirectory.open(new File("C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/index"));
			Directory directory = FSDirectory.open(new File("C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/index2"));
			//2.����IndexWriter
			IndexWriterConfig iwc = new IndexWriterConfig(Version.LUCENE_35, new StandardAnalyzer(Version.LUCENE_35));
			writer = new IndexWriter(directory, iwc);
			//3.����Document����
			Document doc = null;
			//4.ΪDocument���Field
			File f = new File("C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/keywords_per_doucment");
			for(File file:f.listFiles()){
				doc = new Document();
				doc.add(new Field("content",new FileReader(file)));
				doc.add(new Field("filename",file.getName(),Field.Store.YES,Field.Index.NOT_ANALYZED));
				doc.add(new Field("path",file.getAbsolutePath(),Field.Store.YES,Field.Index.NOT_ANALYZED));
				//5.ͨ��IndexWriter����ĵ���������
				writer.addDocument(doc);
			}
		} catch (CorruptIndexException e) {
			e.printStackTrace();
		} catch (LockObtainFailedException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally{
			if(writer!=null)
				try {
					writer.close();
				} catch (CorruptIndexException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
		}
	}
	
	
	//����
	public void searcher(){
		int hitsPerPage = 10;
		//int hitsPerPage = 1;
		try {
			//1.����Directory
			Directory directory = FSDirectory.open(new File("C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/index"));
			//2.����IndexReader
			IndexReader reader = IndexReader.open(directory);
			//3.����IndexReader����IndexSearcher
			IndexSearcher searcher = new IndexSearcher(reader);
			//4.����������Query
			QueryParser parser = new QueryParser(Version.LUCENE_35,"content",new StandardAnalyzer(Version.LUCENE_35));
			//String path_train = "C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/validation_set.tsv";
			//String path_output = "C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/lucene_search_result_validation.txt";
			String path_train = "C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/training_set.tsv";
			String path_output = "C:/workspace/MyPythonWorkspace/kaggle_Allen_AI_get_data/data/lucene_search_result_training.txt";
			Writer writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(path_output), "UTF-8"));
			BufferedReader br = new BufferedReader(new FileReader(path_train));
			String line;
			while((line = br.readLine()) != null){
				line = line.trim();
				String[] lst = line.split("\t");
				String query_s = lst[1];
				if(query_s == "question"){
					System.out.println("AAA");
					continue;
				}
				System.out.println("query_s: "+query_s);
				writer.write(query_s+"\t");
				try{
	                Query query = parser.parse(query_s);
	                System.out.println("Searching for: " + query.toString("content"));
	                doPagingSearch(writer, searcher, query, hitsPerPage);
	            } catch (org.apache.lucene.queryParser.ParseException e) {
	                continue;
	            }

            }
			
			//5.����Seacher����������TopDocs
			//TopDocs tds = searcher.search(query, 10);
			//6.����TopDocs��ȡScoreDoc����
			//ScoreDoc[] sds = tds.scoreDocs;
			//for(ScoreDoc sd : sds){
				//7.����seacher��ScoreDoc��ȡ��������Document����
			//	Document d = seacher.doc(sd.doc);
				//8.����Document�����ȡ��Ҫ��ֵ
			//	System.out.println(d.get("filename")+"["+d.get("path")+"]");
			//}
			//9.�ر�reader
			writer.close();
			reader.close();
		}
		catch (IOException e) {
				// TODO Auto-generated catch block
			e.printStackTrace();
		}	
	}
	public static void doPagingSearch(Writer writer, IndexSearcher searcher, Query query, int hitsPerPage) throws IOException {

		TopDocs results = searcher.search(query, hitsPerPage);
		ScoreDoc[] hits = results.scoreDocs;
		System.out.println("hits.length: " + Integer.toString(hits.length));
		for (int i = 0; i < hits.length; i++) {
		Document doc = searcher.doc(hits[i].doc);
			String path = doc.get("path");
			writer.write(path + ",");
			//tring filename = doc.get("filename");
			//writer.write(filename + ",");
		}
		writer.write("\r\n");
	}
}
