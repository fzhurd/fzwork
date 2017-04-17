package com.fz.automation;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MyService {

	public MyService() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		
		 	MyService myService = new MyService();
	        myService.method("name", "hello");
	        myService.method("name", new Student("frank", 123));
	        
	        List<Student> studentList = new ArrayList<Student>();
	        studentList.add(new Student("frank", 123));
	        studentList.add(new Student("john", 223));
	        
	        myService.method("name", studentList);
	        
	        myService.doIt("ff", "math","english");
	        for (int i=0; i<10; i++){
	        	System.out.println(i);
	        }
	        myService.doIt("ff", "math","english","chemistry","biology");
	        System.out.println("######################");
	        myService.doIt("ss","gg");
	        
//	        myService.<List<Student>>method("name", Lists.newArrayList(new Student("frank", 123)));
	        String[] totalTypes={"red","blue","green", "black","yellow", "CC"};
	        List<String> options=myService.categoryDataTypes(true);
	        List<String> filteredTypes=myService.filterMessages(options, totalTypes);
	        for (int i=0; i<filteredTypes.size(); i++){
	        	System.out.println(filteredTypes.get(i));
	        }
	        
	        
	        
	}
	
	public <T> void method(String name, T para) {
        System.out.println(para.toString());
    }
	
	public void doIt(String name, String... courses){
		for (int i=0; i<courses.length; i++)
		{
		System.out.println(name+ " abc "+ " hello "+ courses[i]);
		}
	}
	
	public List<String> filterMessages(List<String> expectedOptions,  String... messageTypes){
		
		List<String> filteredDataType = new ArrayList<String>(); 
		/*
		for (int i=0; i< messageTypes.length; i++){
			if (expectedOptions.contains(messageTypes[i]))
			{
				filteredDataType.add(messageTypes[i]);
			}
		}
		*/
		for (String type: messageTypes){
			if (expectedOptions.contains(type))
			{
				filteredDataType.add(type);
			}
		}
		return filteredDataType;
		
	}
	
	
	public List<String> categoryDataTypes(String dataType){
		
		 List<String> expectedOptions= new ArrayList<String>();
		 String[] theArray;
	     switch (dataType) {
	         case "Type1":
	        	 theArray=new String[]{"red", "green", "yellow"};    	 
	             break;
	         case "Type2":
	        	 theArray=new String[]{"blue", "green", "black"};
	             break;
	         case "Type3":
	        	 theArray=new String[]{"green", "black", "white"};
	             break;
	         default:
	             throw new IllegalArgumentException("This type still not supported: " + dataType);     
	     }
	     expectedOptions.addAll(Arrays.asList(theArray));
	     return expectedOptions;
	}
	
	public List<String> categoryDataTypes(boolean isEmail){
		
		 List<String> expectedOptions= new ArrayList<String>();
		 String[] emailDropDownFullLists={"red", "green", "yellow", "CC","BCC"};
		 String[] chatDropDownFullLists={"blue", "black","green","CC","BCC"};
		 
	     String[] theArray=isEmail?emailDropDownFullLists:chatDropDownFullLists;
	     expectedOptions.addAll(Arrays.asList(theArray));
	     return expectedOptions;
	}
	

}
