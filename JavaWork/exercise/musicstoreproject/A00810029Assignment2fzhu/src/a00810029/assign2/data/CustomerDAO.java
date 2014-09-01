package a00810029.assign2.data;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
 import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
 import java.util.Collections;
import java.util.List;

import org.apache.log4j.Logger;

public class CustomerDAO {
	
	//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	static Logger logger = Logger.getLogger(CustomerDAO.class);
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    String driver="com.microsoft.sqlserver.jdbc.SQLServerDriver";
	String url="jdbc:sqlserver://Beangrinder.bcit.ca";	
	String user="javastudent";	
	String password="compjava";
	String databaseTableName="A00810029_Customers";
	private Connection _connection;
//	private List<Item> _inventoryItems;
	ArrayList<Customer> customerInventory= new ArrayList<Customer>();
//^^^^^^^^^^^^^^^^^^^^	File theCustomerFile=new File("C://IT/Comp2613/Assignment1/customer.txt");
	Database customerDatabase=new Database();
	private ArrayList <Customer>customerListFromFile= new ArrayList<Customer>();
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//	private static final CustomerDAO _theInstance = new CustomerDAO();

	private final Customer _customer;

	public CustomerDAO() {
		_customer = new Customer();
	}

	public Customer getCustomer() {
		return _customer;
	}

	
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    public void init() throws FileNotFoundException, SQLException {
		
		if(customerDatabase.tableExists("A00810029_Customers")) // if the A00810029_Inventory table exist
		{

		//^^^^	System.out.println("A00810029_Customers has exist, just work on it");
			logger.info("A00810029_Customers has exist, just work on it");
	
	    // This is a switch			
		//	customerDatabase.dropTable();
		//	System.out.println("hello, the A00810029_Customers table has been dropped");
			
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
			customerDatabase.init(); // This syntax call the Customer Database init() method to connect the SQL database			
			Connection _connection=DriverManager.getConnection(
					url, user, password); 
			//@@@@@@@@@@@@@@@@@@@@
			@SuppressWarnings("unused")
			Statement statement=_connection.createStatement();
			readCustomerTable();
							
	//		System.out.println(String.format("DEBUG items = %s", Arrays.toString(customerInventory.toArray(new Item[0]))));
	//		Collections.sort(customerInventory, new ItemDAO.CompareByDescription());
							
		}
				
		
		else if (!customerDatabase.tableExists("A00810029_Customers"))
		{ 
			
//^^^^^^^	System.out.println("A00810029_Customers table does not exist, please create them firstly");
			logger.info("A00810029_Customers table does not exist, please create them firstly");
			// if the A00810029_Customers does not exist
			
			try {
				 customerListFromFile=getCustomerListFromFile(); // step 1: get initial data from file
				 createCustomerTable(customerListFromFile);   // step 2: create the initial table
				
			} catch (IOException e) {
				
				e.printStackTrace();
			}
			
		
	//		System.out.println(String.format("DEBUG items = %s", Arrays.toString(customerInventory.toArray(new Item[0]))));

	//		Collections.sort(_inventoryItems, new ItemDAO.CompareByDescription());
						
			
	} 	//else
		
	
	} // method
	

    
    
	  // This method is to get the customer data from customer file

	  public ArrayList<Customer> getCustomerListFromFile( ) throws IOException
		{
		   ArrayList<Customer> customerListFromFile= new ArrayList<Customer>();
	//^^^^^^^^^^	File theCustomerFile=new File("C://IT/Comp2613/Assignment1/customer.txt");
		   File theCustomerFile=new File("customer.txt");
    //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	//		File theCustomerFile=new File("C://IT/Comp2613/Assignment1/customer2.txt");
			
			BufferedReader inCustomer=new BufferedReader(new FileReader(theCustomerFile));
			String line=null;        
		    List<String> customerList = new ArrayList<String>();
		    while((line=inCustomer.readLine())!=null)  
		        {  
		    	 
		            customerList.add(line);
		        }
		        for(String temp: customerList){
		        	String[] product=temp.split("\\|");       
		            for (int i=0; i<product.length; i++)
		            {
		            System.out.println(product[i]);
		            }
		        }
		          
		        inCustomer.close();
		        //****************************************To this step, the Item has been read out from the inventory file
		        
		        //***************************************************for debug of the splitting
		        for (int i=0; i<customerList.size(); i++)
				      
		        {
		 			String[] itemData = customerList.get(i).split("\\|");
		 			
		 			System.out.println(String.format("DEBUG itemData = %s", Arrays.toString(itemData)));
		 			System.out.println(itemData.length);
		 		}	
		        
		        //*******************************start to split the readable line into the Item arrayList
		        
		        for (int i=0; i<customerList.size(); i++)
		        {
		 		    	
		 			String[] customerData =customerList.get(i).split("\\|");
		 			
		 			ArrayList<String> eachCustomer= new ArrayList<String>();
		 			       	  	
		        	// assign the value of each item
		        	for (int m=0; m<customerData.length; m++)
		        	{
		        		eachCustomer.add(customerData[m]);
		        	}
		        	Customer newCustomer = new Customer();
		        	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		        	newCustomer.setCustomerNumber(Integer.parseInt(eachCustomer.get(0)));
		        	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		        	newCustomer.setFirstName(eachCustomer.get(1));
		        	newCustomer.setLastName(eachCustomer.get(2));
		 			
		        	newCustomer.setCreditCardType(eachCustomer.get(3));
		        	newCustomer.setCredtCardNumber(eachCustomer.get(4));
		        	newCustomer.setStreet(eachCustomer.get(5));
		        	newCustomer.setCity(eachCustomer.get(6));
		        	newCustomer.setPostalCode(eachCustomer.get(7));
		        				 			
		        	customerListFromFile.add(newCustomer);	        	
		        	
		        	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		 		
		 		}
		 	
		          for (int length=0; length<customerInventory.size(); length++)
		          {
		 		    System.out.println(String.format("DEBUG items = %s", customerInventory.get(length).toString()));
		          }
		          
		          return customerListFromFile;
		        
		}
	  
	
		  
	   public void createCustomerTable(ArrayList<Customer> theCustomerList)
		  {
			   
	    	customerDatabase.init();								
										
	    	try {
				_connection = DriverManager.getConnection(
						url, user, password);
				
				Statement statement = _connection.createStatement();
				String query = "INSERT INTO A00810029_Customers ("
						    + "customerNumber,"
						    + "firstName,"
						    + "lastName,"
						    + "creditCardType,"
						    + "creditCardNumber,"
						    + "street,"
						    + "city,"
						    + "postalCode ) VALUES ("
						    + "?, ?, ?, ?, ?, ?, ?, ?)";
			//######	String createTable="create table A00810029_Customers (customerNumber int primary key not null, firstName varchar(50), lastName varchar(50), creditCardType varchar(50), creditCardNumber varchar(50), street varchar(100), city varchar(100), postalCode varchar(50))";
				String createTable="create table A00810029_Customers (customerNumber int primary key not null, firstName varchar(50), lastName varchar(50), creditCardType varchar(50), creditCardNumber varchar(50), street varchar(100), city varchar(100), postalCode varchar(50))";
			//^^^^^^	System.out.println("A00810029_Customers table has been created");
				logger.info("A00810029_Customers table has been created");
			    statement.executeUpdate(createTable);
			    Statement preparedStatement = _connection.prepareStatement(query);
		    
			    // This for loop is to release the data from ArrayList<Item> to the database inventory table
				  for (int i=0; i<theCustomerList.size(); i++)
				  {
					  int theCustomerNumber=theCustomerList.get(i).getCustomerNumber();
					  String theFirstName=theCustomerList.get(i).getFirstName();
					  String theLastName=theCustomerList.get(i).getLastName();
					  String theCreditCardType=theCustomerList.get(i).getCreditCardType();
					  String theCreditCardNumber=theCustomerList.get(i).getCredtCardNumber();
					  String theStreet=theCustomerList.get(i).getStreet();
					  String theCity=theCustomerList.get(i).getCity();
					  String thePostalCode=theCustomerList.get(i).getPostalCode();
				//^^^^	  System.out.println(theCustomerNumber);
					 
				//^^^^	  System.out.println(theFirstName);
				//^^^^	  System.out.println(theLastName);
					  logger.info(theCustomerNumber);
					  logger.info(theFirstName);
					  logger.info(theLastName);
					  ((PreparedStatement) preparedStatement).setInt(1, theCustomerNumber);
					   
					  ((PreparedStatement) preparedStatement).setString(2, theFirstName);
					  ((PreparedStatement) preparedStatement).setString(3, theLastName);
					  ((PreparedStatement) preparedStatement).setString(4, theCreditCardType);
					
					  ((PreparedStatement) preparedStatement).setString(5, theCreditCardNumber);
					  ((PreparedStatement) preparedStatement).setString(6, theStreet);
					  ((PreparedStatement) preparedStatement).setString(7, theCity);
					  ((PreparedStatement) preparedStatement).setString(8,  thePostalCode);
					 				
					  ((PreparedStatement) preparedStatement).executeUpdate();
				//	  System.out.println("YYYYYYYYYYYYYYYYYYY"+theCustomerList.size());
				//^^^^System.out.println("The new Customer data from file has been inserted into the table");
					  logger.info("The new Customer data from file has been inserted into the table");
					  
				  }
			    
			} catch (SQLException e1) {
				
				e1.printStackTrace();
		//^^^^		logger.error("database not connected",e1); 
			}
											  
		      
		  }
	   
	   // This method is to retrive data from Inventory table
		  public ArrayList<Customer> retriveDataFromCustomerTable()
		  {
		   ArrayList<Customer> thatListRetriveFromCustomerTable = new ArrayList<Customer>();
			  
		   int retriveCustomerNumber;
           String retriveFirstName;
           String retriveLastName;
           String retriveCreditCardType;
           String retriveCreditCardNumber;
           String retriveStreet;
           String retriveCity;
 
           String retrivePostalCode;
			 
			  customerDatabase.init();	
			  try {
				_connection = DriverManager.getConnection(
							url, user, password);
				Statement  statement = _connection.createStatement();
				ResultSet resultSet=statement.executeQuery("SELECT * FROM A00810029_Customers");
				while(resultSet.next())
				{
					// read the first 9 column(FIELDS), if want to more, just copy paste change the index
					
			//^^^^		System.out.print(resultSet.getString(1)+", ");
					logger.info(resultSet.getString(1)+", ");
					retriveCustomerNumber=Integer.parseInt(resultSet.getString(1));
					
			//^^^^		System.out.print(resultSet.getString(2)+", ");
					logger.info(resultSet.getString(2)+", ");
					retriveFirstName=resultSet.getString(2);
					
			//^^^^		System.out.print(resultSet.getString(3)+", ");
					logger.info(resultSet.getString(3)+", ");
					retriveLastName=resultSet.getString(3);
					
			//^^^^		System.out.print(resultSet.getString(4)+", ");
					logger.info(resultSet.getString(4)+", ");
					retriveCreditCardType=resultSet.getString(4);
					
			//^^^^		System.out.print(resultSet.getString(5)+", ");
					logger.info(resultSet.getString(5)+", ");
					retriveCreditCardNumber=resultSet.getString(5);
					
			//^^^^		System.out.print(resultSet.getString(6)+", ");
					logger.info(resultSet.getString(6)+", ");
					retriveStreet=resultSet.getString(6);
					
			//^^^^		System.out.print(resultSet.getString(7)+", ");
					logger.info(resultSet.getString(7)+", ");
					retriveCity=resultSet.getString(7);
					
					
			//^^^^		System.out.print(resultSet.getString(8)+"\n");
					logger.info(resultSet.getString(8)+"\n");
					retrivePostalCode=resultSet.getString(8);
					
					Customer retriveIndividualCustomer = new Customer(retriveCustomerNumber, 
							                                          retriveFirstName,
							                                          retriveLastName,
							                                          retriveCreditCardType,
							                                          retriveCreditCardNumber,
							                                          retriveStreet,
							                                          retriveCity,                                                      
							                                          retrivePostalCode
							                                          );
					 
					thatListRetriveFromCustomerTable.add(retriveIndividualCustomer); 
				}
				
			} catch (SQLException e) {
				
				e.printStackTrace();
			    logger.error("database not connected",e); 
			}
				
			  return thatListRetriveFromCustomerTable;
			  
		  }
	
	 // This method is to read the customer table
	
	 public void readCustomerTable()
	  {
		  customerDatabase.init();	
		  try {
			_connection = DriverManager.getConnection(
						url, user, password);
			Statement  statement = _connection.createStatement();
			ResultSet resultSet=statement.executeQuery("SELECT * FROM A00810029_Customers");
			
			while(resultSet.next())
			{
				logger.info(resultSet.getString(1)+", ");
				logger.info(resultSet.getString(2)+", ");
				logger.info(resultSet.getString(3)+", ");
				logger.info(resultSet.getString(4)+", ");
				logger.info(resultSet.getString(5)+", ");
				logger.info(resultSet.getString(6)+", ");
				logger.info(resultSet.getString(7)+", ");				
				logger.info(resultSet.getString(8)+"\n");
			}
			
			//##########################
			 ResultSet rs=statement.executeQuery("SELECT Max(customerNumber) FROM A00810029_Customers");
			 while(rs.next())
			 {
				 rs.getString(1);
				 logger.info("the max is"+rs.getString(1));
			 }
			// System.out.println("the max is"+resultSet2.getString(1));
			//###########################			
			
		} catch (SQLException e) {
			
			e.printStackTrace();
			 logger.error("SQL not connected",e); 
		}
			
		  
	  }
	 
	 //This method is to update the row of the table
	  public int updateCustomerTable(  int updateCustomerNumber, 
			                           String updateCustomerFirstName,
			                           String updateCustomerLastName,
			                           String updateCustomerCreditCardType,
			                           
			                           String updateCustomerCreditCardNumber,
			                           String updateCustomerStreet,
			                           String updateCustomerCity,
			                           String updatePostalCode
			                           )
	  {
		  int isCustomerTableUpdated=0;
		  customerDatabase.init();
		  try {
				_connection = DriverManager.getConnection(
							url, user, password);
				Statement  statement = _connection.createStatement();
			//String createTable="create table A00810029_Customers (customerNumber int primary key not null, firstName varchar(50), lastName varchar(50), creditCardType varchar(50), creditCardNumber varchar(50), street varchar(100), city varchar(100), postalCode varchar(50))";	
				PreparedStatement ps = _connection.prepareStatement(
					      "UPDATE A00810029_Customers SET firstName = ?, lastName = ?, creditCardType = ?, creditCardNumber = ?, street = ?, city = ?, postalCode = ? WHERE customerNumber = ? ");
				ps.setString(1,updateCustomerFirstName);
			    ps.setString(2,updateCustomerLastName);
			    ps.setString(3,updateCustomerCreditCardType);
			    ps.setString(4,updateCustomerCreditCardNumber);
			    ps.setString(5,updateCustomerStreet);
			    ps.setString(6,updateCustomerCity);
			    ps.setString(7,updatePostalCode);
			    ps.setInt(8,updateCustomerNumber);
		
			    ps.executeUpdate();
				
			//	System.out.println("the update data has been input in the database item table");
			    logger.info("the update data has been input in the database item table");
				
			    isCustomerTableUpdated=1;
				
				readCustomerTable();
				
			} catch (SQLException e) {
				e.printStackTrace();
				logger.error("SQL not connected",e);
			}
		     
		     return isCustomerTableUpdated;
	  }
	  
	 	
	
	//This method is to save a new Item in the inventory
		
	  public int saveCustomerTable( int newCustomerNumber, 
			                         String newFirstName,
			                         String newLastName,
			                         String newCreditCardType,			                         
			                         String newCreditCardNumber,
			                         String newStreet,
			                         String newCity,
			                         String newPostalCode
			                        )
	  
	  {
		  int isSavedCustomerTable=0;
		  customerDatabase.init();
		  try {
				_connection = DriverManager.getConnection(
							url, user, password);
				//@@@@@@@@@@@@@@@@@@@@@@
				@SuppressWarnings("unused")
				Statement  statement = _connection.createStatement();
				//@@@@@@@@@@@@@@@@@@@@@@@@
				@SuppressWarnings("unused")
				String createTable="create table A00810029_Customers (customerNumber int primary key not null, firstName varchar(50), lastName varchar(50), creditCardType varchar(50), creditCardNumber varchar(50), street varchar(100), city varchar(100), postalCode varchar(50))";
				String query = "INSERT INTO A00810029_Customers ("
					    + " customerNumber,"
					    + " firstName,"
					    + " lastName,"
					    + " creditCardType,"
					    + " creditCardNumber,"
					    + " street,"
					    + " city,"
					    + " postalCode ) VALUES ("
					    + "?, ?, ?, ?, ?, ?, ?, ?)";
				
			     Statement preparedStatement = _connection.prepareStatement(query);
			     ((PreparedStatement) preparedStatement).setInt(1, newCustomerNumber);
				
				   
				  ((PreparedStatement) preparedStatement).setString(2, newFirstName);
				  ((PreparedStatement) preparedStatement).setString(3, newLastName);
				  ((PreparedStatement) preparedStatement).setString(4, newCreditCardType);
				
				  ((PreparedStatement) preparedStatement).setString(5, newCreditCardNumber);
				  ((PreparedStatement) preparedStatement).setString(6, newStreet);
				  ((PreparedStatement) preparedStatement).setString(7, newCity);
				 
				  ((PreparedStatement) preparedStatement).setString(8, newPostalCode);
				
				  ((PreparedStatement) preparedStatement).executeUpdate();
			    
				System.out.println("the new data has been input in the database item table");
				
				isSavedCustomerTable=1;
				readCustomerTable();
				
			} catch (SQLException e) {
				e.printStackTrace();
				logger.error("SQL not connected",e); 
			}
		      return isSavedCustomerTable;
	  }
	  
	  // This method is to decide whether sku exists or not
	  public boolean checkCustomerNumber(int inputCustomerNumber)
	  {
		  boolean checkedCustomerNumberExist=false;
		  customerDatabase.init();	
		  try {
			_connection = DriverManager.getConnection(
						url, user, password);
			Statement  statement = _connection.createStatement();
			ResultSet resultSet=statement.executeQuery("SELECT customerNumber FROM A00810029_Customers");
			
			while(resultSet.next())
			{
				logger.info(resultSet.getString(1)+", ");
				int theCheckedCustomerNumberFromTable=Integer.parseInt(resultSet.getString(1));
				
				if (inputCustomerNumber==theCheckedCustomerNumberFromTable)
				{
					checkedCustomerNumberExist=true;
				}
			}
					 
			
		} catch (SQLException e) {
			
			e.printStackTrace();
			logger.error("SQL not connected",e); 
		}
		  
		      return checkedCustomerNumberExist;
			
	  }
	  
	  // This method is to find the maxium customer Number in the customer table
	  public int maxCustomerNumberInTable()
	  {
		  int maxCustomerNumber=0;
		  customerDatabase.init();	
		  try {
			_connection = DriverManager.getConnection(
						url, user, password);
			Statement  statement = _connection.createStatement();
			
			 ResultSet rs=statement.executeQuery("SELECT Max(customerNumber) FROM A00810029_Customers");
			 while(rs.next())
			 {
				 rs.getString(1);
				 maxCustomerNumber=Integer.parseInt(rs.getString(1));
				 logger.info("the max is "+rs.getString(1));
			 }
							
			
		} catch (SQLException e) {
			
			e.printStackTrace();
			logger.error("SQL not connected",e); 
		}
		  
		  return maxCustomerNumber;
			
	  }
	  
	  
	//This method is to search whether the customer is in the database or not
	 
	    public Customer find(int theCustomerNumber, String firstName, String lastName, String creditCardNumber, String street, String city,
				String postalCode) 
	    {
	    	Customer foundCustomer= new Customer();
	    	ArrayList<Customer> findCustomerListFromTable = new ArrayList<Customer>();
	    	customerDatabase.init();
			  try {
					_connection = DriverManager.getConnection(
								url, user, password);
					Statement  statement = _connection.createStatement();
					ResultSet resultSet=statement.executeQuery("SELECT * FROM A00810029_Customers");
					
					while(resultSet.next())
					{
						Customer theCustomerFromTable = new Customer(Integer.parseInt(resultSet.getString(1)),
								                                     resultSet.getString(2),
								                                     resultSet.getString(3),
								                                     resultSet.getString(4),
								                                     resultSet.getString(5),
								                                     resultSet.getString(6),
								                                     resultSet.getString(7),
						                                             resultSet.getString(8)   
						                                             );
						
						findCustomerListFromTable.add(theCustomerFromTable);
						
					}	
					
					
	    	
			for (Customer customer: findCustomerListFromTable) {
				
				if (customer.getCustomerNumber()==theCustomerNumber) {
					return customer;
				}
				if (firstName != null && firstName.trim().length() > 0 && customer.getFirstName().contains(firstName)) {
					return customer;
				}
				if (lastName != null && lastName.trim().length() > 0 && customer.getLastName().contains(lastName)) {
					return customer;
				}
				if (creditCardNumber != null && creditCardNumber.trim().length() > 0
						&& customer.getCredtCardNumber().contains(creditCardNumber)) {
					return customer;
				}
				if (street != null && street.trim().length() > 0 && customer.getStreet().contains(street)) {
					return customer;
				}
				if (city != null && city.trim().length() > 0 && customer.getCity().contains(city)) {
					return customer;
				}
				if (postalCode != null && postalCode.trim().length() > 0 && customer.getPostalCode().contains(postalCode)) {
					return customer;
				}
				
				foundCustomer=customer;
			}
			
			  } catch (SQLException e) {
					
					e.printStackTrace();
					logger.error("SQL not connected",e); 
				}
			  
			  
			  return foundCustomer;
		}
	  
	  
	    // This method is to delete the row in the table
		  public void deleteCustomerTableRow(int deleteCustomerNumber)
		  {
			  customerDatabase.init();
			  try {
					_connection = DriverManager.getConnection(
								url, user, password);
					//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
					@SuppressWarnings("unused")
					Statement  statement = _connection.createStatement();
					
					// This is to retrieve data from the table
					String sql = "DELETE FROM A00810029_Customers where customerNumber = ?";
					PreparedStatement prest=_connection.prepareStatement(sql);
					prest.setInt(1,deleteCustomerNumber);
					int del = prest.executeUpdate();
					logger.info("Number of deleted records: " + del);
					logger.info("one row has been deleted in the database item table");	               
					
					readCustomerTable();
					
				} catch (SQLException e) {
					
					e.printStackTrace();
					logger.error("SQL not connected",e); 
				}
			  
		  }
	 

}
