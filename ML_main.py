import impt
import smooth
import pandas as pd





mypath=r"C:\Users\kzhuang\OneDrive\Seisware_Hackathon\code\LAS_notop"
keys = ['POR','GR','RHOB']
x = impt.mk_lib(mypath,keys)    

df_logs = pd.DataFrame.transpose(pd.DataFrame.from_dict(x))
print(df_logs)
df2 = pd.DataFrame(['POR'], ['GR'],['RHOB'])
pd.concat([df2,df_logs],ignore_index=False)
X = df_logs.drop('RHOB')
y = df_logs[2].apply(int)
print(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

import tensorflow as tf
feat_cols =[]
for col in X.columns:
    feat_cols.append(tf.feature_column.numeric_column(col))

input_func = tf.estimator.inputs.pandas_input_fn(x=X_train,y=y_train,batch_size=10,num_epochs=5,shuffle=True)

classifier = tf.estimator.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3,feature_columns=feat_cols)

classifier.train(input_fn=input_func,steps=50)

pred_fn = tf.estimator.inputs.pandas_input_fn(x=X_test,batch_size=len(X_test),shuffle=False)

note_predictions = list(classifier.predict(input_fn=pred_fn))

final_preds  = []

for pred in note_predictions:
    final_preds.append(pred['class_ids'][0])
    
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,final_preds))
