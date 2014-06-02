<?php

// This function is to display the form, it is handled in this php file

function displayForm($username)
{

	echo '<form action="page3.php" method="get">';

	echo 'Email Address       ';
	//	echo '<input type="text" name="username" value='.$valueOfUserName.'>';

	echo '<input type="text" name="username" value='.$username.'>';
	echo "<hr>";
	echo "<br />";
	echo 'Password            ';
	//	echo '<input type="text" name="password" value='.$valueOfPassword.'>';
	echo '<input type="password" name="password" >';
	echo "<br />";
	echo "<hr>";
	echo 'log in'."<br />";
	echo '<input type="submit" name="submit" />';

	echo '</form>';

}

  // This function is to upload the files (10 files)
   function upLoadTenFiles(){
   	echo '<form  enctype="multipart/form-data" action="page2.php" method="post" >';

   	    echo 	'File '.'01'.': '.'<input type="file" name="file1" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'02'.': '.'<input type="file" name="file2" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'03'.': '.'<input type="file" name="file3" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'04'.': '.'<input type="file" name="file4" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'05'.': '.'<input type="file" name="file5" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'06'.': '.'<input type="file" name="file6" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'07'.': '.'<input type="file" name="file7" >.<br/>';
   	    echo "<br />";
	    echo 	'File '.'08'.': '.'<input type="file" name="file8" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'09'.': '.'<input type="file" name="file9" >.<br/>';
   	    echo "<br />";
   		echo 	'File '.'010'.': '.'<input type="file" name="file10" >.<br/>';
   	    echo "<br />";

    	echo "Submit ".'<input type="Submit" value="Submit">';

     	echo	'</form>';


   }


// This function is to check the validality of the email address
// Note: Here the valid email example is like: fzhu11@my.bcit.ca, this is also the email for testing
    function isEmailAddressWellFormed($emailAddress)
    {
	return 1;
	
    }

 // This is to create the colorful rectangular image

    function creatColoredRectangularImage($inputString){


    	$myEmailImage=ImageCreateTrueColor(300,200);
    	$purple =ImageColorAllocate($myEmailImage, 255,0,255);
    	$white =ImageColorAllocate($myEmailImage, 255,255,255);
    	ImageFill($myEmailImage, 0,0, $purple);
    	imageString($myEmailImage,5,20,20,$inputString, $white);
    	imagejpeg($myEmailImage,"myEmailImage.jpg",100);
   
    	imageDestroy($myEmailImage);
    	echo "This is the solid colored email rectangular image<br>"."<img src=\"myEmailImage.jpg\">";

    }


    //product random password
		function createRandomPassword() {
				$chars = "abcdefghijkmnopqrstuvwxyz023456789";
				srand((double)microtime()*1000000);
 	         	$i = 0;
				$pass = '' ;

				while ($i <= 7) {
					$num = rand() % 33;
					$tmp = substr($chars, $num, 1);
					$pass = $pass . $tmp;
					$i++;
				}

					return $pass;

				}

      // function to get images
    function getImages($imageID){

   // require_once('constant.php');
  //	ob_start();
  //	session_start();

// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
// it is unsafe
	$cid = mysql_connect("localhost", "root") or die(mysql_error());
	mysql_select_db("notetomyself") or die(mysql_error());

//	$email = $_SESSION['username'];

	$query8 = mysql_query("SELECT * FROM imagetable WHERE imageID ='$imageID'");
    $row8=mysql_fetch_object($query8);
	while($row8=mysql_fetch_object($query8)){

	header("Content-Type:image/jpeg");
//	 header("Content-type: image/gif") ;


	echo base64_decode($row8->imageContent);
	echo $row->imageID."{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{[";
	}
     }


    //********************************************************session check function

	function isLogged(){
	if($_SESSION['logged']){ # When logged in this variable is set to TRUE
		return TRUE;
		}else{
		return FALSE;
		}
	}

	# Log a user Out
	function logOut(){
	$_SESSION = array();
	if (isset($_COOKIE[session_name()])) {
		setcookie(session_name(), '', time()-42000, '/');
	}
	session_destroy();
	}


# Session Logout after in activity
function sessionX(){
	$logLength = 1800; # time in seconds :: 1800 = 30 minutes
	$ctime = strtotime("now"); # Create a time from a string
	# If no session time is created, create one
	if(!isset($_SESSION['sessionX'])){
		# create session time
		$_SESSION['sessionX'] = $ctime;
	}else{
		# Check if they have exceded the time limit of inactivity
		if(((strtotime("now") - $_SESSION['sessionX']) > $logLength) && isLogged()){
			# If exceded the time, log the user out
			logOut();
			# Redirect to login page to log back in
			header("Location: /logout.php");
			exit;
		}else{
			# If they have not exceded the time limit of inactivity, keep them logged in
			$_SESSION['sessionX'] = $ctime;
		}
	}
}

?>