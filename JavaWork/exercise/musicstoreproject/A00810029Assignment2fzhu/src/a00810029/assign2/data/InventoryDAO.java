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
 import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
 import java.util.Scanner;
 import java.util.ArrayList;

import org.apache.log4j.Logger;


public class InventoryDAO {
	
	static Logger logger = Logger.getLogger(InventoryDAO.class);
	
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    String driver="com.microsoft.sqlserver.jdbc.SQLServerDriver";
	String url="jdbc:sqlserver://Beangrinder.bcit.ca";	
	String user="javastudent";	
	String password="compjava";
//	String databaseTableName="A00810029_Inventory";
	private Connection _connection;
	private List<Item> _inventoryItems= new ArrayList<Item>();
	Database itemDatabase=new Database();
	private ArrayList <Item>itemListFromFile= new ArrayList<Item>();
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	
	public void init() throws FileNotFoundException, SQLException {
		
		if(itemDatabase.tableExists("A00810029_Inventory")) // if the A00810029_Inventory table exist
		{
			_inventoryItems = new ArrayList<Item>();
	   //^^^		System.out.println("A00810029_Inventory has exist, just work on it");
			logger.info("A00810029_Inventory has exist, just work on it");
			
	   //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			
	   // This is a switch			
	  //   itemDatabase.dropTable();
		//	System.out.println("hello, the A00810029_Inventory table has been dropped");
			
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
			itemDatabase.init(); // This syntax call the Database init() method to connect the SQL database
			
			Connection _connection=DriverManager.getConnection(
					url, user, password); 
			
			//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			@SuppressWarnings("unused")
			Statement statement=_connection.createStatement();
			readInventoryTable();
							
			System.out.println(String.format("DEBUG items = %s", Arrays.toString(_inventoryItems.toArray(new Item[0]))));

			Collections.sort(_inventoryItems, new ItemDAO.CompareByDescription());
							
		}
		
		
		
		else if (!itemDatabase.tableExists("A00810029_Inventory"))
		{ 
			
	//^^^^	System.out.println("A00810029_Inventory table does not exist, please create them firstly");
			logger.info("A00810029_Inventory table does not exist, please create them firstly");
			// if the A00810029_Inventory does not exist
			
			try {
				 itemListFromFile=getItemInventoryFromFile(); // step 1: get initial data from file
				 createInventoryTable(itemListFromFile);   // create the initial table
				
			} catch (IOException e) {
				
				e.printStackTrace();
				logger.error("database not connected",e); //^^^^^^^^^^^^^^^^^^
			}
			
		
			System.out.println(String.format("DEBUG items = %s", Arrays.toString(_inventoryItems.toArray(new Item[0]))));

			Collections.sort(_inventoryItems, new ItemDAO.CompareByDescription());
						
			
	} 	//else
		
	
	} // method
	
	
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		  		  
		// This method is to get the Item List from File and put into the Array!!!!!!!!!!!!!!!!!
			public ArrayList<Item> getItemInventoryFromFile( ) throws IOException
			{
			//	 File theInventoryFile= new File("C://IT/Comp2613/Assignment1/inventory.txt");
				
				 ArrayList<Item> itemInventory= new ArrayList<Item>();
				
//^^^^^^^^^^^^	 BufferedReader in=new BufferedReader(new FileReader("C://IT/Comp2613/Assignment1/inventory.txt"));
				 BufferedReader in=new BufferedReader(new FileReader("inventory.txt"));
				 String line=null;        
			     List<String> list = new ArrayList<String>();
			     while((line=in.readLine())!=null)  
			        {  
			    	 
			            list.add(line);
			        }
			        for(String temp: list){
			        	String[] product=temp.split("\\|");       
			            for (int i=0; i<product.length; i++)
			            {
			            System.out.println(product[i]);
			            }
			        }
			          
			        in.close();
			        //****************************************To this step, the Item has been read out from the inventory file
			        
			        //***************************************************for debug of the splitting
			        for (int i=0; i<list.size(); i++)
					      
			        {
			 			String[] itemData = list.get(i).split("\\|");
			 			
			 			System.out.println(String.format("DEBUG itemData = %s", Arrays.toString(itemData)));
			 			System.out.println(itemData.length);
			 		}	
			        
			        //*******************************start to split the readable line into the Item arrayList
			        
			        for (int i=0; i<list.size(); i++)
			        {
			 		    	
			 			String[] itemData = list.get(i).split("\\|");
			 			
			 			ArrayList<String> eachItem= new ArrayList<String>();
			 			       	  	
			        	// assign the value of each item
			        	for (int m=0; m<itemData.length; m++)
			        	{
			        		eachItem.add(itemData[m]);
			        	}
			        	Item item = new Item();
			        	
			     // note: This index means the index from extraction from the file   	
			     item.setStockCode(eachItem.get(3));
			     item.setMake(eachItem.get(0));
			     item.setModelNumber(eachItem.get(2));
			 	 item.setDescription(eachItem.get(1));
			 	 item.setPurchasePrice(eachItem.get(4));			 			 		
			 	 item.setSellingPrice(eachItem.get(5));			 			
			 	 item.setQuantityInStock(eachItem.get(6));
			 	 item.setQuantitySold(eachItem.get(7));			 			
			 	 item.setNumberRented(eachItem.get(8));
			 		
			 	 itemInventory.add(item);
			 		
			 		}
			 	
			          for (int length=0; length<itemInventory.size(); length++)
			          {
			 		    System.out.println(String.format("DEBUG itemInventory = %s", itemInventory.get(length).toString()));
			          }
			          
			          return itemInventory;
			        
			}
			
			
			
   // This method is to create the table
		  
		  public void createInventoryTable(ArrayList<Item> theItemList)
		  {
			   
			       itemDatabase.init();										
										
					try {
						_connection = DriverManager.getConnection(
								url, user, password);
						
						Statement statement = _connection.createStatement();
						String query = "INSERT INTO A00810029_Inventory ("
								    + " sku,"
								    + " make,"
								    + " modalNumber,"
								    + " description,"
								    + " purchasePrice,"
								    + " sellingPrice,"
								    + " quantityInStock,"
								    + " quantitySold,"
								    + " numberRented ) VALUES ("
								    + "?, ?, ?, ?, ?, ?, ?, ?, ?)";

						
					//	String createTable="create table A00810029_Inventory (sku varchar(50), make varchar(100), modalNumber varchar(50), description varchar(50), purchasePrice float(8,4), sellingPrice float(8,4), quantityInStock int, quantitySold int, numberRented int);";
					
						String createTable="create table A00810029_Inventory (sku varchar(50) primary key not null, make varchar(100), modalNumber varchar(50), description varchar(50), purchasePrice varchar(50), sellingPrice varchar(50), quantityInStock varchar(50), quantitySold varchar(50), numberRented varchar(50))";
						System.out.println("A00810029_Inventory table has been created");						
					    statement.executeUpdate(createTable);
					    				    
					    Statement preparedStatement = _connection.prepareStatement(query);
					    
					 // This for loop is to release the data from ArrayList<Item> to the database inventory table
						  for (int i=0; i<theItemList.size(); i++)
						  {
							  String theSKU=theItemList.get(i).getStockCode();
							  String theMake=theItemList.get(i).getMake();
							  String theModel=theItemList.get(i).getModelNumber();
							  String theDescription=theItemList.get(i).getDescription();
							  
				//			  float thePurchasePrice=theItemList.get(i).getPurchasePrice();
							  String thePurchasePrice=Float.toString(theItemList.get(i).getPurchasePrice());
				//			  float theSellingPrice=theItemList.get(i).getSellingPrice();
							  String theSellingPrice=Float.toString(theItemList.get(i).getSellingPrice());
							  
				//			  int theQuantityInStock=theItemList.get(i).getQuantityInStock();
							  String theQuantityInStock= Integer.toString(theItemList.get(i).getQuantityInStock());
							 
				//			  int theQuantitySold=theItemList.get(i).getQuantitySold();
							  String theQuantitySold=Integer.toString(theItemList.get(i).getQuantitySold());
							  
				//			  int theNumberRented=theItemList.get(i).getNumberRented();
							  String theNumberRented=Integer.toString(theItemList.get(i).getNumberRented());
							  
							  System.out.println(thePurchasePrice);
							  System.out.println(theSellingPrice); 
				
				
				//		      String insertData="INSERT INTO A00810029_Inventory" + "VALUES ("+theSKU+", "+theMake+", "+theModel+", "+theDescription+", "+thePurchasePrice+", "+theSellingPrice+", "+theQuantityInStock+", "+theQuantitySold+", "+theNumberRented+");";									
				//			  statement.executeUpdate(insertData);
				//			  String insertData1="INSERT INTO A00810029_Inventory " + "VALUES ("+theSKU+", 'Danelectro', "+theModel+", 'Bass','10', '395.000000', '100','20','50')";
				//			  String insertData2="INSERT INTO A00810029_Inventory " + "VALUES ('999999', 'Danelectro', 'D56BASS-AQUA', 'Bass','10', '395.000000', '100','20','50')";
							
						//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^	  
							 
							  ((PreparedStatement) preparedStatement).setString(1, theSKU);
		
					   
							  ((PreparedStatement) preparedStatement).setString(2, theMake);
							  ((PreparedStatement) preparedStatement).setString(3, theModel);
							  ((PreparedStatement) preparedStatement).setString(4, theDescription);
							
							  ((PreparedStatement) preparedStatement).setString(5, thePurchasePrice);
							  ((PreparedStatement) preparedStatement).setString(6, theSellingPrice);
							  ((PreparedStatement) preparedStatement).setString(7, theQuantityInStock);
							  ((PreparedStatement) preparedStatement).setString(8, theQuantitySold);
							  ((PreparedStatement) preparedStatement).setString(9, theNumberRented);
							
							  ((PreparedStatement) preparedStatement).executeUpdate();
				//			  ((PreparedStatement) preparedStatement).close();
						//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^	  
							  // insert the data into the tables
						//	  statement.executeUpdate(insertData);
						//	  statement.executeUpdate(insertData2);
							  System.out.println("The new Item data has been inserted into the table");
						  }						  						 
						  
						// This test the table of the items
						  readInventoryTable();
						
					} catch (SQLException e1) {
						
						e1.printStackTrace();
						logger.error("SQL not connected",e1); //^^^^^^^^^^^^^^^^^^^^
					}
												      				
			
		  }
		  
		  // This method is to retrive data from Inventory table
		  public ArrayList<Item> retriveDataFromInventoryTable()
		  {
			  ArrayList<Item> thatListRetriveFromInventoryTable = new ArrayList<Item>();
			  
			  String retriveSKU;
              String retriveMake;
              String retriveModel;
              String retriveDescription;
              float retrivePurchasePrice;
              float retriveSellingPrice;
              int retriveQuantityInStock;
              int retriveQuantitySold;
              int retriveNumberRented;
			 
			  itemDatabase.init();	
			  try {
				_connection = DriverManager.getConnection(
							url, user, password);
				Statement  statement = _connection.createStatement();
				ResultSet resultSet=statement.executeQuery("SELECT * FROM A00810029_Inventory");
				while(resultSet.next())
				{
					// read the first 9 column(FIELDS), if want to more, just copy paste change the index
					
		//^^^^^			System.out.print(resultSet.getString(1)+", ");
					logger.info(resultSet.getString(1)+", ");
					
					retriveSKU=resultSet.getString(1);
		//^^^^^			System.out.print(resultSet.getString(2)+", ");
					logger.info(resultSet.getString(2)+", ");
					
					retriveMake=resultSet.getString(2);
		//^^^^^			System.out.print(resultSet.getString(3)+", ");
					logger.info(resultSet.getString(1)+", ");
					retriveModel=resultSet.getString(3);
		//^^^^^^			System.out.print(resultSet.getString(4)+", ");
					logger.info(resultSet.getString(4)+", ");
					retriveDescription=resultSet.getString(4);
		
		//^^^^			System.out.print(resultSet.getString(5)+", ");
					logger.info(resultSet.getString(5)+", ");
					retrivePurchasePrice=Float.valueOf(resultSet.getString(5));
					
		//^^^^^			System.out.print(resultSet.getString(6)+", ");
					logger.info(resultSet.getString(6)+", ");
					
					retriveSellingPrice=Float.valueOf(resultSet.getString(6));
					
		//^^^^			System.out.print(resultSet.getString(7)+", ");
					logger.info(resultSet.getString(7)+", ");
					retriveQuantityInStock=Integer.parseInt(resultSet.getString(7));
					
		//^^^^			System.out.print(resultSet.getString(8)+", ");
					 logger.info(resultSet.getString(8)+", ");
					 retriveQuantitySold=Integer.parseInt(resultSet.getString(8));
					 
		//^^^^			System.out.print(resultSet.getString(9)+"\n");
					 logger.info(resultSet.getString(9)+", ");
					retriveNumberRented=Integer.parseInt(resultSet.getString(9));
					
					Item retriveIndividualItem = new Item( retriveSKU, 
                                                            retriveMake,
                                                            retriveModel,
                                                            retriveDescription,
                                                            retrivePurchasePrice,
                                                            retriveSellingPrice,
                                                            retriveQuantityInStock,
                                                            retriveQuantitySold,
                                                            retriveNumberRented
							                                );
					 
					 thatListRetriveFromInventoryTable.add(retriveIndividualItem); 
				}
				
			} catch (SQLException e) {
				
				e.printStackTrace();
				logger.error("SQL not connected",e);
			}
				
			  return thatListRetriveFromInventoryTable;
			  
		  }
		  
		 // This method is only to read from inventory table 
		  public void readInventoryTable()
		  {
			  itemDatabase.init();	
			  try {
				_connection = DriverManager.getConnection(
							url, user, password);
				Statement  statement = _connection.createStatement();
				ResultSet resultSet=statement.executeQuery("SELECT * FROM A00810029_Inventory");
				
				while(resultSet.next())
				{
					// read the first 3 column(FIELDS), if want to more, just copy paste change the index
					//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
					/*System.out.print(resultSet.getString(1)+", ");
					System.out.print(resultSet.getString(2)+", ");
					System.out.print(resultSet.getString(3)+", ");
					System.out.print(resultSet.getString(4)+", ");
					System.out.print(resultSet.getString(5)+", ");
					System.out.print(resultSet.getString(6)+", ");
					System.out.print(resultSet.getString(7)+", ");
					System.out.print(resultSet.getString(8)+", ");
					System.out.print(resultSet.getString(9)+"\n");*/
					
					logger.info(resultSet.getString(1)+", ");
					logger.info(resultSet.getString(2)+", ");
					logger.info(resultSet.getString(3)+", ");
					logger.info(resultSet.getString(4)+", ");
					logger.info(resultSet.getString(5)+", ");
					logger.info(resultSet.getString(6)+", ");
					logger.info(resultSet.getString(7)+", ");
					logger.info(resultSet.getString(8)+", ");
					logger.info(resultSet.getString(9)+"\n");
				}
														 				
			} catch (SQLException e) {
				
				e.printStackTrace();
				logger.error("SQL not connected",e);
			}
				
			  
		  }
		  
		  
		  //This method is to update the row of the table
		  public int updateInventoryTable( String updateSKU, 
				                           String updateMake,
				                           String updateModel,
				                           String updateDescription,
				                           /*float updatePurchasePrice,
				                           float updateSellingPrice,
				                           int updateQuantityInStock,
				                           int updateQuantitySold,
				                           int updateNumberRented*/
				                           String updatePurchasePrice,
				                           String updateSellingPrice,
				                           String updateQuantityInStock,
				                           String updateQuantitySold,
				                           String updateNumberRented)
		  {
			  int isUpdated=0;
			  itemDatabase.init();
			  try {
					_connection = DriverManager.getConnection(
								url, user, password);
					//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
					@SuppressWarnings("unused")
					Statement  statement = _connection.createStatement();
					
					PreparedStatement ps = _connection.prepareStatement(
						      "UPDATE A00810029_Inventory SET make= ?, modalNumber = ?, description = ?, purchasePrice = ?, sellingPrice = ?, quantityInStock = ?, quantitySold = ?, numberRented = ? WHERE sku = ? ");
					ps.setString(1,updateMake);
				    ps.setString(2,updateModel);
				    ps.setString(3,updateDescription);
				    ps.setString(4,updatePurchasePrice);
				    ps.setString(5,updateSellingPrice);
				    ps.setString(6,updateQuantityInStock);
				    ps.setString(7,updateQuantitySold);
				    ps.setString(8,updateNumberRented);
				    ps.setString(9,updateSKU);
				    ps.executeUpdate();
					
				//	System.out.println("the update data has been input in the database item table");
				    logger.info("the update data has been input in the database item table");
					
					isUpdated=1;
					
					readInventoryTable();
					
				} catch (SQLException e) {
					e.printStackTrace();
					logger.error("SQL not connected",e);
				}
			     
			     return isUpdated;
		  }
		  
		  //This method is to save a new Item in the inventory
		
		  public int saveInventoryTable( String newSKU, 
				                         String newMake,
				                         String newModel,
				                         String newDescription,				                         
				                         String newPurchasePrice,
				                         String newSellingPrice,
				                         String newQuantityInStock,
				                         String newQuantitySold,
				                         String newNumberRented)
		  {
			  int isSaved=0;
			  itemDatabase.init();
			  try {
					_connection = DriverManager.getConnection(
								url, user, password);
					//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
					@SuppressWarnings("unused")
					Statement  statement = _connection.createStatement();
				
					String query = "INSERT INTO A00810029_Inventory ("
						    + " sku,"
						    + " make,"
						    + " modalNumber,"
						    + " description,"
						    + " purchasePrice,"
						    + " sellingPrice,"
						    + " quantityInStock,"
						    + " quantitySold,"
						    + " numberRented ) VALUES ("
						    + "?, ?, ?, ?, ?, ?, ?, ?, ?)";
					
				     Statement preparedStatement = _connection.prepareStatement(query);
				     ((PreparedStatement) preparedStatement).setString(1, newSKU);
					
					   
					  ((PreparedStatement) preparedStatement).setString(2, newMake);
					  ((PreparedStatement) preparedStatement).setString(3, newModel);
					  ((PreparedStatement) preparedStatement).setString(4, newDescription);
					
					  ((PreparedStatement) preparedStatement).setString(5, newPurchasePrice);
					  ((PreparedStatement) preparedStatement).setString(6, newSellingPrice);
					  ((PreparedStatement) preparedStatement).setString(7, newQuantityInStock);
					  ((PreparedStatement) preparedStatement).setString(8, newQuantitySold);
					  ((PreparedStatement) preparedStatement).setString(9, newNumberRented);
					
					  ((PreparedStatement) preparedStatement).executeUpdate();
				    
				//	System.out.println("the new data has been input in the database item table");
					logger.info("the new data has been input in the database item table");
					
					isSaved=1;
					readInventoryTable();
					
				} catch (SQLException e) {
					e.printStackTrace();
					logger.error("SQL not connected",e);
				}
			      return isSaved;
		  }
		  

		  // This method is to decide whether sku exists or not
		  public boolean checkSKU(String inputSKU)
		  {
			  boolean checkedSKUExist=false;
			  itemDatabase.init();	
			  try {
				_connection = DriverManager.getConnection(
							url, user, password);
				Statement  statement = _connection.createStatement();
				ResultSet resultSet=statement.executeQuery("SELECT sku FROM A00810029_Inventory");
				
				while(resultSet.next())
				{
					// read the first 3 column(FIELDS), if want to more, just copy paste change the index
					System.out.print(resultSet.getString(1)+", ");
					String theCheckedSKUFromTable=resultSet.getString(1);
					
					if (inputSKU.equals(theCheckedSKUFromTable))
					{
						checkedSKUExist=true;
					}
				}
				
							
				 
				
			} catch (SQLException e) {
				
				e.printStackTrace();
				logger.error("SQL not connected",e);
			}
			  
			      return checkedSKUExist;
				
		  }
		  
		  // This method is to delete the row in the table
		  public void deleteRow(String deleteSKU)
		  {
			  itemDatabase.init();
			  try {
					_connection = DriverManager.getConnection(
								url, user, password);
					//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
					@SuppressWarnings("unused")
					Statement  statement = _connection.createStatement();
									      
					String sql = "DELETE FROM A00810029_Inventory where sku = ?";
					PreparedStatement prest=_connection.prepareStatement(sql);
					prest.setString(1,deleteSKU);
					int del = prest.executeUpdate();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			//		System.out.println("Number of deleted records: " + del);
			//		System.out.println("one row has been deleted in the database item table");
					logger.info("Number of deleted records: " + del);
					logger.info("one row has been deleted in the database item table");
					
					readInventoryTable();
					
				} catch (SQLException e) {
					
					e.printStackTrace();
					logger.error("SQL not connected",e);
				}
			  
		  }
		 
}
