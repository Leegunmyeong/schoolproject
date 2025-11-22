from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = round(st.download() / 1_000_000, 2)
    upload_speed = round(st.upload() / 1_000_000, 2)
    ping = round(st.results.ping, 2)
    return {
        "download": download_speed,
        "upload": upload_speed,
        "ping": ping
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/speedtest")
def speedtest_api():
    result = run_speedtest()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)

