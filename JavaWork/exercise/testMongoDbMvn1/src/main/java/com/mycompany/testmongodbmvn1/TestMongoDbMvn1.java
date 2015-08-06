/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.testmongodbmvn1;

import java.util.ArrayList;  
import java.util.Date;  
import java.util.List;  
  
 
  
import com.mongodb.MongoClient;  
import com.mongodb.client.MongoCollection;  
import com.mongodb.client.MongoDatabase;  
import com.mongodb.client.MongoIterable;  
 

/**
 *
 * @author frank
 */
public class TestMongoDbMvn1 {
    
    public static void main(String[] args) {
            MongoClient mongo = null;  
            mongo = new MongoClient("localhost", 27017);  
            MongoDatabase testDatabase = mongo.getDatabase("test");
            listDatabases(mongo);
            listCollections(testDatabase);
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
    
}
