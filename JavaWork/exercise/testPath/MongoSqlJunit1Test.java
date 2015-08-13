/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//package sonarsqljunit1;

import static org.junit.Assert.*;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import org.junit.Test;


/**
 *
 * @author frank
 */
public class MongoSqlJunit1Test {
    
    // Database credentials
   private  final static String mongoDatabase="test";
   private  final static String mongoUser = "test";
   private  final static String mongoPass = "test";
   private  final static String mongoCollection="t99";
   
   // JDBC
   private  final static  String JDBC_DRIVER_MYSQL = "com.mysql.jdbc.Driver";
   private  final static  String JDBC_DRIVER_MARIADB = "org.mariadb.jdbc.Driver";

   private  final static  String DB_URL = "jdbc:mysql://127.0.0.1:3307/test";
   private  final static  String DB_URL_NATIVE_MARIADB = "jdbc:mysql://127.0.0.1:3306/test";
   
   //SONARSQL
   private  final static String Dbname="test";
   private  final static String sqlDbUser = "test";
   private  final static String sqlDbPass = "test";
   private  final static String testCollection="t99";
   private  final static String query="SELECT * FROM t99";
   private  Statement stmt = null;
   
   public Statement getStatement(){
       return this.stmt;
   }
   public void setStatement(Statement stmt){
       this.stmt = stmt;
   }
    
    public MongoSqlJunit1Test() {
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


    
    @Test
    public void testNativeMariaDb() throws ClassNotFoundException, SQLException{
       ResultSet rs4 = runQuery(DB_URL_NATIVE_MARIADB, JDBC_DRIVER_MYSQL, Dbname, testCollection, query );
       checkResult(Dbname, testCollection, query, rs4, stmt);
   }
   
   
   
public ResultSet runQuery(String dbUrl, String driver, String Dbname, String testCollection, String query ) throws ClassNotFoundException, SQLException{
        
        Connection conn;
        //Statement stmt = null;
        
        String db=Dbname;
        String collection =testCollection;
   
        //Class.forName("com.mysql.jdbc.Driver");
        Class.forName(driver);
        System.out.println("Connecting to database...");
        conn = (Connection) DriverManager.getConnection(dbUrl, sqlDbUser,sqlDbPass);
        System.out.println("Creating statement...");
        stmt = conn.createStatement();

        String sql;
        sql = query;
        stmt.executeQuery("USE test");
        
        ResultSet rs = stmt.executeQuery(sql);
        System.out.println(rs.getClass().getName());
        
        return rs;
      
        
    }
   
    public void checkResult(String dbname, String testCollection, String query, ResultSet rs, Statement stmt) throws SQLException
    {
        String errorInfo="\n Database: "+dbname+"\n"+"Collection: "+testCollection+"\n"+"Query: "+query+"\n";
        
         List<Integer> resultIds = new ArrayList<>();
         List<Integer> resultCol1 = new ArrayList<>();
         List<String> resultCol2 = new ArrayList<>();
         
         int[] newResultIds = new int[3];
         int i=0;
         
         while(rs.next()){
             
         //Retrieve by column name
         int id  = rs.getInt("_id");
         int a2 = rs.getInt("age");
         String b2 = rs.getString("color");
  
         resultIds.add(id);
         resultCol1.add(a2);
         resultCol2.add(b2);
         
         //Display values
         System.out.print("ID: " + id);
         System.out.print(", age: " + a2);
         System.out.println(", color: " + b2);
        
      }
      
        Integer[] resultsIdsList = resultIds.toArray(new Integer[resultIds.size()]);
        Integer[] resultCol1List = resultCol1.toArray(new Integer[resultCol1.size()]);
        String[]  resultCol2List = resultCol2.toArray(new String[resultCol2.size()]);
        
        assertArrayEquals(errorInfo, new Integer[]{1,2,3}, resultsIdsList);
        assertArrayEquals(errorInfo, new Integer[]{10,20,30}, resultCol1List);
        assertArrayEquals(errorInfo, new String[]{"red","green","blue"}, resultCol2List);
       
      //STEP 6: Clean-up environment
      rs.close();
      stmt.close();
    }
  
    
}
