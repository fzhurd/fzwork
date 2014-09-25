package a00810029.assign2.drive;

import java.awt.EventQueue;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;

import a00810029.assign2.data.*;
import a00810029.assign2.ui.*;


public class AssignmentDrive {
	static Logger logger = Logger.getLogger(AssignmentDrive.class);
//	private  static Database totalDatabase;
//	private  static InventoryDAO mainInventoryDAO;
//	private static ArrayList<Item> theItemInventory= new ArrayList<Item>();
	
	public static void main(String[] args) throws IOException {
		
	//	PropertyConfigurator.configure(args[0]);
		PropertyConfigurator.configure("Assignment2Logging.properties");
		logger.info("start the log");
	
         EventQueue.invokeLater(new Runnable() {
 	
 			public void run() {
 				try {				
 					
 					JMSJFrame mainFrame = new JMSJFrame();
 				
 	
 				} catch (Exception e) {
 					e.printStackTrace();
 				}
 			}
 		});
         
         
	
	}
	
	
    
    

       
	
	

}
