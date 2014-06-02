-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 12, 2012 at 07:24 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `notetomyself`
--

-- --------------------------------------------------------

--
-- Table structure for table `hyperlinktable`
--

CREATE TABLE IF NOT EXISTS `hyperlinktable` (
  `hyperLinkID` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `hyperLinkContent` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`hyperLinkID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `hyperlinktable`
--


-- --------------------------------------------------------

--
-- Table structure for table `imagetable`
--

CREATE TABLE IF NOT EXISTS `imagetable` (
  `imageID` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `imageContent` mediumblob,
  PRIMARY KEY (`imageID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `imagetable`
--


-- --------------------------------------------------------

--
-- Table structure for table `notestable`
--

CREATE TABLE IF NOT EXISTS `notestable` (
  `notesID` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `notesContent` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notesID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `notestable`
--


-- --------------------------------------------------------

--
-- Table structure for table `tbdtable`
--

CREATE TABLE IF NOT EXISTS `tbdtable` (
  `tbdID` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `tbdContent` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`tbdID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tbdtable`
--


-- --------------------------------------------------------

--
-- Table structure for table `userinformation`
--

CREATE TABLE IF NOT EXISTS `userinformation` (
  `userID` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password1` varchar(40) NOT NULL,
  `password2` varchar(40) NOT NULL,
  `numberofvisits` int(10) NOT NULL,
  `hash` varchar(32) NOT NULL,
  `active` int(1) NOT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `userinformation`
--

