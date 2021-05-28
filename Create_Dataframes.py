import pymysql
import pandas as pd

from db import connection_string
def get_data(table_name_low,table_name_rec ):
    conn = pymysql.connect(**connection_string)
    cursor=conn.cursor()
    conn.connect()
    try:
      cursor.execute(f"SELECT * FROM dbname.{table_name_low}")
      rows_low_pcgamebenchmark = cursor.fetchall()
    
      cursor.execute(f"SELECT * FROM dbname.{table_name_rec}")
      rows_rec_pcgamebenchmark = cursor.fetchall()
    
      return rows_low_pcgamebenchmark, rows_rec_pcgamebenchmark
    finally:
    
        conn.close()
        
        
def create_dataframes(table_name_low, table_name_rec):
    rows_low, rows_rec = get_data(table_name_low, table_name_rec)
    low_df = pd.DataFrame(rows_low, columns = ["id", "Game Name", "Description", "OS", "Processor", "Ram", "Graphics", "DirectX", "size", "Notes"])
    rec_df = pd.DataFrame(rows_rec, columns = ["id", "Game Name", "Description", "OS", "Processor", "Ram", "Graphics", "DirectX", "size", "Notes"])
    return low_df, rec_df

def get_games():
    conn = pymysql.connect(**connection_string)
    cursor=conn.cursor()
    conn.connect()
    try:
      cursor.execute(f"SELECT Game_Name FROM low_req_canyourunit")
      games = [item[0] for item in cursor.fetchall()]
    except:
        return None
    return games

if __name__ == '__main__':
    pass
