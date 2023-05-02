CREATE TABLE
    IF NOT EXISTS IS601_Shop_Orders(
        id int AUTO_INCREMENT PRIMARY KEY,
        user_id int REFERENCES IS601_Users(id),
        total_price int DEFAULT 999999,
        number_of_products int,
        address text,
        payment_method ENUM('CASH', 'DEBIT_CARD', 'CREDIT_CARD'),
        money_received int DEFAULT 999999,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (total_price >= 0),
        check (money_received >= 0)
    )