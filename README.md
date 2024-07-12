# Prathmesh Deshkar Portfolio

This project is a personal portfolio website for Prathmesh Deshkar. It showcases his technical skills, work experience, and projects. Additionally, it includes a contact form where users can add their information, which is then stored in a PostgreSQL database and displayed on the webpage.

## Features

- **Responsive Design**: Built using Bootstrap for a responsive and visually appealing design.
- **Dynamic Content**: Users can add their information through a form, and the data is displayed dynamically on the webpage.
- **Projects Showcase**: Displays various projects with descriptions and images.
- **Technical Skills and Experience**: Highlights technical skills and work experience.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Templating**: Jinja2

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/portfolio.git
    cd portfolio
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL**:
    - Ensure PostgreSQL is installed and running.
    - Create a new database (e.g., `flask_database`).
    - Update the database URI in `app.py` if necessary.

5. **Run the application**:
    ```bash
    flask run
    ```

## Database Schema

- **Table Name**: `Task`
    - `sno`: Integer, Primary Key, Auto Increment
    - `YourName`: String(300), Not Null
    - `Email`: String(500), Nullable

## API Endpoints

### 1. `GET /`

- **Description**: Fetch and display all tasks (user information) stored in the database.
- **Response**: Renders the main webpage with the form and a table of all tasks.

### 2. `POST /`

- **Description**: Add a new task (user information) to the database.
- **Request Parameters**:
    - `name`: User's name (string)
    - `email`: User's email (string)
- **Response**: Redirects to the main page to display the updated list of tasks.

## Code Explanation

### HTML Template (`index.html`)

- **Header**: Contains navigation links to various sections like Home, About, Projects, and Contact.
- **Home Section**: Displays a brief introduction with a background image and a profile image.
- **About Section**: Details educational background and technical skills divided into two columns.
- **Projects Section**: Showcases various projects with descriptions and images.
- **Contact Section**: Provides a form for users to add their information and displays the added information in a table.

### Flask Application (`app.py`)

- **Database Configuration**: Connects to the PostgreSQL database using SQLAlchemy.
- **Task Model**: Defines the schema for storing user information.
- **Routes**:
    - **`/`**: Handles both GET and POST requests. On POST, adds a new task to the database and redirects to the main page. On GET, fetches and displays all tasks.
- **Database Initialization**: Creates the necessary tables in the database.

## Screenshots

![image](https://github.com/PRATHAMdeshkar/Flask-profile/assets/115910086/3362d0b6-916a-4707-8dfa-32e267ae66ad)
![image](https://github.com/PRATHAMdeshkar/Flask-profile/assets/115910086/f05dead1-b949-4ca7-9992-4dae6811b1dd)
![image](https://github.com/PRATHAMdeshkar/Flask-profile/assets/115910086/19d042e3-e0ec-4c2d-a599-2715e5c9b403)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
