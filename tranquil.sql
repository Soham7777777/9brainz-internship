-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 22, 2025 at 08:16 AM
-- Server version: 8.0.31
-- PHP Version: 8.1.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tranquil`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_users`
--

DROP TABLE IF EXISTS `admin_users`;
CREATE TABLE IF NOT EXISTS `admin_users` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_text` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_users_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `admin_users`
--

INSERT INTO `admin_users` (`id`, `name`, `email`, `password`, `password_text`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'Admin', 'admin@admin.com', 'Test@123', 'Test@123', NULL, '2024-12-13 01:12:37', '2024-12-19 01:07:09');

-- --------------------------------------------------------

--
-- Table structure for table `area_finish`
--

DROP TABLE IF EXISTS `area_finish`;
CREATE TABLE IF NOT EXISTS `area_finish` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `plan_types_id` bigint UNSIGNED DEFAULT NULL,
  `category_id` bigint UNSIGNED DEFAULT NULL,
  `area` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `finish` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `area_finish_plan_types_id_foreign` (`plan_types_id`),
  KEY `area_finish_category_id_foreign` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'Entry Area', 1, '2024-12-13 04:35:31', '2024-12-13 04:35:31'),
(2, 'COMMON WORK', 1, '2024-12-16 03:22:34', '2024-12-16 03:22:34'),
(3, 'Porch Area', 1, '2024-12-17 02:57:49', '2024-12-17 02:57:49');

-- --------------------------------------------------------

--
-- Table structure for table `category_details`
--

DROP TABLE IF EXISTS `category_details`;
CREATE TABLE IF NOT EXISTS `category_details` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `category_id` bigint UNSIGNED DEFAULT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `unit` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `quantity` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_details_category_id_foreign` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `category_details`
--

INSERT INTO `category_details` (`id`, `category_id`, `description`, `unit`, `quantity`, `created_at`, `updated_at`) VALUES
(48, 1, 'main one', 'no', 'sdfsdfdsf', '2024-12-17 02:44:44', '2024-12-17 02:44:44'),
(49, 1, 'two', 'no', 'SFSDF', '2024-12-17 02:44:44', '2024-12-17 02:44:44'),
(50, 1, 'THREE', 'no', 'SDFSDFDSF', '2024-12-17 02:44:44', '2024-12-17 02:44:44'),
(51, 3, 'main porch', 'yes', 'as per person', '2024-12-24 04:53:51', '2025-01-03 01:19:43'),
(52, 3, 'garden porch', 'yes', 'as per person', '2024-12-24 04:53:51', '2025-01-03 01:19:43'),
(53, 2, 'one', 'no', 'asdasd', '2024-12-24 04:54:00', '2024-12-24 04:54:00'),
(54, 2, 'three', 'no', 'sdfsdf', '2024-12-24 04:54:00', '2024-12-24 04:54:00'),
(55, 2, 'two', 'no', 'dzfsdf', '2024-12-24 04:54:00', '2024-12-24 04:54:00'),
(56, 3, 'flower portion', 'yes', 'as per person', '2025-01-03 01:19:43', '2025-01-03 01:19:43');

-- --------------------------------------------------------

--
-- Table structure for table `failed_jobs`
--

DROP TABLE IF EXISTS `failed_jobs`;
CREATE TABLE IF NOT EXISTS `failed_jobs` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `materials`
--

DROP TABLE IF EXISTS `materials`;
CREATE TABLE IF NOT EXISTS `materials` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `plan_types_id` bigint UNSIGNED DEFAULT NULL,
  `material` text COLLATE utf8mb4_unicode_ci,
  `specification` text COLLATE utf8mb4_unicode_ci,
  `selection_done_by` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `important_point` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `materials_plan_types_id_foreign` (`plan_types_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `materials`
--

INSERT INTO `materials` (`id`, `plan_types_id`, `material`, `specification`, `selection_done_by`, `important_point`, `created_at`, `updated_at`) VALUES
(2, 1, 'CEALING', 'AINT GOBIN POP SHEET AS PER DESIGN 3*3 CFG 8KG NET', 'EXECUTION TEAM', 'ALL HARDWARE AND MATERIAL IS STANDARD LEVEL  OF SPECIFICATION BRAND, ANY UPGRADE OR  PREFERANCE IN PARTICULAR MECHANISAM OR  SYSTEM WILL BE BILLED ADDITIONALLY DRAWER  CHANNEL-TELESCOPIC CHANNEL ARE NON-SOFT  CLOSE HINGES FOR SHUTTER ARE SOFT CLOSE  WORDROBE SLIDING CHANNELS ARE SOFT CLOSE', '2025-01-03 00:52:34', '2025-01-03 01:04:20'),
(3, 1, 'FABRIC FOR CURTAIN  AND LINING WORK', 'SARROM/GM/F&F/DIVIN/D\'DÉCOR ETC DEPENDING ON  SELECTION', 'DESIGNER TEAM AND  CLIENT BOTH', 'PROFILE,COB,PANEL LIGHTS&ROPE LIGHTS WHICH  PROVIDE MINIMUM 02 YRS PRODUCT WARRANTY  (HANGING LIGHT DOES NOT COVER ANY  WARRANTY/GURANTEE', '2025-01-03 01:04:20', '2025-01-03 01:04:20'),
(5, 1, 'LIGHT FITTING', 'BN/STAR EAGLE/NAPTUN', 'DESIGNER TEAM', 'AVERAGE PRICE CONSIDERED IS 3500-4000 FOR  ENTIRE HIUS', '2025-01-03 01:12:39', '2025-01-03 01:12:53'),
(6, 1, 'FAN', 'CROMPTON/HAVELLS/ATOM-BER', 'DESIGNER TEAM', 'AVERAGE PRICE CONSIDERED IS 3500-4000 FOR  ENTIRE HIUS', '2025-01-03 01:12:39', '2025-01-03 01:12:53');

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
CREATE TABLE IF NOT EXISTS `migrations` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_admin_users_table', 1),
(2, '2014_10_12_100000_create_password_resets_table', 1),
(3, '2019_08_19_000000_create_failed_jobs_table', 1),
(4, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(6, '2024_12_13_090802_create_categories_table', 2),
(8, '2024_12_14_061004_create_category_details_table', 3),
(9, '2024_12_19_063213_add_password_text_to_admin_users_table', 4),
(10, '2024_12_23_064257_create_users_table', 5),
(11, '2024_12_23_080353_create_types_table', 6),
(16, '2024_12_23_103200_create_plan_types_table', 7),
(19, '2024_12_26_055437_create_plan_types_bhk_details', 8),
(20, '2024_12_26_062646_create_plan_types_bhk_areas', 8),
(21, '2024_12_26_065704_create_plan_types_bhk_areas_details', 8),
(26, '2024_12_28_065959_create_quotation_details_tables', 10),
(29, '2025_01_02_113017_create_materials_table', 12),
(30, '2024_12_27_080722_add_col_to_users_table', 13),
(31, '2025_01_03_090418_create_settings_table', 14),
(32, '2025_01_04_053444_create_area_finish_table', 15);

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

DROP TABLE IF EXISTS `password_resets`;
CREATE TABLE IF NOT EXISTS `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personal_access_tokens`
--

DROP TABLE IF EXISTS `personal_access_tokens`;
CREATE TABLE IF NOT EXISTS `personal_access_tokens` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `tokenable_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tokenable_id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `abilities` text COLLATE utf8mb4_unicode_ci,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `expires_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `plan_types`
--

DROP TABLE IF EXISTS `plan_types`;
CREATE TABLE IF NOT EXISTS `plan_types` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_one` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_two` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `material_status` enum('yes','no') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'no',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `plan_types`
--

INSERT INTO `plan_types` (`id`, `name`, `image_one`, `image_two`, `is_active`, `material_status`, `created_at`, `updated_at`) VALUES
(1, 'standard', '1304600209.jpg', '1387006894.jpg', 1, 'no', '2024-12-24 03:50:52', '2025-01-02 01:37:38'),
(2, 'premium', '1674247151.jpg', '1287121463.jpg', 1, 'no', '2024-12-24 03:50:52', '2025-01-02 01:42:35'),
(3, 'premium plus', '2145090832.jpg', '699246686.jpg', 1, 'no', '2024-12-24 03:50:52', '2025-01-02 01:42:55'),
(4, 'other', '2112808405.png', '385981153.png', 1, 'no', '2024-12-27 06:23:43', '2024-12-27 06:23:43');

-- --------------------------------------------------------

--
-- Table structure for table `plan_types_bhk_areas`
--

DROP TABLE IF EXISTS `plan_types_bhk_areas`;
CREATE TABLE IF NOT EXISTS `plan_types_bhk_areas` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `plan_types_bhk_details_id` bigint UNSIGNED DEFAULT NULL,
  `category_id` bigint UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `plan_types_bhk_areas_plan_types_bhk_details_id_foreign` (`plan_types_bhk_details_id`),
  KEY `plan_types_bhk_areas_category_id_foreign` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `plan_types_bhk_areas`
--

INSERT INTO `plan_types_bhk_areas` (`id`, `plan_types_bhk_details_id`, `category_id`, `created_at`, `updated_at`) VALUES
(44, 39, 1, '2024-12-27 01:58:34', '2024-12-27 01:58:34'),
(45, 40, 2, '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(46, 41, 3, '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(53, 46, 1, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(54, 46, 2, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(55, 46, 3, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(56, 47, 1, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(57, 47, 2, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(58, 47, 3, '2025-01-01 23:59:40', '2025-01-01 23:59:40');

-- --------------------------------------------------------

--
-- Table structure for table `plan_types_bhk_areas_details`
--

DROP TABLE IF EXISTS `plan_types_bhk_areas_details`;
CREATE TABLE IF NOT EXISTS `plan_types_bhk_areas_details` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `plan_types_bhk_areas_id` bigint UNSIGNED DEFAULT NULL,
  `category_details_id` bigint UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `plan_types_bhk_areas_details_plan_types_bhk_areas_id_foreign` (`plan_types_bhk_areas_id`),
  KEY `plan_types_bhk_areas_details_category_details_id_foreign` (`category_details_id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `plan_types_bhk_areas_details`
--

INSERT INTO `plan_types_bhk_areas_details` (`id`, `plan_types_bhk_areas_id`, `category_details_id`, `created_at`, `updated_at`) VALUES
(56, 44, 49, '2024-12-27 01:58:34', '2024-12-27 01:58:34'),
(57, 45, 54, '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(58, 45, 55, '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(59, 46, 51, '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(60, 46, 52, '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(71, 53, 49, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(72, 53, 50, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(73, 54, 54, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(74, 55, 51, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(75, 55, 52, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(76, 56, 49, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(77, 57, 54, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(78, 58, 51, '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(79, 58, 52, '2025-01-01 23:59:40', '2025-01-01 23:59:40');

-- --------------------------------------------------------

--
-- Table structure for table `plan_types_bhk_details`
--

DROP TABLE IF EXISTS `plan_types_bhk_details`;
CREATE TABLE IF NOT EXISTS `plan_types_bhk_details` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `plan_types_id` bigint UNSIGNED DEFAULT NULL,
  `bhk_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `plan_types_bhk_details_plan_types_id_foreign` (`plan_types_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `plan_types_bhk_details`
--

INSERT INTO `plan_types_bhk_details` (`id`, `plan_types_id`, `bhk_type`, `price`, `created_at`, `updated_at`) VALUES
(39, 3, '4bhk', '4500.00', '2024-12-27 01:58:34', '2024-12-27 01:58:34'),
(40, 2, '8bhk', '4500.00', '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(41, 2, '3bhk', '6700.00', '2024-12-27 01:59:05', '2024-12-27 01:59:05'),
(46, 1, '4bhk', '2300.00', '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(47, 1, '5bhk', '6700.00', '2025-01-01 23:59:40', '2025-01-01 23:59:40'),
(48, 4, NULL, NULL, '2025-01-03 01:22:43', '2025-01-03 01:22:43');

-- --------------------------------------------------------

--
-- Table structure for table `quotation_details`
--

DROP TABLE IF EXISTS `quotation_details`;
CREATE TABLE IF NOT EXISTS `quotation_details` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` bigint UNSIGNED DEFAULT NULL,
  `plan_types_id` bigint UNSIGNED DEFAULT NULL,
  `plan_types_bhk_details_id` bigint UNSIGNED DEFAULT NULL,
  `client_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `client_number` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `site_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `project_code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `project_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `carpet_area` decimal(10,2) DEFAULT NULL,
  `project_cost` decimal(15,2) DEFAULT NULL,
  `other_cost` decimal(15,2) DEFAULT NULL,
  `total_cost` decimal(15,2) DEFAULT NULL,
  `note` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `quotation_details_user_id_foreign` (`user_id`),
  KEY `quotation_details_plan_types_id_foreign` (`plan_types_id`),
  KEY `quotation_details_plan_types_bhk_details_id_foreign` (`plan_types_bhk_details_id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `quotation_details`
--

INSERT INTO `quotation_details` (`id`, `user_id`, `plan_types_id`, `plan_types_bhk_details_id`, `client_name`, `client_number`, `site_name`, `project_code`, `project_name`, `carpet_area`, `project_cost`, `other_cost`, `total_cost`, `note`, `created_at`, `updated_at`) VALUES
(23, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:00:32', '2025-01-02 00:00:32'),
(24, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:02:04', '2025-01-02 00:02:04'),
(25, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:11:08', '2025-01-02 00:11:08'),
(26, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:37:56', '2025-01-02 00:37:56'),
(27, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:39:03', '2025-01-02 00:39:03'),
(28, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:41:11', '2025-01-02 00:41:11'),
(29, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:41:48', '2025-01-02 00:41:48'),
(30, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:52:36', '2025-01-02 00:52:36'),
(31, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:53:48', '2025-01-02 00:53:48'),
(32, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:55:52', '2025-01-02 00:55:52'),
(33, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:58:32', '2025-01-02 00:58:32'),
(34, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 00:59:19', '2025-01-02 00:59:19'),
(35, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:02:20', '2025-01-02 01:02:20'),
(36, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:03:00', '2025-01-02 01:03:00'),
(37, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:03:02', '2025-01-02 01:03:02'),
(38, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:03:55', '2025-01-02 01:03:55'),
(39, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:07:03', '2025-01-02 01:07:03'),
(40, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:08:19', '2025-01-02 01:08:19'),
(41, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:11:12', '2025-01-02 01:11:12'),
(42, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:12:16', '2025-01-02 01:12:16'),
(43, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:18:21', '2025-01-02 01:18:21'),
(44, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:20:43', '2025-01-02 01:20:43'),
(45, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:23:09', '2025-01-02 01:23:09'),
(46, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:26:06', '2025-01-02 01:26:06'),
(47, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:27:06', '2025-01-02 01:27:06'),
(48, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:52:54', '2025-01-02 01:52:54'),
(49, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:57:48', '2025-01-02 01:57:48'),
(50, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 01:59:15', '2025-01-02 01:59:15'),
(51, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:06:52', '2025-01-02 02:06:52'),
(52, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:14:16', '2025-01-02 02:14:16'),
(53, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:16:20', '2025-01-02 02:16:20'),
(54, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:16:25', '2025-01-02 02:16:25'),
(55, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:17:53', '2025-01-02 02:17:53'),
(56, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:18:30', '2025-01-02 02:18:30'),
(57, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:20:31', '2025-01-02 02:20:31'),
(58, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:42:39', '2025-01-02 02:42:39'),
(59, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:46:24', '2025-01-02 02:46:24'),
(60, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:47:47', '2025-01-02 02:47:47'),
(61, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:48:10', '2025-01-02 02:48:10'),
(62, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:53:35', '2025-01-02 02:53:35'),
(63, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:54:11', '2025-01-02 02:54:11'),
(64, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:56:58', '2025-01-02 02:56:58'),
(65, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 02:58:26', '2025-01-02 02:58:26'),
(66, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:00:19', '2025-01-02 03:00:19'),
(67, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:02:14', '2025-01-02 03:02:14'),
(68, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:02:49', '2025-01-02 03:02:49'),
(69, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:03:37', '2025-01-02 03:03:37'),
(70, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:23:57', '2025-01-02 03:23:57'),
(71, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:58:29', '2025-01-02 03:58:29'),
(72, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 03:59:08', '2025-01-02 03:59:08'),
(73, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:00:26', '2025-01-02 04:00:26'),
(74, 1, 1, 47, 'user one', '4567891230', 'site1', NULL, 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:04:42', '2025-01-02 04:04:42'),
(75, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:11:00', '2025-01-02 04:11:00'),
(76, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:19:34', '2025-01-02 04:19:34'),
(77, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:20:09', '2025-01-02 04:20:09'),
(78, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:24:16', '2025-01-02 04:24:16'),
(79, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:26:13', '2025-01-02 04:26:13'),
(80, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:27:04', '2025-01-02 04:27:04'),
(81, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:31:41', '2025-01-02 04:31:41'),
(82, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:33:42', '2025-01-02 04:33:42'),
(83, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:34:19', '2025-01-02 04:34:19'),
(84, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:35:41', '2025-01-02 04:35:41'),
(85, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:36:26', '2025-01-02 04:36:26'),
(86, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:37:40', '2025-01-02 04:37:40'),
(87, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:42:07', '2025-01-02 04:42:07'),
(88, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:43:26', '2025-01-02 04:43:26'),
(89, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:47:39', '2025-01-02 04:47:39'),
(90, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:49:01', '2025-01-02 04:49:01'),
(91, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 04:49:53', '2025-01-02 04:49:53'),
(92, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 05:04:19', '2025-01-02 05:04:19'),
(93, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 05:05:04', '2025-01-02 05:05:04'),
(94, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-02 05:19:33', '2025-01-02 05:19:33'),
(95, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 02:59:08', '2025-01-03 02:59:08'),
(96, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:01:09', '2025-01-03 03:01:09'),
(97, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:02:21', '2025-01-03 03:02:21'),
(98, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:32:54', '2025-01-03 03:32:54'),
(99, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:47:41', '2025-01-03 03:47:41'),
(100, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:50:13', '2025-01-03 03:50:13'),
(101, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:51:09', '2025-01-03 03:51:09'),
(102, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:55:18', '2025-01-03 03:55:18'),
(103, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 03:59:52', '2025-01-03 03:59:52'),
(104, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:02:49', '2025-01-03 04:02:49'),
(105, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:06:12', '2025-01-03 04:06:12'),
(106, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:09:47', '2025-01-03 04:09:47'),
(107, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:13:33', '2025-01-03 04:13:33'),
(108, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:18:36', '2025-01-03 04:18:36'),
(109, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:19:39', '2025-01-03 04:19:39'),
(110, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:23:29', '2025-01-03 04:23:29'),
(111, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:27:40', '2025-01-03 04:27:40'),
(112, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:31:32', '2025-01-03 04:31:32'),
(113, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:38:15', '2025-01-03 04:38:15'),
(114, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:41:05', '2025-01-03 04:41:05'),
(115, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:43:52', '2025-01-03 04:43:52'),
(116, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:45:19', '2025-01-03 04:45:19'),
(117, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:47:42', '2025-01-03 04:47:42'),
(118, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:48:19', '2025-01-03 04:48:19'),
(119, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:50:46', '2025-01-03 04:50:46'),
(120, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:52:02', '2025-01-03 04:52:02'),
(121, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:54:04', '2025-01-03 04:54:04'),
(122, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:56:49', '2025-01-03 04:56:49'),
(123, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 04:57:16', '2025-01-03 04:57:16'),
(124, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:00:20', '2025-01-03 05:00:20'),
(125, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:01:52', '2025-01-03 05:01:52'),
(126, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:06:29', '2025-01-03 05:06:29'),
(127, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:07:18', '2025-01-03 05:07:18'),
(128, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:07:59', '2025-01-03 05:07:59'),
(129, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:08:15', '2025-01-03 05:08:15'),
(130, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:10:33', '2025-01-03 05:10:33'),
(131, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:12:49', '2025-01-03 05:12:49'),
(132, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:20:42', '2025-01-03 05:20:42'),
(133, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:21:57', '2025-01-03 05:21:57'),
(134, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:22:56', '2025-01-03 05:22:56'),
(135, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:24:50', '2025-01-03 05:24:50'),
(136, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:25:43', '2025-01-03 05:25:43'),
(137, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:48:22', '2025-01-03 05:48:22'),
(138, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:49:20', '2025-01-03 05:49:20'),
(139, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:50:22', '2025-01-03 05:50:22'),
(140, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:51:39', '2025-01-03 05:51:39'),
(141, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:52:39', '2025-01-03 05:52:39'),
(142, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 05:56:24', '2025-01-03 05:56:24'),
(143, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 06:16:17', '2025-01-03 06:16:17'),
(144, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 23:31:29', '2025-01-03 23:31:29'),
(145, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 23:33:26', '2025-01-03 23:33:26'),
(146, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 23:36:22', '2025-01-03 23:36:22'),
(147, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 23:37:07', '2025-01-03 23:37:07'),
(148, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-03 23:43:03', '2025-01-03 23:43:03'),
(149, 1, 1, 47, 'user one', '4567891230', 'site1', '123', 'newproject', '2500.00', '1800000.00', '100000.00', '1900000.00', NULL, '2025-01-04 00:09:52', '2025-01-04 00:09:52');

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
CREATE TABLE IF NOT EXISTS `settings` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone_one` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone_two` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `type`, `image`, `phone_one`, `phone_two`, `url`, `created_at`, `updated_at`) VALUES
(1, 'main_section', '1735965214.jpg', '+91 99 756 99 765', '+91 99 756 99 765', 'www.tranquilinteriordesign.com', '2025-01-03 23:02:00', '2025-01-03 23:03:34');

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
CREATE TABLE IF NOT EXISTS `types` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`id`, `name`, `is_active`, `created_at`, `updated_at`) VALUES
(1, '3 BHK', 1, '2024-12-23 03:04:38', '2024-12-23 04:58:46'),
(2, '2 BHK', 1, '2024-12-23 03:16:45', '2024-12-23 04:58:56'),
(3, '4 BHK', 1, '2024-12-23 04:59:06', '2024-12-23 04:59:06'),
(4, 'Office', 1, '2024-12-23 04:59:15', '2024-12-23 04:59:15'),
(5, 'Turn-Key', 1, '2024-12-23 04:59:24', '2024-12-23 04:59:24');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password_text` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `device_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fcm_token` text COLLATE utf8mb4_unicode_ci,
  `remember_token` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `password`, `password_text`, `device_type`, `fcm_token`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'user one', '$2y$10$x.u6LH20SvW4CjMwvg6C2Od2bUoazGz9OaR6RBnPYkG.9MZ47oVji', '123456', 'android', 'token1', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjgwODEvYXBpL3VzZXIvbG9naW4iLCJpYXQiOjE3MzU5NjY4NjEsIm5iZiI6MTczNTk2Njg2MSwianRpIjoiR0FVVHA5dVhWN3RBakVHNSIsInN1YiI6IjEiLCJwcnYiOiJmNjRkNDhhNmNlYzdiZGZhN2ZiZjg5OTQ1NGI0ODhiM2U0NjI1MjBhIn0.yXnIr7QJUZhMy2XmzDEUMU_kn3D56vGjuc9H75SiWJk', '2024-12-23 01:27:30', '2025-01-03 23:31:02');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `area_finish`
--
ALTER TABLE `area_finish`
  ADD CONSTRAINT `area_finish_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `area_finish_plan_types_id_foreign` FOREIGN KEY (`plan_types_id`) REFERENCES `plan_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `category_details`
--
ALTER TABLE `category_details`
  ADD CONSTRAINT `category_details_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `materials`
--
ALTER TABLE `materials`
  ADD CONSTRAINT `materials_plan_types_id_foreign` FOREIGN KEY (`plan_types_id`) REFERENCES `plan_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `plan_types_bhk_areas`
--
ALTER TABLE `plan_types_bhk_areas`
  ADD CONSTRAINT `plan_types_bhk_areas_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `plan_types_bhk_areas_plan_types_bhk_details_id_foreign` FOREIGN KEY (`plan_types_bhk_details_id`) REFERENCES `plan_types_bhk_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `plan_types_bhk_areas_details`
--
ALTER TABLE `plan_types_bhk_areas_details`
  ADD CONSTRAINT `plan_types_bhk_areas_details_category_details_id_foreign` FOREIGN KEY (`category_details_id`) REFERENCES `category_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `plan_types_bhk_areas_details_plan_types_bhk_areas_id_foreign` FOREIGN KEY (`plan_types_bhk_areas_id`) REFERENCES `plan_types_bhk_areas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `plan_types_bhk_details`
--
ALTER TABLE `plan_types_bhk_details`
  ADD CONSTRAINT `plan_types_bhk_details_plan_types_id_foreign` FOREIGN KEY (`plan_types_id`) REFERENCES `plan_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `quotation_details`
--
ALTER TABLE `quotation_details`
  ADD CONSTRAINT `quotation_details_plan_types_bhk_details_id_foreign` FOREIGN KEY (`plan_types_bhk_details_id`) REFERENCES `plan_types_bhk_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `quotation_details_plan_types_id_foreign` FOREIGN KEY (`plan_types_id`) REFERENCES `plan_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `quotation_details_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
