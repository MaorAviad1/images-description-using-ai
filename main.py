import os
import webcolors
import cv2
import numpy as np
from PIL import Image
from collections import Counter
from sklearn.cluster import KMeans
from spacy import displacy
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_tags(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def extract_dominant_colors(image_path, num_colors=3):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    kmeans = KMeans(n_clusters=num_colors)
    labels = kmeans.fit_predict(image)
    color_counts = Counter(labels)

    return [tuple(map(int, kmeans.cluster_centers_[i])) for i in color_counts.keys()]

def color_name(rgb):
    min_diff = float("inf")
    closest_color_name = None
    for name, value in webcolors.CSS3_NAMES_TO_HEX.items():
        diff = sum(abs(v1 - v2) for v1, v2 in zip(webcolors.name_to_rgb(name), rgb))
        if diff < min_diff:
            min_diff = diff
            closest_color_name = name
    return closest_color_name.replace(" ", "").lower()

def create_description(image_path):
    filename = os.path.splitext(os.path.basename(image_path))[0]
    tags = extract_tags(filename)
    colors = extract_dominant_colors(image_path)

    color_names = [color_name(color) for color in colors]
    color_str = ', '.join(color_names[:-1]) + ' and ' + color_names[-1]

    description = f"Show off your unique style with this {tags[0]} {tags[-1]} T-shirt design, featuring {color_str} colors! Perfect for {', '.join(tags[1:-1])} enthusiasts."
    return description

def main():
    image_folder = "C:/Users/Dana/PycharmProjects/images-description-using-ai"
    output_file = "image_descriptions.txt"

    with open(output_file, "w") as f:
        for filename in os.listdir(image_folder):
            if filename.endswith((".jpg", ".jpeg", ".png")):
                image_path = os.path.join(image_folder, filename)
                description = create_description(image_path)
                f.write(f"{filename}: {description}\n")

if __name__ == "__main__":
    main()