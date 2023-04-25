CREATE TABLE
    IF NOT EXISTS IS601_Shop_Products(
        id int AUTO_INCREMENT PRIMARY KEY,
        name varchar(30) UNIQUE,
        description text,
        category_id int REFERENCES IS601_Shop_Categories(id)
        stock int DEFAULT 0,
        cost int DEFAULT 999999,
        image text,
        is_visible tinyint(1) default 1,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (stock >= 0),
        check (cost >= 0)
    )