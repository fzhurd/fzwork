/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mongomariadb1;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;



import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.ArrayList;  
  
import java.util.List;  

import org.bson.Document; 
import com.mongodb.MongoClient;  
import com.mongodb.client.MongoCollection;  
import com.mongodb.client.MongoDatabase;  
import com.mongodb.client.MongoIterable;  


import com.mysql.jdbc.Driver;
import java.sql.*;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 *
 * @author frank
 */
//@RunWith(Suite.class)
//@Suite.SuiteClasses({})
public class MongomariadbTest {
    
   private static final String JDBC_DRIVER = "org.mariadb.jdbc.Driver";
   static final String DB_URL = "jdbc:mysql://localhost:3306/test";
    
    //  Database credentials
   static final String USER = "test";
   static final String PASS = "test";

    @BeforeClass
    public static void setUpClass() throws Exception {
    }

    @AfterClass
    public static void tearDownClass() throws Exception {
    }

    @Before
    public void setUpMongo() throws Exception {
       MongoClient mongo = null;
       mongo = new MongoClient("localhost", 27017); 
       MongoDatabase testDatabase = mongo.getDatabase("test");
       
       MongoCollection mongoCol1 = testDatabase.getCollection("mongoCol1");
       mongoCol1.drop();
       testDatabase.createCollection("mongoCol1");
       MongoCollection mycolNew = testDatabase.getCollection("mongoCol1");
       System.out.println("Collection created successfully");
       insert(mycolNew);
    }
    
    
    /*
    @Before
    public void setUpMariaDb() throws Exception {
       
    }
*/
    @After
    public void tearDown() throws Exception {
    }
    
    
    @Test
    public void testAppSaying(){
        //App app = new App();
        String message = "hello";
        assertEquals(message, "hello");
    }
    
    
    @Test
    public void testAppSaying2(){
        //App app = new App();
        String message2 = "hello";
        assertEquals(message2, "hello");
    }
    
    
   @Test
   public void testSonarSqlJDBC () throws ClassNotFoundException, SQLException{
        Connection conn = null;
        Statement stmt = null;
        
        String db="test";
        String collection ="col3";
        
   
        Class.forName("com.mysql.jdbc.Driver");
        System.out.println("Connecting to database...");
        conn = (Connection) DriverManager.getConnection(DB_URL,USER,PASS);
        System.out.println("Creating statement...");
        stmt = conn.createStatement();

            
        String sql;
        sql = "SELECT * from col3";
        
        String errorInfo="\n Database: "+db+"\n"+"Collection: "+collection+"\n"+"Query: "+sql+"\n";
        ResultSet rs = stmt.executeQuery(sql);
        System.out.println(rs.getClass().getName());
      
      
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("_id");
         int a2 = rs.getInt("a");
         String b2 = rs.getString("b");
         
         if (id==1){
             assertEquals(errorInfo,a2,1);
             assertEquals(errorInfo,b2, "red");
         }
         else if(id==2){
             
             assertEquals(errorInfo,a2,2);
             assertEquals(errorInfo,b2, "green");
             
         }
         else if (id==3){
             assertEquals(errorInfo,a2,3);
             assertEquals(errorInfo,b2, "blue1");
         }
       

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", a: " + a2);
         System.out.print(",b: " + b2);
        
      }
       
      //STEP 6: Clean-up environment
      rs.close();
      stmt.close();
   }
    
    public static void insert(MongoCollection<Document> collection){  
        List<Document> documents = new ArrayList<Document>();  
        for (int i = 1; i < 3; i++) {  
            //documents.add(new Document("_id", i).append("age", (20+i)).append("name", new Date()));  
            documents.add(new Document("_id", i).append("age", (20+i)).append("grade", Integer.toString(i) ));
        }  
        collection.insertMany(documents);  
    }
    
}
