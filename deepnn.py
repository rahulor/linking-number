# TensorFlow and tf.keras
import tensorflow as tf
print(tf.__version__)
#tf.sysconfig.get_build_info() 

import keras
from tensorflow.keras import datasets, layers, models
import pickle
import helper
import numpy as np


if __name__ == "__main__":
    print('loading dataset..')
    # training data
    loops_list, label_list = helper.unpickle_from('data/train_loops_labels')
    train_labels = np.array(label_list)
    train_loops = np.array([loops.flatten('F') for loops in loops_list])
    print('training data', len(train_loops), len(train_labels))

    # Testing data
    loops_list, label_list = helper.unpickle_from('data/test_loops_labels')
    test_labels = np.array(label_list)
    test_loops = np.array([loops.flatten('F') for loops in loops_list])
    print('training data', len(train_loops), len(train_labels))
    loops_list, label_list = 0, 0
    
    # configure network
    model = models.Sequential()
    model.add(layers.Flatten(input_shape=(306,)))
    model.add(layers.Dropout(rate=0.1))
    model.add(layers.Dense(2**14, activation='relu'))
    model.add(layers.Dropout(rate=0.2))
    model.add(layers.Dense(2**10, activation='relu'))
    model.add(layers.Dropout(rate=0.1))
    model.add(layers.Dense(2, activation='softmax'))
    # model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(51, 51, 3)))
    # model.add(layers.MaxPooling2D((2, 2)))
    # # model.add(layers.Conv2D(32, (3, 3), activation='relu'))
    # model.add(layers.MaxPooling2D((2, 2)))
    # # model.add(layers.Conv2D(16, (3, 3), activation='relu'))
    # model.add(layers.Flatten())
    # #model.add(layers.Dense(4, activation='relu'))
    # model.add(layers.Dense(2))
    model.summary()
    
    model.compile(loss="sparse_categorical_crossentropy", 
                    optimizer=keras.optimizers.SGD(learning_rate=0.2), 
                    metrics=['accuracy'])
    
    print('='*50)
    history = model.fit(train_loops, train_labels, epochs=10, batch_size = 1024*1,
                    validation_data=(test_loops, test_labels))
    
    print('='*50)
    test_loss, test_acc = model.evaluate(test_loops,  test_labels, verbose=2)
    #helper.pickle_to('data/tfmodel', model)
    
    