<?php
		//*******************************************************************
		ob_start();
		session_start();

		// check secure sessions

		if(!isset($_SESSION['secretsession']))
		{
			$userAgent = $_SERVER['HTTP_USER_AGENT'];

			$strong_id = 'secret'.$userAgent.session_id().'comp';

			$_SESSION['secretsession'] = sha1($strong_id);

			setcookie('secretcookie','comp');

			$_SESSION['timestamp'] = time();

		}

	else{
//	  echo "You have logged in, directly to the login page";
	//	header("location: notetomyself.php");
	}




//********************************************************************

?>



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

	<head>
		<title>Registration Page</title>
                <link type="text/css" rel="stylesheet" href="loginstyle2.css" />
	</head>

<body>
  <h1>Register</h1>
	<form action="processregisterpage.php" method="post">

	 <ul>

        <li>
            <h3>Email address<span id="validEmail"></span></h3>
            <p>
                <input type="text" name="email"  />
				</p>
        </li>

        <li>
            <h3 >Password<span id="validPass"></span></h3>

            <p>
                <input type="password" id="passwd" name="passwd1" /></p>
        </li>


				 <li>
            <h3 >Password<span id="validPass"></span></h3>

            <p>
                <input type="password" id="passwd" name="passwd2" /></p>
        </li>
         <li>
             <?php
             require_once('recaptchalib.php');
             $publickey = "6LerBtISAAAAAI34ZLeU4kVJTIDKwWaudWBWLbOF"; // you got this from the signup page
             echo recaptcha_get_html($publickey);
             ?>
         </li>

        <li class="last">
            <p>
				<!--<a id="signup" href="#"> -->
					<input type="image" id="submit" src="button2.png" alt="register button" style="vertical-align:middle;" tabindex="5" />
				<!--</a>-->
				</p>
		</li>

		<li>
				<p><a href="registerpage.php">Register</a> or <a href="loginpage.php">log in</a>
				</p>
        </li>


    </ul>

	</form>


</body>
</html>
