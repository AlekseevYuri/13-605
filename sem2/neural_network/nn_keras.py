import os
import numpy as np
import math
from tensorflow.keras import models, layers

def t(x,y):
    if abs(x)+abs(y) <= 2 and  x**2+y**2 >= 0.5:
        return 1
    else:
        return 0

XY = np.random.random((5_000, 2)).astype(np.float32) * 4.0 - 2.0

Z = np.array([t(x,y) for [x,y] in XY] , dtype=np.float32)

model = models.Sequential([
    layers.InputLayer(input_shape=(2,)),
    layers.Dense(100, activation='sigmoid', use_bias=True),
    layers.Dense(20, activation='sigmoid', use_bias=True),
    layers.Dense(1, activation='sigmoid', use_bias=False)
])

model.compile(
    loss='mean_squared_error',
    optimizer='adam',
    metrics='accuracy'
)

if  os.path.isfile("smart_duckling_colab.h5"):
    print("Loading existing synapses...")
    model.load_weights("smart_duckling_colab.h5")
else:
    print("Training the duckling...")
    model.fit(
        XY, Z,
        epochs=1000,
        batch_size=1000,
        use_multiprocessing=True,
        verbose=False
    )
    model.save("smart_duckling_colab.h5")

print("Done,", model.evaluate(XY, Z))



import matplotlib.pyplot as plt

plt.axis('equal')

c = np.linspace(-2,2,50)


XY = np.transpose([np.tile(c, len(c)), np.repeat(c, len(c))])

Z = model.predict(XY)

for (x, y), z in zip(XY, Z):
    plt.scatter(x, y, c='red' if z[0] >= 0.5 else 'green', marker='.')

plt.show()


