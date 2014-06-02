
<?php

	require_once('constant.php');
	ob_start();
	session_start();

	// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
	// it is unsafe

	$cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	mysql_select_db("a8251972_note") or die(mysql_error());
//*******************************************************************************

	if (!isset($_COOKIE['loggedin'])) {

	echo "You are not loggedin, register firstly";
	header("location: registerpage.php");


	}
//********************************************************************************

$userAgent = $_SERVER['HTTP_USER_AGENT'];
$createdString = sha1('secret'.$userAgent.session_id().'comp');

if($_SESSION['secretsession']== $createdString)
{


//********************************************************************************8
    $inputNotes = $_REQUEST['notes'];
    $email = $_SESSION['username'];

    echo $_SESSION['username'];
    echo $inputNotes;

	$query1 = "SELECT email FROM notestable WHERE email='$email'";

	$query5 = "SELECT notesContent FROM notestable WHERE email='$email'";
	$result1 = mysql_query($query1) or die(mysql_error());
	$result5 = mysql_query($query5) or die(mysql_error());

    $updateNewNotes="UPDATE notestable SET notesContent='$inputNotes' WHERE  email='$email';";

    $res2=mysql_query($updateNewNotes)or die(mysql_error());

     //*******************************************************************

       // start to store the tbd content
       $inputTbdContent =$_REQUEST['tbd'];
       $query7 = "SELECT tbdContent FROM tbdtable WHERE email='$email'";
       $result7 = mysql_query($query7) or die(mysql_error());

       $updateTbd="UPDATE tbdtable SET tbdContent='$inputTbdContent' WHERE  email='$email';";

		$res7=mysql_query($updateTbd)or die(mysql_error());

     //******************************************************************

    // start to store the hyperlink data

             $updateNewHyperLinks = array();

         	 $updateNewHyperLinks[] = $_REQUEST['website1'];
         	 $updateNewHyperLinks[] = $_REQUEST['website2'];
         	 $updateNewHyperLinks[] = $_REQUEST['website3'];
         	 $updateNewHyperLinks[] = $_REQUEST['website4'];
         	 $updateNewHyperLinks[] = $_REQUEST['website5'];


   echo "00000000000000".$updateNewHyperLinks." is ".count($updateNewHyperLinks);
    echo "<br/>";

    $updateNewHyperLinksInString = serialize($updateNewHyperLinks);
    echo $updateNewHyperLinksInString;

    $updateNewHyperLinksInString = mysql_real_escape_string($updateNewHyperLinksInString);

    $query6="UPDATE hyperlinktable SET hyperLinkContent='$updateNewHyperLinksInString' WHERE email='$email';";

	$res3 = mysql_query($query6) or die(mysql_error());


    // start to store the image
    //**************************************************************Check the numbers of images in the database


	$query8 = "SELECT imageID FROM imagetable WHERE email='$email'";
    $result8 = mysql_query($query8) or die(mysql_error());
    $result8 = mysql_num_rows($result8);

    //**********************************************************************Here start to handle the delete images

    if (isset( $_REQUEST['delete'] ) ) {
    	$deletedImagedArray = $_REQUEST['delete'];
	foreach ($deletedImagedArray as $deletedImageID ) {

		$deleteImageQuery= "DELETE FROM imagetable WHERE email='$email' AND imageID='$deletedImageID' ";
		$resultDeleteImage = mysql_query($deleteImageQuery) or die(mysql_error());
	}
}

    //****************************************************************

	$file = $_FILES['image']['tmp_name'];

	if (!isset ($file))
	{
	echo "Please select an image";
	}
    else if( !empty($_FILES['image']['tmp_name']))
    {

	$imageB = base64_encode(file_get_contents($_FILES['image']['tmp_name']));
	$image_size = getimagesize($_FILES['image']['tmp_name']);

	if($image_size==false)
    {
	echo "Thats not an image<br/>";
	}
    else if($result8>4)
    {
    	echo "Your maximum images are 4,now you try to store more than 4 images";
    }
	else if (  ( ($_FILES['image']["type"] == "image/gif")||($_FILES['image']["type"] == "image/jpeg" )  )&& ($result8<5 )     )

	{

    	$insert = mysql_query("INSERT INTO imagetable VALUES ('','$email','$imageB')") or die("Problem uploading image.");

	}

     else
     {
     	echo "it must be jpeg/gif images, and the maximum images are 4";
     }


	}

     header("location:notetomyself.php");

}


?>

