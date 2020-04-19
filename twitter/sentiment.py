from tensorflow.python.keras.models import Sequential, load_model
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Flatten
from tensorflow.python.keras.layers.embeddings import Embedding
from tensorflow.python.keras.callbacks import ModelCheckpoint
from os.path import isfile
from read_tc import ReadTC
from constants import *

if isfile(filename):
    print("\nLoading existing network\n\n")
    model = load_model(filename)
else:
    print("Building new network\n\n")
    model = Sequential()
    model.add(Embedding(vocab_size, embed_size, batch_input_shape=(batch_size, input_length)))
    model.add(Flatten())
    model.add(Dense(2, activation= 'sigmoid'))
    model.compile(optimizer= 'rmsprop', loss= 'binary_crossentropy', metrics= ['acc'])
tc = ReadTC('train.csv', input_length, vocab_size, train_percent)
save_callback = ModelCheckpoint(filename)
model.fit_generator(tc.get_train_data(batch_size= batch_size), num_batches, num_epochs,
validation_data= tc.get_test_data(batch_size= batch_size), validation_steps= num_batches,
callbacks=[save_callback])
