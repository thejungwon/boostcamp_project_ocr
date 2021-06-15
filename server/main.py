from flask import Flask, request
from PIL import Image
import base64
import json
import io
from inference import inference
from flask_cors import CORS, cross_origin



app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route("/susik_recognize", methods=["POST"])
@cross_origin()
def susik_recognize():
    image = request.json['image']
    
    image = image.split(",")[1]
    image = base64.b64decode(image)
    image = io.BytesIO(image)
    image = Image.open(image)
    
    data=inference(image)
    data = {'result':data}
    return json.dumps(data)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6006, debug=True)