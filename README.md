# Image Description Generator

This Python script generates marketing descriptions for images, especially T-shirt designs. It processes images in a given folder and creates a description based on the file name, dominant colors, and relevant tags. The generated descriptions are written to a text file named "image_descriptions.txt".

## Dependencies

-   Python 3.7 or later
-   OpenCV
-   webcolors
-   scikit-learn
-   spaCy
-   Pillow

To install the required libraries, run the following command:

bashCopy code

`pip install opencv-python-headless webcolors scikit-learn spacy Pillow` 

Additionally, download the spaCy English model by running:

bashCopy code

`python -m spacy download en_core_web_sm` 

## Usage

1.  Set the `image_folder` variable in the `main()` function to the folder containing your images.
2.  Run the script:

bashCopy code

`python main.py` 

3.  The generated image descriptions will be written to "image_descriptions.txt" in the same directory as the script.

## Functions

-   `extract_tags(text)`: Extracts relevant tags from the given text.
-   `extract_dominant_colors(image_path, num_colors=3)`: Extracts the dominant colors from the image.
-   `color_name(rgb)`: Returns the closest CSS3 color name for the given RGB color.
-   `create_description(image_path)`: Generates a marketing description for the image based on its file name, dominant colors, and relevant tags.
-   `main()`: Processes images in the given folder and writes the generated descriptions to the output file.
