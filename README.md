# EduKid

Edukid is designed to make learning engaging and fun for kids. It features engaging video lessons, quizzes, and educational games that cover a variety of subjects.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Screenshots](#screenshots)
4. [Technologies Used](#technologies-used)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [Authors](#license)
9. [Contact](#contact)

## Introduction
EduKid is a web application aimed at providing educational content for children in a fun and interactive way. This project was born from the struggle to find educational video content suitable for children and teenagers without exposing them to adult materials.
---
The project is still in its development phase, although MVP has been deployed.
View deployed via this [link](edukid.michaeloyedeposervices.tech).

## Features
1. **Interactive Lessons**: Engaging and interactive lessons covering various subjects.
2. **Quizzes**: Quizzes to test the knowledge gained from the lessons.
3. **Educational Games**: Fun games that reinforce the learning material.
4. **Save video**: Save a video and watch later.

## Screenshots
### Home
![Home page](/static/images/feature1.png)

### Filtered search
![Filtered search](/static/images/feature2.png)

### Save Videos
![Saved Videos](/static/images/feature3.png)

## Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Python, Flask
- **Database**: MySQL
- **Others**: Nginx, Gunicorn

## Installation
### Prerequisites
- Python 3.x
- pip (Python package installer)
- MySQL

### Clone the Repository
```sh
git clone https://github.com/Mr-Michael-dev/Edukid.git
cd Edukid
```

### Backend Setup
1. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the database:**
    ```sh
    echo setup_mysql_dev.sql | sudo mysql -uroot
    ```

4. **Run the application:**
    ```sh
    ./run_app.sh
    ```

### Running the App
You can run the app locally with the following command:
```sh
./run_app.sh
```
Visit `http://127.0.0.1:5000` in your browser to access the application.


## Areas for improvement
1. User profile editing
- update profile image
- edit name
2. User ability to delete saved video
3. Watch history
4. improve on filtered search functionality
5. organize video lessons based on subject and level
6. Implement quiz

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Authors
See the [AUTHORS](AUTHORS) file for details.

## Contact
- **Project Maintainer**: Michael Oyedepo
- **Email**: michael.oyedepo@gmail.com
- **LinkedIn**: [My LinkedIn Profile](https://www.linkedin.com/in/michael-oyedepo)
- **GitHub**: [My GitHub Profile](https://github.com/Mr-Michael-dev)
- **Twitter**: [My Twitter Profile](https://twitter.com/michealoyedepo)
