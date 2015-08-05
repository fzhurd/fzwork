
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
//      String query = "SELECT Data FROM Images LIMIT 1";
//       PreparedStatement     pst = conn.prepareStatement(query);
            
      String sql;
      sql = "SELECT * from col3";
      ResultSet rs = stmt.executeQuery(sql);
      
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("_id");
         int a = rs.getInt("a");
         String b = rs.getString("b");
       

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