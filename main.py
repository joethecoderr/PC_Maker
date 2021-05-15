# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:19:31 2021

@author: jesus
"""
import Create_Dataframes
import joblib
import pipeline
import transformers
import model_manage
import numpy as np
def main():
    
    
    # df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
    # transformed_df = model_manage.Create_New_Transformers(df_low)
    # model_manage.Create_New_Model(transformed_df, 7, "test_model")

    
    
   
    #new_instance = [['887', 'BioShock Infinite', 'Indebted to the wrong people with his life on the line veteran of the U S Cavalry and now hired gun Booker DeWitt has only one opportunity to wipe his slate clean He must rescue Elizabeth a mysterious girl imprisoned since childhood and locked up in the flying city of Columbia ', ' Windows Vista Service Pack 2 32-bit', ' Intel Core 2 Duo Q6867', ' 2 GB', ' ATI Radeon HD 3870', '', ' 20 GB', ""]]
    new_instance =  Create_Dataframes.look_for_game_db("DIRT 5", "rec_req_pcbenchmark")
    
    if len(new_instance) > 0 :
        
        print(f'new instance = {new_instance}')
        print(len(new_instance))
        instance_transformed = pipeline.transform_input(new_instance)
        print(f'Transformed instance = {instance_transformed.shape}')
        model = joblib.load("Models/test_model.pkl")
        unique, counts = np.unique(model.labels_, return_counts=True)
        print(unique, counts)
        print(model.predict(instance_transformed))
        
        
    else:
         print("GAME NOT FOUND")
    
if __name__ == '__main__':
    main()
