from flask import Flask, render_template, request
import os
from openai import AzureOpenAI
import json
import httpx


app = Flask(__name__)

# Creando el cliente de Azure
client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="",
    api_key="",
)


@app.route('/', methods=["GET", "POST"])
def index():

    # Creando el app de openAI
    image_url = None

    if request.method == "POST":
        object_to_generate = request.form["object_to_generate"]
        time_of_the_day = request.form["time_of_the_day"]
        additional_feature = request.form.get("additional_feature", "")

        prompt = f"Generate an image of {object_to_generate} {
            time_of_the_day} , {additional_feature}"

        result = client.images.generate(
            model="Dalle3",  # the name of your DALL-E 3 deployment
            prompt=prompt,
            n=1
        )

        image_url = result.data[0].url

    return render_template("index.html", image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)
