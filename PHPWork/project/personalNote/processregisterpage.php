<?php

		require_once('constant.php');
		require_once('recaptchalib.php');
		ob_start();
		session_start();
		//*******************************************************************
		$userAgent = $_SERVER['HTTP_USER_AGENT'];
		$createdString = sha1('secret'.$userAgent.session_id().'comp');

		if($_SESSION['secretsession']== $createdString)
		{


		//********************************************************************

		// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
		// it is unsafe
        $cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	    mysql_select_db("a8251972_note") or die(mysql_error());
    	$inputEmail = $_REQUEST['email'];
		$passwordInRegistration1=$_REQUEST['passwd1'];
		$passwordInRegistration2=$_REQUEST['passwd2'];

   //This is to validate the length of the password
	 if ((strlen($passwordInRegistration1)<4)||strlen($passwordInRegistration2)<4) {

	 	header("location: registerpage.php");
	 	echo "password is too short, at least 4 numbers.<br />";
	 }
      else if ($passwordInRegistration1!=$passwordInRegistration2) {

      	    header("location:registerpage.php");
         	echo "password does NOT match.<br />";

	}

//*****************************************************verification

	$privatekey = "6LerBtISAAAAAA_jd693HeeCkc02ONeEHKh-H06D";
	$resp = recaptcha_check_answer ($privatekey,
                   $_SERVER["REMOTE_ADDR"],
        $_POST["recaptcha_challenge_field"],
        $_POST["recaptcha_response_field"]);

	if (!$resp->is_valid) {
	// What happens when the CAPTCHA was entered incorrectly
	die ("The reCAPTCHA wasn't entered correctly. Go back and try it again." .
	     "(reCAPTCHA said: " . $resp->error . ")");
	} else {
	// Your code here to handle a successful verification
//***************************************************************************************
		$passwordInRegistration1=md5($passwordInRegistration1);  //encry passwords
		$passwordInRegistration2=md5($passwordInRegistration2);

		$hashCode =md5(createRandomPassword());
//***************************************************************************************
	   $checkEmailForm =isEmailAddressWellFormed($inputEmail);

   		 $query1 = "SELECT email FROM userinformation WHERE email='$inputEmail'";
		/*
   $query2 = "SELECT password1 FROM userinformation WHERE password1='$passwordInRegistration1'";
   $query3 = "SELECT email, password1 FROM userinformation WHERE email='$inputEmail' and password1='$passwordInRegistration1'";
		   */
		$query2 = "SELECT password1 FROM userinformation WHERE password1='$passwordInRegistration1'";
		$query3 = "SELECT email, password1 FROM userinformation WHERE email='$inputEmail' and password1='$passwordInRegistration1'";


    $result1 = mysql_query($query1) or die(mysql_error());
    $result2 = mysql_query($query2) or die(mysql_error());
    $result3 = mysql_query($query3) or die(mysql_error());

    $countUsername=mysql_num_rows($result1);

    $userExist=true;
    if($countUsername==0)
    {
    	echo "This username does not exist, you could register it.";
    	$userExist =false;
    }

    else
    {
    	echo "The user has exist, change another user name";
    }
   // $countPassword=mysql_num_rows($result2);
  //  $countUsernameAndPassword=mysql_num_rows($result3);



    // register a new user and put the new user information in the database
	if ($checkEmailForm && ($passwordInRegistration1==$passwordInRegistration2)&&($userExist==false)) {

		//******************************************************************************
		echo "unused email, go on <br/>";
		// This is to create the new user information
		/*
		$queryInsertNewUser ="INSERT INTO userinformation (userID, email, password1, password2, numberofvisits, hash, active)
	    VALUES (null, '$inputEmail', '$passwordInRegistration1','$passwordInRegistration2', 0, '', 0);";

		$resultInputNewUser = mysql_query($queryInsertNewUser) or die(mysql_error());
		   */

		$queryInsertNewUser ="INSERT INTO userinformation (userID, email, password1, password2, numberofvisits, hash, active)
	    VALUES (null, '$inputEmail', '$passwordInRegistration1','$passwordInRegistration2', 0, '$hashCode', 0);";

		$resultInputNewUser = mysql_query($queryInsertNewUser) or die(mysql_error());

		//this is to create the text contents table
		$queryInsertNewUserNotesTable ="INSERT INTO notestable (notesID, email, notesContent) VALUES (null, '$inputEmail', '');";
		$resultInputNewUser = mysql_query($queryInsertNewUserNotesTable) or die(mysql_error());


		//this is to create the hyperlink table
		$queryInsertNewUserHyperLinkTable ="INSERT INTO hyperlinktable (hyperLinkID, email, hyperLinkContent) VALUES (null, '$inputEmail', '');";
		$resultInputNewUserForHyperLink = mysql_query($queryInsertNewUserHyperLinkTable) or die(mysql_error());

        //This is to create the table for image stock

		$queryInsertNewUserImageTable ="INSERT INTO imagetable (imageID, email, imageContent) VALUES (null, '$inputEmail', '');";
		$resultInputNewUserForImage = mysql_query($queryInsertNewUserImageTable) or die(mysql_error());

		$queryInsertNewUsertbdTable ="INSERT INTO tbdtable (tbdID, email, tbdContent) VALUES (null, '$inputEmail', '');";
		$resultInputNewUserForTBD = mysql_query($queryInsertNewUsertbdTable) or die(mysql_error());

               // send email to activate the user

				$to  = $inputEmail;
				$subject = 'user name registration';
  			//	$message = 'Congratulation! the user email has been registered, please click to activate! http://localhost/Assignment2Comp2920/20120525Assignment2/verify.php?email='.$inputEmail.'&hash='.$hashCode.' ';
			    $message = 'Congratulation! the user email has been registered, please click to activate! http://fzhu.net63.net/php/project/20120525Assignment2/verify.php?email='.$inputEmail.'&hash='.$hashCode.' ';
				$headers = 'From: fzhucomp2920@gmail.com' . "\r\n" .
				'Reply-To: fzhucomp2920@gmail.com' . "\r\n" .
				'X-Mailer: PHP/' . phpversion();

				if(mail($to, $subject, $message, $headers)) {
				echo 'Email sent successfully!Please check your email to activate the registration name';
				} else {
				die('Failure: Email was not sent!');
				}

	}

	}


}


?>