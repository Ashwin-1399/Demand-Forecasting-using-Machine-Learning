-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 31, 2020 at 11:17 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `demandforecasting`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone_num` varchar(12) NOT NULL,
  `message` varchar(50) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `message`, `date`) VALUES
(1, 'abhi', 'abhi99809@gmail.com', '7405660785', 'dfhjjhdhghh', '2020-10-30 08:51:52.574924');

-- --------------------------------------------------------

--
-- Table structure for table `forgetpassword`
--

CREATE TABLE `forgetpassword` (
  `id` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `token` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `forgetpassword`
--

INSERT INTO `forgetpassword` (`id`, `email`, `token`) VALUES
(1, 'taloleaakash@gmail.com', '8t5RZA'),
(2, 'tech.hiteshpawar@gmail.com', 'IsQhlw');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `rno` int(11) NOT NULL,
  `rname` varchar(20) NOT NULL,
  `remail` varchar(30) NOT NULL,
  `rpassword` varchar(15) NOT NULL,
  `rcpassword` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`rno`, `rname`, `remail`, `rpassword`, `rcpassword`) VALUES
(1, 'qqqqqq', 'qqqqq@h.in', '111111', '111111'),
(2, 'abhi', 'abhi@gmail.com', '123456', '123456'),
(3, 'ram', 'demoproject58@gmail.com', '123456', '123456'),
(4, 'aakash', 'taloleaakash@gmail.com', '123456', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `forgetpassword`
--
ALTER TABLE `forgetpassword`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`rno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `forgetpassword`
--
ALTER TABLE `forgetpassword`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `rno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
