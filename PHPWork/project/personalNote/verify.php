

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

	<head>
		<title>Login page</title>
                <link type="text/css" rel="stylesheet" href="loginstyle2.css" />
	</head>

<body>
  Thank you for confirming your registration for . You may now <a href="loginpage.php">log in</a>. <!-- verified the user, redirect to the login page -->

<?php

		require_once('constant.php');
		require_once('recaptchalib.php');
		ob_start();
		session_start();

// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
// it is unsafe

	$cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	        mysql_select_db("a8251972_note") or die(mysql_error());

		//**************************************************************************************
$userAgent = $_SERVER['HTTP_USER_AGENT'];
$createdString = sha1('secret'.$userAgent.session_id().'comp');



//**************************************************************************************

   //  if(isset($_GET['inputEmail']) && !empty($_GET['inputEmail']) AND isset($_GET['hashCode']) && !empty($_GET['hashCode'])){
    if(isset($_GET['email']) && !empty($_GET['email']) AND isset($_GET['hash']) && !empty($_GET['hash'])){

    	$email = mysql_escape_string($_GET['email']); // Set email variable
    	$hash = mysql_escape_string($_GET['hash']); // Set hash variable

     	 $search = mysql_query("SELECT email, hash, active FROM userinformation WHERE email='".$email."' AND hash='".$hash."' AND active='0'") or die(mysql_error());
     	 $match  = mysql_num_rows($search);
      	 echo $match."<br />";

	if($match > 0)
	{
	  	    echo "your input is matched";// We have a match, activate the account
			mysql_query("UPDATE userinformation SET active=1 WHERE email='".$email."' AND hash='".$hash."' AND active='0'") or die(mysql_error());
	}
     else{
		    echo 'No match'."<br/>"; //-> invalid url or account has already been activated.
		}



     }

//}

     ?>


</body>
</html>