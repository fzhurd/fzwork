
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">


	<head>
		<title>Login page</title>
                <link type="text/css" rel="stylesheet" href="loginstyle2.css" />
	</head>

<body>
  <h1>Reset Your Password</h1>
	<form action="processforgetpasswordpage.php" method="post">
	<p>Type your email address in the text box below. A new password will be sent to your email address. </p>
	 <ul>

        <li>
            <h3>Email address<span id="validEmail"></span></h3>
            <p>
                <input type="text" name="inputEmailForResetPass"  />
				</p>
        </li>



        <li class="last">
            <p>
				<!--<a id="signup" href="#"> -->
				<!--	<input type="image" value="Email new password" id="submit" alt="reset button" style="vertical-align:middle;" tabindex="5" /> -->
					<input type="submit" value="Email new password" alt="password-reminder button" style="vertical-align:middle;" tabindex="5" />
				<!--</a>-->
				</p>
		</li>



    </ul>

	</form>


</body>
</html>
