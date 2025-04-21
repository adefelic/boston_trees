from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return app.send_static_file("index.html")

@app.route("/trees")
def trees():
	return app.send_static_file("data/boston_trees_with_native_column.geojson")
