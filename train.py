# Import libraries.
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

import numpy as np
import os
import pandas as pd
import pickle


# Load train dataset.
df_train = pd.read_csv('data/train.csv')

# Load informations of the model.
model_info = 'model/relevant_columns.bin'
with open(model_info, 'rb') as f:
    relevant_columns = pickle.load(f)
    f.close()

# Select relevant columns
df_train = df_train[relevant_columns]

# Split predictors and target
y_train = df_train.target.values
del df_train['target']
X_train = df_train.values

model = RandomForestClassifier(criterion='entropy', min_samples_leaf=1, min_samples_split=2, n_estimators=100, verbose=5)
model.fit(X_train, y_train)

# Load the test dataset.
df_test = pd.read_csv('data/test.csv')

# Select relevant columns.
df_test = df_test[relevant_columns]

# Split predictors and target.
y_test = df_test.target.values
del df_test['target']
X_test = df_test.values

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f'Training score: {train_score}')
print(f'Testing score: {test_score}')

MODEL_PATH = 'model'
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
    print('Directory was created!')

# Save the results of the model.
with open(f'{MODEL_PATH}/scores_model.txt', 'w') as f:
	l1 = 'CREDIT CARD FRAUD ML DETECTION'
	l2 = '\n'
	l3 = f'Training score: {train_score}'
	l4 = f'Testing score: {test_score}'
	f.writelines([l1, l2, l3, l4])

# Save the model.    
with open(f'{MODEL_PATH}/model.bin', 'wb') as f:
    pickle.dump(model, f)
    f.close()
