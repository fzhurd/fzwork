<?php
//mongo

$dbhost = '127.0.0.1';
$dbname = 'test';
 
// Connect to test database
$m = new Mongo("mongodb://$dbhost");
$db = $m->$dbname;
 
// select the collection
$collection = $db->col1;
 
// pull a cursor query
$cursor = $collection->find();

foreach($cursor as $document) {
 //var_dump($document);
    echo $document['color']."\n";
}

 $db2 = $m->test2;
   echo "Database mydb selected";
   $collection2 = $db2->createCollection("col101");
   $document = array( 
      "title" => "MongoDB", 
      "description" => "database", 
      "likes" => 100,
      "url" => "http://www.tutorialspoint.com/mongodb/",
      "by", "tutorials point"
   );
   $collection2->insert($document);
   echo "Document inserted successfully";
   
// connect to mongodb
/*
   $m = new MongoClient();
   echo "Connection to database successfully";
   // select a database
   $db = $m->mydb;
   echo "Database mydb selected";
 * *
 */

//mysqli
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
