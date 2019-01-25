''''''
'''
https://blog.csdn.net/baimafujinji/article/details/78384792
https://blog.csdn.net/baimafujinji/article/details/80705578
“多输入-多输出”模型
'''
from keras.layers import Input, Dense
from keras.models import Model
from keras.utils import to_categorical
import numpy as np

'''----------------------------------------------------------------'''
# This returns a tensor
inputs = Input(shape=(784,))

# a layer instance is callable on a tensor, and returns a tensor
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

# This creates a model that includes
# the Input layer and three Dense layers
model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labels)  # starts training

'''----------------------多输入-多输出------------------------------------------'''
from keras.layers import concatenate

x_in = Input(shape=(100,), name='x_in')
y_in = Input(shape=(100,), name='y_in')

# a layer instance is callable on a tensor, and returns a tensor
x = Dense(64, activation='relu')(x_in)
y = Dense(64, activation='relu')(y_in)

z = concatenate([x, y])

x = Dense(1, activation='sigmoid', name='x_out')(z)
y = Dense(10, activation='softmax', name='y_out')(z)

model = Model(inputs=[x_in, y_in], outputs=[x, y])

model.summary()

data = np.random.random((1000, 100))
xs = np.random.randint(2, size=(1000, 1))
ys = np.random.randint(10, size=(1000, 1))

model.compile(optimizer='rmsprop',
              loss={'x_out': 'binary_crossentropy', 'y_out': 'categorical_crossentropy'},
              loss_weights={'x_out': 1., 'y_out': 0.2})

# And trained it via:
model.fit({'x_in': data, 'y_in': data},
          {'x_out': xs, 'y_out': to_categorical(ys)},
          epochs=1, batch_size=32)