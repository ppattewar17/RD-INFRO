import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Input
import numpy as np

# Step 1: Load Pre-trained CNN for Feature Extraction
def create_feature_extractor():
    base_model = ResNet50(weights="imagenet", include_top=False, pooling="avg")
    return Model(inputs=base_model.input, outputs=base_model.output)

# Step 2: Load and Preprocess Image
def preprocess_image(image_path):
    from tensorflow.keras.applications.resnet50 import preprocess_input
    from tensorflow.keras.preprocessing.image import load_img, img_to_array

    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

# Step 3: Caption Generation Model
def create_caption_model(vocab_size, max_length):
    image_input = Input(shape=(2048,))
    img_features = Dense(256, activation="relu")(image_input)

    seq_input = Input(shape=(max_length,))
    seq_embedding = Embedding(vocab_size, 256, mask_zero=True)(seq_input)
    lstm_output = LSTM(256)(seq_embedding)

    combined = tf.keras.layers.add([img_features, lstm_output])
    output = Dense(vocab_size, activation="softmax")(combined)

    return Model(inputs=[image_input, seq_input], outputs=output)

# Step 4: Train and Evaluate
# Use COCO or Flickr8k dataset for training

def generate_caption(image_features, tokenizer, model, max_length):
    input_seq = [tokenizer.word_index['<start>']]
    for _ in range(max_length):
        seq_padded = tf.keras.preprocessing.sequence.pad_sequences([input_seq], maxlen=max_length, padding='post')
        predictions = model.predict([image_features, seq_padded], verbose=0)
        predicted_id = np.argmax(predictions)
        word = tokenizer.index_word.get(predicted_id, None)
        if word is None or word == '<end>':
            break
        input_seq.append(predicted_id)
    return ' '.join([tokenizer.index_word[i] for i in input_seq if i > 0])

if __name__ == "__main__":
    feature_extractor = create_feature_extractor()
    image_path = "example.jpg"
    image_features = feature_extractor.predict(preprocess_image(image_path))
    # Assume `tokenizer` and `caption_model` are pre-trained
    caption = generate_caption(image_features, tokenizer, caption_model, max_length=20)
    print("Generated Caption:", caption)
