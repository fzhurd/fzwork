package a00810029.assign2.ui;


import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.HeadlessException;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import net.miginfocom.swing.MigLayout;

import javax.swing.JDialog;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.List;

import javax.swing.JMenuItem;

import org.apache.log4j.Logger;

import a00810029.assign2.data.*;
import a00810029.assign2.ui.*;


import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;

public class JMSJFrame extends JFrame {
	
	static Logger logger = Logger.getLogger(JMSJFrame.class);

	private JPanel purchaseItemsJLabel;
	JTextField customerField;
	private JTextField dollarField;
	private JTextField salesTextField;
	public JTextField rentalTotalJTextField;
	private JTextField totalJTextField;
	JMenuItem saveDataJMenuItem = new JMenuItem("Save Data");
	JComboBox itemComboBox = new JComboBox();
	JComboBox quantitySpinnerComboBox = new JComboBox();
	JTextArea purchasedItemsTextArea = new JTextArea();
	JTextArea rentalAgreementsJTextArea = new JTextArea();
	
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private ArrayList<Item> theItems= new ArrayList<Item>();
	File theInventoryFileInJMS=new File("C://IT/Comp2613/Assignment1/inventory.txt");
	//+++ File theInventoryFileInJMS=new File("inventory.txt");
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private Database databaseJMS= new Database();
	
	private ArrayList<Item> JMSInventoryItems = new ArrayList<Item>();
	
	private double doubSoldAllItemTotalFee;
	
	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    String driver="com.microsoft.sqlserver.jdbc.SQLServerDriver";
	String url="jdbc:sqlserver://Beangrinder.bcit.ca";	
	String user="javastudent";	
	String password="compjava";
	String databaseTableName="A00810029_Inventory";
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private Connection _connection;
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private List<Item> _inventoryItems= new ArrayList<Item>();
	Database itemDatabaseInJMS=new Database();
	private InventoryDAO inventoryDAOINJMS= new InventoryDAO();
	
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private ArrayList<Item> itemListFromFileInJMS= new ArrayList<Item>();
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	public JMSJFrame() {
		setTitle("Java Music Store");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	//	setBounds(100, 100, 450, 300);
		setSize(800,600);
		setLocationRelativeTo(null);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu fileMenu = new JMenu("File");
		menuBar.add(fileMenu);
		
	//	JMenuItem saveDataJMenuItem = new JMenuItem("Save Data");
		saveDataJMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				JOptionPane.showMessageDialog(null,"The data have been saved");
			}
		});
		
		JMenuItem purgeBothTableMenuItem = new JMenuItem("purgeTable");
		purgeBothTableMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			try {
				if (	 databaseJMS.tableExists("A00810029_Inventory") && databaseJMS.tableExists("A00810029_Customers") )
				{
					itemDatabaseInJMS.dropTable();
					JOptionPane.showMessageDialog(null,"The A00810029_Inventory and A00810029_Customers Tables have been droped");
					logger.info("A00810029_Inventory and A00810029_Customers tables have been droped");
					System.exit(0);
				}
				else if (!databaseJMS.tableExists("A00810029_Customers") )
				{
					JOptionPane.showMessageDialog(null,"Customer database has not been created, please click the Customr menu to creat it firstly");
					logger.info("Customer database has not been created, please click the Customr menu to creat it firstly");
				}
			} catch (HeadlessException e1) {
				
				e1.printStackTrace();
			} catch (SQLException e1) {
				
				e1.printStackTrace();
			}
			}
		});
		fileMenu.add(purgeBothTableMenuItem);
		saveDataJMenuItem.setMnemonic('S');
		fileMenu.add(saveDataJMenuItem);
		
		JMenuItem exitJMenuItem = new JMenuItem("Exit");
		exitJMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		exitJMenuItem.setMnemonic('E');
		fileMenu.add(exitJMenuItem);
		
		JMenu manageMenu = new JMenu("Manage");
		menuBar.add(manageMenu);
		
		JMenuItem customersMenuItems = new JMenuItem("Customers");
		customersMenuItems.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				//@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@SuppressWarnings("unused")
				CustomerDialog theCustomerForm = new CustomerDialog(JMSJFrame.this);
				logger.info("Customer dialog is clicked");
			}
		});
		manageMenu.add(customersMenuItems);
		
		JMenuItem rentalJMenuItem = new JMenuItem("Rentals");
		rentalJMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
				@SuppressWarnings("unused")
				RentalDialog newRentalForm = new RentalDialog(JMSJFrame.this);
				logger.info("Rental dialog is clicked");
				
			}
		});
		manageMenu.add(rentalJMenuItem);
		
		JMenuItem inventoryJMenuItem = new JMenuItem("Inventory");
		//this is to fill the inventory combobox/////////////////////////////////////////////////////////////////////////////
		inventoryJMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) 
			{	
				try {
					//@@@@@@@@@@@@@@@@@@@@@@@@@
					@SuppressWarnings("unused")
					InventoryDialog theInventoryForm= new InventoryDialog(JMSJFrame.this);
					logger.info("Inventory dialog is clicked");
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}				
				
			}
		});
		
		manageMenu.add(inventoryJMenuItem);
		
		JMenu helpMenu = new JMenu("Help");
		
		menuBar.add(helpMenu);
		
		JMenuItem aboutJMenuItem = new JMenuItem("About");
		aboutJMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null,"COMP2613 Assignment2 \n by Frank Zhu, A00810029");
				
			}
		});
		aboutJMenuItem.setMnemonic('A');
		helpMenu.add(aboutJMenuItem);
		purchaseItemsJLabel = new JPanel();
		purchaseItemsJLabel.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(purchaseItemsJLabel);
		purchaseItemsJLabel.setLayout(new MigLayout("", "[86px,grow][4px][34px][4px][92px][4px][34px][52px][4px][92px,grow]", "[23px][23px][14px][116px][][][grow][][][][]"));
		
		JLabel customerLabel = new JLabel("Customer");
		purchaseItemsJLabel.add(customerLabel, "cell 0 0,alignx left,aligny center");
		
		customerField = new JTextField();
		purchaseItemsJLabel.add(customerField, "cell 1 0 7 1,growx,aligny center");
		customerField.setColumns(10);
		
		JButton detailButton = new JButton("Details");
		detailButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		purchaseItemsJLabel.add(detailButton, "cell 9 0,growx,aligny top");
		
		JLabel itemLabel = new JLabel("Item");
		purchaseItemsJLabel.add(itemLabel, "cell 0 1,alignx left,aligny center");
		//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		//    JMSInventoryItems=databaseJMS.getItemInventoryFromFile(theInventoryFileInJMS);
		    try {
				inventoryDAOINJMS.init();
			} catch (FileNotFoundException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			} catch (SQLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		    JMSInventoryItems=inventoryDAOINJMS.retriveDataFromInventoryTable();
		 //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
		    ItemDAO.CompareByDescription itemSort= new ItemDAO.CompareByDescription();
			Collections.sort(JMSInventoryItems,itemSort);	
			this.setInventoyItems(JMSInventoryItems);		
		
		itemComboBox.addItemListener(new ItemListener() {
			public void itemStateChanged(ItemEvent e) {
				
				if(e.getStateChange() == ItemEvent.SELECTED)
				{
					Item item = (Item) itemComboBox .getSelectedItem();
		       
		              dollarField.setText(String.valueOf(item.getSellingPrice()));
		              System.out.println(dollarField.getText());
				} 
				
			}
		});
		purchaseItemsJLabel.add(itemComboBox, "cell 1 1 3 1,growx,aligny center");
		
		dollarField = new JTextField();
		purchaseItemsJLabel.add(dollarField, "cell 4 1 3 1,growx,aligny center");
		dollarField.setColumns(10);
		
	//	JComboBox quantitySpinnerComboBox = new JComboBox();
		for (int i=0; i<32; i++)
		{
			int theDay=i;
			quantitySpinnerComboBox.addItem(theDay);
		}
		purchaseItemsJLabel.add(quantitySpinnerComboBox, "cell 7 1,growx,aligny center");
		
		JButton addButton = new JButton("Add");
		addButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				Item selectedItemInJMS=(Item)itemComboBox.getSelectedItem();
				String strSelectedItemInJMS= selectedItemInJMS.toString();
				String strDollarTextFied =dollarField.getText();
				purchasedItemsTextArea.append(strSelectedItemInJMS+" "+strDollarTextFied+"\n");
				
				int soldNumber=0;
				soldNumber=(Integer)quantitySpinnerComboBox.getSelectedItem();
				//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				String needMinusItemSKU=selectedItemInJMS.getStockCode();
				String needMinusItemMake=selectedItemInJMS.getMake();
				String needMinusItemModal=selectedItemInJMS.getModelNumber();
				String needMinusItemDescription=selectedItemInJMS.getDescription();
				String needMinusItemPurchasePrice= String.valueOf(selectedItemInJMS.getPurchasePrice());
				String needMinusItemSellingPrice=String.valueOf(selectedItemInJMS.getSellingPrice());
				String needMinuItemQuanityInStock= Integer.toString((selectedItemInJMS.getQuantityInStock()-soldNumber));
				String needMinusItemQuantitySold=Integer.toString((selectedItemInJMS.getQuantitySold()+soldNumber));
				String needMinusItemNumberRented=Integer.toString(selectedItemInJMS.getNumberRented());
				inventoryDAOINJMS.updateInventoryTable(needMinusItemSKU,
						                               needMinusItemMake,
						                               needMinusItemModal,
						                               needMinusItemDescription,
						                               needMinusItemPurchasePrice,
						                               needMinusItemSellingPrice,
						                               needMinuItemQuanityInStock,
						                               needMinusItemQuantitySold,
						                               needMinusItemNumberRented
						                               );
				//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				
				double eachItemFee=Double.parseDouble(strDollarTextFied); 			
				double totalSoldOneItemsFee=eachItemFee*soldNumber;
				String totalSoldOneItemFeeStr=Double.toString(totalSoldOneItemsFee);
				
				
				 double doubOneItemSoldTotalFee=Double.valueOf(totalSoldOneItemFeeStr.trim()).doubleValue();
	             doubSoldAllItemTotalFee=doubSoldAllItemTotalFee+doubOneItemSoldTotalFee;
	             String strAllItemTotalFee=Double.toString(doubSoldAllItemTotalFee);
							
				
				salesTextField.setText(strAllItemTotalFee);
				
				//***********************************************************calculat total for payment
				  String strRentalTotalPayment=rentalTotalJTextField.getText();
					double doubRentalTotalPayment=Double.valueOf(strRentalTotalPayment).doubleValue();
					
					double doubTotalPayment=doubSoldAllItemTotalFee+doubRentalTotalPayment;
					String strTotalPayment=Double.toString(doubTotalPayment);
					totalJTextField.setText(strTotalPayment);	
					logger.info("Selected Items are added in the main window");
				
			}
		});
		purchaseItemsJLabel.add(addButton, "cell 9 1,growx,aligny top");
		
		JLabel lblPurchasedItems = new JLabel("Purchased Items");
		purchaseItemsJLabel.add(lblPurchasedItems, "cell 0 2,alignx left,aligny top");
		
	//	JTextArea purchasedItemsTextArea = new JTextArea();
		purchaseItemsJLabel.add(purchasedItemsTextArea, "cell 0 3 8 2,grow");
		
		JLabel salesTotalJLabel = new JLabel("Sales Total");
		purchaseItemsJLabel.add(salesTotalJLabel, "cell 9 3,alignx left,aligny bottom");
		
		salesTextField = new JTextField();
		purchaseItemsJLabel.add(salesTextField, "cell 8 4 2 1,growx,aligny center");
		salesTextField.setColumns(10);
		
		JLabel rentalAgreementsJlabel = new JLabel("Rental Agreements");
		purchaseItemsJLabel.add(rentalAgreementsJlabel, "cell 0 5");
		
	//	JTextArea rentalAgreementsJTextArea = new JTextArea();
		purchaseItemsJLabel.add(rentalAgreementsJTextArea, "cell 0 6 9 2,grow");
		
		JLabel rentalTotalJLabel = new JLabel("Rental Total");
		purchaseItemsJLabel.add(rentalTotalJLabel, "cell 9 6,aligny bottom");
		
		rentalTotalJTextField = new JTextField("0");
	 //   rentalTotalJTextField.setText("0");
		purchaseItemsJLabel.add(rentalTotalJTextField, "cell 9 7,growx");
		rentalTotalJTextField.setColumns(10);
		
		JLabel purchaseSummaryJLabel = new JLabel("Purchase Summary");
		purchaseItemsJLabel.add(purchaseSummaryJLabel, "cell 0 9");
		
		JLabel totalJLabel = new JLabel("Total");
		purchaseItemsJLabel.add(totalJLabel, "cell 7 9,alignx right");
		
		totalJTextField = new JTextField();
		purchaseItemsJLabel.add(totalJTextField, "cell 9 9,growx");
		totalJTextField.setColumns(10);
		
		JButton printReceiptButton = new JButton("Print Receipt");
		printReceiptButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				//*************************************************************************************************************
				JDialog theDialog = new JDialog( );
				JTextArea textAreaReceipt = new JTextArea();
				String customerInformation=customerField.getText();
				String tempPurchaseArea=purchasedItemsTextArea.getText();
			    String tempRentalArea=rentalAgreementsJTextArea.getText();
			  
			    String rentalTotalJTextFieldInformation=rentalTotalJTextField.getText();
				String totalJTextFieldInformation= totalJTextField.getText();
				String salesTextFieldInformation=salesTextField.getText();
			//	String[] tempPurchaseArea=showInterFaceLayoutSecond(Lab4JFrame.receiptTextArea);
								
				String text=printReceiptContent(customerInformation,tempPurchaseArea,salesTextFieldInformation,tempRentalArea,rentalTotalJTextFieldInformation,totalJTextFieldInformation);
				textAreaReceipt.append(text);
									
				theDialog.getContentPane().add(textAreaReceipt);
				theDialog.setBounds(100, 100, 900, 600);
				
				theDialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
				theDialog.setVisible(true);
				logger.info("Receipt dialog is clicked");
				//***********************************************************************************************************************
				
			}
		});
		purchaseItemsJLabel.add(printReceiptButton, "cell 9 10,grow");
		
		
		setVisible(true);
	}
	

	          public void setInventoyItems(ArrayList<Item> items) {
						
				for (int i=0; i<items.size(); i++)
				{
					itemComboBox.addItem(items.get(i));
													
				}
			}

			public JTextArea getRentalAgreementsJTextArea() {
				return rentalAgreementsJTextArea;
			}

			public void setRentalAgreementsJTextArea(JTextArea rentalAgreementsJTextArea) {
				this.rentalAgreementsJTextArea = rentalAgreementsJTextArea;
			}

			//Method to print out the receipt
	          
			public  String printReceiptContent(String inputCustomerInformation,
					                           String inputPurchaseArea,
					                           String inputSalesFee,
					                           String inputRentalArea,
					                           String inputRentalTotalFee,
					                           String inputTotaFee)
			 {
				 String printInTextArea;
				 SimpleDateFormat df = new SimpleDateFormat("MM-dd, yyyy");
				 double sum = 0.0;
				 String firstLine="**********************************************\n";
				 String secondLine="         Thank you for shopping at           \n";
				 String thirdLine=("               Quade & McLong\n");
				 String fourthLine="                                             \n";
				 String fifthLine="Date" + " " + df.format(new Date())+"\n";
				 String customerLine="Customer:"+inputCustomerInformation+"\n";
				 String seventhLine= "Your purchase:\n";
			     String eighthLine=inputPurchaseArea+"\n";
				 String ninthLine= "Purchase total Fee:"+inputSalesFee +"\n";		
				 String tenthLine="Your Rental:\n";
				 String eleventhLine=inputRentalArea+"\n";
				 String twelvethLine="Rental total Fee:"+inputRentalTotalFee+"\n";
				 String thirteenthLine="Total payment:"+inputTotaFee+"\n";
		
			
			     String fourteenthLine="**********************************************";
				    
					printInTextArea = firstLine+secondLine+thirdLine+fourthLine+fifthLine+customerLine+seventhLine+eighthLine
							           +ninthLine+tenthLine+eleventhLine+twelvethLine
							           +thirteenthLine+fourteenthLine;
				    return printInTextArea;
			 }


			public JTextField getCustomerField() {
				return customerField;
			}


			public void setCustomerField(JTextField customerField) {
				this.customerField = customerField;
			}
	          
	          
	
}
