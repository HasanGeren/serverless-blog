-- Create the database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS blog_platform_db;
USE blog_platform_db;

-- Create user_info table
CREATE TABLE user_info (
    user_id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create contents table
CREATE TABLE contents (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    bucket_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_info(user_id) ON DELETE CASCADE
);

-- Create categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Create content_categories table (many-to-many relationship between contents and categories)
CREATE TABLE content_categories (
    content_id INT,
    category_id INT,
    PRIMARY KEY (content_id, category_id),
    FOREIGN KEY (content_id) REFERENCES contents(content_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create comments table
CREATE TABLE comments (
    comment_id INT PRIMARY KEY,
    content_id INT,
    user_id INT,
    comment_body TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES contents(content_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user_info(user_id) ON DELETE CASCADE
);

SHOW tables;