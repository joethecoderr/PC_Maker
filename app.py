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
import scrap_main 

app = Flask(__name__)
CORS(app,supports_credentials=True, resources={r'/.*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
<<<<<<< HEAD
@app.route('/get_games', methods = ['GET'])
def get_games():
    games = Create_Dataframes.get_games()
    if games is not None:
        return jsonify(games)
    else:
        return jsonify({'Error': 'No se encontraron juegos'})

=======
>>>>>>> 66a7e32964a939968814082d4b7d280b8c876ad7
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        id = request.form.get('id')
<<<<<<< HEAD
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
        Processors = []
        cluster_predicted_idx = np.where(model.labels_==result[0])
        for idx in cluster_predicted_idx[0]:
            Graphics.append(df_rec['Graphics'][idx])
            Processors.append(df_rec["Processor"][idx])
        unique_graphics, counts_graphics = np.unique(Graphics, return_counts=True)
        unique_processors,counts_processors = np.unique(Processors, return_counts=True)
        max_value_graphics = max(counts_graphics) 
        max_graphic = unique_graphics[np.where(counts_graphics==max_value_graphics)]
        max_value_processors = max(counts_processors) 
        max_processor = unique_processors[np.where(counts_processors==max_value_processors)]
        return jsonify({'Graphic Card':str(max_graphic),
                        'Processor':str(max_processor),
                        'Ram': str(ram), 
                        'Disk Space': str(size)
                        })

=======
        game = request.form.get('name')
        #look on db for req
        new_instance = Create_Dataframes.look_for_game_db(game, "rec_req_pcbenchmark")
        if len(new_instance) > 0:
            instance_transformed = pipeline.transform_input(new_instance)
            model = joblib.load("Models/test_model.pkl")
            result = model.predict(instance_transformed)
            df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
            Graphics = []
            Processors = []
            cluster_predicted_idx = np.where(model.labels_==result[0])
            for idx in cluster_predicted_idx[0]:
                Graphics.append(df_rec['Graphics'][idx])
                Processors.append(df_rec["Processor"][idx])
            unique_graphics, counts_graphics = np.unique(Graphics, return_counts=True)
            unique_processors,counts_processors = np.unique(Processors, return_counts=True)
            max_value_graphics = max(counts_graphics) 
            max_graphic = unique_graphics[np.where(counts_graphics==max_value_graphics)]
            max_value_processors = max(counts_processors) 
            max_processor = unique_processors[np.where(counts_processors==max_value_processors)]
            return jsonify({'Graphic Card':str(max_graphic),
                            'Processor':str(max_processor),
                            'Ram': new_instance["Ram"][0], 
                            'Disk Space': new_instance["size"][0]
                            })
        else :
            #Scrap, save, train and save model
            scrap_main.scrap_save_new_game(game)
            
            df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
            transformed_df = model_manage.Create_New_Transformers(df_low)
            model_manage.Create_New_Model(transformed_df, 7, "test_model")
            instance_transformed = pipeline.transform_input(new_instance)
            model = joblib.load("Models/test_model.pkl")
            result = model.predict(instance_transformed)
            df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
            Graphics = []
            Processors = []
            cluster_predicted_idx = np.where(model.labels_==result[0])
            for idx in cluster_predicted_idx[0]:
                Graphics.append(df_rec['Graphics'][idx])
                Processors.append(df_rec["Processor"][idx])
            unique_graphics, counts_graphics = np.unique(Graphics, return_counts=True)
            unique_processors,counts_processors = np.unique(Processors, return_counts=True)
            max_value_graphics = max(counts_graphics) 
            max_graphic = unique_graphics[np.where(counts_graphics==max_value_graphics)]
            max_value_processors = max(counts_processors) 
            max_processor = unique_processors[np.where(counts_processors==max_value_processors)]
            return jsonify({'Graphic Card':str(max_graphic),
                            'Processor':str(max_processor),
                            'Ram': new_instance["Ram"][0], 
                            'Disk Space': new_instance["size"][0]
                            })
            
>>>>>>> 66a7e32964a939968814082d4b7d280b8c876ad7
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
