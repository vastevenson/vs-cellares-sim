Goal:
Build an app to control and monitor a simple, simulated hardware system.

Author:
Vincent Stevenson

Date:
2020-10-20

How to run app:
0. Make sure all dependencies in requirements.txt are installed
1. Have an Elasticsearch instance running at localhost:9200
2. Run run.py with Python 3.6+
3. Navigate to localhost:5000
4. Enter a time for simulation (seconds)
5. Click Start
6. After clicking start, a Stop button will appear, which you can click to send a stop command.
7. Start, Stop, and Machine State Changes are logged to the Elasticsearch instance under an index called sim_logs

Missing features and comments:
1. A better front end that displays current machine state value and connection status.
2. A way to properly terminate a running simulation process.

1. To address this issue, I would then use JavaScript's setInterval() method to call a function to hit an API within Flask that uses the SimProcess.py's object's get_current_state method and updates HTML elements with the current values.

2. I would create a better sim.py class/use an alternate way of simulating hardware. There should be a while loop that reference's the current status and there should be a way of externally changing this current status from the front end so the loop can be exited early if needed.


