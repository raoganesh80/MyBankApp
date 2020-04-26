-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 26, 2020 at 04:56 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mybankapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `mba10001`
--

CREATE TABLE `mba10001` (
  `sr_no` int(11) NOT NULL,
  `transaction_id` varchar(20) NOT NULL,
  `transaction_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `transaction_with` varchar(40) DEFAULT 'self',
  `transaction_type` varchar(10) NOT NULL,
  `transaction_amt` double(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mba10001`
--

INSERT INTO `mba10001` (`sr_no`, `transaction_id`, `transaction_date`, `transaction_with`, `transaction_type`, `transaction_amt`) VALUES
(1, 'p66Ec9pY', '2020-04-26 04:51:11', 'self', 'credit', 10000.00),
(2, 'Tc8xAjtC', '2020-04-26 04:51:32', '10002/tejuu@gmail.com', 'debit', 2000.00),
(3, '0nkxC00qqK', '2020-04-26 04:53:34', 'self', 'debit', 5000.00),
(4, 'Q6xmTa3pgO', '2020-04-26 06:04:52', 'self', 'credit', 5000.00),
(5, 'Ye6263bhT0', '2020-04-26 06:08:07', 'self', 'debit', 100.00),
(6, 'aW5bhwJZ6e', '2020-04-26 06:08:21', 'self', 'debit', 100.00),
(7, 'tyqeLPT1ZK', '2020-04-26 06:08:30', 'self', 'debit', 100.00),
(8, 'HnDydSp33d', '2020-04-26 06:08:36', 'self', 'debit', 100.00),
(9, 'grIEYSMLpl', '2020-04-26 14:00:23', '10003/ravi@gmail.com', 'credit', 20000.00),
(10, 'bSIhDTB0Ch', '2020-04-26 14:32:31', '10004/parwati@gmail.com', 'credit', 2000.00);

-- --------------------------------------------------------

--
-- Table structure for table `mba10002`
--

CREATE TABLE `mba10002` (
  `sr_no` int(11) NOT NULL,
  `transaction_id` varchar(20) NOT NULL,
  `transaction_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `transaction_with` varchar(40) DEFAULT 'self',
  `transaction_type` varchar(10) NOT NULL,
  `transaction_amt` double(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mba10002`
--

INSERT INTO `mba10002` (`sr_no`, `transaction_id`, `transaction_date`, `transaction_with`, `transaction_type`, `transaction_amt`) VALUES
(1, 'Tc8xAjtC', '2020-04-26 04:51:32', '10001/raoganesh80@gmail.com', 'credit', 2000.00);

-- --------------------------------------------------------

--
-- Table structure for table `mba10003`
--

CREATE TABLE `mba10003` (
  `sr_no` int(11) NOT NULL,
  `transaction_id` varchar(20) NOT NULL,
  `transaction_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `transaction_with` varchar(40) DEFAULT 'self',
  `transaction_type` varchar(10) NOT NULL,
  `transaction_amt` double(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mba10003`
--

INSERT INTO `mba10003` (`sr_no`, `transaction_id`, `transaction_date`, `transaction_with`, `transaction_type`, `transaction_amt`) VALUES
(1, 'BDTnPaEbqz', '2020-04-26 13:59:38', 'self', 'credit', 50000.00),
(2, 'grIEYSMLpl', '2020-04-26 14:00:23', '10001/raoganesh80@gmail.com', 'debit', 20000.00);

-- --------------------------------------------------------

--
-- Table structure for table `mba10004`
--

CREATE TABLE `mba10004` (
  `sr_no` int(11) NOT NULL,
  `transaction_id` varchar(20) NOT NULL,
  `transaction_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `transaction_with` varchar(40) DEFAULT 'self',
  `transaction_type` varchar(10) NOT NULL,
  `transaction_amt` double(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mba10004`
--

INSERT INTO `mba10004` (`sr_no`, `transaction_id`, `transaction_date`, `transaction_with`, `transaction_type`, `transaction_amt`) VALUES
(1, 'FO8Zwsfp8Y', '2020-04-26 14:31:31', 'self', 'credit', 2000.00),
(2, 'bSIhDTB0Ch', '2020-04-26 14:32:31', '10001/raoganesh80@gmail.com', 'debit', 2000.00);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Acc_no` int(6) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `LastName` varchar(20) DEFAULT 'N/A',
  `Email` varchar(40) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Balance` int(10) NOT NULL DEFAULT 2000
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Acc_no`, `FirstName`, `LastName`, `Email`, `Password`, `Balance`) VALUES
(10001, 'Ganesh', 'Rao', 'raoganesh80@gmail.com', 'Grras@123', 31600),
(10002, 'G', 'Tejeshwari', 'tejuu@gmail.com', 'Teju@123', 4000),
(10003, 'Ravi', 'Kumar', 'ravi@gmail.com', 'Ravi@123', 32000),
(10004, 'Parwati', 'Rao', 'parwati@gmail.com', 'Parwati@123', 2000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mba10001`
--
ALTER TABLE `mba10001`
  ADD PRIMARY KEY (`sr_no`),
  ADD UNIQUE KEY `transaction_id` (`transaction_id`);

--
-- Indexes for table `mba10002`
--
ALTER TABLE `mba10002`
  ADD PRIMARY KEY (`sr_no`),
  ADD UNIQUE KEY `transaction_id` (`transaction_id`);

--
-- Indexes for table `mba10003`
--
ALTER TABLE `mba10003`
  ADD PRIMARY KEY (`sr_no`),
  ADD UNIQUE KEY `transaction_id` (`transaction_id`);

--
-- Indexes for table `mba10004`
--
ALTER TABLE `mba10004`
  ADD PRIMARY KEY (`sr_no`),
  ADD UNIQUE KEY `transaction_id` (`transaction_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Acc_no`),
  ADD UNIQUE KEY `Acc_no` (`Acc_no`,`Email`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mba10001`
--
ALTER TABLE `mba10001`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `mba10002`
--
ALTER TABLE `mba10002`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `mba10003`
--
ALTER TABLE `mba10003`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `mba10004`
--
ALTER TABLE `mba10004`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `Acc_no` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10005;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
