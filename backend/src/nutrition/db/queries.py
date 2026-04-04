import sqlite3

def select_food_nutrient(
        con:sqlite3.Connection, 
        fdc_ids:list[int]
    ) -> list[dict]:
    if not fdc_ids: return []
    parameters = fdc_ids
    placeholders = ",".join(["?"] * len(fdc_ids))
    sql = f"""
        SELECT 
            fn.fdc_id,
            fn.nutrient_id,
            fn.nutrient_amount,
            n.nutrient_name,
            n.nutrient_unit,
            f.description,
            f.category_id,
            f.category_name,
            f.data_source,
            f.publication_date
        FROM food_nutrient fn
        JOIN food f ON fn.fdc_id = f.fdc_id
        JOIN nutrient n ON fn.nutrient_id = n.nutrient_id
        WHERE fn.fdc_id IN ({placeholders});
    """
    cur = con.execute(sql, parameters)
    return [dict(r) for r in cur.fetchall()]

def select_food_nutrient_summed(
        con: sqlite3.Connection, 
        fdc_ids: list[int], 
        amounts: list[int],
    ) -> list[dict]:
    if not fdc_ids: return []
    parameters = [e for tup in zip(fdc_ids, amounts) for e in tup]
    placeholders = ",".join(["(?,?)"] * len(fdc_ids))
    sql = f"""
    WITH params(fdc_id, food_amount) AS 
        ( VALUES {placeholders} )
    SELECT 
        n.nutrient_id,
        n.nutrient_name,
        n.nutrient_unit,
        SUM(params.food_amount * fn.nutrient_amount / 100.0) AS nutrient_amount
    FROM params
    JOIN food_nutrient fn ON params.fdc_id = fn.fdc_id
    JOIN nutrient n ON n.nutrient_id = fn.nutrient_id
    GROUP BY 
        n.nutrient_id,
        n.nutrient_name,
        n.nutrient_unit
    ORDER BY n.nutrient_id;
    """
    cur = con.execute(sql, parameters)
    return [dict(r) for r in cur.fetchall()]

def select_food(con: sqlite3.Connection, fdc_ids: list[int]) -> list[dict]:
    if not fdc_ids: return []
    parameters = fdc_ids
    placeholders = ",".join(["?"] * len(fdc_ids))
    sql = f"""
        SELECT 
            fdc_id,
            data_source,
            publication_date,
            description,
            category_id,
            category_name
        FROM food 
        WHERE fdc_id IN ({placeholders})
    """
    cur = con.execute(sql, parameters)
    return [dict(r) for r in cur.fetchall()]

def select_nutrient(con: sqlite3.Connection, nut_ids: list[int]) -> list[dict]:
    if not nut_ids: return []
    parameters = nut_ids
    placeholders = ",".join(["?"] * len(nut_ids))
    sql = f"""
        SELECT 
            nutrient_id,
            nutrient_name,
            nutrient_unit
        FROM nutrient
        WHERE nutrient_id IN ({placeholders});
    """
    cur = con.execute(sql, parameters)
    return [dict(r) for r in cur.fetchall()]
