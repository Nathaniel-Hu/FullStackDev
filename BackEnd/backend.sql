connect to root@localhost;

--------------------------------
CREATE TABLE Seller (
    username VARCHAR(16) NOT NULL,
    password VARCHAR(16) NOT NULL,
    seller_id INT NOT NULL,
    name VARCHAR(32),
    description VARCHAR(256),
    profile_pic VARCHAR(128),
    PRIMARY KEY(username, password)
);

--------------------------------
CREATE TABLE Category (
    category_id INT NOT NULL,
    name VARCHAR(32),
    description VARCHAR(256),
    PRIMARY KEY(category_id)
);

--------------------------------
CREATE TABLE Product (
    seller_id INT NOT NULL,
    category_id INT NOT NULL,
    product_id INT NOT NULL,
    name VARCHAR(32),
    description VARCHAR(256),
    PRIMARY KEY(product_id),
    FOREIGN KEY(seller_id) REFERENCES Seller(seller_id) ON DELETE CASCADE,
    FOREIGN KEY(category_id) REFERENCES Category(category_id) ON DELETE CASCADE
);

--------------------------------
CREATE TABLE Photo (
    product_id INT NOT NULL,
    photo_id INT NOT NULL,
    name VARCHAR(32),
    datapath VARCHAR(128),
    PRIMARY KEY(photo_id),
    FOREIGN KEY(product_id) REFERENCES Product(product_id) ON DELETE CASCADE
);

--------------------------------

DESCRIBE Product;
