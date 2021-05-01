CREATE TABLE `threads` (
  `id` int(11) NOT NULL,
  `date_modified` timestamp NULL DEFAULT current_timestamp(),
  `date_created_4chan` timestamp NULL DEFAULT NULL,
  `date_last_modified_4chan` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `thread_id` int(11) NOT NULL,
  `topic` text CHARACTER SET utf8 NOT NULL,
  `replies` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `ratings` (
  `id` int(11) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `thread_id` int(11) NOT NULL,
  `reply_count` int(11) NOT NULL,
  `has_results` tinyint(1) NOT NULL DEFAULT 1,
  `top1` varchar(255) DEFAULT NULL,
  `top2` varchar(255) DEFAULT NULL,
  `top3` varchar(255) DEFAULT NULL,
  `top4` varchar(255) DEFAULT NULL,
  `top5` varchar(255) DEFAULT NULL,
  `count1` int(11) DEFAULT NULL,
  `count2` int(11) DEFAULT NULL,
  `count3` int(11) DEFAULT NULL,
  `count4` int(11) DEFAULT NULL,
  `count5` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
