import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

def create_model(input_vocab_size, output_vocab_size, max_length):
    input_layer = Input(shape=(max_length,))
    encoder = TransformerEncoder(num_layers=4, d_model=128, num_heads=8, dff=512, 
input_vocab_size=input_vocab_size, maximum_position_encoding=max_length)
    decoder = TransformerDecoder(num_layers=4, d_model=128, num_heads=8, dff=512, 
target_vocab_size=output_vocab_size, maximum_position_encoding=max_length)

    enc_padding_mask = create_padding_mask(input_layer)

    encoder_output = encoder(input_layer, training=True, mask=enc_padding_mask)
    decoder_output = decoder(target, encoder_output, training=True, look_ahead_mask=None, 
padding_mask=None)

    output_layer = Dense(output_vocab_size)(decoder_output)

    model = Model(inputs=input_layer, outputs=output_layer)
    return model

# Example usage:
model = create_model(input_vocab_size, output_vocab_size, max_length)

