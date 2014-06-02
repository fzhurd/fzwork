<?php

		require_once('constant.php');
		ob_start();
		session_start();

		// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
		// it is unsafe
	
	$cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	mysql_select_db("a8251972_note") or die(mysql_error());

		//********************************************************************************
		if(!isset($_SESSION['secretsession']))
	{
	$userAgent = $_SERVER['HTTP_USER_AGENT'];

	$strong_id = 'secret'.$userAgent.session_id().'comp';

	$_SESSION['secretsession'] = sha1($strong_id);

	setcookie('secretcookie','comp');

	$_SESSION['timestamp'] = time();

	$_SESSION['logAttempt']=0;

	}


	//********************************************************************************

	if(isset($_REQUEST['username'])&&isset($_REQUEST['password']) )

	{
	// if it has received the value
	// trying to log in, first time log in
	//********************************************************************

			$username=$_REQUEST['username'];
			$password=$_REQUEST['password'];

	// This is to standarlize the input username and password
			$username = stripslashes($username);
			$password = stripslashes($password);

	// This is to standarlize the input username and password
			$username = mysql_real_escape_string($username);
			$password = mysql_real_escape_string($password);

			$password = md5($password); //This is to change the input password and MD5 TO 32 BITES to check in the database

		$query1 = "SELECT email FROM userinformation WHERE email='$username'";
		$query2 = "SELECT password1 FROM userinformation WHERE password1='$password'";
		$query3 = "SELECT email, password1 FROM userinformation WHERE email='$username' and password1='$password'";
		$query5 = "SELECT numberofvisits FROM userinformation WHERE email='$username' and password1='$password'";

	//verify active
		$query6 = "SELECT active FROM userinformation WHERE email='$username' and password1='$password'";


		$result1 = mysql_query($query1) or die(mysql_error());
		$result2 = mysql_query($query2) or die(mysql_error());
		$result3 = mysql_query($query3) or die(mysql_error());
		$result5 = mysql_query($query5) or die(mysql_error());

		$result6 = mysql_query($query6) or die(mysql_error());

		while($record=mysql_fetch_row($result6))
		{
			foreach($record as $fieldActive)
			{
				$activeRecord=$fieldActive;
				echo $activeRecord."#######################################";
			}
		}

	// Mysql_num_row is counting table row
	$countUsername=mysql_num_rows($result1);
	$countPassword=mysql_num_rows($result2);
	$countUsernameAndPassword=mysql_num_rows($result3);

	// retrieve the visit number previously from the table

	while($record=mysql_fetch_row($result5))
	{
		foreach($record as $field)
		{
			$countHaveVistitedNumbers=$field;
		}
	}
 //   $_SESSION['logAttempt'];


	// This is to check the username and password, if it is verified, then logged in and set sessions and cookies
	if( ($countUsernameAndPassword==1) && ($activeRecord>0) )

	{
		header("location: notetomyself.php"); // direct to the notetomyself page

		$_SESSION['username']=$username;
		$_SESSION['password']=$password;
		$_SESSION['logAttempt']=0;  // If it is successfully logged in, the log attems will be reset to 0
		$_SESSION['login']=1;
		// this is to check the inactive time$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
		$_SESSION['logged']=time();

		$vistitNumber=$countHaveVistitedNumbers;
		$vistitNumber++;
		//		echo $vistitNumber."*******************************";

		setcookie("loggedin",1,(time()+600));
		setcookie("username",$username,(time()+60));
		setcookie("password",$password,(time()+60));
		setcookie("logintime",time(),(time()+60));

		echo "You logged in<br />";

	 }  // if($countUsernameAndPassword==1)

	else if( ($countUsernameAndPassword==1) && ($activeRecord==0) )
	{
		echo "Please active your registration name firstly<br/>";
	}

	else if($countUsername==0)
	{

		// if no user name is input, then the login atems will be counted
		echo "no such user<br />";
		$_SESSION['logAttempt']++;
		echo "You have tried ".$_SESSION['logAttempt']." times to log in".'<br />';

		// if the log attems >3, it will be redirected to the bcit website
		if ($_SESSION['logAttempt']>3)
		{
			echo "You have tried more than 3 times to log in<br />";
		    header("location: forgetpasswordpage.php");

		}    //($_SESSION['logAttempt']>3)
	}  //($countUsername==0)

	else if($countPassword==0)   // if the password is wrong, the failed times will be added one
	{
		echo "wrong password<br />";
		$_SESSION['logAttempt']++;

		echo "You have tried ".$_SESSION['logAttempt']." times to log in".'<br />';
		if ($_SESSION['logAttempt']>=3)
		{
			 echo "You have tried more than 3 times to log in<br />";
			 header("location: forgetpasswordpage.php");

		}  //($_SESSION['logAttempt']>=3)

	}  //($countPassword==0)
	else if($countUsernameAndPassword==0)  // if the username and password are not matched, it will count the log attempt times
	{

		echo "Wrong Username or Password<br />";
		$_SESSION['logAttempt']++;

		echo "You have tried ".$_SESSION['logAttempt']." times to log in".'<br />';
		if ($_SESSION['logAttempt']>=3)
		{
			echo "Wrong Username or Password<br />";
			echo "You have tried more than 3 times to log in<br />";
			header("location: forgetpasswordpage.php");

		}  //if ($_SESSION['logAttempt']>=3)


	}  // ($countUsernameAndPassword==0)

  }
	   //	if(isset($_REQUEST['username'])&&isset($_REQUEST['password']) )
	else
	{

		echo "Please input user name and password";
	}



    ?>