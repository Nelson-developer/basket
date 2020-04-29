from flask import Flask
from graph import graph_todo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.register_blueprint(graph_todo)





if __name__ == "__main__":
    app.run(debug= True, port=4000)
