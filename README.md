# Student Database

The Student Database project is a web application developed using Django framework. It allows users to manage student records by performing operations such as adding, updating, and deleting student information. Each student record consists of fields like Name, Age, Email, and Password.

## Features

- User-friendly interface for managing student records.
- Add new student records by entering data into the provided fields.
- Import student records from a CSV file.
- Update existing student records with updated information.
- Delete student records from the database.
- Export student records from the database to a CSV file.

## Installation

To run the Student Database project locally, please follow these steps:

1. Clone the repository:

git clone https://github.com/Ammar-Munirr/Student-Database.git

2. Navigate to the project directory:

cd student-database

3. Create and activate a virtual environment (optional but recommended):

python3 -m venv env
source env/bin/activate

4. Install the project dependencies:

pip install -r requirements.txt

5. Apply the database migrations:

python manage.py migrate

6. Start the development server:

python manage.py runserver


Access the application by visiting http://localhost:8000 in your web browser.

# Usage
Once the application is running, you can perform the following actions:

1. Add Student Record: Click on the "Add Student" button and enter the required information (Name, Age, Email, Password) into the provided fields.   Click "Submit" to add the record to the database.

2. Import Student Records from CSV: Click on the "Import CSV" button and select a CSV file containing student records. The file should have columns for Name, Age, Email, and Password. Click "Submit" to import the records into the database.

3. Update Student Record: Each student record in the database is displayed with an "Edit" button. Click on the button to update the corresponding student's information. Make the necessary changes in the fields and click "Submit" to save the updated information.

4. Delete Student Record: Each student record in the database is displayed with a "Delete" button. Click on the button to remove the corresponding student's record from the database.

5. Export Student Records to CSV: Click on the "Export CSV" button to export all the student records from the database into a CSV file. The exported file will contain columns for Name, Age, Email, and Password.

# Contributing
If you would like to contribute to the Student Database project, you can follow these steps:

Fork the repository on GitHub.

Clone your forked repository to your local machine.

Create a new branch for your feature/bug fix.

Make the necessary changes and additions.

Commit and push your changes to your forked repository.

Submit a pull request to the main repository.

Please ensure your code follows the project's coding style and conventions. Include relevant details and tests for your changes.

# Acknowledgements
The Student Database project was inspired by the need for a simple and efficient solution for managing student records.
Thanks to the Django framework and its contributors for providing a powerful and flexible web development framework.