<?php
// Connect to MySQL database
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "database_name";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve data from POST request
$englishSentence = $_POST['englishSentence'];
$bengaliSentence = $_POST['bengaliSentence'];

// Insert data into the database
$sql = "INSERT INTO sentences (english_sentence, bengali_sentence, posted_datetime) VALUES ('$englishSentence', '$bengaliSentence', NOW())";
if ($conn->query($sql) === TRUE) {
    echo "Data saved successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
