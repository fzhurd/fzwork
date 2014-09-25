package a00810029.assign2.data;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

    public class ItemDAO 
    {
	
    	public ItemDAO()
    	{
    		
    	}

	   
		public static class CompareByDescription implements Comparator<Item> 
		{
			
			public int compare(Item item1, Item item2) 
			{
				String description1=item1.getDescription();
				String description2=item2.getDescription();
				
				return(description1.compareTo(description2));
			}
			
		}
		
		public static class CompareByStockCode implements Comparator <Item>
		{
			
			public int compare(Item item1, Item item2) 
			{
				String stockCode1=item1.getStockCode();
				String stockCode2=item2.getStockCode();
				
				return(stockCode1.compareTo(stockCode2));
			}
			
		}
		
		
		
		
				

    }	


		
      
