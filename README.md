# RPS
Deep learing for Rock-Paper-Scissors using keras

## RPS.py
Main application which gives predictions on the opponents next move. Uses RPS_model.h5 as the model to do these predictions. Saves all played games as new lines in data.txt

## RPS_learner.py
Creates a new model, teaches it with data from data.txt and saves the model to RPS_model.h5. This script is very computationaly expensive. A good GPU helps.

## RPS_model.h5
Machine learning model created by RPS_learner.py and used by RPS.py

## data.txt
Data file. Each row is one series of RPS games and contains what the opponent played during that game. 0 means Rock, 1 Paper, and 2 Scissors. TODO: Add players own actions also to the data file.