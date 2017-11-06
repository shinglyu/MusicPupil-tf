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

v Try some mock music data
Use real music data
Split training script and prediction script, passing model files
  - v Save the model after training
  - Write a prediction script that takes the model and make prediction
Figure out how to save log and model into organized folders
  - Need to highlight parameters and assumptions
Automatic Train/Test splitting 
Automatic parameter selection
Use the audio and visual dashboard in TensorBoard
Test Python3
