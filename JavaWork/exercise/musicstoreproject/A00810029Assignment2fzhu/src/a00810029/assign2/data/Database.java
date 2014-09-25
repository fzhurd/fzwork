package a00810029.assign2.data;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.*;

import javax.swing.JOptionPane;



public class Database {
		
	private ArrayList <Item> itemDatabase= new ArrayList<Item>();
	private ArrayList <Customer> customerDatabase =  new ArrayList <Customer>();
	//@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
    private Customer thisCustomer= new Customer();
    
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    String driver="com.microsoft.sqlserver.jdbc.SQLServerDriver";
	String url="jdbc:sqlserver://Beangrinder.bcit.ca";	
	String user="javastudent";	
	String password="compjava";
	String databaseTableName="A00810029_Inventory";
	private Connection _connection;
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	//default constructor
	public Database() 
	{
		
	}
       	
	   public Database(ArrayList<Item> itemDatabase,
			           ArrayList<Customer> customerDatabase) 
	   {
		super();
		this.itemDatabase=itemDatabase;
		this.customerDatabase = customerDatabase;
	}
 
    // get and set start here

	public ArrayList<Item> getItemDatabase() {
		return itemDatabase;
	}


	public void setItemDatabase(ArrayList<Item> itemDatabase) {
		this.itemDatabase=itemDatabase;
	}


	public ArrayList<Customer> getCustomerDatabase() {
		return customerDatabase;
	}


	public void setCustomerDatabase(ArrayList<Customer> customerDatabase) {
		this.customerDatabase = customerDatabase;
	}
	
	
	//***********************above finish the set and get
	
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	public void init()
	{		
		// next step to establish physical connection to a database
		
		try {
			Class.forName(driver);
			
			 _connection=DriverManager.getConnection(
					url, user, password);  
			
		} catch (ClassNotFoundException e) {
			
			e.printStackTrace();
			
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
		
		
	}
	
	// This method is to check whether the table exists or not
		public  boolean tableExists(String tableName) throws SQLException
			{
			   
			    init();
				DatabaseMetaData databaseMetaData=_connection.getMetaData();
				ResultSet resultSet=databaseMetaData.getTables(_connection.getCatalog(), "%", "%", null);
				String name=null;
				while(resultSet.next()){
					name=resultSet.getString("TABLE_NAME");
					if(name.equalsIgnoreCase(tableName)){
						return true;
					}
				}
				
				return false;
			}
		  
	
	// method to shut down the table, close the connection	
		public void shutdown()
		{
			
			try {
				_connection.close();
			} catch (SQLException e) {
				
				e.printStackTrace();
			}
		}
	
		

        // This method is to drop down the table		  		
			public void dropTable()
			{
						   
				   Statement stmt = null;
				   init();
				    try {
						stmt = _connection.createStatement();
					} catch (SQLException e) {
						
						e.printStackTrace();
					}
				      
				      String sql1 = "DROP TABLE A00810029_Inventory";
				      String sql2= "DROP TABLE A00810029_Customers";
				 
				      try {
						stmt.executeUpdate(sql1);
						stmt.executeUpdate(sql2);
					} catch (SQLException e) {
						
						e.printStackTrace();
					}
				      System.out.println("Table  deleted in given database...");
			
				      try{
				         if(stmt!=null)
				            _connection.close();
				      }catch(SQLException se){
				      }// do nothing
				      try{
				         if(_connection!=null)
				        	 _connection.close();
				      }catch(SQLException se){
				         se.printStackTrace();
				   }//end try
			}
	

}
