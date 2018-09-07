/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.27.1
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : 192.168.27.1:3306
 Source Schema         : order_food

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 07/09/2018 09:58:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Boss
-- ----------------------------
DROP TABLE IF EXISTS `Boss`;
CREATE TABLE `Boss`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nick_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` int(11) DEFAULT NULL,
  `city` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `province` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `country` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `avatarUrl` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `cashbox` decimal(8, 2) DEFAULT NULL,
  `band_card_number` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `openid` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `openid`(`openid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for Customer
-- ----------------------------
DROP TABLE IF EXISTS `Customer`;
CREATE TABLE `Customer`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `openid` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nick_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` int(11) DEFAULT NULL,
  `city` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `province` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `country` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `avatarUrl` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `cashbox` decimal(8, 2) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `openid`(`openid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for Food
-- ----------------------------
DROP TABLE IF EXISTS `Food`;
CREATE TABLE `Food`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` int(10) UNSIGNED NOT NULL,
  `ref_restaurant_id` int(10) UNSIGNED NOT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ref_restaurant_id`(`ref_restaurant_id`) USING BTREE,
  CONSTRAINT `Food_ibfk_1` FOREIGN KEY (`ref_restaurant_id`) REFERENCES `Restaurant` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for Order
-- ----------------------------
DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `total_price` int(10) UNSIGNED NOT NULL,
  `ref_customer_id` int(10) UNSIGNED NOT NULL,
  `time` datetime(0) DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ref_customer_id`(`ref_customer_id`) USING BTREE,
  CONSTRAINT `Order_ibfk_1` FOREIGN KEY (`ref_customer_id`) REFERENCES `Customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for OrderItem
-- ----------------------------
DROP TABLE IF EXISTS `OrderItem`;
CREATE TABLE `OrderItem`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `ref_food_id` int(10) UNSIGNED NOT NULL,
  `ref_order_id` int(10) UNSIGNED NOT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `test` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ref_food_id`(`ref_food_id`) USING BTREE,
  INDEX `ref_order_id`(`ref_order_id`) USING BTREE,
  CONSTRAINT `OrderItem_ibfk_1` FOREIGN KEY (`ref_food_id`) REFERENCES `Food` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `OrderItem_ibfk_2` FOREIGN KEY (`ref_order_id`) REFERENCES `Order` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for Restaurant
-- ----------------------------
DROP TABLE IF EXISTS `Restaurant`;
CREATE TABLE `Restaurant`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ref_boss_id` int(10) UNSIGNED NOT NULL,
  `introduction` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `address` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ref_boss_id`(`ref_boss_id`) USING BTREE,
  CONSTRAINT `Restaurant_ibfk_1` FOREIGN KEY (`ref_boss_id`) REFERENCES `Boss` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('499935e62997');

SET FOREIGN_KEY_CHECKS = 1;
