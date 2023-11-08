from flask import Flask
from flask import request, jsonify

import pandas as pd
import pickle

with open('model/relevant_columns.bin', 'rb') as f:
    relevant_columns = pickle.load(f)
    f.close()

with open('model/model.bin', 'rb') as f:
    model = pickle.load(f)
    f.close()

app = Flask('credit_card_fraud_detection')

@app.route('/predict', methods=['POST'])
def predict():
    sample = request.get_json()
    sample = pd.Series(sample)
    X = sample[relevant_columns]
    X = X.values
    y_pred = model.predict_proba(X)[0, 1]
       
    result = {
        'probability': float(y_pred),
    }
    
    return jsonify(result)
	
if __name__ == '__main__':
	 app.run(debug=True, host='0.0.0.0', port=9696)

