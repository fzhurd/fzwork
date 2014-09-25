package a00810029.assign2.ui;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
//import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import net.miginfocom.swing.MigLayout;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JComboBox;

import org.apache.log4j.Logger;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;

import java.util.List;

import a00810029.assign2.data.*;

import java.awt.Color;


public class CustomerDialog extends JDialog {
	
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	static Logger logger = Logger.getLogger(CustomerDAO.class);
	
	private final JPanel contentPanel = new JPanel();
	private JTextField firstNameJTextField;
	
	private JTextField lastNameJTextField;
	private JTextField creditCardNumberJTextField;
	private JTextField streetJTextField;
	private JTextField cityJTextField;
	private JTextField postalCodeJTextField;
	
	private JComboBox creditCardTypeJComboBox = new JComboBox();
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private Database theDatabase= new Database(null, null);
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private ArrayList<Customer> theCustomerList;
	ArrayList<Customer> customerInventory= new ArrayList<Customer>();
	// File theCustomerFile=new File("C://IT/Comp2613/Assignment1/customer.txt");
	
	//++++++++ File theCustomerFile=new File("customer.txt");
	 
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	    String driver="com.microsoft.sqlserver.jdbc.SQLServerDriver";
		String url="jdbc:sqlserver://Beangrinder.bcit.ca";	
		String user="javastudent";	
		String password="compjava";
		String databaseTableName="A00810029_Customers";
		//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@SuppressWarnings("unused")
		private Connection _connection;
		private CustomerDAO customerDAOInCustomerDialog= new CustomerDAO ();
		Database customerDatabaseForCustomerDialog=new Database();
		private JTextField textFieldJCustomerField;
	
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	public CustomerDialog(final JMSJFrame  thisJMSJFrame ) {
		
		try {
			customerDAOInCustomerDialog.init();
		} catch (FileNotFoundException e3) {
			logger.error("File not found",e3); 
			e3.printStackTrace();
		} catch (SQLException e3) {
			logger.error("sql not connected",e3); 
			e3.printStackTrace();
		}
		setTitle("Customer Information");
	//	setBounds(100, 100, 450, 300);
		setSize(600,300);
		setLocationRelativeTo(null);
		
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(new MigLayout("", "[82px][53px,grow][][4px][57px][4px][57px][4px][][145px]", "[][20px][20px][20px][20px][20px][20px][20px][23px]"));
		{
			JLabel customerNumberJLabel = new JLabel("Customer #");
			contentPanel.add(customerNumberJLabel, "cell 0 0,alignx trailing");
		}
		
			
		
		{
			textFieldJCustomerField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			int theFirstCustomerNumber=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getCustomerNumber();
			textFieldJCustomerField.setText(Integer.toString(theFirstCustomerNumber));
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			Color color=new Color(238,232,170);
			textFieldJCustomerField.setBackground(color);
			contentPanel.add(textFieldJCustomerField, "cell 1 0 9 1,growx");
			textFieldJCustomerField.setColumns(10);
		}
		{
			JLabel firstNameJLabel = new JLabel("First Name");
			contentPanel.add(firstNameJLabel, "cell 0 1,alignx right,aligny center");
		}
		{
			firstNameJTextField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			String theFirstCustomerFirstName=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getFirstName();
			firstNameJTextField.setText(theFirstCustomerFirstName);
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			contentPanel.add(firstNameJTextField, "cell 1 1 9 1,growx,aligny top");
			firstNameJTextField.setColumns(10);
		}
		{
			JLabel lastNameJLabel = new JLabel("Last Name");
			contentPanel.add(lastNameJLabel, "cell 0 2,alignx right,aligny center");
		}
		{
			lastNameJTextField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			String theFirstCustomerLastName=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getLastName();
			lastNameJTextField.setText(theFirstCustomerLastName);
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			contentPanel.add(lastNameJTextField, "cell 1 2 9 1,growx,aligny top");
			lastNameJTextField.setColumns(10);
		}
		{
			JLabel lblCreditCardType = new JLabel("Credit Card Type");
			contentPanel.add(lblCreditCardType, "cell 0 3,alignx left,aligny center");
		}
		{
			// JComboBox creditCardTypeJComboBox = new JComboBox();
		//	creditCardTypeJComboBox.setModel(new DefaultComboBoxModel(CreditCardType.values()));
			
		
			/*creditCardTypeJComboBox.addItem("Amex");
			creditCardTypeJComboBox.addItem("Mastercard");
			creditCardTypeJComboBox.addItem("Visa");*/
			
			creditCardTypeJComboBox.addItem(CreditCardType.AMEX.getDescription());
			creditCardTypeJComboBox.addItem(CreditCardType.MASTERCARD.getDescription());
			creditCardTypeJComboBox.addItem(CreditCardType.VISA.getDescription());
			contentPanel.add(creditCardTypeJComboBox, "cell 1 3 9 1,growx,aligny top");
		}
		{
			JLabel lblCreditCard = new JLabel("Credit Card #");
			contentPanel.add(lblCreditCard, "cell 0 4,alignx right,aligny center");
		}
		{
			creditCardNumberJTextField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			String theFirstCustomerCreditCardNumber=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getCredtCardNumber();
			creditCardNumberJTextField.setText(theFirstCustomerCreditCardNumber);
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			contentPanel.add(creditCardNumberJTextField, "cell 1 4 9 1,growx,aligny top");
			creditCardNumberJTextField.setColumns(10);
		}
		{
			JLabel streetJLabel = new JLabel("Street");
			contentPanel.add(streetJLabel, "cell 0 5,alignx right,aligny center");
		}
		{
			streetJTextField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			String theFirstCustomerStreet=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getStreet();
			streetJTextField.setText(theFirstCustomerStreet);
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			contentPanel.add(streetJTextField, "cell 1 5 9 1,growx,aligny top");
			streetJTextField.setColumns(10);
		}
		{
			JLabel cityJLabel = new JLabel("City");
			contentPanel.add(cityJLabel, "cell 0 6,alignx right,aligny center");
		}
		{
			cityJTextField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			String theFirstCustomerCity=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getCity();
			cityJTextField.setText(theFirstCustomerCity);
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			contentPanel.add(cityJTextField, "cell 1 6 9 1,growx,aligny top");
			cityJTextField.setColumns(10);
		}
		{
			JLabel lblPostalCode = new JLabel("Postal Code");
			contentPanel.add(lblPostalCode, "cell 0 7,alignx right,aligny center");
		}
		{
			postalCodeJTextField = new JTextField();
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			String theFirstCustomerPostalCode=customerDAOInCustomerDialog.retriveDataFromCustomerTable().get(0).getPostalCode();
			postalCodeJTextField.setText(theFirstCustomerPostalCode);
			//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			contentPanel.add(postalCodeJTextField, "cell 1 7 9 1,growx,aligny top");
			postalCodeJTextField.setColumns(10);
		}
		{
			JButton findJButton = new JButton("Find");
			findJButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					int searchedCustomerNumber=Integer.parseInt(textFieldJCustomerField.getText());
					String searchedFirstName=firstNameJTextField.getText();
					String searchedLastName=lastNameJTextField.getText();
					String searchedCreditCardNumber=creditCardNumberJTextField.getText();
					String searchedStreet=streetJTextField.getText();
					String searchedCity=cityJTextField.getText();
					String searchedPostalCode=postalCodeJTextField.getText();
					
					Customer foundCustomer=customerDAOInCustomerDialog.find(
							searchedCustomerNumber,
							searchedFirstName,
							searchedLastName,
							searchedCreditCardNumber,
							searchedStreet,
							searchedCity,
							searchedPostalCode
							);
					
					if (foundCustomer==null)
					{
					//@@@	System.out.println("No customer exist!!");
						logger.info("No customer exist!!");
						JOptionPane.showMessageDialog(null,"No searched Customer exist");
					}
					
					else 
					{
						 textFieldJCustomerField.setText( Integer.toString( foundCustomer.getCustomerNumber()) );
						 firstNameJTextField.setText( foundCustomer.getFirstName());
			        	 lastNameJTextField.setText(  foundCustomer.getLastName() );
			        	 creditCardNumberJTextField.setText( foundCustomer.getCredtCardNumber());
						 streetJTextField.setText( foundCustomer.getStreet());
						 cityJTextField.setText( foundCustomer.getCity());
						 postalCodeJTextField.setText( foundCustomer.getPostalCode());
					}
					
				}
			});
		
			contentPanel.add(findJButton, "cell 1 8,alignx left,aligny top");
		}
		{
			JButton clearJButton = new JButton("Clear");
			clearJButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					textFieldJCustomerField.setText(null);
					firstNameJTextField.setText(null);
					lastNameJTextField.setText(null);
					creditCardNumberJTextField.setText(null);
					streetJTextField.setText(null);
					cityJTextField.setText(null);
					postalCodeJTextField.setText(null);
					logger.info("All fields are cleard");
				}
			});
			{
				JButton newJButton = new JButton("New");
				newJButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						
						int newCustomerNumber=( customerDAOInCustomerDialog.maxCustomerNumberInTable() )+1;
						System.out.println(newCustomerNumber);
						
						textFieldJCustomerField.setText(Integer.toString(newCustomerNumber));
						firstNameJTextField.setText(null);
						lastNameJTextField.setText(null);
						creditCardNumberJTextField.setText(null);
						streetJTextField.setText(null);
						cityJTextField.setText(null);
						postalCodeJTextField.setText(null);		
						logger.info("New customer will be created");
						
					}
				});
				contentPanel.add(newJButton, "cell 2 8");
			}
			contentPanel.add(clearJButton, "cell 6 8,alignx left,aligny top");
		}
		{
			JButton saveJButton = new JButton("Save");
			saveJButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					
					int inputCustomerNumber=Integer.parseInt(textFieldJCustomerField.getText());
					String inputFirstName=firstNameJTextField.getText();
					String inputLastName=lastNameJTextField.getText();
					
					String inputCreditCardType=(String)creditCardTypeJComboBox.getSelectedItem();
					String inputCreditCardNumber=creditCardNumberJTextField.getText();
					String inputStreet=streetJTextField.getText();
					String inputCity=cityJTextField.getText();
					String inputPostalCode=postalCodeJTextField.getText();
					
					if (customerDAOInCustomerDialog.checkCustomerNumber(inputCustomerNumber))
					{
						JOptionPane.showMessageDialog(null,"hello, customer number has existed, the information has been updated for the exist customer");
						System.out.println("hello, customer number has existed, the information has been updated for the exist customer");
						
						customerDAOInCustomerDialog.updateCustomerTable(
								                                         inputCustomerNumber, 
                                                                         inputFirstName,
                                                                         inputLastName,
                                                                         inputCreditCardType,			                         
                                                                         inputCreditCardNumber,
                                                                         inputStreet,
                                                                         inputCity,
                                                                         inputPostalCode
                                                                         );
						logger.info("Customer information is updated");
				//#######		JOptionPane.showMessageDialog(null,"One customer has been saved in the A00810029_Customers table");
					}
					
					else if (!customerDAOInCustomerDialog.checkCustomerNumber(inputCustomerNumber))
					{
						customerDAOInCustomerDialog.saveCustomerTable( inputCustomerNumber, 
								                                       inputFirstName,
								                                       inputLastName,
								                                       inputCreditCardType,			                         
								                                       inputCreditCardNumber,
								                                       inputStreet,
								                                       inputCity,
								                                       inputPostalCode
		                                                              );
						JOptionPane.showMessageDialog(null,"One customer has been saved in the A00810029_Customers table");
						logger.info("One customer has been saved in the database");
		                        System.exit(0);      
		                        
					}
										
				}
			});
			
		
			contentPanel.add(saveJButton, "cell 4 8,alignx left,aligny top");
		}
		
		{
			JButton closeJButton = new JButton("Cancel");
			closeJButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				//	setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
				//	setDefaultCloseOperation(JDialog.DO_NOTHING_ON_CLOSE);
					dispose();
					//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				//	System.exit(0);
				}
			});
			{
				JButton okJButton = new JButton("OK");
				okJButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						
						int inputCustomerNumber=Integer.parseInt(textFieldJCustomerField.getText());
						String inputFirstName=firstNameJTextField.getText();
						String inputLastName=lastNameJTextField.getText();
						
						String inputCreditCardType=(String)creditCardTypeJComboBox.getSelectedItem();
						String inputCreditCardNumber=creditCardNumberJTextField.getText();
						String inputStreet=streetJTextField.getText();
						String inputCity=cityJTextField.getText();
						String inputPostalCode=postalCodeJTextField.getText();
						
						if (customerDAOInCustomerDialog.checkCustomerNumber(inputCustomerNumber))
						{
							JOptionPane.showMessageDialog(null,"hello, the customer information has been passed to the main window");
							String firstNameForJMS=firstNameJTextField.getText();
							String lastNameForJMS=lastNameJTextField.getText();
							 thisJMSJFrame.getCustomerField().setText(firstNameForJMS+"  "+lastNameForJMS);
							 logger.info("The customer in the main window has been updated");
					//		System.out.println("hello, customer number has existed,the information has been updated for the exist customer");
						}
						
						else if (!customerDAOInCustomerDialog.checkCustomerNumber(inputCustomerNumber))
						{
							customerDAOInCustomerDialog.saveCustomerTable( inputCustomerNumber, 
									                                       inputFirstName,
									                                       inputLastName,
									                                       inputCreditCardType,			                         
									                                       inputCreditCardNumber,
									                                       inputStreet,
									                                       inputCity,
									                                       inputPostalCode
			                                                              );
						//	 thisJMSJFrame.
							JOptionPane.showMessageDialog(null,"One customer has been saved in the A00810029_Customers table");
							logger.info("One customer has been saved");
			                        System.exit(0);      
			                        
						}																	
						
					}
				});
				contentPanel.add(okJButton, "cell 8 8");
			}
			contentPanel.add(closeJButton, "cell 9 8,alignx left,aligny top");
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
		}
		setVisible(true);
	}
	
	 enum CreditCardType 
	{
		
	   AMEX("AMEX"), MASTERCARD("MASTERCARD"), VISA("VISA");
	   
	   private String description;
	   
	     CreditCardType(String description)
		 {
			 this.description=description;
		 }
	     
	     public String getDescription() {
				return description;
			}
	
     }
	     //save customer
	
	    /*  public void saveCustomerInFile() throws IOException
	   {
		   
		      
		    try 
		      {	       
		    	  //++++   FileWriter outWriterCustomer = new FileWriter("C://IT/Comp2613/Assignment1/customer.txt", true);
		    	    FileWriter outWriterCustomer = new FileWriter("customer.txt", true);
		    	    BufferedWriter outputCustomer=new BufferedWriter(outWriterCustomer);
		    	    
		    	    outputCustomer.newLine();
		    //	    System.getProperty("line.separator");
		            outputCustomer.write(firstNameJTextField.getText()+"|");
		            outputCustomer.flush();
		            outputCustomer.write(lastNameJTextField.getText()+"|");
		            outputCustomer.flush();
		            outputCustomer.write((String)creditCardTypeJComboBox.getSelectedItem()+"|");
		            outputCustomer.flush();
		            outputCustomer.write(creditCardNumberJTextField.getText()+"|");
		            outputCustomer.flush();
		            outputCustomer.write(streetJTextField.getText()+"|");
		            outputCustomer.flush();
		            outputCustomer.write(cityJTextField.getText()+"|");
		            outputCustomer.flush();
		            outputCustomer.write(postalCodeJTextField.getText());
		            outputCustomer.flush();
		           	                     				
		            outputCustomer.close();
		            
		        
		      } 
		      
		      catch ( FileNotFoundException e ) 
		      {
		         JOptionPane.showMessageDialog( null, e.getMessage() );
		         e.printStackTrace();
		      }
		    
	   }
	      */
	      // Add the Customer in the Database
		   /* public void addCustomerInCustomerDatabase(ArrayList<Customer> customerPool, Customer inputCustomer) 
		    {
		    		    	
		    customerPool= theDatabase.getCustomerDatabase();
		    customerPool.add(inputCustomer);
		    
		    for (int i=0; i<customerPool.size(); i++)
		    {
		    System.out.println(customerPool.get(i).toString());
		    System.out.println("%%%%%%%%%%%%%%%%%%"+customerPool.size());
		    }

		   }  
		   
           //This method is to search whether the customer is in the database or not
		    public Customer searchCustomer( ArrayList<Customer> theCustomerPool, String searchedThing )
			   {
				
		    	Customer foundCustomer= new Customer(0, null, null, null, null, null,null, null);
		    	for (int i=0; i<theCustomerPool.size(); i++)
		    	{
		    		if ( theCustomerPool.get(i).getLastName().equals(searchedThing))
		    		{
		    			System.out.println("The Customer is in the database");
		    		}
		    		
		    		
		    		  foundCustomer= theCustomerPool.get(i);
		    	}
		    	
		    	      return foundCustomer;
		    	
			   }
	*/
		    
		    //*************************************************************************************find the customer from customer database
		   
			 /* public ArrayList<Customer> getCustomerListFromFile(File theCustomerFile) throws IOException
				{
			
					theCustomerFile=new File("C://IT/Comp2613/Assignment1/customer.txt");
					//++++++     theCustomerFile=new File("customer.txt");
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
				        
				        for (int i=1; i<customerList.size(); i++)
				        {
				 		    	
				 			String[] customerData =customerList.get(i).split("\\|");
				 			
				 			ArrayList<String> eachCustomer= new ArrayList<String>();
				 			       	  	
				        	// assign the value of each item
				        	for (int m=0; m<customerData.length; m++)
				        	{
				        		eachCustomer.add(customerData[m]);
				        	}
				        	Customer newCustomer = new Customer();
				        	newCustomer.setFirstName(eachCustomer.get(0));
				        	newCustomer.setLastName(eachCustomer.get(1));
				 			
				        	newCustomer.setCreditCardType(eachCustomer.get(2));
				        	newCustomer.setCredtCardNumber(eachCustomer.get(3));
				        	newCustomer.setStreet(eachCustomer.get(4));
				        	newCustomer.setCity(eachCustomer.get(5));
				        	newCustomer.setPostalCode(eachCustomer.get(6));
				        				 			
				 			customerInventory.add(newCustomer);
				 		
				 		}
				 	
				          for (int length=0; length<customerInventory.size(); length++)
				          {
				 		    System.out.println(String.format("DEBUG items = %s", customerInventory.get(length).toString()));
				          }
				          
				          return customerInventory;
				        
				}*/
}
