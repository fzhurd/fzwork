package a00810029.assign2.ui;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

import java.util.List;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import net.miginfocom.swing.MigLayout;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JComboBox;

import org.apache.log4j.Logger;



import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import a00810029.assign2.data.*;


//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@SuppressWarnings("serial")
public class InventoryDialog extends JDialog {
	
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	static Logger logger = Logger.getLogger(InventoryDialog.class);
    String driver="com.microsoft.sqlserver.jdbc.SQLServerDriver";
	String url="jdbc:sqlserver://Beangrinder.bcit.ca";	
	String user="javastudent";	
	String password="compjava";
	String databaseTableName="A00810029_Inventory";
	private Connection _connection;
	private InventoryDAO inventoryDAO = new InventoryDAO ();
	Database itemDatabaseForInventoryDialog=new Database();
	private final JComboBox comboBoxJSKU = new JComboBox();
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	private final JPanel contentPanel = new JPanel();
	private JTextField descriptionJTextField;
	private JTextField quantityInStockJTextField;
	private JTextField quantitySoldJTextField;
	private JTextField textField;
	private JTextField sellingPriceJTextField;
	private JTextField numberRentedJTextField;
	
	
	// File theInventoryFileInJMS=new File("C://IT/Comp2613/Assignment1/inventory.txt");
	//+++  File theInventoryFileInJMS=new File("inventory.txt");
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private ArrayList<Item> inventoryItems= new ArrayList<Item>();
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private Database databaseInv= new Database();
	private JTextField textFieldJModel;
	private JTextField textFieldJMake;
	
	public InventoryDialog(final JMSJFrame thisJMSJFrame) throws IOException {
		setTitle("Inventory Informaiton");
	//	setBounds(100, 100, 450, 300);
		setSize(787, 365);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(new MigLayout("", "[][grow]", "[][][][][][][][][]"));
		{
			JLabel SKUJLabel = new JLabel("SKU");
			contentPanel.add(SKUJLabel, "cell 0 0,alignx trailing");
		}
		{
			//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		//	final JComboBox comboBoxJSKU = new JComboBox();
			
			comboBoxJSKU.setEditable(true);
			contentPanel.add(comboBoxJSKU, "cell 1 0,growx");
			itemDatabaseForInventoryDialog.init();
			try {
				_connection = DriverManager.getConnection(
						url, user, password);
				
				Statement statement=_connection.createStatement();
				ResultSet resultSet=statement.executeQuery("SELECT sku FROM A00810029_Inventory");
				while(resultSet.next())
				{
					String thatSKU=resultSet.getString(1);				
					comboBoxJSKU.addItem(thatSKU);
					
				}
			} catch (SQLException e1) {
				
				e1.printStackTrace();
			}
				
			comboBoxJSKU.addItemListener(new ItemListener() {
				public void itemStateChanged(ItemEvent arg0) {
					
					try {
						
						_connection = DriverManager.getConnection(
								url, user, password);
					
						Statement statement=_connection.createStatement();
						String selectedSKU= (String)comboBoxJSKU.getSelectedItem();
						//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
						String sqlSelection="SELECT * FROM A00810029_Inventory WHERE sku="+selectedSKU+"";
						ResultSet resultSet=statement.executeQuery(sqlSelection);
						System.out.println("###############################################################");
						while(resultSet.next())
						{
						//	String thatSKU=resultSet.getString(1);				
							textFieldJMake.setText(resultSet.getString(2));
							System.out.println(resultSet.getString(2));
							textFieldJModel.setText(resultSet.getString(3));
							descriptionJTextField.setText(resultSet.getString(4));
							textField.setText(resultSet.getString(5));
							sellingPriceJTextField.setText(resultSet.getString(6));
							quantityInStockJTextField.setText(resultSet.getString(7));
							quantitySoldJTextField.setText(resultSet.getString(8));
							numberRentedJTextField.setText(resultSet.getString(9));
						}
					} catch (SQLException e1) {
						
						e1.printStackTrace();
					}
					
				}
			});
			 
		}
		
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		{
			JLabel makeJLabel = new JLabel("Make");
			contentPanel.add(makeJLabel, "cell 0 1,alignx trailing");
		}
		{
			textFieldJMake = new JTextField();
			contentPanel.add(textFieldJMake, "cell 1 1,growx");
			textFieldJMake.setColumns(10);
		}
		{
			JLabel modelJlabel = new JLabel("Model");
			contentPanel.add(modelJlabel, "cell 0 2,alignx trailing");
		}
		{
			textFieldJModel = new JTextField();
			contentPanel.add(textFieldJModel, "cell 1 2,growx");
			textFieldJModel.setColumns(10);
		}
		{
			JLabel descriptionJLabel = new JLabel("Description");
			contentPanel.add(descriptionJLabel, "cell 0 3,alignx trailing");
		}
		{
			descriptionJTextField = new JTextField();
			contentPanel.add(descriptionJTextField, "cell 1 3,growx");
			descriptionJTextField.setColumns(10);
		}
		{
			JLabel quantityInStockJLabel = new JLabel("Quantity  in Stock");
			contentPanel.add(quantityInStockJLabel, "cell 0 6,alignx trailing");
		}
		{
			quantityInStockJTextField = new JTextField();
			contentPanel.add(quantityInStockJTextField, "cell 1 6,growx");
			quantityInStockJTextField.setColumns(10);
		}
		{
			JLabel quantitySoldJLabel = new JLabel("Quantity Sold");
			contentPanel.add(quantitySoldJLabel, "cell 0 7,alignx trailing");
		}
		{
			quantitySoldJTextField = new JTextField();
			contentPanel.add(quantitySoldJTextField, "cell 1 7,growx");
			quantitySoldJTextField.setColumns(10);
		}
		{
			JLabel purchasePriceJLabel = new JLabel("Purchase Price");
			contentPanel.add(purchasePriceJLabel, "cell 0 4,alignx trailing");
		}
		{
			textField = new JTextField();
			contentPanel.add(textField, "cell 1 4,growx");
			textField.setColumns(10);
		}
		{
			JLabel sellingPriceJLabel = new JLabel("Selling Price");
			contentPanel.add(sellingPriceJLabel, "cell 0 5,alignx trailing");
		}
		{
			sellingPriceJTextField = new JTextField();
			contentPanel.add(sellingPriceJTextField, "cell 1 5,growx");
			sellingPriceJTextField.setColumns(10);
		}
		{
			JLabel numberRentedJLabel = new JLabel("Number Rented");
			contentPanel.add(numberRentedJLabel, "cell 0 8,alignx trailing");
		}
		{
			numberRentedJTextField = new JTextField();
			contentPanel.add(numberRentedJTextField, "cell 1 8,growx");
			numberRentedJTextField.setColumns(10);
		}
		{
		//	JComboBox _itemsComboBox = new JComboBox();
			{
			ArrayList<Item> inventoryItems= new ArrayList<Item>();
		//>>>>>	inventoryItems= thisJMSJFrame.getItemInventoryFromFile(theInventoryFileInJMS);
		
			
			
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//^^^^^^^^			inventoryItems=databaseInv.getItemInventoryFromFile(theInventoryFileInJMS);
			try {
				inventoryDAO.init();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
			
			    ItemDAO.CompareByStockCode itemSort= new ItemDAO.CompareByStockCode();
				Collections.sort(inventoryItems,itemSort);	
				this.setInventoyItems(inventoryItems);
			}
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton saveButton = new JButton("Save");
				saveButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
										
						//#######################################################
						if (    !inventoryDAO.checkSKU((String)comboBoxJSKU.getSelectedItem())    )
						{
						String newSKU=(String)comboBoxJSKU.getSelectedItem();
						String newMake=textFieldJMake.getText();
						String newModel=textFieldJModel.getText();
						String newDescription=descriptionJTextField.getText();
												
						String newPurchasePrice=textField.getText();
						String newSellingPrice=sellingPriceJTextField.getText(); 
						String newQuantityInStockJTextField=quantityInStockJTextField.getText();
						String newquantitySoldJTextField=quantitySoldJTextField.getText();
						String newnumberRentedJTextField=numberRentedJTextField.getText();
						
											
						inventoryDAO.saveInventoryTable(newSKU,
								                           newMake,
								                           newModel,
								                           newDescription,
								                           newPurchasePrice,
								                           newSellingPrice,
								                           newQuantityInStockJTextField,
								                           newquantitySoldJTextField,
								                           newnumberRentedJTextField);																								
						JOptionPane.showMessageDialog(null,"The new inventory information has been saved");
						//@@@@@@@@@@@@@@@@@@@@
						logger.info("The new inventory information has been saved");
						}
						else
						{
							JOptionPane.showMessageDialog(null,"The Items has exist, you could only update them, SAVE is for new item");
							logger.info("The Items has exist, you could only update them, SAVE is for new item");
						}
					}
				});
				
					
				
			//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
				{
					JButton updateJButton = new JButton("Update");
					updateJButton.addActionListener(new ActionListener() {
						public void actionPerformed(ActionEvent e) {
							
							if (    inventoryDAO.checkSKU((String)comboBoxJSKU.getSelectedItem())    )
							{
							
							String newSKU=(String)comboBoxJSKU.getSelectedItem();
							String newMake=textFieldJMake.getText();
							String newModel=textFieldJModel.getText();
							String newDescription=descriptionJTextField.getText();
							
							String newPurchasePrice=textField.getText();
							String newSellingPrice=sellingPriceJTextField.getText(); 
							String newQuantityInStockJTextField=quantityInStockJTextField.getText();
							String newquantitySoldJTextField=quantitySoldJTextField.getText();
							String newnumberRentedJTextField=numberRentedJTextField.getText();
							
							inventoryDAO.updateInventoryTable( newSKU,
									                           newMake,
									                           newModel,
									                           newDescription,
									                           newPurchasePrice,
									                           newSellingPrice,
									                           newQuantityInStockJTextField,
									                           newquantitySoldJTextField,
									                           newnumberRentedJTextField);
							JOptionPane.showMessageDialog(null,"The Inventory information for this Item has been updated");
							//@@@@@@@@@@@@@@@@@@@@@@@@@
							logger.info("The Inventory information for this Item has been updated");
							}
							else
							{
								JOptionPane.showMessageDialog(null,"The item does not exist, please make new one and SAVE it");
								logger.info("The item does not exist, please make new one and SAVE it");
							}
						}
											
					});
					buttonPane.add(updateJButton);
				}
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				saveButton.setActionCommand("save");
				
				buttonPane.add(saveButton);
				getRootPane().setDefaultButton(saveButton);
			}
			{
				JButton cancelButton = new JButton("Close");
				cancelButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
						
						int response = JOptionPane.showConfirmDialog(null,"Do you want to Save the changes?","Option panel",JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.WARNING_MESSAGE); 
								{
								  switch(response) {
								  case JOptionPane.YES_OPTION:    
								  {
									  
									  if (    !inventoryDAO.checkSKU((String)comboBoxJSKU.getSelectedItem())    )
										  
									  {
										  
									    String newSKU=(String)comboBoxJSKU.getSelectedItem();
									    
									    
										String newMake=textFieldJMake.getText();
										String newModel=textFieldJModel.getText();
										String newDescription=descriptionJTextField.getText();
										
										String newPurchasePrice=textField.getText();
										String newSellingPrice=sellingPriceJTextField.getText(); 
										String newQuantityInStockJTextField=quantityInStockJTextField.getText();
										String newquantitySoldJTextField=quantitySoldJTextField.getText();
										String newnumberRentedJTextField=numberRentedJTextField.getText();
										
										inventoryDAO.saveInventoryTable(   newSKU,
												                           newMake,
												                           newModel,
												                           newDescription,
												                           newPurchasePrice,
												                           newSellingPrice,
												                           newQuantityInStockJTextField,
												                           newquantitySoldJTextField,
												                           newnumberRentedJTextField
												                           );
										JOptionPane.showMessageDialog(null,"The New Inventory information has been saved");
										//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
										logger.info("The New Inventory information has been saved");
										 System.exit(0);
									  }
									  
									  else if( inventoryDAO.checkSKU((String)comboBoxJSKU.getSelectedItem()) )
									  {
										    String newSKU=(String)comboBoxJSKU.getSelectedItem();								    										    
											String newMake=textFieldJMake.getText();
											String newModel=textFieldJModel.getText();
											String newDescription=descriptionJTextField.getText();
											String newPurchasePrice=textField.getText();
											String newSellingPrice=sellingPriceJTextField.getText(); 
											String newQuantityInStockJTextField=quantityInStockJTextField.getText();
											String newquantitySoldJTextField=quantitySoldJTextField.getText();
											String newnumberRentedJTextField=numberRentedJTextField.getText();
										  
										  inventoryDAO.updateInventoryTable(newSKU,
						                                                    newMake,
						                                                    newModel,
						                                                    newDescription,
						                                                    newPurchasePrice,
						                                                    newSellingPrice,
						                                                    newQuantityInStockJTextField,
						                                                    newquantitySoldJTextField,
						                                                    newnumberRentedJTextField
						                                                    );
										  JOptionPane.showMessageDialog(null,"The Item was found in the database, the new information has been saved");
										  logger.info("The Item was found in the database, the new information has been saved");
									  }
										
									}
								  
								  case JOptionPane.NO_OPTION:       
									  {
									//	  JOptionPane.showMessageDialog(null,"No information has been saved");
										  System.exit(0);
									  }
								  case JOptionPane.CANCEL_OPTION:   break;
								  case JOptionPane.CLOSED_OPTION:  break;  // Don't quit!
								}	
								 												
						}
						
					}
				});
			
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			
			}
		}		
		
	               setVisible(true);
	}
	
	   public void setInventoyItems(ArrayList<Item> items) {
		
		for (int i=0; i<items.size(); i++)
		{
			
		/*  _itemsComboBox.addItem(items.get(i));*/
			System.out.println(items.size());
			
		}
	}
	  
	   
	       /* public Item foundItemExist(String inputDescription, String inputStockCode) throws IOException
	        {
	        	
	        	 Item checkedResult=null;
	        	 ArrayList<Item> currentItemList= new ArrayList<Item>();
	        	 File theInventoryFile=new File("C://IT/Comp2613/Assignment1/inventory.txt");
	        	//+++	 File theInventoryFile=new File("inventory.txt");
	        	 BufferedReader in=new BufferedReader(new FileReader(theInventoryFile));
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
			 			item.setMake(eachItem.get(0));
			 			item.setDescription(eachItem.get(1));
			 			
			 			item.setModelNumber(eachItem.get(2));
			 			item.setStockCode(eachItem.get(3));
			 			item.setSellingPrice(eachItem.get(4));
			 			item.setPurchasePrice(eachItem.get(5));
			 			item.setQuantityInStock(eachItem.get(6));
			 			item.setQuantitySold(eachItem.get(7));
			 			
			 			item.setNumberRented(eachItem.get(8));
			 					 		
			 			currentItemList.add(item);
			 		
			 		}
			        
			        
			        for (Item theItem: currentItemList)
			        {		        	
			          
			        	 boolean decide=false;
			   //     if (  ((descriptionJTextField.getText()).equals(theItem.getDescription()))&& ((stockCodeJLabel.getText()).equals(theItem.getStockCode()) ))
			          if ( (inputDescription.equals(theItem.getDescription()))&& (inputStockCode.equals(theItem.getStockCode()) ) )
			        		{
			        	        System.out.println("this Item exists, you will update it");
			        	        checkedResult=theItem;
				                
			        		}
			        			 	            			               		            
			        }
	        	             		     
							
			        return checkedResult;
			                 
	        }
	        */
	         
	      /*  public void updateItems(ArrayList<Item> currentItems, Item needUpdatedItem, Item updatedItem) throws IOException
	        {
	        File specificFile=new File("C://IT/Comp2613/Assignment1/inventory.txt");
	      //+++      File specificFile=new File("inventory.txt");
	        //>>>>	currentItems=getItemInventoryFromFile(specificFile);
	        	currentItems=databaseInv.getItemInventoryFromFile(specificFile);
		    	 
	        	needUpdatedItem=foundItemExist(needUpdatedItem.getDescription(), needUpdatedItem.getStockCode());
	        	
	        	for (int j=0; j<currentItems.size(); j++)
	        	{
	        		if (( currentItems.get(j).getDescription() ).equals( needUpdatedItem.getDescription() ) && ( currentItems.get(j).getStockCode() ).equals( needUpdatedItem.getStockCode() )  )
	        		{
	        			currentItems.remove(j);
	        		}
	        	}
	        	
	        
	        	ArrayList<Item> updatedItems= currentItems;
	   
	        	//***************************************************add the new updated item firstly
	        	
	        	try{
	        	 FileWriter outWriter1 = new FileWriter(specificFile,false);
    			 BufferedWriter output1=new BufferedWriter(outWriter1);
    		//	 output1.newLine();
    		//	 System.getProperty("line.separator");
		    	    output1.write(updatedItem.getMake()+"|");
		    	    output1.flush();
		            output1.write(updatedItem.getDescription()+"|");
		            output1.flush();
		            
		            output1.write(updatedItem.getModelNumber()+"|");
		            output1.flush();     
		            output1.write(updatedItem.getStockCode()+"|");
		            output1.flush();
		            output1.write(Double.toString(updatedItem.getSellingPrice())+"|");	
		            output1.flush();
		            output1.write(Double.toString(updatedItem.getPurchasePrice())+"|");
		            output1.flush();
		            
		            output1.write(Integer.toString(updatedItem.getQuantityInStock())+"|");
		            output1.flush();
		          
					output1.write(Integer.toString(updatedItem.getQuantitySold())+"|");			
					output1.flush();
					   					
					output1.write(Integer.toString(updatedItem.getNumberRented()));	
					output1.flush();
	           			
		            output1.close();
    			 
	        	}
	        	
	        	  catch ( FileNotFoundException e ) 
	   		      {
	   		         JOptionPane.showMessageDialog( null, e.getMessage() );
	   		          e.printStackTrace();
	        	}
	        	
	        	// add the new items in the file, this new item list have excluded the updated one
	        	for(Item thatItem: updatedItems)
	        	{
	        		 try 
	   		      {
	        			 FileWriter outWriter = new FileWriter(specificFile,true);
	        			 BufferedWriter output=new BufferedWriter(outWriter);
	   		   
	   		    	    output.newLine();
	   		    	//   System.getProperty("line.separator");
	   		    	    output.write(thatItem.getMake()+"|");
	   		    	    output.flush();
	   		            output.write(thatItem.getDescription()+"|");
	   		            output.flush();
	   		            
	   		            output.write(thatItem.getModelNumber()+"|");
	   		            output.flush();     
	   		            output.write(thatItem.getStockCode()+"|");
	   		            output.flush();
	   		            output.write(Double.toString(thatItem.getSellingPrice())+"|");	
	   		            output.flush();
	   		            output.write(Double.toString(thatItem.getPurchasePrice())+"|");
	   		            output.flush();
	   		            
	   		            output.write(Integer.toString(thatItem.getQuantityInStock())+"|");
	   		            output.flush();
	   		          
	   					output.write(Integer.toString(thatItem.getQuantitySold())+"|");			
	   					output.flush();
	   					   					
	   					output.write(Integer.toString(thatItem.getNumberRented()));	
	   					output.flush();
	   	           			
	   		            output.close();
	   		        
	   		      } 
	   		      
	   		      catch ( FileNotFoundException e ) 
	   		      {
	   		         JOptionPane.showMessageDialog( null, e.getMessage() );
	   		          e.printStackTrace();
	        	}
	        	 
	        }
	        	
	        }*/
	 
}
