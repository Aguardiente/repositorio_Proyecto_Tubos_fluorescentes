-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-02-2019 a las 04:03:14
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_fluorescentes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marca`
--

CREATE TABLE `marca` (
  `id_marca` int(11) NOT NULL,
  `nombre_marca` varchar(500) NOT NULL,
  `modelo_marca` varchar(500) NOT NULL,
  `industria_marca` varchar(500) NOT NULL,
  `cantidad_marca` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marca_prueba`
--

CREATE TABLE `marca_prueba` (
  `id_marca` int(11) NOT NULL,
  `nombre_marca` varchar(50) NOT NULL,
  `cantidad_marca` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `marca_prueba`
--

INSERT INTO `marca_prueba` (`id_marca`, `nombre_marca`, `cantidad_marca`) VALUES
(1, 'CD & P', 25),
(2, 'CHIYODA', 0),
(3, 'D&P', 0),
(4, 'EMAJHONNS.S.R.L', 1),
(5, 'GENERAL ELECTRIC', 1),
(6, 'IDEA CE', 0),
(7, 'LANCER', 0),
(8, 'LEELITE', 0),
(9, 'LTD', 0),
(10, 'LUZ ANDINO CHILE', 0),
(11, 'NARVA CE', 0),
(12, 'OSMAR', 0),
(13, 'OSRAM', 0),
(14, 'PHILIPS', 1),
(15, 'POLYLUX', 0),
(16, 'RELUX', 0),
(17, 'SICA', 0),
(18, 'SPIRAL', 0),
(19, 'STANDARD', 0),
(20, 'STANFORD', 0),
(21, 'TOSHIBA', 0),
(22, 'ULIX', 0),
(23, 'ZIHINK ZEUSSS', 1),
(24, 'Desconocido', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `marca`
--
ALTER TABLE `marca`
  ADD PRIMARY KEY (`id_marca`);

--
-- Indices de la tabla `marca_prueba`
--
ALTER TABLE `marca_prueba`
  ADD PRIMARY KEY (`id_marca`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `marca`
--
ALTER TABLE `marca`
  MODIFY `id_marca` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
