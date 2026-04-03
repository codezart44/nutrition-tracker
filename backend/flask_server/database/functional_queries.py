
from pprint import pprint
import sqlite3
import numpy as np
import os
import json



def get_col_names(table_name: str, con: sqlite3.Connection) -> list[str]:
    '''
    '''
    cur = con.cursor()

    sql_get_cols = f"""
    --sql
    PRAGMA table_info({table_name})
    ;
    """
    cur.execute(sql_get_cols)
    col_info = cur.fetchall()
    cur.close()

    col_names = [info[1] for info in col_info]

    return col_names

def update_row(table_name:str, row_id:int, col_names:list, row:list, con:sqlite3.Connection) -> None:
    '''
    '''
    assert row[0] == row_id
    args = row[1:]

    cur = con.cursor()
    cols_sql = ', '.join([f'{col} = ?' for col in col_names[1:]])

    sql_update = f"""
    --sql
    UPDATE {table_name} SET {cols_sql}
        WHERE fdc_id = {row_id}  
    ;
    """
    cur.execute(sql_update, args)
    cur.close()

    con.commit()

def insert_row(table_name:str, col_names:list, row:list, con:sqlite3.Connection) -> None:
    '''
    '''
    cur = con.cursor()
    cols_sql = ', '.join(col_names)
    params_sql = ','.join(['?' for _ in col_names])

    sql_insert = f"""
    --sql
    INSERT INTO {table_name} ({cols_sql}) 
        VALUES ({params_sql})  
    ;
    """
    cur.execute(sql_insert, row)
    cur.close()

    con.commit()

def insert_multiple_rows(table_name:str, col_names:list, rows:list[list], con:sqlite3.Connection) -> None:
    '''
    '''
    cur = con.cursor()
    cols_sql = ', '.join(col_names)
    params_sql = ','.join(['?' for _ in col_names])

    sql_insert = f"""
    --sql
    INSERT INTO {table_name} ({cols_sql}) 
        VALUES ({params_sql})  
    ;
    """
    cur.executemany(sql_insert, rows)
    cur.close()

    con.commit()

def delete_row(table_name:str, row_id:int, con:sqlite3.Connection) -> None:
    '''
    '''
    cur = con.cursor()

    sql_delete = f"""
    --sql
    DELETE FROM {table_name} WHERE fdc_id = ?
    ;
    """
    cur.execute(sql_delete, (row_id, ))
    cur.close()
    con.commit()

def get_rows(table_name:str, row_ids:list, con:sqlite3.Connection) -> list:
    '''
    '''
    cur = con.cursor()
    params_sql = ','.join(['?' for id in row_ids])

    sql_fetch = f"""
    --sql
    SELECT * FROM {table_name}
        WHERE fdc_id in ({params_sql})
    ;
    """
    cur.execute(sql_fetch, row_ids)
    rows = cur.fetchall()

    cur.close()
    con.commit()

    return rows





def __main():
    
    fdc_id = 1234567        # NOTE for testing
    test_row = [fdc_id, 'chedddar', 'creamy', 'FNDDS', '2018-10-15', 'cheese, cheddar', 2124345, '{nutrients...}', '{food_measures...}', np.nan]

    db_path = os.path.dirname(__file__)+'/food.db'
    con = sqlite3.connect(db_path)
    
    table_name = 'fndds_foods'

    col_names = get_col_names(table_name=table_name, con=con)
    print(col_names)

    test_ids = [2344665, 2344662]
    rows = get_rows(table_name=table_name, row_ids=test_ids, con=con)
    print(rows)
    # update_row(table_name=table_name, row_id=fdc_id, col_names=col_names, row=test_row, con=con)

    # insert_row(table_name=table_name, col_names=col_names, row=test_row, con=con)

    # NOTE-XXX WARNING - REMEMBER IT ALSO DELETES THE id, THE WHOLE ROW
    # delete_row(row_id=fdc_id, table_name=table_name, con=con)

    con.close()



if __name__=='__main__':
    __main()

