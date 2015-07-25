<?php

// mysqli
$mysqli = new mysqli("127.0.01", "root", "root", "test");
$result = $mysqli->query("SELECT * from col2");
while($row = $result->fetch_assoc()){
    echo 'a:'.$row['a']."\n";
    echo 'b:'.$row['b']."\n";
}

echo "\n";

// PDO
$pdo = new PDO('mysql:host=127.0.0.1;dbname=test', 'root', 'root');
$results_pdo = $pdo->query("SELECT b from col2");
foreach($results_pdo->FetchAll() as $eachResult) {
    echo 'b:'.$eachResult['b']."\n";
}

echo "\n";
//mysql

// mysql
$c = mysql_connect("127.0.0.1", "root", "root") 
        or die("Unable to connect to MySQL");
echo "Connected to MySQL<br>";
mysql_select_db("test", $c);
$result_mysql = mysql_query("SELECT * from col2");

while ($row = mysql_fetch_array($result_mysql)) {
   echo "_id:".$row{'_id'}." a: ".$row{'a'}." b: ". $row{'b'}."\n";
}
//close the connection
mysql_close($c);



 

