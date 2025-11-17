from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/", methods=["POST"])
def predict():
    """
    Provide your name for a personal greeting
    ---
    parameters:
      - name: name
        in: body
        description: Add name to a JSON object, like {"name":"John"}
    responses:
        200:
            description: A personal greeting
    """
    json = request.get_json()
    return "Hello {}!".format(str(json["name"]))

app.run(host="0.0.0.0", port=8080, debug=True)