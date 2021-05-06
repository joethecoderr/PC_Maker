from sklearn.cluster import KMeans
import joblib
import transformers
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def Create_New_Model(df, clusters, model_name):
    model = KMeans(n_clusters=clusters)
    model.fit(df)
    joblib.dump(model, f"Models/{model_name}.pkl")
    


def Create_New_Transformers(df):

    
    clean_GB = transformers.clean_GB_df()
    df = clean_GB.transform(df, "size")
    df = clean_GB.transform(df, "Ram") 
    Ram_scaler_low = StandardScaler()
    size_scaler_low = StandardScaler()
    
    df[["size_scaled"]] = size_scaler_low.fit_transform(df[["size"]])
    df[["Ram_scaled"]] = Ram_scaler_low.fit_transform(df[["Ram"]])
    
    joblib.dump(size_scaler_low, "Transformers/size_scaler_rec.pkl")
    joblib.dump(Ram_scaler_low, "Transformers/Ram_scaler_rec.pkl")

    OHE_processor_low = transformers.OneHotEncoder_transformer("Processor")
    OHE_processor_low.fit(df, "Processor")
    df =  OHE_processor_low.transform(df, "Processor")
    joblib.dump(OHE_processor_low, "Transformers/OHE_processor_rec.pkl")
    
    OHE_Graphics_low = transformers.OneHotEncoder_transformer("Graphics")
    OHE_Graphics_low.fit(df, "Graphics")
    df =  OHE_Graphics_low.transform(df, "Graphics")
    joblib.dump(OHE_Graphics_low, "Transformers/OHE_Graphics_rec.pkl")
    
    windows_transformer = transformers.Round_Windows()
    df["OS"] = windows_transformer.fit_transform(df["OS"])
    OHE_Windows_low = transformers.OneHotEncoder_transformer("OS")
    OHE_Windows_low.fit(df, "OS")
    df = OHE_Windows_low.transform(df, "OS")
    joblib.dump(OHE_Windows_low, "Transformers/OHE_Windows_rec.pkl")

    df = df.drop([ "DirectX", "Notes", "Description", "Game Name", "id"], axis=1)
    PCA_transformer_90_low = PCA(n_components=0.90)
    print(df.shape)
    df = PCA_transformer_90_low.fit_transform(df.drop(["Graphics", "Processor","size", "Ram", "OS"], axis=1))
    joblib.dump(PCA_transformer_90_low, "Transformers/PCA_transformer_90_rec.pkl")
    return df