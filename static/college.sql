-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 25, 2020 at 09:11 PM
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
-- Database: `university`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL,
  `name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`dept_id`, `name`) VALUES
(1, 'comps'),
(2, 'etrx'),
(3, 'extc'),
(4, 'it'),
(5, 'mech');

-- --------------------------------------------------------

--
-- Table structure for table `enrolls`
--

CREATE TABLE `enrolls` (
  `roll_no` varchar(15) NOT NULL,
  `sub_id` varchar(10) NOT NULL,
  `marks` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `enrolls`
--

INSERT INTO `enrolls` (`roll_no`, `sub_id`, `marks`) VALUES
('10', '4', 57),
('13', '17', 34),
('15', '8', 73),
('16', '15', 43),
('17', '11', 83),
('2', '15', 60),
('20', '13', 54),
('21', '16', 39),
('5', '10', 70),
('7', '19', 67);

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `name` varchar(20) NOT NULL,
  `fac_id` varchar(10) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `year_of_join` varchar(4) NOT NULL,
  `post` varchar(20) NOT NULL,
  `dept_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`name`, `fac_id`, `qualification`, `year_of_join`, `post`, `dept_id`) VALUES
('Alex', '1', 'Business Development', '1986', 'Structural Analysis ', 2),
('Gay', '10', 'Accounting', '2009', 'Accountant IV', 2),
('Rosalyn', '11', 'Research and Develop', '2011', 'Office Assistant I', 1),
('BDA', '111', 'Python', '2018', 'Teacher', 1),
('Germayne', '12', 'Accounting', '1998', 'Senior Quality Engin', 2),
('Odey', '13', 'Accounting', '1992', 'Engineer II', 2),
('Stavro', '14', 'Legal', '1996', 'Chemical Engineer', 2),
('Cinda', '15', 'Legal', '2008', 'Chemical Engineer', 2),
('Ryann', '16', 'Support', '1987', 'Statistician I', 1),
('Analiese', '17', 'Engineering', '2001', 'Chemical Engineer', 2),
('Brok', '18', 'Accounting', '2002', 'Professor', 2),
('Wald', '19', 'Human Resources', '1989', 'Business Systems Dev', 1),
('Diannne', '2', 'Support', '1998', 'Engineer II', 2),
('Arlina', '20', 'Training', '2009', 'Analog Circuit Desig', 1),
('Car', '21', 'Engineering', '2012', 'Financial Advisor', 2),
('Garek', '22', 'Legal', '2011', 'Chief Design Enginee', 1),
('Efren', '23', 'Human Resources', '1984', 'Sales Representative', 2),
('Delbert', '24', 'Human Resources', '1996', 'Director of Sales', 1),
('Clo', '25', 'Accounting', '1985', 'Administrative Assis', 1),
('Genvieve', '3', 'Accounting', '2004', 'Cost Accountant', 2),
('Esdras', '4', 'Human Resources', '2003', 'Paralegal', 1),
('Town', '5', 'Product Management', '1999', 'Junior Executive', 2),
('Rosita', '6', 'Training', '1992', 'Graphic Designer', 1),
('Sibel', '7', 'Legal', '1997', 'Programmer III', 1),
('Reeba', '8', 'Marketing', '1995', 'Systems Administrato', 2),
('Shanie', '9', 'Human Resources', '1993', 'General Manager', 2);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `name` varchar(20) NOT NULL,
  `address` varchar(40) NOT NULL,
  `roll_no` varchar(15) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `email_id` varchar(20) NOT NULL,
  `sem` int(11) NOT NULL,
  `year_of_admission` varchar(4) NOT NULL,
  `dept_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`name`, `address`, `roll_no`, `age`, `gender`, `email_id`, `sem`, `year_of_admission`, `dept_id`) VALUES
('Lucius', '12850 Claremont Park', '1', 18, 'M', 'lvicarey0@oaic.gov.a', 4, '2008', 3),
('Hamil', '4 Mariners Cove Way', '10', 30, 'M', 'hphethean9@economist', 1, '1995', 3),
('Moyra', '06481 Kennedy Hill', '11', 16, 'F', 'mhancilla@unicef.org', 7, '2012', 4),
('Shayne', '2 Blaine Place', '12', 24, 'M', 'sosoriob@studiopress', 6, '2001', 4),
('Glen', '679 Magdeline Center', '13', 25, 'F', 'gdunrigec@goo.gl', 3, '2010', 4),
('Scarface', '289 Macpherson Place', '14', 22, 'M', 'sjaffrad@harvard.edu', 2, '2005', 2),
('Haleigh', '2 Carey Junction', '15', 24, 'F', 'hringere@cpanel.net', 6, '1995', 2),
('Florence', '193 Debra Avenue', '16', 19, 'F', 'fdovingtonf@economis', 1, '1989', 2),
('Hurley', '6529 Clyde Gallagher Lane', '17', 25, 'M', 'hhumpageg@behance.ne', 6, '1996', 3),
('Harsh', '123,MD Road,Ghatkopar', '1711007', 20, 'M', 'harsh@somaiya.edu', 7, '2017', 1),
('Tedd', '51029 Washington Crossing', '18', 16, 'M', 'tsaffellh@google.co.', 8, '2013', 5),
('Dougie', '1 North Road', '19', 16, 'M', 'dstollei@skype.com', 1, '2007', 1),
('Kordula', '4835 Annamark Trail', '2', 19, 'F', 'kpeel1@cnn.com', 1, '1994', 4),
('Kathleen', '2 Kenwood Court', '20', 24, 'F', 'kwindrossj@epa.gov', 4, '1999', 4),
('Lannie', '537 Tomscot Street', '21', 25, 'M', 'lrowthornek@ifeng.co', 1, '2001', 1),
('Evyn', '804 Heath Drive', '22', 27, 'M', 'elabuschl@dailymotio', 5, '2007', 2),
('Sunny', '31 Ridgeway Plaza', '23', 18, 'F', 'sstainsonm@yale.edu', 4, '2007', 2),
('Conrade', '5 Anhalt Place', '24', 15, 'M', 'chatton@prweb.com', 4, '1988', 2),
('Theobald', '72 Butterfield Hill', '25', 15, 'M', 'tgrigolono@webeden.c', 8, '1990', 5),
('Skelly', '00 Doe Crossing Way', '3', 25, 'M', 'sklesl2@statcounter.', 6, '1995', 3),
('Wayne', '2906 Crest Line Way', '4', 26, 'M', 'wfrotton3@washington', 7, '1999', 4),
('Chlo', '27 Springs Crossing', '5', 21, 'F', 'cmaccartney4@meetup.', 4, '1988', 5),
('Brewster', '63 Glacier Hill Circle', '6', 21, 'M', 'burvoy5@paypal.com', 7, '1993', 1),
('Marijn', '0962 Sachtjen Street', '7', 26, 'M', 'mfurminger6@noaa.gov', 7, '2009', 5),
('Catrina', '91 Del Sol Drive', '8', 25, 'F', 'ctrounce7@globo.com', 6, '2002', 5),
('Yancy', '4 Rigney Trail', '9', 30, 'M', 'ybatrim8@ihg.com', 1, '2010', 2);

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `sub_id` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  `sem` int(11) NOT NULL,
  `dept_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`sub_id`, `name`, `description`, `sem`, `dept_id`) VALUES
('1', 'Business Development', 'Open-source neutral utilisation', 2, 5),
('10', 'Training', 'Synergized bifurcated internet solution', 6, 3),
('11', 'Marketing', 'Robust fresh-thinking alliance', 8, 3),
('12', 'Product Management', 'Multi-lateral 24 hour throughput', 2, 1),
('13', 'Human Resources', 'Multi-layered interactive secured line', 3, 5),
('14', 'Engineering', 'Triple-buffered zero tolerance hub', 1, 4),
('15', 'Engineering', 'Fully-configurable grid-enabled attitude', 5, 4),
('16', 'Business Development', 'Robust heuristic algorithm', 1, 4),
('17', 'Services', 'Automated foreground product', 3, 1),
('18', 'Legal', 'Enterprise-wide executive info-mediaries', 8, 5),
('19', 'Business Development', 'Multi-channelled user-facing middleware', 5, 4),
('2', 'Accounting', 'Optional 3rd generation emulation', 4, 2),
('20', 'Accounting', 'Switchable user-facing framework', 8, 5),
('21', 'Human Resources', 'Self-enabling multi-state definition', 1, 1),
('22', 'Legal', 'Seamless foreground product', 1, 1),
('23', 'Services', 'Up-sized attitude-oriented knowledge base', 3, 3),
('24', 'Support', 'Face to face bifurcated benchmark', 1, 1),
('25', 'Legal', 'Digitized grid-enabled customer loyalty', 4, 4),
('3', 'Accounting', 'Persistent actuating interface', 2, 5),
('4', 'Sales', 'Enhanced stable alliance', 3, 4),
('5', 'Sales', 'Customizable asynchronous capability', 6, 2),
('6', 'Legal', 'Re-engineered fresh-thinking superstructure', 7, 5),
('7', 'Marketing', 'Sharable clear-thinking focus group', 8, 1),
('8', 'Training', 'Quality-focused fault-tolerant parallelism', 1, 1),
('9', 'Engineering', 'Extended static installation', 5, 4);

-- --------------------------------------------------------

--
-- Table structure for table `teaches`
--

CREATE TABLE `teaches` (
  `fac_id` varchar(10) NOT NULL,
  `sub_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teaches`
--

INSERT INTO `teaches` (`fac_id`, `sub_id`) VALUES
('10', '10'),
('11', '10'),
('111', '4'),
('12', '14'),
('15', '9'),
('18', '21'),
('18', '3'),
('25', '19'),
('3', '15');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dept_id`);

--
-- Indexes for table `enrolls`
--
ALTER TABLE `enrolls`
  ADD PRIMARY KEY (`roll_no`,`sub_id`),
  ADD KEY `enrolls_subjects` (`sub_id`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`fac_id`),
  ADD KEY `faculty_dept` (`dept_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`roll_no`),
  ADD KEY `student_dept` (`dept_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`sub_id`),
  ADD KEY `subjects_dept` (`dept_id`);

--
-- Indexes for table `teaches`
--
ALTER TABLE `teaches`
  ADD PRIMARY KEY (`fac_id`,`sub_id`),
  ADD KEY `teaches_subjects` (`sub_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `enrolls`
--
ALTER TABLE `enrolls`
  ADD CONSTRAINT `enrolls_student` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `enrolls_subjects` FOREIGN KEY (`sub_id`) REFERENCES `subjects` (`sub_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `faculty`
--
ALTER TABLE `faculty`
  ADD CONSTRAINT `faculty_dept` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_dept` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subjects`
--
ALTER TABLE `subjects`
  ADD CONSTRAINT `subjects_dept` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `teaches`
--
ALTER TABLE `teaches`
  ADD CONSTRAINT `teaches_faculty` FOREIGN KEY (`fac_id`) REFERENCES `faculty` (`fac_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `teaches_subjects` FOREIGN KEY (`sub_id`) REFERENCES `subjects` (`sub_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
