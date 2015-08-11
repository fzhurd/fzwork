/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mongomariadb2;

import java.sql.ResultSet;
import java.sql.SQLException;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;


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


import com.mysql.jdbc.Driver;
import java.sql.*;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 *
 * @author frank
 */
public class MongoMariaDb2Test {
    
    // Database credentials
   private  final static String mongoDatabase="test";
   private  final static String mongoUser = "test";
   private  final static String mongoPass = "test";
   private  final static String mongoCollection="mongoCol1";
   
   private  final static  String JDBC_DRIVER_MYSQL = "com.mysql.jdbc.Driver";
   private  final static  String JDBC_DRIVER_MARIADB = "org.mariadb.jdbc.Driver";
   private  final static  String DB_URL = "jdbc:mysql://localhost:3306/test";
   
   private  final static String Dbname="test";
   private  final static String sqlDbUser = "test";
   private  final static String sqlDbPass = "test";
   private  final static String testCollection="col3";
   private  final static String query="SELECT * FROM col3";
   private  Statement stmt = null;
   
   public Statement getStatement(){
       return this.stmt;
   }
   public void setStatement(Statement stmt){
       this.stmt = stmt;
   }
    
    public MongoMariaDb2Test() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of main method, of class MongoMariaDb2.
     */
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
   public void testMysqlDriver2() throws ClassNotFoundException, SQLException{
       ResultSet rs3 = runQuery(JDBC_DRIVER_MYSQL, Dbname, testCollection, query );
       checkResult(Dbname, testCollection, query, rs3, stmt);
   }
   
   
   public ResultSet runQuery(String driver, String Dbname, String testCollection, String query ) throws ClassNotFoundException, SQLException{
        
        Connection conn = null;
        //Statement stmt = null;
        
        String db=Dbname;
        String collection =testCollection;
        
   
        //Class.forName("com.mysql.jdbc.Driver");
        Class.forName(driver);
        System.out.println("Connecting to database...");
        conn = (Connection) DriverManager.getConnection(DB_URL,sqlDbUser,sqlDbPass);
        System.out.println("Creating statement...");
        stmt = conn.createStatement();

            
        String sql;
        sql = query;
        
        ResultSet rs = stmt.executeQuery(sql);
        System.out.println(rs.getClass().getName());
        
        return rs;
      
        
    }
    
    public void checkResult(String dbname, String testCollection, String query, ResultSet rs, Statement stmt) throws SQLException
    {
        String errorInfo="\n Database: "+dbname+"\n"+"Collection: "+testCollection+"\n"+"Query: "+query+"\n";

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
             assertEquals(errorInfo,b2, "blue");
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
    
}
