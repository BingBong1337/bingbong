-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 26 maj 2022 kl 17:02
-- Serverversion: 10.4.24-MariaDB
-- PHP-version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `databas`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `info`
--

CREATE TABLE `info` (
  `id` int(100) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `SureName` varchar(50) NOT NULL,
  `Age` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `info`
--

INSERT INTO `info` (`id`, `FirstName`, `SureName`, `Age`) VALUES
(18, 'Rufus', 'Hegardt', 19),
(19, 'Albin ', 'Alvelius', 19),
(23, 'Vicot', 'Forseman', 19);

-- --------------------------------------------------------

--
-- Tabellstruktur `signininfo`
--

CREATE TABLE `signininfo` (
  `id` int(100) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `signininfo`
--

INSERT INTO `signininfo` (`id`, `Username`, `Password`) VALUES
(0, 'Admin', 'Admin'),
(18, 'BruhMan', 'Password'),
(19, 'Albinzzz', '1234'),
(23, 'VicotMan64', 'Password');

-- --------------------------------------------------------

--
-- Tabellstruktur `travel`
--

CREATE TABLE `travel` (
  `id` int(100) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Time` varchar(20) NOT NULL,
  `FromCity` varchar(50) NOT NULL,
  `ToCity` varchar(50) NOT NULL,
  `Klass` varchar(20) NOT NULL,
  `Price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `info`
--
ALTER TABLE `info`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
