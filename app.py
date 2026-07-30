from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
	return {"status": "ok" ,"message": "hello from devops lab"}

@app.route("/health")
def health():
	return {"status": "healthy"}, 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
