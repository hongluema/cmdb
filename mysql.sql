CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8;

CREATE TABLE `machine_room` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(64) DEFAULT NULL,
 `addr` varchar(128) DEFAULT NULL,
 `ip_ranges` text,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

CREATE TABLE `asset` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `sn` varchar(125) NOT NULL COMMENT '资产标号',
 `hostname` varchar(64) DEFAULT NULL COMMENT '主机名',
 `os` varchar(64) DEFAULT NULL COMMENT '操作系统',
 `ip` varchar(256) DEFAULT NULL COMMENT 'ip地址',
 `machine_room_id` int(11) DEFAULT NULL COMMENT '机房ID',
 `vendor` varchar(256) DEFAULT NULL COMMENT '生产厂商',
 `model` varchar(64) DEFAULT NULL COMMENT '型号',
 `ram` int(11) DEFAULT NULL COMMENT '内存, 单位G',
 `cpu` int(11) DEFAULT NULL COMMENT 'cpu核数',
 `disk` int(11) DEFAULT NULL COMMENT '硬盘，单位G',
 `time_on_shelves` date DEFAULT NULL COMMENT '上架时间',
 `over_guaranteed_date` date DEFAULT NULL COMMENT '过保时间',
 `buiness` varchar(256) DEFAULT NULL COMMENT '业务',
 `admin` varchar(256) DEFAULT NULL COMMENT '使用者',
 `status` int(11) DEFAULT NULL COMMENT '0正在使用, 1 维护, 2 删除',
 PRIMARY KEY (`id`),
 UNIQUE KEY `sn` (`sn`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
