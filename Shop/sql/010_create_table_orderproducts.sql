CREATE TABLE
    IF NOT EXISTS IS601_Shop_OrderProducts(
        id int AUTO_INCREMENT PRIMARY KEY,
        quantity int DEFAULT 0,
        cost int DEFAULT 999999,
        order_id int REFERENCES IS601_Shop_Orders(id),
        product_id int REFERENCES IS601_Shop_Products(id),
        user_id int REFERENCES IS601_Users(id),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (quantity >= 0),
        check (cost >= 0),
        UNIQUE KEY (order_id, product_id, user_id)
    )