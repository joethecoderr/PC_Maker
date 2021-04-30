import joblib
import numpy as np

from flask import Flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import Create_Dataframes
import joblib
import pipeline
import transformers
import model_manage

app = Flask(__name__)
CORS(app,supports_credentials=True, resources={r'/.*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':

  
        id = request.form.get('id')
        name = request.form.get('name')
        descr = request.form.get('descr')
        windows = request.form.get('windows')
        processor = request.form.get('processor')
        ram = request.form.get('ram')
        graphics = request.form.get('graphics')
        DirectX = request.form.get('DirectX')
        size = request.form.get('size')
        Notes = request.form.get('Notes')
    
        new_instance_low = [[f' {id}', f' {name}', f' {descr}', f' {windows}',f' {processor}', f' {ram}', f' {graphics}', f' {DirectX}', f' {size}', f' {Notes}']]
        instance_transformed = pipeline.transform_input(new_instance_low)
        model = joblib.load("Models/test_model.pkl")
        result = model.predict(instance_transformed)
        
        df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
        Graphics = []
        cluster_predicted_idx = np.where(model.labels_==result[0])
        for idx in cluster_predicted_idx[0]:
            Graphics.append(df_low['Graphics'][idx])
         
        unique, counts = np.unique(Graphics, return_counts=True)
            
        max_value = max(counts) 
        max_graphic = unique[np.where(counts==max_value)]
        return jsonify({'Prediction':str(max_graphic) })

@app.route('/try', methods=['GET', 'POST'])
@cross_origin(allow_headers=['Content-Type' ], supports_credentials=True)
def hello2():
    if request.method == 'POST':
        #age = request.form.get('age')
        pass
        if prediction[0] == 1:
            pass
        else:
            pass
        
if __name__ == "__main__":
    app.run()
