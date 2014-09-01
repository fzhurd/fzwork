package a00810029.assign2.data;

 import java.awt.Component;

public class Item {
	private String make;
	private String Description;
	private String modelNumber;
	private String stockCode;
	private int quantityInStock;
	private int quantitySold;
	private float purchasePrice;
	private float sellingPrice;
	private int numberRented;
	
	
	// default constructor
	public Item()
	{
		
	}

   // constructor start
	public Item(String stockCode,
			   String make, 
			    String description, 
			    String modelNumber,                
                float sellingPrice,
                float purchasePrice, 
                int quantityInStock,
			    int quantitySold, 
			    int numberRented) {
		super();
		this.stockCode = stockCode;
		this.modelNumber =modelNumber;
		this.make=make;
		Description = description;
		
		this.quantityInStock = quantityInStock;
		this.quantitySold = quantitySold;
		this.purchasePrice = purchasePrice;
		this.sellingPrice = sellingPrice;
		this.numberRented = numberRented;
	}

	
	

	public String getModelNumber() {
		return modelNumber;
	}

	public void setModelNumber(String modelNumber) {
		this.modelNumber = modelNumber;
	}

	public String getMake() {
		return make;
	}

	public void setMake(String make) {
		this.make = make;
	}

	public String getDescription() {
		return Description;
	}

	public void setDescription(String description) {
		Description = description;
	}

	public String getStockCode() {
		return stockCode;
	}

	public void setStockCode(String stockCode) {
		this.stockCode = stockCode;
	}

	public int getQuantityInStock() {
		return quantityInStock;
	}

	public void setQuantityInStock(String quantityInStock) {
		this.quantityInStock =  Integer.parseInt(quantityInStock);
	}

	public int getQuantitySold() {
		return quantitySold;
	}

	public void setQuantitySold(String quantitySold) {
		this.quantitySold = Integer.parseInt(quantitySold);
	}

	public float getPurchasePrice() {
		return purchasePrice;
	}

	public void setPurchasePrice(String purchasePrice) {
		this.purchasePrice = Float.parseFloat(purchasePrice);
	}

	public float getSellingPrice() {
		return sellingPrice;
	}

	public void setSellingPrice(String sellingPrice) {
		this.sellingPrice = Float.parseFloat(sellingPrice);
		
	}

	public int getNumberRented() {
		return numberRented;
	}

	public void setNumberRented(String numberRented) {
		this.numberRented = Integer.parseInt(numberRented);
	}

	@Override
	public String toString() {
		return "make=" + make + ", model=" + modelNumber;
	}
	
	/*public String toString() {
		return "Desc=" + Description + ", stoCode=" + stockCode;
	}*/

	//@Override
	/*public String toString() {
		return "Item [Description=" + Description + ", stockCode=" + stockCode
				+ "]";
	}*/
    
	
	/*public String toString() {
		return "Item [make=" + make + ", Description=" + Description
				+ ", modelNumber=" + modelNumber + ", stockCode=" + stockCode
				+ ", quantityInStock=" + quantityInStock + ", quantitySold="
				+ quantitySold + ", purchasePrice=" + purchasePrice
				+ ", sellingPrice=" + sellingPrice + ", numberRented="
				+ numberRented + "]";
	}

*/
	

	
	}
	
	
	


