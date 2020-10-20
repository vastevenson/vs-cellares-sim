from app import app
from flask import render_template, request
from app.sim import SimProcess
from app.log_to_elk import Log_to_elk

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/process", methods=["GET", "POST"])
def process():
    data = request.json
    sim_dur_s = data['sim_dur_s']

    if sim_dur_s == "-1":
        Log_to_elk({"message": "Stop button was clicked."})
        return ''
    else:
        Log_to_elk({"message": "Start button was clicked.",
                    "requested_duration_sec": sim_dur_s})
        SimProcess(int(sim_dur_s))
