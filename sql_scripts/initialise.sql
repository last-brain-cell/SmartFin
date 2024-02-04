CREATE TABLE "user" (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL, -- Hashed
    email VARCHAR(100) UNIQUE NOT NULL,
    profile_id INT UNIQUE,
    balance DECIMAL(12, 2),
    FOREIGN KEY (profile_id) REFERENCES profile(profile_id)
);

CREATE TABLE profile (
    profile_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    address TEXT
);

CREATE TABLE financial_transaction (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT,
    amount DECIMAL(12, 2),
    description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category_id INT,
    FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) UNIQUE
);

CREATE TABLE budget (
    budget_id SERIAL PRIMARY KEY,
    user_id INT,
    category_id INT,
    budget_amount DECIMAL(12, 2),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES "user"(user_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE financial_goal (
    goal_id SERIAL PRIMARY KEY,
    user_id INT,
    goal_description TEXT,
    target_amount DECIMAL(12, 2),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES "user"(user_id)
);

CREATE TABLE investment (
    investment_id SERIAL PRIMARY KEY,
    user_id INT,
    investment_type VARCHAR(50),
    amount DECIMAL(12, 2),
    description TEXT,
    investment_date DATE,
    FOREIGN KEY (user_id) REFERENCES "user"(user_id)
);
