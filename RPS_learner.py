import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, LSTM

EPOCH_NP = 20

INPUT_SHAPE = (1, -1, 1)
OUTPUT_SHAPE = (1, -1, 3)

DATA_FILE = "data.txt"
MODEL_FILE = "RPS_model.h5"


def simple_model():
    # Creates a simle model
    new_model = Sequential()
    new_model.add(LSTM(units=64, input_shape=(None, 1), return_sequences=True, activation='sigmoid'))
    new_model.add(LSTM(units=64, return_sequences=True, activation='sigmoid'))
    new_model.add(LSTM(units=64, return_sequences=True, activation='sigmoid'))
    new_model.add(Dense(64, activation='relu'))
    new_model.add(Dense(64, activation='relu'))
    new_model.add(Dense(3, activation='softmax'))
    new_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy', 'categorical_crossentropy'])
    return new_model

def batch_generator(filename):
    # Generate teaching data tensors from a data file
    with open('data.txt', 'r') as data_file:
        for line in data_file:
            # Convert line to numpy array
            data_vector = np.array(list(line[:-1]))
            data_vector = data_vector.astype(np.float)

            # The three dimensions are: 
            #    samples (we have only 1),
            #    time steps (different rounds of the game, variable). Leave out the last value
            #    features (we have only 1)
            input_data = data_vector[np.newaxis, :-1, np.newaxis]

            temp = np_utils.to_categorical(data_vector, num_classes=3)
            # Missing column accounts for missing datasets
            output_data = temp[np.newaxis, 1:]   # Leave out the first value.
            yield (input_data, output_data)


# Create model
np.random.seed(7)
model = simple_model()


# Load data and train
for i in range(EPOCH_NP):    # manual epochs
    for (input_data, output_data) in batch_generator('data.txt'):
            model.fit(input_data, output_data, epochs=1, batch_size=100)

# Do built-in evaluation
print("evaluating")
validation = '100101000110221110101002201101101101002201011012222210221011011101011122110010101010101'
input_validation = np.array(list(validation[:-1])).reshape(INPUT_SHAPE)
input_validation = input_validation.astype(np.float)
output_validation = np_utils.to_categorical(np.array(list(validation[1:]))).reshape(OUTPUT_SHAPE)
loss_and_metrics = model.evaluate(input_validation, output_validation, batch_size=100)
print("\n Evaluation results")
for i in range(len(loss_and_metrics)):
    print(model.metrics_names[i], loss_and_metrics[i])

# Test to predict a pretty easy sequence
input_test = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2]).reshape(INPUT_SHAPE)
res = model.predict(input_test)
prediction = np.argmax(res[0], axis=1)
print(res, prediction)

model.save(MODEL_FILE)
del model
