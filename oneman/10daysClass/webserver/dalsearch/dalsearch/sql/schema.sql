drop user 'seuser'@'localhost';
flush privileges;
CREATE USER 'seuser'@'localhost' IDENTIFIED BY 'se!@#$';
CREATE DATABASE IF NOT EXISTS dalsearch DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
#GRANT ALL  privileges ON dalsearch.* TO 'seuser'@'localhost' IDENTIFIED BY 'se!@#$';
grant all privileges on dalsearch.* to 'seuser'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE document_page (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `url` VARCHAR(255) NOT NULL,
    `title` VARCHAR(125) NOT NULL,
    `image` VARCHAR(255) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `pagecontent` TEXT NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


CREATE TABLE document_graph (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `from_page`INT(11) NOT NULL ,
    `to_page` INT(11) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
