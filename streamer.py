import base64
import json
import time

import cv2
import pyrebase

from imutils.video import VideoStream, FPS


def init_stream():
    print('[INFO] connecting to firebase...')

    with open('firebase_config.json') as file:
        firebase_config = json.load(file)

    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()

    print('[INFO] starting video stream...')

    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    fps = FPS().start()
    start_time = time.time()

    while True:
        frame = vs.read()
        cv2.imshow('Webcam live stream', frame)

        if time.time() - start_time >= 1:
            frame_string = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
            try:
                db.update({'frame': f'data:image/jpeg;base64,{frame_string}'})
            except Exception as e:
                print(e)
            start_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        fps.update()

    fps.stop()

    print(f'[INFO] elapsed time: {fps.elapsed():.2f}')
    print(f'[INFO] approx. FPS: {fps.fps():.2f}')

    cv2.destroyAllWindows()
    vs.stop()


if __name__ == '__main__':
    init_stream()