#!/usr/bin/env python
import pickle
import tensorflow as tf
import pandas as pd
import numpy as np
import subprocess
from sklearn.preprocessing import MinMaxScaler

def main():
    # TODO: hardcoded path, use argparse
    #testing_data_df = pd.read_csv("data/test_0_testing.csv", dtype=float)
    #np.save("data/test_0_testing.npy", testing_data_df.as_matrix())
    #subprocess.run(['saved_model_cli', 'run', '--dir', 'exported_model', '--inputs', 'data/test_-1_)testing.npy'])

    # TODO: hardcoded path, use argparse
    export_dir = "./exported_model"
    with tf.Session() as session:
        tf.saved_model.loader.load(session, [tf.saved_model.tag_constants.SERVING], export_dir)

        testing_data_df = pd.read_csv("data/test_0_testing.csv", dtype=float)
        target = "midi_velocity" # How to handle multiple variable?
        X_testing = testing_data_df.drop(target, axis=1).values
        X_scaler = pickle.load(open('exported_model/x_scaler.pkl', 'rb'))
        Y_scaler = pickle.load(open('exported_model/y_scaler.pkl', 'rb'))
        X_scaled = X_scaler.transform(X_testing)
        print(X_scaled)

        #for op in session.graph.get_operations():
            #print(op)
        prediction = session.graph.get_operation_by_name("output/prediction").outputs[0]

        Y_predicted_scaled = session.run(prediction, feed_dict={'input/Placeholder:0': X_scaled})
        #Y_predicted_scaled = session.run('tensorflow/serving/predict', feed_dict={'input/Placeholder:0': X_scaled})

        # Unscale the data back to it's original units (dollars)
        #Y_scaler = MinMaxScaler(feature_range=(0, 1))
        Y_predicted = Y_scaler.inverse_transform(Y_predicted_scaled)
        print(Y_predicted)

if __name__ == "__main__":
    main()
