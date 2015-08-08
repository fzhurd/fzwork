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
   static final String DB_URL = "jdbc:mysql://localhost:3306/naaforjoin2";
    
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
    public void setUp() throws Exception {
    }

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
        assertEquals(message2, "Hello");
    }
    
}
