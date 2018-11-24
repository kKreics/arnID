import threading
import time

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/request_processing')
def request_processing():
    # insert into database
    # start processing thread
    tt = TaskThread('user', 'password123')
    tt.start()

    return 'Hello, World!'

@app.route('/get_processing_results')
def get_processing_results():
    return 'Hello, World!'

@app.route('/send_gdpr')
def send_gdpr():
    return 'Hello, World!'


class TaskThread (threading.Thread):
    def __init__(self, name, password):
        threading.Thread.__init__(self)
        self.name = name
        self.password = password

    def run(self):
        print ("Starting " + self.name)
        time.sleep(3)
        #   start pump
        #   start aggregator
        #   insert results into database
        print ("Exiting " + self.name)
