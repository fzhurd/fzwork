
<?php

  require_once('constant.php');
  ob_start();
  session_start();

	// connect the database, here the database is established in my labtop local database, the user is 'root' and NO password is set, probably
	// it is unsafe

	$cid = mysql_connect("mysql1.000webhost.com", "a8251972_note","tat999") or die(mysql_error());
	mysql_select_db("a8251972_note") or die(mysql_error());
//	***************************************************************************// preventing visit the page before logging in

		if (!isset($_COOKIE['loggedin'])) {

			echo "You are not loggedin, register firstly";
			header("location: registerpage.php");


		}
	//**********************************************************************check inactive time
	sessionX();

	//***********************************************************************************************


//**********************************************************************************************
	 $email = $_SESSION['username'];

 	//**********************************************************************image printout
 		$query18 = mysql_query("SELECT * FROM imagetable WHERE email = '$email'");

 	//*************************************************************************

 	    $query4 = "SELECT notesContent FROM notestable WHERE email='$email'";
    	$result4 = mysql_query($query4) or die(mysql_error());


  		$currentNotesContent = array();  //this is an array

 	 while($record=mysql_fetch_row($result4))
 	{
	foreach($record as $field)
	{
		 $currentNotesContent = $field;

	}
	 }

   //here start the tbd
	$query5 = "SELECT tbdContent FROM tbdtable WHERE email='$email'";
    $result5 = mysql_query($query5) or die(mysql_error());


   $currentTbdContent = array();  //this is an array

	while($record=mysql_fetch_row($result5))
	{
	foreach($record as $field)
	{
		$currentTbdContent = $field;

	}
	}

   // here start the hyperlink
   $query6 = "SELECT hyperLinkContent FROM hyperlinktable WHERE email='$email'";  //hyperLinkContent is serilized string
   $result6 = mysql_query($query6) or die(mysql_error());

	$currentHyperLinksInString = '';  //this is an array

	while($record=mysql_fetch_row($result6))
   {
	   foreach($record as $field)
	{
		$currentHyperLinksInString = $field;

	}
   }

	$websites = unserialize($currentHyperLinksInString);  //The string is unserilized into array again, every element means one url

    //here start the images
	$query8 = "SELECT imageContent FROM imagetable WHERE email='$email'";  //hyperLinkContent is serilized string
	$result8 = mysql_query($query8) or die(mysql_error());

	$query9 = "SELECT imageContent from imagetable where email='$email'";
	$rs = mysql_fetch_array(mysql_query($query9));


  ?>



<html>
		<head>
			<title>Note-to-myself : notes</title>
					<link rel="shortcut icon" href="pencil.ico" />
	<script type="text/javascript">
			function openInNew(textbox){
			window.open("http://"+textbox.value);
			this.blur();
	}
			</script>
         <?php
         $query88 = "SELECT imageID FROM imagetable WHERE email='$email'";
         $result87 = mysql_query($query88) or die(mysql_error());
         $result88 = mysql_num_rows($result87);
         $number =$result88-1;
         echo "You have ".$number." images and it must be jpeg or gif";

            ?>
         <br />

					<link href="mainpage.css" rel="stylesheet" type="text/css" media="screen" />


			</head>
<body>

<div id="wrapper">
<form action="processmainpage.php" enctype="multipart/form-data" method="post">
    <h2 id="header"> <?php echo $_SESSION['username']; ?> - <span><a href="logout.php">Log out</a></span></h2>


    <div id="section1">

        <div id="column1">
			<h2>notes</h2>
           <textarea cols="16" rows="40" id="notes" name="notes" /><?php echo $currentNotesContent; ?></textarea>
        </div>

        <div id="column2">
			<h2>websites</h2><h3>click to open</h3>

			<input type='text' name='website1' value='<?php echo $websites[0]; ?>' onclick='openInNew(this);' /><br >
            <input type="text" name="website2" value='<?php echo $websites[1]; ?>'onclick='openInNew(this);' /><br >
            <input type="text" name="website3" value='<?php echo $websites[2]; ?>'onclick='openInNew(this);' /><br >
            <input type="text" name="website4" value='<?php echo $websites[3]; ?>' onclick='openInNew(this);' /><br >
            <input type="text" name="website5" value='<?php echo $websites[4]; ?>'  onclick='openInNew(this);' /><br >
         <!--       \"<a href=\". \"$websites[1]\" .'>'.'$websites[1]'.'</a>'                     -->
        </div>

    </div>

    <div id="section2">

        <div id="column3">
		   <h2>images</h2><h3>click for full size</h3>
          <!-- <textarea cols="16" rows="40" id="image" name="image" /></textarea> -->

			<!--		<input type="file" name="image" id='image' />  <img name = "img" src="loopimages.php" />	<br /> -->
		<!--	<input type="file" name="image" id='image' />  <?php echo "<img src=\"loop.php\" />" ?>	<br /> -->


     	<input type="file" name="image" id='image' />

		<!--		<?php echo "<a href=\"loopimages.php\">Show Image</a>"  ?> <br /> -->
		<!--   ---------------------------------------------------------------------------------------------------  -->

		<!--  Display the images   -->


		<?php
		while($row18=mysql_fetch_object($query18)){

            if($row18->imageContent!=null)
            {


		    echo "<a href=\"get.php?imageID=".$row18->imageID."\" \">";
			echo "<img src=\"get.php?imageID=".$row18->imageID."\" width='200' height='150' />";

		    echo " </a>";

		//	echo "<input type='checkbox' name='delete[]' value='261' />";
			echo "<input type='checkbox' name='delete[]' value=$row18->imageID  />";
			echo  "<label for='delete[]'>".'delete'."</label>";
			echo "<br />";
			echo "<br />";

            }
			else
			{
				$deleteNonFirstImage =  "DELETE FROM imagetable WHERE email='$email' AND imageContent IS NULL";
				$resultDeleteNonFirstImage = mysql_query($deleteNonFirstImage) or die(mysql_error());
			}


		}
		?>


<!-- --------------------------------------------------------------------

      <a href =" " >
		<?php
		while($row18=mysql_fetch_object($query18)){

		 	echo "<img src=\"get.php?imageID=".$row18->imageID."\" width='200' height='150' />";

		}
		?>
      </a>

  -------------------------------------------------------------------------   -->

				 <br />

					<div>


					</div>


        </div>

        <div id="column4">
			<h2>tbd</h2>
           <textarea cols="16" rows="40" id="tbd" name="tbd" /><?php echo $currentTbdContent; ?></textarea>
        </div>

    </div>

    <div id="footer">
      <input type="submit" value="Save" name="submitting" />
    </div>

</div>

</body>
</html>