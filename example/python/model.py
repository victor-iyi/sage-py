"""Model construction.

   @author
     Victor I. Afolabi
     Artificial Intelligence Expert & Researcher.
     Email: javafolabi@gmail.com | victor.afolabi@zephyrtel.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: model.py
     Created on 11 March, 2019 @ 06:31 AM.

   @license
     Apache 2.0 License
     Copyright (c) 2019. Victor I. Afolabi. All rights reserved.
"""

import tensorflow as tf


def bi_directional_lstm(embedding_matrix, max_len, max_features, embed_size):
    """Bi-Directional LSTM Keras model.

    Args:
        embedding_matrix (np.ndarray): Embedding matrix.
        max_len (int): Max sequence length.
        max_features (int): Max feature length.
        embed_size (int): Embedding dimension.

    Returns:
        tf.keras.Model: A compiled Keras model.
    """

    inp = tf.keras.Input(shape=(max_len,))
    x = tf.keras.layers.Embedding(max_features, embed_size,
                                  weights=[embedding_matrix])(inp)
    x = tf.keras.layers.Bidirectional(
        tf.keras.layers.CuDNNLSTM(64, return_sequences=True))(x)

    avg_pool = tf.keras.layers.GlobalAveragePooling1D()(x)
    max_pool = tf.keras.layers.GlobalMaxPooling1D()(x)

    conc = tf.keras.layers.concatenate([avg_pool, max_pool])
    conc = tf.keras.layers.Dense(64, activation='relu')(conc)
    conc = tf.keras.layers.Dropout(0.1)(conc)

    # Output layer.
    out = tf.keras.layers.Dense(1, activation='sigmoid')(conc)

    model = tf.keras.Model(inputs=inp, outputs=out)
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model
