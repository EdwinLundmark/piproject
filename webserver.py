from calculations import startSchedule
import threading
import flask

# scheduleThread = threading.Thread(target=startSchedule)
# scheduleThread.start()

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')
