from flask import Flask, request, jsonify, send_from_directory
import os
from wheel_generator import create_wheel
from datetime import datetime

app = Flask(__name__)
OUTPUT_FOLDER = "static/generated"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/generate_color_wheel", methods=["POST"])
def generate_color_wheel():
    data = request.get_json()
    colors_logged = data.get("colors_logged", [])

    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    create_wheel(colors_logged, output_path)

    image_url = f"{request.url_root}static/generated/{filename}"
    return jsonify({"image_url": image_url})
