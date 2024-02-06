import numpy as np

def extract_features(message, preprocess_data ):
    message = message.lower()
    features = []

    for word in preprocess_data["top_words"]:
        features.append(message.count(word))

    for character in preprocess_data["top_characters"]:
        features.append(message.count(character))
   
    features.append(len(message)/preprocess_data["average_length"])
    return np.array(features)


