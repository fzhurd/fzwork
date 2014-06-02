<?php



	require_once('constant.php');
	ob_start();
	session_start();

	// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
	// it is unsafe
	$cid = mysql_connect("localhost", "root") or die(mysql_error());
	mysql_select_db("notetomyself") or die(mysql_error());

//	   echo "hello, thubmailed images";

	$email = $_SESSION['username'];
// echo $email." uuuuuuuuuuuuuuuuuuuuuu<br/>";
    $imageID = $_REQUEST['imageID'];
//echo $id."#################################";
    $query11 = mysql_query("SELECT * FROM imagetable WHERE imageID ='$imageID'");
    $row11=mysql_fetch_object($query11);
//    while($row8=mysql_fetch_object($query8)){
//$imageID =$row8->imageID;
     $imageID =$row11->imageContent;
//	echo "<img src='data:image/png;base64,$imgStr' />";
      header("Content-Type:image/jpeg");

      echo base64_decode($row11->imageContent);


?>