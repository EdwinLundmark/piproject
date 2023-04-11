from calculations import startSchedule
import threading
import flask

# scheduleThread = threading.Thread(target=startSchedule)
# scheduleThread.start()

app = flask.Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<path>')
def sendStatic(path):
    return app.send_static_file(path)


app.run(debug=True)
