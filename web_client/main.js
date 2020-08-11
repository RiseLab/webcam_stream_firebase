document.addEventListener('DOMContentLoaded', function () {
    fetch('../firebase_config.json')
        .then(response => response.json())
        .then(data => {
            // App's Firebase configuration
            let firebaseConfig = data;
            // Initialize Firebase
            firebase.initializeApp(firebaseConfig);
            // Get a reference to the database service
            let db = firebase.database();
            // Listen for value updates
            let ref = firebase.database().ref('frame');
            ref.on('value', function(snapshot) {
                document.getElementById('camView').src = snapshot.val();
            });
        });
});