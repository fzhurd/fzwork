class Employee {
	constructor(){
		this.firstName="john";
		this.lastName="wong";
	}

	printinfo(){
		console.log(this.firstName+" "+this.lastName);
	}


}

e1=new Employee("Jerry", "Zhang");
e1.printinfo();