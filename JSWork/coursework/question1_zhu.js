

window.onload=function(){

	document.forms[0].onsubmit=function(){

		var els = this.elements;

		for(var i = 0; i < els.length; i++){


			// alert(els[i].className);

            //check the required textbox is empty or not
			if(els[i].className.indexOf("required") != -1){
				if(els[i].value == ""){
					els[i].focus();
					return false;
				}
			}
		}	
		
	
	// check the username
	if(  !((document.getElementById('u').value.length >=5)&& (document.getElementById('u').value.length <=10) )    )
	{
            alert ("username invalid");
			return false; // do not submit the form
	}
	//check the email address
	else if ( ! ((document.getElementById('e').value.indexOf('@') != -1)&&(document.getElementById('e').value.indexOf('.') != -1)  ) )
				
	{
	    alert("email invalid");
				return false;
	}
//	check the street
	else if (   isNaN( document.getElementById('s').value.charAt(0) )   )
	{
			//document.getElementById('y').select();
			alert("Street invalid");
			return false;
		}
	else if( isNaN(document.getElementById('y').value)   ){   //check the birthday
		//	document.getElementById('y').select();
		    alert("Birth of Date invalid");
			return false;
		}
		else 
		{
		 return true;
		}
		
	   
	
	} //onsubmit
	
	
} // window onload

