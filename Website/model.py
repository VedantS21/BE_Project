import pandas as pd
import numpy as np
import streamlit as st
import os
import sys
from io import BytesIO,StringIO

import argparse
import os
import json
import tensorflow as tf
from PIL import Image
import numpy as np

# from .tf_example import TFModel

EXPORT_MODEL_VERSION = 1


class TFModel:
    def __init__(self, model_dir) -> None:
        # make sure our exported SavedModel folder exists
        self.model_dir = model_dir
        with open(os.path.join(model_dir, "signature.json"), "r") as f:
            self.signature = json.load(f)
        self.model_file = model_dir + "/" + self.signature.get("filename")
        print(self.model_file)
        if not os.path.isfile(self.model_file):
            raise FileNotFoundError(f"Model file does not exist")
        self.inputs = self.signature.get("inputs")
        self.outputs = self.signature.get("outputs")
        # placeholder for the tensorflow session
        self.session = None

        # Look for the version in signature file.
        # If it's not found or the doesn't match expected, print a message
        version = self.signature.get("export_model_version")
        if version is None or version != EXPORT_MODEL_VERSION:
            print(
                f"There has been a change to the model format. Please use a model with a signature 'export_model_version' that matches {EXPORT_MODEL_VERSION}."
            )

    def load(self) -> None:
        self.cleanup()
        # create a new tensorflow session
        self.session = tf.compat.v1.Session(graph=tf.Graph())
        # load our model into the session
        tf.compat.v1.saved_model.loader.load(sess=self.session, tags=self.signature.get("tags"), export_dir=self.model_dir)

    def predict(self, image: Image.Image) -> dict:
        # load the model if we don't have a session
        if self.session is None:
            self.load()

        image = self.process_image(image, self.inputs.get("Image").get("shape"))
        # create the feed dictionary that is the input to the model
        # first, add our image to the dictionary (comes from our signature.json file)
        feed_dict = {self.inputs["Image"]["name"]: [image]}

        # list the outputs we want from the model -- these come from our signature.json file
        # since we are using dictionaries that could have different orders, make tuples of (key, name) to keep track for putting
        # the results back together in a dictionary
        fetches = [(key, output["name"]) for key, output in self.outputs.items()]

        # run the model! there will be as many outputs from session.run as you have in the fetches list
        outputs = self.session.run(fetches=[name for _, name in fetches], feed_dict=feed_dict)
        return self.process_output(fetches, outputs)

    def process_image(self, image, input_shape) -> np.ndarray:
        """
        Given a PIL Image, center square crop and resize to fit the expected model input, and convert from [0,255] to [0,1] values.
        """
        width, height = image.size
        # ensure image type is compatible with model and convert if not
        if image.mode != "RGB":
            image = image.convert("RGB")
        # center crop image (you can substitute any other method to make a square image, such as just resizing or padding edges with 0)
        if width != height:
            square_size = min(width, height)
            left = (width - square_size) / 2
            top = (height - square_size) / 2
            right = (width + square_size) / 2
            bottom = (height + square_size) / 2
            # Crop the center of the image
            image = image.crop((left, top, right, bottom))
        # now the image is square, resize it to be the right shape for the model input
        input_width, input_height = input_shape[1:3]
        if image.width != input_width or image.height != input_height:
            image = image.resize((input_width, input_height))

        # make 0-1 float instead of 0-255 int (that PIL Image loads by default)
        image = np.asarray(image) / 255.0
        # format input as model expects
        return image.astype(np.float32)

    def process_output(self, fetches, outputs) -> dict:
        # do a bit of postprocessing
        out_keys = ["label", "confidence"]
        results = {}
        # since we actually ran on a batch of size 1, index out the items from the returned numpy arrays
        for i, (key, _) in enumerate(fetches):
            val = outputs[i].tolist()[0]
            if isinstance(val, bytes):
                val = val.decode()
            results[key] = val
        confs = results["Confidences"]
        labels = self.signature.get("classes").get("Label")
        output = [dict(zip(out_keys, group)) for group in zip(labels, confs)]
        sorted_output = {"predictions": sorted(output, key=lambda k: k["confidence"], reverse=True)}
        return sorted_output

    def cleanup(self) -> None:
        # close our tensorflow session if one exists
        if self.session is not None:
            self.session.close()
            self.session = None

    def __del__(self) -> None:
        self.cleanup()


# model = open("C:/Users/vedan/Desktop/BE Project/Skin Detection Model/BE Project/Final TensorFlow/saved_model.pb")   # Windows


model_path = "C:/Users/vedan/Desktop/BE_Project/SDModel/Final_TensorFlow"

STYLE = """
<style>
img{
    max-width: 40%;
}
</style>
"""

html_temp = """
<h2 style="colour:white;text; align:centre">First Trial </h2>
"""

"""
tf_model = TFModel(model_path)
tf_model.load()


def main():

    st.title("Skin Disease Detection")
    # st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown(STYLE, unsafe_allow_html = True)
    file = st.file_uploader("Upload file with skin disease image", type=["csv","png","jpg"])
    show_file = st.empty()

    if not file:
        print("File not selected")
        show_file.info("Please UPLOAD a file : {} ".format(''.join(["csv","png","jpg"])))
        return
    content = file.getvalue()

    if isinstance(file, BytesIO):
        show_file.image(file)
    else:
        data = pd.read_csv(file)
        st.dataframe(data.head(10))
    file.close()

    print(type(file))
    print(type(content))
    image = Image.open(BytesIO(content))
    output = tf_model.predict(image)
    max_conf = 1.0
    final_pred = dict()
    for pred in output["predictions"]:
        print(pred)
        if pred["confidence"] == max_conf:
            final_pred = pred
    st.write("Disease: "+final_pred['label'])
"""