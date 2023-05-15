# LoopMaker: A random curve generator
The LoopMaker app lets you easily create random 3D loops with the click of a button. You can customize your loops using intuitive controls and tweak the scaling to your liking. Additionally, the app produces a datafile that you can use to further analyze and manipulate your curves.

See the [LoopMaker](https://loopmaker.streamlit.app/) app in production!

## Motivation
Having access to adequate datasets for closed curves is crucial in the field of computational topology. Such datasets are not only useful for testing simulations, but also find application in various areas where trajectories are used, such as drones and unmanned vehicles. Additionally, the study of curves is a fundamental aspect of geometry and can be of immense value in computer vision. Thus, the LoopMaker app can provide researchers and enthusiasts with a platform to generate and explore a vast array of random closed curves, facilitating advancements in diverse fields.

One a personal note, I wish I had this app several years ago during my PhD research to experiment with some of my unconventional ideas.
## Requirements

- Python 3.10.6 or later
- Required Python packages (see `requirements.txt`)

Install required packages in a your virtual environment using
```
pip install -r requirements.txt
```
## Usage

Run the `Home.py` as
```
streamlit run Home.py
```

## LoopMaker in action
<p align="center">
  <img width="800" src="https://github.com/rahulor/linking-number/assets/69508071/a93f8a23-42b4-48fc-b4a4-9dd77882bfc7" alt>
</p>
<p align="center">
Lk = 0 if the loops are unlinked, whereas Lk = 1 if they are linked.
</p>
