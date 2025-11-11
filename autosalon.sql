-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Ноя 11 2025 г., 13:28
-- Версия сервера: 8.0.29
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `autosalon`
--

-- --------------------------------------------------------

--
-- Структура таблицы `automobile`
--

CREATE TABLE `automobile` (
  `ID` int NOT NULL,
  `Marka` int DEFAULT NULL,
  `Model` varchar(100) DEFAULT NULL,
  `Cvet` int DEFAULT NULL,
  `Obiem_dvigatelya` double(8,2) DEFAULT NULL,
  `Complectacia` varchar(50) DEFAULT NULL,
  `Stoimost` double(10,2) DEFAULT NULL,
  `Foto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `automobile`
--

INSERT INTO `automobile` (`ID`, `Marka`, `Model`, `Cvet`, `Obiem_dvigatelya`, `Complectacia`, `Stoimost`, `Foto`) VALUES
(1, 1, 'Camry', 1, 2.50, 'LE', 2500000.00, '1.png'),
(2, 2, '3 Series (320i)', 2, 2.00, 'Luxury Line', 3800000.00, '2.png'),
(3, 3, 'E-Class (E 200)', 3, 2.00, 'Exclusive', 4500000.00, '3.png'),
(4, 4, 'A4', 4, 2.00, 'Sport', 3700000.00, '4.png'),
(5, 5, 'Focus', 5, 1.50, 'Titanium', 1600000.00, '5.png'),
(6, 6, 'Civic', 6, 1.50, 'Sport', 1900000.00, '6.png'),
(7, 7, 'Golf', 7, 1.40, 'Highline', 2200000.00, '7.png'),
(8, 8, 'Qashqai', 8, 2.00, 'Tekna', 2300000.00, '8.png'),
(9, 9, 'Model 3', 9, NULL, 'Long Range', 4800000.00, '9.png'),
(10, 10, 'Sonata', 10, 2.50, 'Style', 2100000.00, '10.png');

-- --------------------------------------------------------

--
-- Структура таблицы `client`
--

CREATE TABLE `client` (
  `ID` int NOT NULL,
  `Familia` varchar(100) DEFAULT NULL,
  `Imya` varchar(100) DEFAULT NULL,
  `Otchestvo` varchar(100) DEFAULT NULL,
  `Data_rozhdenia` date DEFAULT NULL,
  `Nomer_telephona` varchar(20) DEFAULT NULL,
  `Pass` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `client`
--

INSERT INTO `client` (`ID`, `Familia`, `Imya`, `Otchestvo`, `Data_rozhdenia`, `Nomer_telephona`, `Pass`) VALUES
(1, 'Иванов', 'Алексей', 'Сергеевич', '1985-03-15', '+7(912)345-67-89', '49218376'),
(2, 'Смирнова', 'Елена', 'Викторовна', '1990-07-22', '+7(903)876-54-32', '80594213'),
(3, 'Кузнецов', 'Дмитрий', 'Анатольевич', '1978-09-11', '+7(495)123-45-67', '17654329'),
(4, 'Попова', 'Марина', 'Игоревна', '0200-01-01', '+7(926)987-65-43', '93820741'),
(5, 'Новиков', 'Сергей', 'Павлович', '1995-06-30', '+7(910)234-56-78', '61479832'),
(6, 'Соколова', 'Ольга', 'Дмитриевна', '1982-12-14', '+7(999)111-22-33', '70316589'),
(7, 'Михайлов', 'Андрей', 'Николаевич', '1975-02-28', '+7(925)555-44-66', '85269430'),
(8, 'Фёдорова', 'Наталья', 'Юрьевна', '1988-09-05', '+7(901)765-43-21', '12974865'),
(9, 'Васильев', 'Роман', 'Александрович', '1992-04-19', '+7(912)678-90-12', '46523197'),
(10, 'Петрова', 'Анна', 'Владимировна', '1980-10-11', '+7(915)432-10-98', '79032486');

-- --------------------------------------------------------

--
-- Структура таблицы `complectyushie`
--

CREATE TABLE `complectyushie` (
  `ID` int NOT NULL,
  `Nazvanie` varchar(50) DEFAULT NULL,
  `ID_marki` int DEFAULT NULL,
  `Model` varchar(100) DEFAULT NULL,
  `Stoimost` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `complectyushie`
--

INSERT INTO `complectyushie` (`ID`, `Nazvanie`, `ID_marki`, `Model`, `Stoimost`) VALUES
(1, 'Тормозные колодки', 1, 'Camry', '1000.00'),
(2, 'Воздушный фильтр', 2, '3 Series (320i)', '500.00'),
(3, 'Свеча зажигания', 3, 'E-Class (E200)', '800.00'),
(4, 'Амортизатор передний', 1, 'A4', '200.00'),
(5, 'Радиатор охлаждения', 5, 'Focus', '1500000.00'),
(6, 'Масляный фильтр', 6, 'Civic', '1255.00'),
(7, 'Рулевая тяга', 7, 'Golf', '14555.00'),
(8, 'Шаровая опора', 2, 'Qashqai', '10000.00'),
(9, 'Аккумулятор', 9, 'Model 3', '50000.00'),
(10, 'Генератор', 10, 'Sonata', '25000.00');

-- --------------------------------------------------------

--
-- Структура таблицы `cvet`
--

CREATE TABLE `cvet` (
  `ID` int NOT NULL,
  `Nazvanie` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `cvet`
--

INSERT INTO `cvet` (`ID`, `Nazvanie`) VALUES
(1, 'Чёрный'),
(2, 'Белый'),
(3, 'Серебристый'),
(4, 'Серый'),
(5, 'Красный'),
(6, 'Синий'),
(7, 'Тёмно-зелёный'),
(8, 'Золотистый'),
(9, 'Коричневый'),
(10, 'Бежевый');

-- --------------------------------------------------------

--
-- Структура таблицы `dolzhnosti`
--

CREATE TABLE `dolzhnosti` (
  `ID` int NOT NULL,
  `Dolzhnost` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `dolzhnosti`
--

INSERT INTO `dolzhnosti` (`ID`, `Dolzhnost`) VALUES
(1, 'Менеджер по продажам автомобилей'),
(2, 'Консультант по подбору автомобилей'),
(3, 'Специалист по кредитованию и лизингу'),
(4, 'Специалист по сервисному обслуживанию'),
(5, 'Мастер-приёмщик'),
(6, 'Техник по ремонту автомобилей'),
(7, 'Администратор автосалона'),
(8, 'Маркетолог автосалона'),
(9, 'Менеджер по работе с клиентами'),
(10, 'Кассир / Бухгалтер');

-- --------------------------------------------------------

--
-- Структура таблицы `marka`
--

CREATE TABLE `marka` (
  `ID` int NOT NULL,
  `Nazvanie` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `marka`
--

INSERT INTO `marka` (`ID`, `Nazvanie`) VALUES
(1, 'Toyota'),
(2, 'BMW'),
(3, 'Mercedes-Benz'),
(4, 'Audi'),
(5, 'Ford'),
(6, 'Honda'),
(7, 'Volkswagen'),
(8, 'Nissan'),
(9, 'Tesla'),
(10, 'Hyundai');

-- --------------------------------------------------------

--
-- Структура таблицы `postuplenie_na_sklad_automobiley`
--

CREATE TABLE `postuplenie_na_sklad_automobiley` (
  `ID` int NOT NULL,
  `ID_automobilya` int DEFAULT NULL,
  `ID_sotrudnika` int DEFAULT NULL,
  `Data_postuplenia` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `postuplenie_na_sklad_automobiley`
--

INSERT INTO `postuplenie_na_sklad_automobiley` (`ID`, `ID_automobilya`, `ID_sotrudnika`, `Data_postuplenia`) VALUES
(1, 1, 1, '2025-09-01'),
(2, 2, 2, '2025-09-02'),
(3, 3, 3, '2025-09-03'),
(4, 4, 4, '2025-09-04'),
(5, 5, 5, '2025-09-05'),
(6, 6, 6, '2025-09-06'),
(7, 7, 7, '2025-09-07'),
(8, 8, 8, '2025-09-08'),
(9, 9, 9, '2025-09-09'),
(10, 10, 10, '2025-09-10');

-- --------------------------------------------------------

--
-- Структура таблицы `postuplenie_na_sklad_complectyushih`
--

CREATE TABLE `postuplenie_na_sklad_complectyushih` (
  `ID` int NOT NULL,
  `ID_complectyushego` int DEFAULT NULL,
  `ID_sotrudnika` int DEFAULT NULL,
  `Data_postuplenia` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `postuplenie_na_sklad_complectyushih`
--

INSERT INTO `postuplenie_na_sklad_complectyushih` (`ID`, `ID_complectyushego`, `ID_sotrudnika`, `Data_postuplenia`) VALUES
(1, 1, 1, '2025-09-01'),
(2, 2, 2, '2025-09-02'),
(3, 3, 3, '2025-09-03'),
(4, 4, 4, '2025-09-04'),
(5, 5, 5, '2025-09-05'),
(6, 6, 6, '2025-09-06'),
(7, 7, 7, '2025-09-07'),
(8, 8, 8, '2025-09-08'),
(9, 9, 9, '2025-09-09'),
(10, 10, 10, '2025-09-10');

-- --------------------------------------------------------

--
-- Структура таблицы `prodazhi_automobiley`
--

CREATE TABLE `prodazhi_automobiley` (
  `ID` int NOT NULL,
  `ID_sotrudnika` int DEFAULT NULL,
  `ID_clienta` int DEFAULT NULL,
  `ID_automobilya` int DEFAULT NULL,
  `Data_prodazhi` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `prodazhi_automobiley`
--

INSERT INTO `prodazhi_automobiley` (`ID`, `ID_sotrudnika`, `ID_clienta`, `ID_automobilya`, `Data_prodazhi`) VALUES
(1, 1, 1, 1, '2025-09-01'),
(2, 2, 2, 2, '2025-09-02'),
(3, 3, 3, 3, '2025-09-03'),
(4, 4, 4, 4, '2025-09-04'),
(5, 5, 5, 5, '2025-09-05'),
(6, 6, 6, 6, '2025-09-06'),
(7, 7, 7, 7, '2025-09-07'),
(8, 8, 8, 8, '2025-09-08'),
(9, 9, 9, 9, '2025-09-09'),
(10, 10, 10, 10, '2025-09-10'),
(11, NULL, 1, 7, '2025-11-10'),
(12, NULL, 1, 7, '2025-11-10');

-- --------------------------------------------------------

--
-- Структура таблицы `prodazhi_complectyushih`
--

CREATE TABLE `prodazhi_complectyushih` (
  `ID` int NOT NULL,
  `ID_sotrudnika` int DEFAULT NULL,
  `ID_clienta` int DEFAULT NULL,
  `Data_prodazhy` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `prodazhi_complectyushih`
--

INSERT INTO `prodazhi_complectyushih` (`ID`, `ID_sotrudnika`, `ID_clienta`, `Data_prodazhy`) VALUES
(1, 1, 1, '2025-09-01'),
(2, 2, 2, '2025-09-02'),
(3, 3, 3, '2025-09-03'),
(4, 4, 4, '2025-09-04'),
(5, 5, 5, '2025-09-05'),
(6, 6, 6, '2025-09-06'),
(7, 7, 7, '2025-09-07'),
(8, 8, 8, '2025-09-08'),
(9, 9, 9, '2025-09-09'),
(10, 10, 10, '2025-09-10');

-- --------------------------------------------------------

--
-- Структура таблицы `sostav_prodazhi_complectyushih`
--

CREATE TABLE `sostav_prodazhi_complectyushih` (
  `ID` int NOT NULL,
  `ID_complectyushego` int DEFAULT NULL,
  `ID_prodazhi` int DEFAULT NULL,
  `Kolichestvo` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `sostav_prodazhi_complectyushih`
--

INSERT INTO `sostav_prodazhi_complectyushih` (`ID`, `ID_complectyushego`, `ID_prodazhi`, `Kolichestvo`) VALUES
(1, 1, 1, 10),
(2, 2, 2, 20),
(3, 3, 3, 30),
(4, 4, 4, 40),
(5, 5, 5, 50),
(6, 6, 6, 60),
(7, 7, 7, 70),
(8, 8, 8, 80),
(9, 9, 9, 90),
(10, 10, 10, 100);

-- --------------------------------------------------------

--
-- Структура таблицы `sotrudnik`
--

CREATE TABLE `sotrudnik` (
  `ID` int NOT NULL,
  `Familia` varchar(50) DEFAULT NULL,
  `Imya` varchar(50) DEFAULT NULL,
  `Otchestvo` varchar(50) DEFAULT NULL,
  `Dolzhnost` int DEFAULT NULL,
  `Login` varchar(50) DEFAULT NULL,
  `Pass` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `sotrudnik`
--

INSERT INTO `sotrudnik` (`ID`, `Familia`, `Imya`, `Otchestvo`, `Dolzhnost`, `Login`, `Pass`) VALUES
(1, 'Степанов', 'Алексей', 'Викторович', 1, 'stepanovav', '58392017'),
(2, 'Ковалёва', 'Мария', 'Ивановна', 2, 'kovalevami', '74019385'),
(3, 'Фролов', 'Дмитрий', 'Алексеевич', 3, 'frolovda', '21647809'),
(4, 'Соколова', 'Надежда', 'Петровна', 4, 'sokolovanp', '90583214'),
(5, 'Лазарев', 'Михаил', 'Сергеевич', 5, 'lazarevms', '37160928'),
(6, 'Воронова', 'Анна', 'Юрьевна', 6, 'voronovaau', '86427591'),
(7, 'Кузьмин', 'Алексей', 'Михайлович', 7, 'kuzminam', '49018276'),
(8, 'Громова', 'Виктория', 'Владимировна', 8, 'gromovavv', '15293740'),
(9, 'Егоров', 'Игорь', 'Павлович', 9, 'egorovip', '67805413'),
(10, 'Зайцева', 'Ольга', 'Александровна', 10, 'zaitsevaoa', '02918465');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `automobile`
--
ALTER TABLE `automobile`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_automobile_cvet` (`Cvet`),
  ADD KEY `fk_tables_automobile_marka` (`Marka`);

--
-- Индексы таблицы `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `complectyushie`
--
ALTER TABLE `complectyushie`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_compectyushie_marka` (`ID_marki`);

--
-- Индексы таблицы `cvet`
--
ALTER TABLE `cvet`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `dolzhnosti`
--
ALTER TABLE `dolzhnosti`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `marka`
--
ALTER TABLE `marka`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `postuplenie_na_sklad_automobiley`
--
ALTER TABLE `postuplenie_na_sklad_automobiley`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_prodazhi_postuplenie_na_sklad_automobiley_automobile` (`ID_automobilya`),
  ADD KEY `fk_tables_prodazhi_postuplenie_na_sklad_automobiley_sotrudnik` (`ID_sotrudnika`);

--
-- Индексы таблицы `postuplenie_na_sklad_complectyushih`
--
ALTER TABLE `postuplenie_na_sklad_complectyushih`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_postuplenie_na_sklad_complectyushih_complectyushie` (`ID_complectyushego`),
  ADD KEY `fk_tables_postuplenie_na_sklad_complectyushih_sotrudnik` (`ID_sotrudnika`);

--
-- Индексы таблицы `prodazhi_automobiley`
--
ALTER TABLE `prodazhi_automobiley`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_prodazhi_automobiley_sotrudnik` (`ID_sotrudnika`),
  ADD KEY `fk_tables_prodazhi_automobiley_client` (`ID_clienta`),
  ADD KEY `fk_tables_prodazhi_automobiley_automobile` (`ID_automobilya`);

--
-- Индексы таблицы `prodazhi_complectyushih`
--
ALTER TABLE `prodazhi_complectyushih`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_prodazhi_complectyushih_client` (`ID_clienta`),
  ADD KEY `fk_tables_prodazhi_complectyushih_sotrudnik` (`ID_sotrudnika`);

--
-- Индексы таблицы `sostav_prodazhi_complectyushih`
--
ALTER TABLE `sostav_prodazhi_complectyushih`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tables_sostav_prodazhi_complectyushih_complectyushie` (`ID_complectyushego`),
  ADD KEY `fk_tables_sostav_prodazhi_complectyushih_prodazhi` (`ID_prodazhi`);

--
-- Индексы таблицы `sotrudnik`
--
ALTER TABLE `sotrudnik`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Dolzhnost` (`Dolzhnost`);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `automobile`
--
ALTER TABLE `automobile`
  ADD CONSTRAINT `fk_tables_automobile_cvet` FOREIGN KEY (`Cvet`) REFERENCES `cvet` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_automobile_marka` FOREIGN KEY (`Marka`) REFERENCES `marka` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `complectyushie`
--
ALTER TABLE `complectyushie`
  ADD CONSTRAINT `fk_tables_compectyushie_marka` FOREIGN KEY (`ID_marki`) REFERENCES `marka` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `postuplenie_na_sklad_automobiley`
--
ALTER TABLE `postuplenie_na_sklad_automobiley`
  ADD CONSTRAINT `fk_tables_prodazhi_postuplenie_na_sklad_automobiley_automobile` FOREIGN KEY (`ID_automobilya`) REFERENCES `automobile` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_prodazhi_postuplenie_na_sklad_automobiley_sotrudnik` FOREIGN KEY (`ID_sotrudnika`) REFERENCES `sotrudnik` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `postuplenie_na_sklad_complectyushih`
--
ALTER TABLE `postuplenie_na_sklad_complectyushih`
  ADD CONSTRAINT `fk_tables_postuplenie_na_sklad_complectyushih_complectyushie` FOREIGN KEY (`ID_complectyushego`) REFERENCES `complectyushie` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_postuplenie_na_sklad_complectyushih_sotrudnik` FOREIGN KEY (`ID_sotrudnika`) REFERENCES `sotrudnik` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `prodazhi_automobiley`
--
ALTER TABLE `prodazhi_automobiley`
  ADD CONSTRAINT `fk_tables_prodazhi_automobiley_automobile` FOREIGN KEY (`ID_automobilya`) REFERENCES `automobile` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_prodazhi_automobiley_client` FOREIGN KEY (`ID_clienta`) REFERENCES `client` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_prodazhi_automobiley_sotrudnik` FOREIGN KEY (`ID_sotrudnika`) REFERENCES `sotrudnik` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `prodazhi_complectyushih`
--
ALTER TABLE `prodazhi_complectyushih`
  ADD CONSTRAINT `fk_tables_prodazhi_complectyushih_client` FOREIGN KEY (`ID_clienta`) REFERENCES `client` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_prodazhi_complectyushih_sotrudnik` FOREIGN KEY (`ID_sotrudnika`) REFERENCES `sotrudnik` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `sostav_prodazhi_complectyushih`
--
ALTER TABLE `sostav_prodazhi_complectyushih`
  ADD CONSTRAINT `fk_tables_sostav_prodazhi_complectyushih_complectyushie` FOREIGN KEY (`ID_complectyushego`) REFERENCES `complectyushie` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tables_sostav_prodazhi_complectyushih_prodazhi` FOREIGN KEY (`ID_prodazhi`) REFERENCES `prodazhi_complectyushih` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `sotrudnik`
--
ALTER TABLE `sotrudnik`
  ADD CONSTRAINT `sotrudnik_ibfk_1` FOREIGN KEY (`Dolzhnost`) REFERENCES `dolzhnosti` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `sotrudnik_ibfk_2` FOREIGN KEY (`Dolzhnost`) REFERENCES `dolzhnosti` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
