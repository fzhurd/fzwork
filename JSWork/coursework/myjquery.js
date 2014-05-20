$(document).ready(function(){
		// $('form').validate();	
	$('form').validate({
      rules: {
      "u": {
      required: true,
      minlength: 5,
	  maxlength: 10
    }
  }
});
	});