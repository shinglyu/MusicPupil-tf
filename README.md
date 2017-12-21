# Install 
```
virtualenv -p python3 venv # Path can't have spaces
source venv/bin/activate
pip install tensorflow
pip install pandas scikit-learn scipy numpy pytest music21
```

# Run 
## Unittest 

```
python -m pytest
```

## Training
* Extract the data, see the README.md in feature_extractor/
* Put the data in `data/`
* Run 
```
source venv/bin/activate
python train.py
```
* Output:
  * Model in `exported_model/`
  * logs in `logs/`

* To inspect the training process:

```
tensorboard --logdir=logs
```
TODO:

Split training script and prediction script, passing model files
  - v Save the model after training
  - Write a prediction script that takes the model and make prediction
  - Use reverse feature_extractor to recreate music
Make all the file path configurable
Support multiple input and output
v Try some mock music data
v Use real music data
Figure out how to save log and model into organized folders
  - Need to highlight parameters and assumptions
v Automatic Train/Test splitting 
Automatic parameter selection
Use the audio and visual dashboard in TensorBoard
Test Python3
v Connect feature extractor output to TF

