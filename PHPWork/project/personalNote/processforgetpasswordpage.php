<?php

	require_once('constant.php');
	require_once('recaptchalib.php');
	ob_start();
	session_start();

// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
// it is unsafe

	$cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	mysql_select_db("a8251972_note") or die(mysql_error());
	//************************************************************************

//*****************************************************************************************

$userAgent = $_SERVER['HTTP_USER_AGENT'];
$createdString = sha1('secret'.$userAgent.session_id().'comp');



//*****************************************************************************************
    $inputEmailForResetPass =$_REQUEST['inputEmailForResetPass'];

    $resetPasswordBeforeHandle = createRandomPassword();
    //*************************************************** Hash the password

	$resetPasswordAfterHandle=md5($resetPasswordBeforeHandle);  //encry passwords
	$hashCode =md5(createRandomPassword());


    //********************************************************************

	$to  = $inputEmailForResetPass;
	$subject = 'new password is reset';
	$message = 'Your new password is ,'. $resetPasswordBeforeHandle.' please click to activate! http://localhost/Assignment2Comp2920/20120525Assignment2/verify.php?email='.$inputEmailForResetPass.'&hash='.$hashCode.' ';
	$headers = 'From: fzhurd@gmail.com' . "\r\n" .
	'Reply-To: fzhurd@gmail.com' . "\r\n" .
	'X-Mailer: PHP/' . phpversion();

	if(mail($to, $subject, $message, $headers))
	{
	echo 'Email sent successfully!';

		// reset two password after encry and store in the database
		$updateResetPassword1="UPDATE userinformation SET password1='$resetPasswordAfterHandle' WHERE  email='$inputEmailForResetPass';";
		$updateResetPassword2="UPDATE userinformation SET password2='$resetPasswordAfterHandle' WHERE  email='$inputEmailForResetPass';";

		// reset hashcode and active
		$updateResetHashcode="UPDATE userinformation SET hash='$hashCode' WHERE  email='$inputEmailForResetPass';";
		$updateResetActive="UPDATE userinformation SET active=0 WHERE  email='$inputEmailForResetPass';";



		$res9=mysql_query($updateResetPassword1)or die(mysql_error());
		$res10=mysql_query($updateResetPassword2)or die(mysql_error());

		$res11=mysql_query($updateResetHashcode)or die(mysql_error());
		$res12=mysql_query($updateResetActive)or die(mysql_error());

		echo $inputEmailForResetPass."<br/>";
		echo $resetPasswordBeforeHandle."<br />";
		session_destroy();
	}
     else {
	die('Failure: Email was not sent!');
	}

//}
?>