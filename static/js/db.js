
var firebaseConfig = {
  apiKey: "AIzaSyBzO0tbhyreIsMGOItWcUJfLm3zfZLW0JM",
  authDomain: "lasmun-beade.firebaseapp.com",
  projectId: "lasmun-beade",
  storageBucket: "lasmun-beade.appspot.com",
  messagingSenderId: "193275202252",
  appId: "1:193275202252:web:094501be6bedb2c9301069",
  measurementId: "G-VC005N91BY"
};
firebase.initializeApp(firebaseConfig);
  
var db = firebase.firestore();

document.getElementById("email-form").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent the default form submission
  
    // Get form values
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;
    const response = grecaptcha.getResponse();
  

    if (!response.length > 0){
        alert("Captcha Not Complete")
        throw new Error ("Captcha Not Complete")
    }
    // Add a new document to Firestore
    db.collection("messages")
      .add({
        name: name,
        email: email,
        subject: subject,
        message: message,
      })
      .then(function (docRef) {
        // Reset the form and show a success message
        document.getElementById("email-form").reset();
        document.querySelector(".sent-message").style.display = "block";
      })
      .catch(function (error) {
        // Handle errors and show an error message
        console.error("Error adding document: ", error);
        document.querySelector(".error-message").style.display = "block";
      });
  });