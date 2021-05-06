# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:39:13 2021

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
    # transformed_df = model_manage.Create_New_Transformers(df_rec)
    # model_manage.Create_New_Model(transformed_df, 7, "test_model")

    
    
    # #new_instance_low = [['887', 'Cyberpunk 2077', 'dummy descr ', ' Windows 7 64-Bit', ' Intel Core i5-3570K', ' 8 GB',  " NVIDIA GeForce GTX 780", '', ' 70 GB', ""]]
    # new_instance_low = [['887', 'BioShock Infinite', 'Indebted to the wrong people with his life on the line veteran of the U S Cavalry and now hired gun Booker DeWitt has only one opportunity to wipe his slate clean He must rescue Elizabeth a mysterious girl imprisoned since childhood and locked up in the flying city of Columbia ', ' Windows Vista Service Pack 2 32-bit', ' Intel Core 2 Duo Q6867', ' 2 GB', ' ATI Radeon HD 3870', '', ' 20 GB', ""]]
    # #new_instance_low = [['1', 'fornite', 'dummy descr', ' Windows 7/8/10 64-bit', ' Intel Core i3-2100', ' 4 GB', ' Intel HD 4000', '', ' 15 GB', ""]]
    # instance_transformed = pipeline.transform_input(new_instance_low)
    # model = joblib.load("Models/test_model.pkl")
    # unique, counts = np.unique(model.labels_, return_counts=True)
    # print(unique, counts)
    # print(model.predict(instance_transformed))
    
if __name__ == '__main__':
    main()