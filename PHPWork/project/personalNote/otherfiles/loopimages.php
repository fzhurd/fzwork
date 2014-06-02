<?php

	require_once('constant.php');
	ob_start();
	session_start();

// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
// it is unsafe
	$cid = mysql_connect("localhost", "root") or die(mysql_error());
	mysql_select_db("notetomyself") or die(mysql_error());

	$email = $_SESSION['username'];

   // $imgg=getImages();
//echo $id."#################################";
	$query = mysql_query("SELECT * FROM imagetable WHERE email = '$email'");
//	echo "<img src=\".getImages()\" />";


	while($row=mysql_fetch_object($query)){

	//   header("Content-Type:image/jpeg");
	//	 header("Content-type: image/gif") ;

	//	echo "<img src=get.php?imageID=$lastid>";

		echo "get.php?".$row->imageID;
		echo "<img src=\"get.php?imageID=".$row->imageID."\" />";

	//	echo "<img src=\"getImages($row->imageID)\">";
        echo $row->imageID;

//	echo base64_decode($row->imageContent);

	//	echo $row->imageID."{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{[";



}







?>