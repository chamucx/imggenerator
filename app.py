from flask import Flask, render_template, request
from openai import AzureOpenAI
import httpx

app = Flask(__name__)

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://antoniox.openai.azure.com/",
    api_key="18db2af83abc498b92d10bf0397fbdda",
)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        # Obtener los datos del formulario
        object_to_generate = request.form["object_to_generate"]
        time_of_day = request.form["time_of_day"]
        additional_feature = request.form.get("additional_feature", "")

        # Crear el prompt dinámico
        prompt = f"Generate an image of {object_to_generate} {time_of_day}, {additional_feature}."

        # Generar la imagen
        result = client.images.generate(
            model="deploymentmodel",  # nombre de tu modelo de despliegue
            prompt=prompt,
            n=1
        )

        # Obtener la URL de la imagen generada
        image_url = result.data[0].url  

    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)