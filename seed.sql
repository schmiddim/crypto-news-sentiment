CREATE TABLE `threads` (
  `id` int(11) NOT NULL,
  `date_modified` timestamp NULL DEFAULT current_timestamp(),
  `date_created_4chan` timestamp NULL DEFAULT NULL,
  `date_last_modified_4chan` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `thread_id` int(11) NOT NULL,
  `topic` text CHARACTER SET utf8 NOT NULL,
  `replies` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;