	<?php

	require_once('constant.php');
	ob_start();
	session_start();

	// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
	// it is unsafe

   	$cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	mysql_select_db("a8251972_note") or die(mysql_error());

	//*****************************************************************************************


	//***************************************************************************************

	$email = $_SESSION['username'];
	session_destroy();
	setcookie('secretcookie',(time()-60));
	setcookie("loggedin",(time()-60));
	setcookie("username",(time()-60));
	setcookie("password",(time()-60));
	setcookie("logintime",(time()-60));
   ?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<link rel="shortcut icon" href="pencil.ico" />

<title>Note to Myself - Log in</title>
<link type="text/css" href="css/register2.css" rel="stylesheet" media="screen"></link>

	<script src="js/jquery-1.4.1.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="js/login2.js"></script>

</head>
<body>
   <h2> <?php echo $_SESSION['username']; ?> is now logged out. Thank you.</h2
   <p><a href='loginpage.php'>Log in</a> again.
   </p>

   </body>
   </html>


