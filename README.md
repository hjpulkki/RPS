# RPS
Deep learing for Rock-Paper-Scissors using keras. The goal is to predict the next move from the earlier moves that the player has made. Ideally this model could be used in an online game to collect a lot of training data for even better models. As for now, the training dataset contains only a couple of games me and my friends played with this.

This was my hobby project when I was learning about recurrent neural networks. Hopefully this could also be useful piece of code for others who want to learn more about this stuff :).

## Instructions
On linux command line:

    git clone https://github.com/hjpulkki/RPS.git
    cd RPS
    pip install venv
    source venv/bin/activate to enter the virtual environment
    pip install -r requirements.txt
    
Now you are ready to start a new game with
    python RPS.py

## RPS.py
Main application which gives predictions on the opponents next move. Uses RPS_model.h5 as the model to do these predictions. Saves all played games as new lines in data.txt

## RPS_learner.py
Creates a new model, teaches it with data from data.txt and saves the model to RPS_model.h5. This script is very computationaly expensive.

## RPS_model.h5
Machine learning model created by RPS_learner.py and used by RPS.py

## data.txt
Data file. Each row is one series of RPS games and contains what the opponent played during that game. 0 means Rock, 1 Paper, and 2 Scissors. TODO: Add players own actions also to the data file.