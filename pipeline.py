import transformers
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
def import_model_transformers():
    pass
    
def transform_input(input_data):
    OHE_processor_low = joblib.load("Transformers/OHE_processor_rec.pkl")
    OHE_Graphics_low = joblib.load("Transformers/OHE_Graphics_rec.pkl")
    OHE_Windows_low = joblib.load("Transformers/OHE_Windows_rec.pkl")
    size_scaler_low = joblib.load("Transformers/size_scaler_rec.pkl")
    Ram_scaler_low = joblib.load("Transformers/Ram_scaler_rec.pkl")
    PCA_transformer_90_low = joblib.load("Transformers/PCA_transformer_90_rec.pkl")
    df = pd.DataFrame(input_data, columns = ["id", "Game Name", "Description", "OS", "Processor", "Ram", "Graphics", "DirectX", "size", "Notes"])
    clean_GB = transformers.clean_GB_df()
    df = clean_GB.transform(df, "size")
    df = clean_GB.transform(df, "Ram") 

    df = OHE_processor_low.transform(df, "Processor")
    df = OHE_Graphics_low.transform(df, "Graphics")
    windows_transformer = transformers.Round_Windows()
    df["OS"] = windows_transformer.fit_transform(df["OS"])
    df = OHE_Windows_low.transform(df, "OS")
    df[["size_scaled"]] = size_scaler_low.transform(df[["size"]])
    df[["Ram_scaled"]] = Ram_scaler_low.transform(df[["Ram"]])
    df = df.drop([ "DirectX", "Notes", "Description", "Game Name", "id"], axis=1)
    df = PCA_transformer_90_low.transform(df.drop(["Graphics", "Processor","size", "Ram", "OS"], axis=1))
    
    return df