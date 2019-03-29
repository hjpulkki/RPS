try:
    # On Windows
    import msvcrt as getch
except ModuleNotFoundError:
    # On Linux
    import getch

from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "data.txt"
MODEL_FILE = "RPS_model.h5"
KEY_MAP = {
    b'0': 0, b'1': 1, b'2': 2, b'r': 0, b'p': 1, b's': 2, b'R': 0, b'P': 1, b'S': 2, b'k': 0, b'K': 0,
    '0': 0, '1': 1, '2': 2, 'r': 0, 'p': 1, 's': 2, 'R': 0, 'P': 1, 'S': 2, 'k': 0, 'K': 0,
}
NAMES = {0: "Rock", 1: "Paper", 2: "Scissors"}
RESULTS = {0: "draw", 1: "win", -1: "lose"}
INPUT_SHAPE = (1, -1, 1)
DEBUG = False

model = load_model(MODEL_FILE)

# Test with user inputs
data = []
score = 0

prediction = 1
if DEBUG:
    print("The computer is planning to play", NAMES.get((prediction+1)%3))
while True:
    key = getch.getch()
    print("key", key)

    if key in ('q', 'Q', b'q', b'Q'):
        print("Exiting...")
        if len(data) > 10:
            # Add new data to data file
            with open(DATA_FILE, 'a') as data_file:
                data_file.write("".join(str(x) for x in data) + "\n")
        del model
        break

    if key in KEY_MAP:
        value = KEY_MAP.get(key)
    else:
        print("Invalid key. Press q to exit.")
        continue

    result = -((value - prediction) % 3 - 1)
    score += result
    print("Opponent played", NAMES.get(value), "Result:", RESULTS.get(result), "Score:", score)

    data.append(value)

    data_vector = np.array(data)
    input_data = data_vector[np.newaxis, :, np.newaxis]
    res = model.predict(input_data)

    # Print probabilites to the graph
    plt.clf()
    y = np.transpose(res[0][-21:])
    x = list(range(y.shape[1]))
    plt.stackplot(x, y)
    plt.pause(0.001)

    prediction = np.argmax(res[0][-1])
    accuracy = np.max(res[0][-1])/np.sum(res[0][-1])
    if DEBUG:
        print("The model predicts", NAMES.get(prediction), "with probability of", round(accuracy*100), "%. The computer is planning to play", NAMES.get((prediction+1)%3))
