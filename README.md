# Install 
```
virtualenv venv # Path can't have spaces
source venv/bin/activate
pip install tensorflow
pip install pandas scikit-learn scipy numpy
```

# Run 
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

Try some mock music data
Use real music data
Split training script and prediction script, passing model files
Figure out how to save log and model into organized folders
  - Need to highlight parameters and assumptions
Automatic Train/Test splitting 
Automatic parameter selection

