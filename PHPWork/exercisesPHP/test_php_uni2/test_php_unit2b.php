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
  
  public function setUpMySqlConnector(){
      
  }
  
  
  public function testIsMyString()
  {
        $string = "Mostly Harmless";
        $this->assertGreaterThan(0,strlen($string));
  }

  public function testBigNumber()
  {
        $num = 20;
        $this->assertGreaterThan($num, 21);
  }
  
  public function testPDO()
  {
      try{
      $pdo=$this->setUpPDO('127.0.0.1','test3', 'test', 'test');
      }
      catch (Exception $e)
      {
          echo $e;
      }
   
      $results_pdo = $pdo->query("SELECT a, b from test_php_mysql");
      
      echo var_dump($results_pdo);
      
 
    
foreach($results_pdo->fetchAll(PDO::FETCH_ASSOC) as $eachResult) {
   echo 'b:'.$eachResult['b']."\n";
}
     
       
  }
  
  public function testMysqli(){
      
      //$mysqli = new mysqli('127.0.0.1','test', 'test', 'test3');
      $mysqli = $this->setUpMysqli('127.0.0.1','test', 'test', 'test3');
      
      $result = $mysqli->query("SELECT a, b from test_php_mysql");
    while($row = $result->fetch_assoc()){
    echo 'a:'.$row['a']."\n";
    echo 'b:'.$row['b']."\n";
}
     
  }

}
