-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 07, 2020 at 04:35 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `lab`
--

-- --------------------------------------------------------

--
-- Table structure for table `lab_reg`
--

CREATE TABLE IF NOT EXISTS `lab_reg` (
  `labid` int(10) NOT NULL AUTO_INCREMENT,
  `labname` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `state` varchar(20) NOT NULL,
  `district` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pincode` varchar(20) NOT NULL,
  `contactnum` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`labid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `lab_reg`
--

INSERT INTO `lab_reg` (`labid`, `labname`, `address`, `state`, `district`, `place`, `pincode`, `contactnum`, `email`, `password`) VALUES
(1, 'ky', 'sadfg', 'asdcvfb', '', 'sadfg', '683517', '1234567', 'chinchu@gmail.com', '9078'),
(2, 'st', 'padan house\r\nchariyamthuruth', 'Kerala', 'ernakulam', 'CHARIYAMTHURUTH', '683517', '9447840422', 'kunju@gmail.com', '1234'),
(3, 'St.Antony', 'padan house\r\nchariyamthuruth', 'Kerala', '', 'CHARIYAMTHURUTH', '683517', '9447840422', 'aparnamicheal97@gmail.com', '1234'),
(5, 'kmk', 'abc building', 'kerala', '', '', '', '', '', ''),
(6, 'kmk', 'abc building', 'kerala', '', '', '', '', '', ''),
(7, 'kmk', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '123456'),
(8, 'kmk', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '123456'),
(9, 'ky', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '9078'),
(10, 'ky', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '9078'),
(11, 'St.Antony', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '1234'),
(12, 'St.Antony', '', '', '', '', '', '', '', ''),
(13, 'st', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '00000000000'),
(14, 'st', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '888888888'),
(15, 'abc', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'Nithinkrishnan87@gmail.com', '123456'),
(16, 'st', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'nithinkrishnan87@gmail.com', '0000000'),
(17, '', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'kunju@gmail.com', '1234'),
(18, 'xyz', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'apsaramicheal02@gmail.com', '123456'),
(19, 'st', 'padan house\r\nchariyamthuruth', 'Kerala', '', 'CHARIYAMTHURUTH', '683517', '9447840422', 'aparnamicheal97@gmail.com', '1234'),
(20, 'ky', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'kunju@gmail.com', '1111'),
(21, 'st', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', 'kunju@gmail.com', '9078'),
(22, 'St.Antony', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', 'aparnamicheal97@gmail.com', '');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`email`, `password`, `type`) VALUES
('admin@gmail.com', '1234', 'admin'),
('aparna@gmail.com', '9447', 'staff'),
('chinchu@gmail.com', '456', 'user'),
('chinchu@gmail.com', '9078', 'lab'),
('kunju@gmail.com', '1234', 'lab'),
('', '', 'lab'),
('', '', 'lab'),
('aparnamicheal97@gmai', '123456', 'lab'),
('aparnamicheal97@gmai', '123456', 'lab'),
('aparnamicheal97@gmai', '9078', 'lab'),
('aparnamicheal97@gmai', '9078', 'lab'),
('aparnamicheal97@gmai', '454', 'lab'),
('aparnamicheal97@gmai', '1234', 'lab'),
('aparnamicheal97@gmai', '1234', 'lab'),
('', '', 'lab'),
('aparnamicheal97@gmai', '00000000000', 'lab'),
('aparnamicheal97@gmai', '888888888', 'lab'),
('Nithinkrishnan87@gma', '123456', 'lab'),
('apsaramicheal02@gmai', '1111', 'staff'),
('apsaramicheal02@gmai', '000000', 'staff'),
('aparnamicheal97@gmai', '', 'staff'),
('Nithinkrishnan87@gma', '', 'staff'),
('aparnamicheal97@gmai', '', 'staff'),
('aparnamicheal97@gmai', '', 'staff'),
('nithinkrishnan87@gma', '0000000', 'lab'),
('kunju@gmail.com', '1234', 'lab'),
('kunju@gmail.com', '1234', 'staff'),
('apsaramicheal02@gmai', '0000', 'staff'),
('apsaramicheal02@gmai', '123456', 'lab'),
('aparnamicheal97@gmai', '0000', 'staff'),
('aparnamicheal97@gmai', '1234', 'staff'),
('aparnamicheal97@gmai', '1234', 'staff'),
('aparnamicheal97@gmai', '1234', 'lab'),
('kunju@gmail.com', '1111', 'lab'),
('aparnamicheal97@gmai', '1234', 'staff'),
('kunju@gmail.com', '1234', 'staff'),
('kunju@gmail.com', '9078', 'lab'),
('aparnamicheal97@gmai', '', 'lab');

-- --------------------------------------------------------

--
-- Table structure for table `new_test`
--

CREATE TABLE IF NOT EXISTS `new_test` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `rate` int(11) NOT NULL,
  PRIMARY KEY(`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `new_test`
--

INSERT INTO `new_test` (`category_id`, `category_name`, `type`, `rate`) VALUES
(1, 'None', 'rbc', 10),
(2, 'None', 'wbc', 50),
(3, 'None', 'rbc', 10),
(4, 'None', 'rbc', 10),
(5, 'None', 'rbc', 10);

-- --------------------------------------------------------

--
-- Table structure for table `staff_reg`
--

CREATE TABLE IF NOT EXISTS `staff_reg` (
  `staffid` int(10) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `state` varchar(20) NOT NULL,
  `district` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pincode` varchar(20) NOT NULL,
  `contactnum` varchar(50) NOT NULL,
  `alternatenum` varchar(50) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `staff_reg`
--

INSERT INTO `staff_reg` (`staffid`, `firstname`, `lastname`, `dob`, `gender`, `qualification`, `address`, `state`, `district`, `place`, `pincode`, `contactnum`, `alternatenum`, `email`, `password`) VALUES
(8, 'Apsara', 'michael', '2002-07-24', 'female', '', 'padan house\r\nchariyamthuruth\r\nvarapuzha p.o', 'Kerala', 'ernakulam', 'CHARIYAMTHURUTH', '683517', 'None', 'None', 'apsaramicheal02@gmai', '0000'),
(9, 'kavya', 'michael', '0000-00-00', 'female', '', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', '4523665', 'aparnamicheal97@gmai', '0000'),
(10, 'Apsara', 'michael', '2002-07-24', 'female', 'dmlt', 'padan house\r\nchariyamthuruth', 'Kerala', 'ernakulam', 'CHARIYAMTHURUTH', '683517', '12233', '4523665', 'aparnamicheal97@gmai', '1234'),
(11, 'Apsara', 'michael', '0000-00-00', 'None', '', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', '4523665', 'aparnamicheal97@gmai', '1234'),
(12, 'Apsara', 'michael', '0000-00-00', 'None', '', 'padan house\r\nchariyamthuruth', 'Kerala', '', '', '683517', '9447840422', '4523665', 'aparnamicheal97@gmai', '1234'),
(13, 'chinchu', 'michael', '0000-00-00', 'None', '', 'vaippusseri house\r\niddukki', 'Kerala', '', '', '683517', '9447840422', '', 'kunju@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `test_category`
--

CREATE TABLE IF NOT EXISTS `test_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(20) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `test_category`
--

INSERT INTO `test_category` (`category_id`, `category_name`) VALUES
(1, 'abc'),
(2, 'xyz'),
(4, 'prq'),
(5, 'red');

-- --------------------------------------------------------

--
-- Table structure for table `user_reg`
--

CREATE TABLE IF NOT EXISTS `user_reg` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL,
  `state` varchar(20) NOT NULL,
  `district` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pincode` varchar(20) NOT NULL,
  `contactnum` varchar(20) NOT NULL,
  `alternatenum` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_reg`
--

