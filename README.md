# Webcam online streamer demo app
Streaming video from local webcam to website using Firebase. 

## Using
1. Create and configure Realtime Database in your Firebase console.
1. Copy and rename file `firebase_config.example.json` to `firebase_config`.json. Fill it with your web app's Firebase configuration data.
1. To run `streamer.py` (server) install all required packages:

    ```console
    pip install python-opencv pyrebase imutils
    ```

   You also need webcam connected to computer of course.
1. To run client webpage just open `web_client/index.html` in your browser.