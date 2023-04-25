INSERT INTO
    IS601_Shop_Categories (
        id,
        name
    )
VALUES (-1, 'Other') ON DUPLICATE KEY
UPDATE name = name;

-- prevents this from failing after first insert