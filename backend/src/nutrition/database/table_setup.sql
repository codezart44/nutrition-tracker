
DROP TABLE fndds_items;
DROP TABLE fndds_nutrients;
DROP TABLE fndds_measures;

CREATE TABLE IF NOT EXISTS [fndds_items] (
    [fdc_id] INT PRIMARY KEY
    , [item_name] TEXT NOT NULL
    , [description] TEXT
    , [additional_descriptions] TEXT
    , [data_type] TEXT
    , [published_date] DATE
    , [category] TEXT NOT NULL
    , [subcategory] TEXT NOT NULL
    , [fndds_subcategory] TEXT
    , [fndds_subcategory_id] INT
);

CREATE TABLE IF NOT EXISTS [fndds_nutrients] (
    [food_nutrient_id] INT PRIMARY KEY
    , [fdc_id] INT NOT NULL
    , [nutrient_id] INT NOT NULL
    , [nutrient_name] TEXT NOT NULL         --Water, Protein, Sodium etc...
    , [nutrient_number] TEXT
    , [nutrient_category] TEXT NOT NULL     --Proximates, Minerals etc...
    , [unit_name] TEXT NOT NULL
    , [value] REAL NOT NULL
    , FOREIGN KEY(fdc_id) REFERENCES fndds_items(fdc_id)
    -- , FOREIGN KEY(nutrient_id) REFERENCES nutrient_metadata(nutrient_id)
);

CREATE TABLE IF NOT EXISTS [fndds_measures] (
    [measure_id] INT PRIMARY KEY
    , [fdc_id] INT NOT NULL
    , [dissemination_text] TEXT NOT NULL
    , [gram_weight] REAL
    -- , [measure_unit_abbreviation] TEXT
    -- , [measure_unit_id] INT
    -- , [measure_unit_name] TEXT
    , FOREIGN KEY(fdc_id) REFERENCES fndds_items(fdc_id)
);


CREATE TRIGGER delete_fndds_nutrients 
    AFTER DELETE ON fndds_items
    FOR EACH ROW
        BEGIN 
            DELETE FROM fndds_nutrients WHERE fdc_id = OLD.fdc_id;
        END;


CREATE TRIGGER delete_fndds_measures
     AFTER DELETE ON fndds_items
     FOR EACH ROW
        BEGIN 
            DELETE FROM fndds_measures WHERE fdc_id = OLD.fdc_id;
        END;


-- CREATE TABLE IF NOT EXISTS [nutrient_metadata] (
--     [nutrient_id] INT PRIMARY KEY
--     , [nutrient_name] TEXT NOT NULL
--     , [fndds_description] TEXT NOT NULL
--     , [nutrient_category] TEXT NOT NULL     --Proximates, Minerals etc...
--     , [unit_name] TEXT NOT NULL
--     , [nutrient_number] INT
-- );

-- fdc_id, 
-- item_name, 
-- description, 
-- additional_description, 
-- data_type, 
-- published_date, 
-- category, 
-- subcategory, 
-- fndds_subcategory, 
-- fndds_subcategory_id

-- 'foodNutrientId'
-- 'nutrientId',
-- 'nutrientName',
-- 'nutrientNumber'
-- 'unitName',
-- 'value',

