<?php

require_once 'PHPUnit/Autoload.php';
//function __autoload($class) {include_once("../main/".$class.".php");}

class SonarSqlTest extends PHPUnit_Framework_TestCase
{
  public function setUp()
  { 
      $createdCollection = $this->setUpMongo('127.0.0.1',27017, 'test3','test_php1');
      //$pdo=$this->setUpSonarSqlPDO('mysql:host=127.0.0.1;dbname=test', 'root', 'root');
      
  }
  
  public function tearDown()
  { 
      
  }

  public function arrays_are_similar($a, $b) {
  // if the indexes don't match, return immediately
    echo count(array_diff_assoc($a, $b));
    echo '$$$$$$$$$$$$$$$$$';
  if (count(array_diff_assoc($a, $b))) {
    return false;
  }
  // we know that the indexes, but maybe not values, match.
  // compare the values between the two arrays
  foreach($a as $k => $v) {
    if ($v !== $b[$k]) {
      return false;
    }
  }
  // we have identical indexes, and no unequal values
  return true;
}

  public function setUpMongo($dbhost, $port, $dbname,$collection)
  {
        
        $m = new Mongo("mongodb://$dbhost:$port");
        $db = $m->$dbname;
        
  
        $db->dropCollection($collection);
        $createdCollection = $db->createCollection($collection);
        
        $document1 = array("_id" => 1, "a" => "blue", "b" => 10);
        $document2 = array("_id" => 2, "a" => "black", "b" => 20);
        
        $createdCollection->insert($document1);
        $createdCollection->insert($document2);
        
        return $createdCollection;
                
 
  }
  
  public function setUpPDO($dbhost, $db, $user, $passwd)
  {
      $pdo = new PDO("mysql:host=$dbhost;dbname=$db", $user, $passwd);
      return $pdo;
  }
  
  public function setUpMysqli($dbhost,  $user, $passwd, $db)
  {
       $mysqli = new mysqli($dbhost, $user, $passwd, $db);
       return $mysqli;

  }
  
  public function setUpMySqlConnector($dbhost, $user, $passwd)
   {
      
      $mysql_connector = mysql_connect($dbhost, $user, $passwd);
      return $mysql_connector;
      
  }
 
  public function testPDO()
  {
      $expectedResults = array( );

      $expectedResults[0]=array('a' => 'orange', 'b' => 2);
      $expectedResults[1]=array('a' => 'strawberry','b' => 5);
      
      $pdo=$this->setUpPDO('127.0.0.1','test3', 'test', 'test');
      
   
      $results_pdo = $pdo->query("SELECT a, b from test_php_mysql");

     // echo gettype($results_pdo)."\n";
      //echo gettype($results_pdo->fetchAll(PDO::FETCH_ASSOC))."\n";

      $results = $results_pdo->fetchAll(PDO::FETCH_ASSOC);
      //var_dump($results);
      //print_r($results);
    
      $this->assertTrue($results==$expectedResults);
       
  }
  
  public function testMysqli(){

      $expectedResults = array( );

      $expectedResults[0]=array('a' => 'orange', 'b' => 2);
      $expectedResults[1]=array('a' => 'strawberry','b' => 5);
      
    
      $mysqli = $this->setUpMysqli('127.0.0.1','test', 'test', 'test3');
      $resultsMysqli = $mysqli->query("SELECT a, b from test_php_mysql");
 
      
      while($row = $resultsMysqli->fetch_assoc())
      {
        $results[]=$row; 
      }

      $this->assertTrue($results==$expectedResults);
     
  }
  
  public function testMysqlConnector(){
      $mysql_connector = $this->setUpMySqlConnector("127.0.0.1", "test", "test");
      mysql_select_db("test3", $mysql_connector);
$result_mysql = mysql_query("SELECT a, b from test_php_mysql");


while ($row = mysql_fetch_array($result_mysql)) {
   echo " a: ".$row{'a'}." b: ". $row{'b'}."\n";
}
 echo "avoce is testMysqlConnector";
//close the connection
mysql_close($mysql_connector);
  }

}
