CREATE TABLE
    IF NOT EXISTS IS601_Shop_Cart(
        id int AUTO_INCREMENT PRIMARY KEY,
        quantity int DEFAULT 0,
        cost int DEFAULT 999999,
        product_id int REFERENCES IS601_Shop_Products(id),
        user_id int REFERENCES IS601_Users(id),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (quantity >= 0),
        check (cost >= 0),
        UNIQUE KEY (product_id, user_id)
    )