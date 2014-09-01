package a00810029.assign2.data;

public class Customer {
	
	private int customerNumber;
	private String firstName;
	private String lastName;
	private String creditCardType;
	private String credtCardNumber;
	private String street;
	private String city;
	private String postalCode;
	
	// default constructor
	public Customer()
	{
		
	}
	
	// constructor start here

	public Customer(int customerNumber, String firstName, String lastName, String creditCardType,
			String credtCardNumber, String street, String city,
			String postalCode) {
		super();
		this.customerNumber=customerNumber;
		this.firstName = firstName;
		this.lastName = lastName;
		this.creditCardType = creditCardType;
		this.credtCardNumber = credtCardNumber;
		this.street = street;
		this.city = city;
		this.postalCode = postalCode;
	}
   
	
	public int getCustomerNumber() {
		return customerNumber;
	}

	public void setCustomerNumber(int customerNumber) {
		this.customerNumber = customerNumber;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getCreditCardType() {
		return creditCardType;
	}

	public void setCreditCardType(String creditCardType) {
		this.creditCardType = creditCardType;
	}

	public String getCredtCardNumber() {
		return credtCardNumber;
	}

	public void setCredtCardNumber(String credtCardNumber) {
		this.credtCardNumber = credtCardNumber;
	}

	public String getStreet() {
		return street;
	}

	public void setStreet(String street) {
		this.street = street;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getPostalCode() {
		return postalCode;
	}

	public void setPostalCode(String postalCode) {
		this.postalCode = postalCode;
	}

	@Override
	public String toString() {
		return "Customer [customerNumber=" + customerNumber + ", firstName="
				+ firstName + ", lastName=" + lastName + ", creditCardType="
				+ creditCardType + ", credtCardNumber=" + credtCardNumber
				+ ", street=" + street + ", city=" + city + ", postalCode="
				+ postalCode + "]";
	}

	
	
	/*public String toString() {
		return "Customer [firstName=" + firstName + ", lastName=" + lastName
				+ ", creditCardType=" + creditCardType + ", credtCardNumber="
				+ credtCardNumber + ", street=" + street + ", city=" + city
				+ ", postalCode=" + postalCode + "]";
	}*/
	
	
	
	
	

}
