CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    category TEXT,
    item TEXT,
    quantity INTEGER,
    storageType TEXT
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    description TEXT
);

CREATE TABLE recipeingredients (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    recipe_id INTEGER,
    ingredient TEXT,
    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
);

CREATE TABLE recipedirections (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    recipe_id INTEGER,
    direction TEXT,
    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
);
