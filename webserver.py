from calculations import getPrices, calculateBrightness, price
import multiprocessing
import flask
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

getPrices()

scheduler = BackgroundScheduler()
scheduler.add_job(func=getPrices, trigger='interval', seconds=10)
scheduler.add_job(func=calculateBrightness, trigger='interval', seconds=5)
scheduler.start()


def shutdown():
    scheduler.shutdown()
    print("shutdown")


atexit.register(shutdown)

app = flask.Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<path>')
def sendStatic(path):
    return app.send_static_file(path)


@app.route('/get-brightness')
def sendBrightness():
    return str(calculateBrightness() * 100) + "%"


app.run()
