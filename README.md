                                                                                 Medical Appointment Scheduler

The Medical Appointment Scheduler is a web application built using Flask, a lightweight Python web framework, designed to help manage appointments and patients in a medical practice. This project utilizes an SQLite database for storing appointment and patient information, allowing for efficient data management and retrieval.

Features:
Appointment Management: Users can add new appointments with patient details and appointment dates. Existing appointments can be viewed, edited, and deleted as needed.
Patient Management: Patients can be added with their name and contact information. The patient list can be accessed to view, edit, and delete patient records.
Dynamic Content Rendering: The frontend interface dynamically fetches and displays appointment and patient data using JavaScript and AJAX requests to provide a seamless user experience.
Responsive Design: The application is designed with a responsive layout, ensuring optimal display on various devices such as desktops, tablets, and smartphones.
SQLite Database Integration: Appointment and patient data are stored in an SQLite database, providing a lightweight and scalable solution for data storage and retrieval.
Usage:
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the Flask application using python app.py.
Access the application in your web browser at http://localhost:5000.
Technologies Used:
Flask: Python web framework for building the backend of the application.
SQLite: Lightweight relational database management system used for storing appointment and patient data.
HTML/CSS/JavaScript: Frontend development languages for creating the user interface and dynamic content rendering.
Flask-CORS: Flask extension for handling Cross-Origin Resource Sharing (CORS) to allow communication between the frontend and backend.
Future Enhancements:
Implement user authentication and authorization features for secure access.
Add calendar integration to display appointments in a calendar format.
Enhance the user interface with additional styling and interactive elements.
Implement email notifications for appointment reminders and updates.
