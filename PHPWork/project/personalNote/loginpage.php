
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

	<head>
		<title>Login page</title>
        <link type="text/css" rel="stylesheet" href="loginstyle2.css" />
	</head>

<body>
  <h1>Log in</h1>
	<form action="processloginpage.php" method="get">
	 <ul>
        <li>
            <h3>Email address<span id="validUsername"></span></h3>
                <p>
                <input type="text" name="username" id="username" />
				</p>
        </li>

        <li>
            <h3 >Password<span id="validPass"></span></h3>

            <p>
                <input type="password" id="password" name="password" /></p>
        </li>


        <li class="last">
            <p>
				<!--<a id="signup" href="#"> -->
					<input type="image" id="submit" src="login2.png" alt="register button" style="vertical-align:middle;" tabindex="5" />
				<!--</a>-->
				</p>
		</li>

		<li>
				<p><a href= "registerpage.php" >Register</a> | <a href="forgetpasswordpage.php">Forgot password</a>
				</p>
        </li>

        <li id="errormessage" style="color:red;"></li>
		<li><a href="http://twitter.com/#!/notes_myself">Twitter</a></li>
    </ul>

	</form>


</body>
</html>
