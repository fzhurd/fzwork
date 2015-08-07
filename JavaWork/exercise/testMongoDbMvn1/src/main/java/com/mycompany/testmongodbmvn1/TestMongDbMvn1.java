/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.testmongodbmvn1;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;



import java.util.ArrayList;  
  
import java.util.List;  

import org.bson.Document; 
import com.mongodb.MongoClient;  
import com.mongodb.client.MongoCollection;  
import com.mongodb.client.MongoDatabase;  
import com.mongodb.client.MongoIterable;  
 
 

/**
 *
 * @author frank
 */
public class TestMongDbMvn1 {
    
    
    private static final String JDBC_DRIVER = "org.mariadb.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost:3306/test";
    
    //  Database credentials
   static final String USER = "test";
   static final String PASS = "test";
    
   public static void main(String[] args) throws ClassNotFoundException, SQLException { 
   
       MongoClient mongo = null;
       mongo = new MongoClient("localhost", 27017); 
       MongoDatabase testDatabase = mongo.getDatabase("test"); 
       listCollections(testDatabase);
  
       MongoCollection col6= testDatabase.getCollection("col6");

       for (Object document : col6.find()) {  
            System.out.println(document);  
        }  
       
       
       MongoCollection mycol = testDatabase.getCollection("mycol");
       mycol.drop();
       testDatabase.createCollection("mycol");
       MongoCollection mycolNew = testDatabase.getCollection("mycol");
       System.out.println("Collection created successfully");
       
       insert(mycolNew);
       
       
       Connection conn = null;
        Statement stmt = null;
   
        Class.forName("com.mysql.jdbc.Driver");
        System.out.println("Connecting to database...");
        conn = (Connection) DriverManager.getConnection(DB_URL,USER,PASS);
        System.out.println("Creating statement...");
        stmt = conn.createStatement();
            
        String sql;
        //sql = "SELECT CLR_CGI_NEW_LAC,CLR_CGI_NEW_CI, CLR_CAUSETYPE,  CLR_CAUSEVALUE from voice_int_mysql limit 1";
        //sql = "SELECT CLR_CGI_NEW_LAC,CLR_CGI_NEW_CI, CLR_CAUSETYPE,  CLR_CAUSEVALUE from voice_int limit 1";
        sql = "SELECT a, b from t9";
        stmt.executeQuery("USE test");
        //stmt.executeQuery("USE naa6");
        ResultSet rs = stmt.executeQuery(sql);
      
        while(rs.next()){
            /*
            //Retrieve by column name
            int ccnl  = rs.getInt("CLR_CGI_NEW_LAC");
            int ccnc = rs.getInt("CLR_CGI_NEW_CI");
            int ccType  = rs.getInt("CLR_CAUSETYPE");
            int ccv = rs.getInt("CLR_CAUSEVALUE");
    
            //Display values
            System.out.println("CLR_CGI_NEW_LAC: " + ccnl);
            System.out.println("CLR_CGI_NEW_CI: " + ccnc);
            System.out.println("CLR_CAUSETYPE: " +  ccType);
            System.out.println("CLR_CAUSEVALUE: " + ccv);
          */
           String name =  rs.getString("a");
           int age = rs.getInt("b");
           System.out.println("name: "+ name);
           System.out.println("age: "+age);
      }
      //STEP 6: Clean-up environment
      rs.close();
      stmt.close();
       
       
   
       

   
   } 
   
   public static void listDatabases(MongoClient mongo) {  
        // list all databases  
        MongoIterable<String> allDatabases = mongo.listDatabaseNames();  
        for (String db : allDatabases) {  
            System.out.println("Database name: " + db);  
          
        }  
    }  
  
    public static void listCollections(MongoDatabase database) {  
        // list all databases  
        MongoIterable<String> allCollections = database.listCollectionNames();  
        for (String collection : allCollections) {  
            System.out.println("Collection name: " + collection);  
        }  
    }  
      
    
    public static void listAllDocuments(MongoCollection<Document> collection) {  
        System.out.println("begin get all document >>>>>>");  
        for (Document document : collection.find()) {  
            System.out.println(document);  
        }  
        System.out.println("finish get all document >>>>>>");  
    }
    
    
    public static void insert(MongoCollection<Document> collection){  
        List<Document> documents = new ArrayList<Document>();  
        for (int i = 1; i < 3; i++) {  
            //documents.add(new Document("_id", i).append("age", (20+i)).append("name", new Date()));  
            documents.add(new Document("_id", i).append("age", (20+i)).append("grade", Integer.toString(i) ));
        }  
        collection.insertMany(documents);  
    }  
    
    
    
   @Test
   public void testSonarSqlJDBC () throws ClassNotFoundException, SQLException{
   Connection conn2 = null;
   Statement stmt2 = null;
   
   Class.forName("com.mysql.jdbc.Driver");
   System.out.println("Connecting to database...");
      conn2 = (Connection) DriverManager.getConnection(DB_URL,USER,PASS);
      System.out.println("Creating statement...");
      stmt2 = conn2.createStatement();

            
      String sql2;
      sql2 = "SELECT * from col3";
      ResultSet rs2 = stmt2.executeQuery(sql2);
      System.out.println(rs2.getClass().getName());
      
      
      while(rs2.next()){
         //Retrieve by column name
         int id  = rs2.getInt("_id");
         int a2 = rs2.getInt("a");
         String b2 = rs2.getString("b");
         
         if (id==1){
             assertEquals(a2,1);
             assertEquals(b2, "red");
         }
         else if(id==2){
             
             assertEquals(a2,2);
             assertEquals(b2, "");
             
         }
         else if (id==3){
             assertEquals(a2,3);
             assertEquals(b2, true);
         }
       

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", a: " + a2);
         System.out.print(",b: " + b2);
        
      }
       
      //STEP 6: Clean-up environment
      rs2.close();
      stmt2.close();
   }
    
}
