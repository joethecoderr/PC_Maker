import joblib
import numpy as np
from flask import Flask
from flask import jsonify, request, make_response
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
@app.route('/get_games', methods = ['GET'])
def get_games():
    games = Create_Dataframes.get_games()
    if games is not None:
        return jsonify(games)
    else:
        return jsonify({'Error': 'No se encontraron juegos'})


@app.route('/train_model', methods = ['GET'])
def TrainModel():
    if request.method == 'GET':
        try:
            df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
            model_manage.Create_New_Model(df_rec, 10, "test_model")
            return make_response(jsonify({"message": "Success!"}), 200)
        except Exception:
            return make_response(jsonify({"message": "AAAAAAAAAAAAAA!"}),500)
       
    
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        id = request.form.get('id')
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
            print(unique_processors, counts_processors)
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
