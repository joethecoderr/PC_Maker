import pymysql
import pandas as pd
def get_data(table_name_low,table_name_rec ):
    conn = pymysql.connect(
        host='pcmakerinstance.c15oncijbytw.us-east-2.rds.amazonaws.com',
        port=int(3306),
        user="admin",
        passwd="password",
        db="dbname",
        )
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