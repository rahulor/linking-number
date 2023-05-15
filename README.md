# Linking number
- Generates random loops using the [LoopMaker](https://loopmaker.streamlit.app/) app.
- Computes the [linking number](https://en.wikipedia.org/wiki/Linking_number#Gauss's_integral_definition) which can be considered as a label corresponding to a loop-combination.
- Visualize it from the data-file for further analysis if needed.

- [in progress] Classification task using deep neural network

See the [linking-number.streamlit.app](https://linking-number.streamlit.app/) app in production!

## Requirements

- Python 3.10.6 or later
- Required Python packages (see `requirements.txt`)

Install required packages in your virtual environment using
```
pip install -r requirements.txt
```
## Usage
Run the script `Home.py` as
```
streamlit run Home.py
```

The data has been already generated and available in the directory `data`. One can re-run the code and modify the data using
```
python curve.py
```
Look at `inputs.py` to change the parameters.


## Visualization
<p align="center">
  <img width="800" src="https://github.com/rahulor/linking-number/assets/69508071/5b189a41-38eb-4012-858e-60aebd19a550" alt>
</p>
<p align="center">
Lk = 0 if the loops are unlinked, whereas Lk = 1 if they are linked.
</p>
