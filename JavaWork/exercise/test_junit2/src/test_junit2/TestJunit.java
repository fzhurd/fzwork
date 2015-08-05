
package test_junit2;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class TestJunit {
	
   String message = "Hello World";	
   MessageUtil messageUtil = new MessageUtil(message);
   
   // JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost:3306/test";

   //  Database credentials
   static final String USER = "root";
   static final String PASS = "root";

   @Test
   public void testPrintMessage() {
      assertEquals(message,messageUtil.printMessage());
   }
   
   @Test
   public void testSonarSqlJDBC () throws ClassNotFoundException, SQLException{
   Connection conn = null;
   Statement stmt = null;
   
   Class.forName("com.mysql.jdbc.Driver");
   System.out.println("Connecting to database...");
      conn = (Connection) DriverManager.getConnection(DB_URL,USER,PASS);
      System.out.println("Creating statement...");
      stmt = conn.createStatement();

            
      String sql;
      sql = "SELECT * from col3";
      ResultSet rs = stmt.executeQuery(sql);
      System.out.println(rs.getClass().getName());
      
      
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("_id");
         int a = rs.getInt("a");
         String b = rs.getString("b");
         
         if (id==1){
             assertEquals(a,1);
             assertEquals(b, "red");
         }
         else if(id==2){
             
             assertEquals(a,2);
             assertEquals(b, "");
             
         }
         else if (id==3){
             assertEquals(a,3);
             assertEquals(b, true);
         }
       

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", a: " + a);
         System.out.print(",b: " + b);
        
      }
       
      //STEP 6: Clean-up environment
      rs.close();
      stmt.close();
   }
}