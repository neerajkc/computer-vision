from flask import Flask, render_template, Response
from detection import face_detection
from recognition import face_recognize
from tracking import face_tracking

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/face_recog')
def face_recog():
    return Response(face_recognize(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face_detect')
def face_detect():
    return Response(face_detection(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face_track')
def face_track():
    return Response(face_tracking(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port=5000)