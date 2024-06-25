-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2024 at 08:17 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 7.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text DEFAULT NULL,
  `CREATE_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `img_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `title`, `content`, `CREATE_at`, `update_at`, `img_path`) VALUES
(1, 'Breakthrough in Quantum Computing: Scientists Achieve Room-Temperature Quantum Entanglement', 'In an unprecedented leap forward, researchers at the Quantum Computing Institute have successfully demonstrated room-temperature quantum entanglement. This groundbreaking achievement could revolutionize the field of quantum computing, potentially making current technologies obsolete.\r\n\r\nDr. Emily Carter, lead scientist on the project, stated, \"This discovery opens up new possibilities for practical quantum computers that can operate in everyday environments. Our findings will pave the way for more accessible and efficient quantum technologies.\"\r\n\r\nThe team\'s work focuses on using a novel type of qubit that remains stable at higher temperatures, unlike traditional qubits that require extremely cold environments. This advancement could significantly reduce the costs and complexity associated with quantum computing, bringing us closer to a future where quantum computers are a part of our daily lives.\r\n\r\nIn an unprecedented leap forward, researchers at the Quantum Computing Institute have successfully demonstrated room-temperature quantum entanglement. This groundbreaking achievement could revolutionize the field of quantum computing, potentially making current technologies obsolete.\r\n\r\nDr. Emily Carter, lead scientist on the project, stated, \"This discovery opens up new possibilities for practical quantum computers that can operate in everyday environments. Our findings will pave the way for more accessible and efficient quantum technologies.\"\r\n\r\nThe team\'s work focuses on using a novel type of qubit that remains stable at higher temperatures, unlike traditional qubits that require extremely cold environments. This advancement could significantly reduce the costs and complexity associated with quantum computing, bringing us closer to a future where quantum computers are a part of our daily lives.', '2024-06-25 06:16:49', '2024-06-25 06:16:49', '/static/uploads/new.png');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `password` varchar(250) NOT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `create_at`) VALUES
(25, 'mark', '$2b$12$/QVF5zvFAXsonjaQUrc6k.5hrLX4BUHLXMqVxRJDoGC2SRXn18BzW', '2024-06-25 06:01:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
