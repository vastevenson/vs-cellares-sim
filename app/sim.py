'''
Goal: simulate a hardware device that has start and stop commands
and outputs a random integer between 0 and 100 every second

Hardware state:
ConnectionStatus: Connected \ NotConnected
Status: Started \ Stopped
Random: Random integer (0-100) generated on instrument every second.
Time Remaining (seconds)

'''

import time
import random
from app.log_to_elk import Log_to_elk

class SimProcess:
    def __init__(self, dur_sec):
        # duration in seconds to simulate hardware
        self.dur_sec = dur_sec
        self.frequency_hz = 1 # duration between data points

        # initialize vars so we can return a current machine state to front end
        self.status = "Stopped"
        self.arb_val = -1
        self.remaining_seconds = -1

        self.execute()

    def execute(self):
        t = 0
        while t <= self.dur_sec:
            self.arb_val = int(random.random()*100)
            self.remaining_seconds = int(self.dur_sec) - t
            msg = "Value: " + str(self.arb_val) + " at t = " + str(t) \
                  + " seconds. Remaining time, sec: " + str(self.remaining_seconds)

            print(msg)
            Log_to_elk({
                "value": str(self.arb_val),
                "runtime_seconds": str(t),
                "remaining_seconds": self.remaining_seconds
            })
            time.sleep(self.frequency_hz)
            t += self.frequency_hz
            # if time has exceeded specified duration, set status to stopped
            if t > self.dur_sec:
                self.status = "Stopped"


    def get_current_state(self):
        return {
            "status": self.status,
            "random": self.arb_val,
            "time_remaining_seconds": self.remaining_seconds
        }