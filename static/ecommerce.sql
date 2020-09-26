-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 25, 2020 at 08:48 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smart_bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`company_id`, `company_name`, `address`) VALUES
(1, 'Jatri', 'Missouri'),
(2, 'Edgeify', 'South Dakota'),
(3, 'Pixope', 'Texas'),
(4, 'Oyonder', 'Texas'),
(5, 'Gabcube', 'Alabama'),
(6, 'Yodel', 'Washington'),
(7, 'Avamm', 'Virginia'),
(8, 'Skyndu', 'Indiana'),
(9, 'Realblab', 'Georgia'),
(10, 'Trudeo', 'District of Columbia'),
(11, 'Myworks', 'District of Columbia'),
(12, 'Divanoodle', 'Georgia'),
(13, 'Bluejam', 'Florida'),
(14, 'Topicstorm', 'Pennsylvania'),
(15, 'Nlounge', 'Texas'),
(16, 'Edgeclub', 'Virginia'),
(17, 'Tagchat', 'North Carolina'),
(18, 'Realblab', 'North Carolina'),
(19, 'Yakitri', 'Michigan'),
(20, 'Devpulse', 'New York'),
(21, 'Zava', 'Ohio'),
(22, 'Jabbercube', 'California'),
(23, 'Twiyo', 'Florida'),
(24, 'Bubbletube', 'District of Columbia'),
(25, 'Skidoo', 'New York');

-- --------------------------------------------------------

--
-- Table structure for table `company_product`
--

CREATE TABLE `company_product` (
  `company_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company_product`
--

INSERT INTO `company_product` (`company_id`, `product_id`) VALUES
(1, 16),
(2, 21),
(4, 10),
(4, 21),
(5, 2),
(9, 21),
(13, 5),
(13, 10),
(17, 12),
(24, 19),
(25, 3),
(25, 16);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `mobile` int(10) NOT NULL,
  `mail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `mobile`, `mail`) VALUES
(1, 'Jerrilyn', 2147483647, 'jdentith0@blogs.com'),
(2, 'Lu', 2147483647, 'lwylie1@e-recht24.de'),
(3, 'Tim', 2147483647, 'tmilstead2@4shared.com'),
(4, 'Kathrine', 2147483647, 'kbenoit3@free.fr'),
(5, 'Horatio', 1994087447, 'hkemme4@google.ca'),
(6, 'Durant', 351253394, 'dchamp5@wired.com'),
(7, 'Shina', 2147483647, 'smingo6@va.gov'),
(8, 'Granville', 2123362611, 'gvanbruggen7@homestead.com'),
(9, 'Gene', 2147483647, 'gocoskerry8@skyrock.com'),
(10, 'Anica', 2147483647, 'aobeirne9@uol.com.br'),
(11, 'Oona', 536063478, 'oguya@wisc.edu'),
(12, 'Bail', 228982839, 'bolliarb@utexas.edu'),
(13, 'Ned', 2147483647, 'nfrankumc@dell.com'),
(14, 'Erek', 2147483647, 'ekilfeatherd@usda.gov'),
(15, 'Maxie', 2147483647, 'mcremine@lycos.com'),
(16, 'Idell', 2147483647, 'iriglesfordf@flickr.com'),
(17, 'Leyla', 2147483647, 'lseelg@tmall.com'),
(18, 'Loni', 2147483647, 'lsoamesh@qq.com'),
(19, 'Albrecht', 2147483647, 'aaumerlei@msn.com'),
(20, 'Justinn', 2147483647, 'jsprayj@studiopress.com'),
(21, 'Malory', 2147483647, 'mbrandlik@addthis.com'),
(22, 'Vitia', 2147483647, 'vrosenblooml@gov.uk'),
(23, 'Catherin', 2147483647, 'csalem@ucsd.edu'),
(24, 'Stevena', 2147483647, 'smullingern@123-reg.co.uk'),
(25, 'Hussein', 2147483647, 'hfillano@utexas.edu'),
(1083, 'Gray', 2147483647, 'gclemits3@ezinearticles.com'),
(1232, 'Lauritz', 2147483647, 'lmcmenemy5@homestead.com'),
(1507, 'Hewie', 2147483647, 'hwhatsize1@taobao.com'),
(1686, 'Christoforo', 2147483647, 'cmulcaster7@ihg.com'),
(1698, 'Sherlocke', 2147483647, 'soloshkin0@microsoft.com'),
(1874, 'Albie', 2147483647, 'aeasterbrook6@indiatimes.com'),
(1881, 'Mike', 2147483647, 'mmarshfield2@opensource.org'),
(1896, 'Kelci', 1942746458, 'kvondrys4@yahoo.com');

-- --------------------------------------------------------

--
-- Table structure for table `customer_product`
--

CREATE TABLE `customer_product` (
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_product`
--

INSERT INTO `customer_product` (`customer_id`, `product_id`) VALUES
(1, 6),
(6, 7),
(8, 3),
(9, 6),
(10, 13),
(14, 19),
(17, 6),
(19, 21),
(22, 17),
(23, 10),
(23, 16);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `user_rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `category`, `company`, `price`, `user_rating`) VALUES
(1, 'Toyota', 'Industrial', 'Yotz', 50604, 2.3),
(2, 'Dodge', 'Computers', 'Digitube', 38475, 0.3),
(3, 'Oldsmobile', 'Automotive', 'Fivespan', 27611, 1.3),
(4, 'BMW', 'Shoes', 'Devcast', 12741, 4.3),
(5, 'Buick', 'Tools', 'Divape', 24822, 3.2),
(6, 'Pontiac', 'Grocery', 'Edgewire', 50061, 0.2),
(7, 'Toyota', 'Jewelery', 'Geba', 33496, 2.9),
(8, 'Lexus', 'Industrial', 'Blogtag', 39865, 2.2),
(9, 'Chevrolet', 'Sports', 'Jabberstorm', 36149, 0.2),
(10, 'Mazda', 'Kids', 'Mydo', 34451, 0.3),
(11, 'Toyota', 'Movies', 'Linkbuzz', 21188, 1.8),
(12, 'Chrysler', 'Games', 'Photofeed', 58663, 2.5),
(13, 'Mercury', 'Movies', 'Edgewire', 51932, 0.4),
(14, 'Pontiac', 'Home', 'Chatterpoint', 50164, 0.2),
(15, 'Jeep', 'Outdoors', 'Dabfeed', 31953, 3.6),
(16, 'Nissan', 'Games', 'Skinder', 19019, 1.6),
(17, 'Volkswagen', 'Computers', 'Mita', 58414, 0.3),
(18, 'Chevrolet', 'Grocery', 'Edgewire', 58500, 0.8),
(19, 'Ford', 'Kids', 'Viva', 20298, 0.7),
(20, 'Toyota', 'Toys', 'Avamm', 22420, 3.4),
(21, 'Mazda', 'Health', 'Livetube', 49175, 1.1),
(22, 'Cadillac', 'Toys', 'Jaxworks', 6686, 2.7),
(23, 'Lexus', 'Kids', 'Brainverse', 58428, 1.8),
(24, 'Bentley', 'Sports', 'Kanoodle', 25902, 1.9),
(25, 'Isuzu', 'Industrial', 'Quaxo', 30022, 4.8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`company_id`);

--
-- Indexes for table `company_product`
--
ALTER TABLE `company_product`
  ADD PRIMARY KEY (`company_id`,`product_id`),
  ADD KEY `company_product_ibfk_2` (`product_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `customer_product`
--
ALTER TABLE `customer_product`
  ADD PRIMARY KEY (`customer_id`,`product_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `company_product`
--
ALTER TABLE `company_product`
  ADD CONSTRAINT `company_product_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `company_product_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `customer_product`
--
ALTER TABLE `customer_product`
  ADD CONSTRAINT `customer_product_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `customer_product_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
