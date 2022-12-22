
# PART 1 (Preprocessing)

# tokenization: the process of converting words to numbers, and therefore sentences to numbers

from lib2to3.pgen2 import token
from msilib import sequence
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequence

# initialize the Tokenizer class from Tensorflow, looking at the most frequent 100 words
tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")

sentences = [
    'I am a Senator',
    'I am a Representative'
]

tokenizer.fit_on_texts(sentences)

print(tokenizer.word_index)

# PART 2 (Preprocssing)

# will create lists of numbers representing each sentence
sequences = tokenizer.text_to_sequences(sentences)
print(sequences)

# once a tokenizer is trained on a set of sentence, and creates its corpus (word index) of words,
# if we use it to sequence sentences with unknown words, they will be dropped
# we use the OOV token to replace unknown words

# to handle sentences of different length when training a neutral network, we 
# pad the sentences
padded = pad_sequence(sequences, padding='post')

# PART 3 (Training)

# First create training and testing split
# Then preprocessing: Tokenizer, fit_to_texts, text_to_sequence, pad_sequence

# Training involves seeing how sequence vectors (its word, turned into a vector, 
# and summed up) points, and then
# using other sequence's vector's directions to guest its classification

model = tf.keras.Sequential([
    tf.keras.layers.Embedding('vocab_size', 'embedding_dim', input_length='max_length'),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

num_opochs = 30

history = model.fit('training_padded', 'training_labels', epochs=num_opochs,
                    validation_data=('testing_padded', 'testing_labels'), verbose=2)

# PART 4

# Recurrent Neural Networks takes the sequence of tokens into account when it's learning

