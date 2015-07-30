<?php

require_once('RemoteConnect.php');
//require_once ('PHPUnit/Framework/TestCase.php');
require_once 'PHPUnit/Autoload.php';

class RemoteConnectTest extends PHPUnit_Framework_TestCase
{
  public function setUp(){ }
  public function tearDown(){ }
/*
  public function testConnectionIsValid()
  {
    // test to ensure that the object from an fsockopen is valid
    $connObj = new RemoteConnect();
    $serverName = 'www.google.com';
    $this->assertTrue($connObj->connectToServer($serverName) !== false);
  }
  
  
  function testIsRightObject() {
    $connObj = new RemoteConnect();
    $returnedObject = $connObj->returnSampleObject();
    $this->assertType('remoteConnect', $returnedObject);
    }
*/

public function testIsMyString(){
  $string = "Mostly Harmless";
  $this->assertGreaterThan(0,strlen($string));
  $this->assertContains("42",$string);
}
}
