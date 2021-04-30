from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from scipy import stats
import pandas as pd
import numpy as np

class Round_Windows(BaseEstimator, TransformerMixin):
  def __init__(self):
    return
  def fit(self, X, y=None):
    return self
  def transform(self, X):
    X = ["Windows 7+" if "Windows 7" in os else os for os in X]
    X = ["Windows 10+" if "Windows 10" in os else os for os in X]
    X = ["Anything" if "Windows 10" not in os and "Windows 7" not in os else os for os in X]
    return X



class OneHotEncoder_transformer(BaseEstimator,TransformerMixin):
  
  def __init__(self, column):
    self.encoder = OneHotEncoder()
    self.column = column

  def fit(self, df, y=None):
    encoded_column = self.encoder.fit(df[[self.column]])
    print(self.encoder.categories_)
    print(len(self.encoder.categories_[0]))
  def transform(self, df, column):
    encoded_column = self.encoder.transform(df[[column]])
    encoded_column = encoded_column.toarray()
    for i in range(len(self.encoder.get_feature_names([column]))):
      df[self.encoder.get_feature_names([column])[i]] = encoded_column[:,i]
    return df



class clean_GB_df(BaseEstimator,TransformerMixin):
  def __init__(self):
    pass

  def fit(self, df, y=None):
    return self
 
  def transform(self, df, column):
    df[column] = df[column].replace('[GB]', '', regex=True)
    df[column] = df[column].replace('[RAM]', '', regex=True)
    df[column] = df[column].replace('[available space]', '', regex=True) 
    df[column] = [value if "M" not in value else str(int(value.replace("M",""))/1000) for value in df[column]]
    df[column] = df[column].str.strip()
    df[column] = df[column].replace(r'[a-zA-Z]+', '', regex=True)
    df[column] = df[column].replace('', '0', regex=True)
    df[column] = df[column].replace('Unknown', '0', regex=True)
    
    df = df[pd.to_numeric(df[column],errors='coerce').notnull()]
    df[column] = df[column].astype(float)
    df[column] = df[column].replace(0.0, np.mean(df[column]), regex=True)
    return df