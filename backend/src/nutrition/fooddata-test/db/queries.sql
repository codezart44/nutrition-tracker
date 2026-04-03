


CREATE TABLE IF NOT EXISTS food_items (
    fdc_id                      INT PRIMARY KEY,
    [description]               TEXT,
    additional_descriptions     TEXT,
    data_type                   TEXT,
    published_date              DATE,
    food_category               TEXT,
    food_category_id            INT,
    food_nutrients              JSON,
    food_measures               JSON,
    food_icon                   TEXT            -- SVG files consist of XML text
);


-- 'fdcId',
-- 'description',
-- 'additionalDescriptions',
-- 'dataType',
-- 'publishedDate',
-- 'foodCategory',
-- 'foodCategoryId',
-- 'foodNutrients', 
-- 'foodMeasures', 




-- CREATE TABLE IF NOT EXISTS proximates (
--     fdc_id                      INT PRIMARY KEY,
--     water                       JSON,
--     energy                      JSON,
--     protein                     JSON,
--     fat                         JSON
-- );

-- CREATE TABLE IF NOT EXISTS carbohydrates (
--     fdc_id                      INT PRIMARY KEY,
--     carbohydrate                JSON,
--     fiber                       JSON,
--     sugars                      JSON
-- );


-- CREATE TABLE IF NOT EXISTS minerals (
--     fdc_id                      INT PRIMARY KEY,
--     calcium                     JSON,
--     iron                        JSON,
--     magnesium                   JSON,
--     phosphorus                  JSON,
--     potassium                   JSON,
--     sodium                      JSON,
--     zinc                        JSON,
--     copper                      JSON,
--     selenium                    JSON
-- );


-- CREATE TABLE IF NOT EXISTS vitamins (
--     fdc_id                      INT PRIMARY KEY,
--     vitamin_C                   JSON,
--     thiamin                     JSON,
--     riboflavin                  JSON,
--     niacin                      JSON,
--     vitamin_B6                  JSON,
--     folate_total                JSON,
--     folic_acid                  JSON,
--     folate_food                 JSON,
--     folate_DFE                  JSON,
--     choline_total               JSON,
--     vitamin_B12                 JSON,
--     vitamin_B12_added           JSON,
--     vitamin_A                   JSON,
--     retinol                     JSON,
--     carotene_beta               JSON,
--     carotene_alpha              JSON,
--     cryptoxanthin_beta          JSON,
--     lycopene                    JSON,
--     lutein_zeaxanthin           JSON,
--     vitamin_E                   JSON,
--     vitamin_E_added             JSON,
--     vitamin_D                   JSON,
--     vitamin_K                   JSON
-- );


-- CREATE TABLE IF NOT EXISTS other (
--     fdc_id                      INT PRIMARY KEY,
--     sfa_tot                     JSON,
--     mufa_tot                    JSON,
--     pufa_tot                    JSON,
--     cholesterol                 JSON,
--     alcohol                     JSON,
--     caffeine                    JSON,
--     theobromine                 JSON
-- );



-- Trigger function making all child tables inherit the ids inserted into movie_base (parent)
-- CREATE TRIGGER insert_id_trigger
--     AFTER INSERT ON base
--     FOR EACH ROW
--     BEGIN
--         INSERT INTO proximates      (fdc_id) VALUES (NEW.fdc_id);
--         INSERT INTO carbohydrates   (fdc_id) VALUES (NEW.fdc_id);
--         INSERT INTO minerals        (fdc_id) VALUES (NEW.fdc_id);
--         INSERT INTO vitamins        (fdc_id) VALUES (NEW.fdc_id);
--         INSERT INTO other           (fdc_id) VALUES (NEW.fdc_id);
--     END;

-- CREATE TRIGGER delete_id_trigger
--     AFTER DELETE ON base
--     FOR EACH ROW
--     BEGIN
--         DELETE FROM proximates      WHERE fdc_id = OLD.fdc_id;
--         DELETE FROM carbohydrates   WHERE fdc_id = OLD.fdc_id;
--         DELETE FROM minerals        WHERE fdc_id = OLD.fdc_id;
--         DELETE FROM vitamins        WHERE fdc_id = OLD.fdc_id;
--         DELETE FROM other           WHERE fdc_id = OLD.fdc_id;
--     END;


-- DANGER
-- DROP TABLE food_items;
-- DROP TABLE proximates;
-- DROP TABLE carbohydrates;
-- DROP TABLE minerals;
-- DROP TABLE vitamins;
-- DROP TABLE other;