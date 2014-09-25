package a00810029.assign2.ui;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import net.miginfocom.swing.MigLayout;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JComboBox;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.List;

import a00810029.assign2.data.*;

import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class RentalDialog extends JDialog {

	private final JPanel buttonSave = new JPanel();
	private JTextField textFieldCustomer;
	private JTextField textFieldDate;
	private JTextField textFieldDailyFee;
	private JTextField textFieldTotalFee;

	private final JComboBox comboBoxNumberOfDays = new JComboBox();
	private final JComboBox comboBoxItem = new JComboBox();

	private double dailyFee;
	
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	
	private ArrayList<Item> rentalInventoryItems= new ArrayList<Item>();
	 File theInventoryFileInJMS=new File("C://IT/Comp2613/Assignment1/inventory.txt");
	//+++ File theInventoryFileInJMS=new File("inventory.txt");
	ArrayList<Item> itemInventory= new ArrayList<Item>();
	
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@SuppressWarnings("unused")
	private Database databaseRental=new Database();

	private double doubAllItemTotalFee=0.0;
	private String strAllItemTotalFee=" ";
	
	
	public RentalDialog(final JMSJFrame thisJMSJFrame) {
		setTitle("Rental Information");
		// setBounds(100, 100, 450, 300);
		setSize(450,300);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		buttonSave.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(buttonSave, BorderLayout.CENTER);
		buttonSave.setLayout(new MigLayout("", "[][grow]", "[][][][][][][]"));
		{
			JLabel lblCustomer = new JLabel("Customer");
			buttonSave.add(lblCustomer, "cell 0 0,alignx trailing");
		}
		{
			textFieldCustomer = new JTextField();
			buttonSave.add(textFieldCustomer, "cell 1 0,growx");
			textFieldCustomer.setColumns(10);
		}
		{
			JLabel dateLabel = new JLabel("Date");
			buttonSave.add(dateLabel, "cell 0 1,alignx trailing");
		}
		{
			textFieldDate = new JTextField();
			SimpleDateFormat df = new SimpleDateFormat("MM-dd, yyyy");
			textFieldDate.setText(df.format(new Date()));
			buttonSave.add(textFieldDate, "cell 1 1,growx");
			textFieldDate.setColumns(10);
		}
		{
			JLabel itemLabel = new JLabel("Item");
			buttonSave.add(itemLabel, "cell 0 2,alignx trailing");
		}
		{
		//###############################################################
		//	JComboBox comboBoxItem = new JComboBox();
			/*try {
				
			//	rentalInventoryItems=getItemInventoryFromFile(theInventoryFileInJMS);
				rentalInventoryItems=databaseRental.getItemInventoryFromFile(theInventoryFileInJMS);
				
				ItemDAO.CompareByStockCode itemSort= new ItemDAO.CompareByStockCode();
 				Collections.sort(rentalInventoryItems,itemSort);	
 				this.setInventoyItems(rentalInventoryItems);
			
			} catch (IOException e1) {
				
				e1.printStackTrace();
			}*/
					
			buttonSave.add(comboBoxItem, "cell 1 2,growx");
		}
		{
			JLabel dailyFeeLabel = new JLabel("Daily Fee");
			buttonSave.add(dailyFeeLabel, "cell 0 3,alignx trailing");
		}
		{
			textFieldDailyFee = new JTextField();
			textFieldDailyFee.setText("0");
			buttonSave.add(textFieldDailyFee, "cell 1 3,growx");
			textFieldDailyFee.setColumns(10);
		}
		{
			JLabel lblOfDays = new JLabel("# of Days");
			buttonSave.add(lblOfDays, "cell 0 4,alignx trailing");
		}
		{
			// JComboBox comboBoxNumberOfDays = new JComboBox();
			for (int i=0; i<32; i++)
			{
				int theDay=i;
				comboBoxNumberOfDays.addItem(theDay);
			}
			   comboBoxNumberOfDays.addItemListener(new ItemListener() {
			   	public void itemStateChanged(ItemEvent e) {
			   		
			   		if(e.getStateChange() == ItemEvent.SELECTED)
			   		{
			   		
			   		double days=0.0;
					days=(Integer)comboBoxNumberOfDays.getSelectedItem();
					dailyFee=Double.parseDouble(textFieldDailyFee.getText()); 			
					double totalFee=dailyFee*days;
					String totalFeeStr=Double.toString(totalFee);
					textFieldTotalFee.setText(totalFeeStr);
			   		}
			   		
			   	}
			   });
			   comboBoxNumberOfDays.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent arg0) {
				 
					
				}
			});
			buttonSave.add(comboBoxNumberOfDays, "cell 1 4,alignx left");
		}
		{
			JLabel totalFeeLabel = new JLabel("Total Fee");
			buttonSave.add(totalFeeLabel, "cell 0 5,alignx trailing");
		}
		{
			textFieldTotalFee = new JTextField();
					
			buttonSave.add(textFieldTotalFee, "cell 1 5,growx");
			textFieldTotalFee.setColumns(10);
		}
		{
			JButton btnSave = new JButton("Save");
			btnSave.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					
					try {
						saveRental();
						
						
				//		String strSetCustomer=textFieldCustomer.getText();
					
						Item thatItem=(Item)comboBoxItem.getSelectedItem();
						
					//	rentedItemListForPay.add(thatItem);
						
						String strThatItem=thatItem.toString();

			    	    String strDailyFee=textFieldDailyFee.getText();
			    	   
			            
			            int dayNumbers=(Integer)comboBoxNumberOfDays.getSelectedItem();
			            String strDayNumbers=Integer.toString(dayNumbers);	
			           
			             
			             String strOneItemTotalFee=textFieldTotalFee.getText();
			             double doubOneItemTotalFee=Double.valueOf(strOneItemTotalFee.trim()).doubleValue();
			             doubAllItemTotalFee=doubAllItemTotalFee+doubOneItemTotalFee;
			             strAllItemTotalFee=Double.toString(doubAllItemTotalFee);
			            
			             thisJMSJFrame.getRentalAgreementsJTextArea().append(strThatItem+" "+strDailyFee+" "+ strDayNumbers+" "+strOneItemTotalFee+"\n");
			             thisJMSJFrame.rentalTotalJTextField.setText(strAllItemTotalFee);		
						
					} catch (IOException e1) {
						
						e1.printStackTrace();
					}
					
				}
			});
			buttonSave.add(btnSave, "flowx,cell 1 6");
		}
		{
			JButton closeButton = new JButton("Close");
			closeButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent arg0) {
					System.exit(0);
				}
			});
			buttonSave.add(closeButton, "cell 1 6");
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
		}
		setVisible(true);
	}
	
	  public void setInventoyItems(ArrayList<Item> items) {
			//	_inventoryItems = items;
				
				for (int i=0; i<items.size(); i++)
				{
					comboBoxItem.addItem(items.get(i));
				
					
					
				}
			}
	  

	  //This method is to save the rental items in the rental file
	  public void saveRental() throws IOException
	   {
		   	      
		    try 
		      {
		       
		    	    FileWriter outRentalWriter = new FileWriter("C://IT/Comp2613/Assignment1/rental.txt", true);
		    	  //+++++	    FileWriter outRentalWriter = new FileWriter("rental.txt", true);
		    	    BufferedWriter outputRental=new BufferedWriter(outRentalWriter);
		    	    outputRental.newLine();
		    	    System.getProperty("line.separator");
		    	    outputRental.write("customer"+"|");
		    	    outputRental.flush();
		    	    
		    	    outputRental.write(textFieldDate.getText()+"|");
		    	    outputRental.flush();
		            
		    	    outputRental.write( textFieldDailyFee.getText()+"|");
		    	    outputRental.flush();
		            
		            int dayNumbers=(Integer)comboBoxNumberOfDays.getSelectedItem();
		            outputRental.write(Integer.toString(dayNumbers)+"|");	
		            outputRental.flush();
		             
		            outputRental.write(textFieldTotalFee.getText()+"|");
		            outputRental.flush();
		            
		            
		            Item tempItem=(Item)comboBoxItem.getSelectedItem();
		            outputRental.write(tempItem.toString()+"|");
		            outputRental.flush();
		            	                     			
		            outputRental.close();
		        
		      } 
		      
		      catch ( FileNotFoundException e ) 
		      {
		         JOptionPane.showMessageDialog( null, e.getMessage() );
		          e.printStackTrace();
		      }
		    // the inventory collection add item, when the new item is input
		    
		   /* Item inputItem =new Item("UN",
		    		                  descriptionJTextField.getText(),	    		                 
		    		                  stockCodeJLabel.getText(),
		    		                  "UN",
		    		                  Double.parseDouble(sellingPriceJTextField.getText()),
		    		                  Double.parseDouble(textField.getText()),		
		    		                  Integer.parseInt(quantityInStockJTextField.getText()),
		    		                  Integer.parseInt(quantitySoldJTextField.getText()),
		    		                     		                      		                
		    		                  Integer.parseInt(numberRentedJTextField.getText())
		    		                  );
		    _inventoryItems.add(inputItem);
		    for (int i=0; i<_inventoryItems.size(); i++)
		    {
		    System.out.println(_inventoryItems.get(i).toString());
		    System.out.println("%%%%%%%%%%%%%%%%%%"+_inventoryItems.size());
		    }*/

		   }  
	  //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

}
