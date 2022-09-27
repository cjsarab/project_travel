DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR (255),
    is_visited BOOLEAN DEFAULT false
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR (255),
    is_visited BOOLEAN DEFAULT false,
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    sight_name VARCHAR (255),
    is_visited BOOLEAN DEFAULT false,
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE
);

