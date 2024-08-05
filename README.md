# Full Stack Web Development Project

**Domain:** Full Stack Web Development  
**Mentor:** Santhosh Kumar  
**Company:** Codtech IT Solutions  
**Duration:** June to August 2024


# NextGen Mini Blog

NextGen is a mini blog application built with Flask. It allows users to create, update, delete, and view blog posts. The application includes an admin dashboard for managing posts and user authentication for login and logout functionality.

## Features

- **Create Post**: Admin can create new blog posts.
- **Update Post**: Admin can update existing blog posts.
- **Delete Post**: Admin can delete blog posts.
- **View Post**: Users can view blog posts.
- **Admin Dashboard**: Controls for managing posts.
- **User Authentication**: Login and logout functionality for admin.


## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/NextGen-MiniBlog.git
    cd NextGen-MiniBlog
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    

4. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Set up the database**:
   - Make sure you have MySQL installed and running.
   - Create a database named `blog`.
   - Update the database connection settings in `app.py` if necessary.

6. **Run the application**:

    ```sh
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000`.

## Usage

1. **Home Page**: View the latest blog posts.
2. **Admin Dashboard**: Access the admin dashboard by logging in.
3. **Login**: Use the login page to authenticate as an admin.
4. **Signup**: Register a new admin user.
5. **Create Post**: Use the admin dashboard to create new blog posts.
6. **Update Post**: Use the admin dashboard to update existing blog posts.
7. **Delete Post**: Use the admin dashboard to delete blog posts.
8. **View Full Article**: Click on a blog post to view the full article.
9. **Logout**: Use the logout functionality to end the admin session.

## Configuration

- **Database Settings**: Update the MySQL connection settings in `app.py` to match your database configuration.

```python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
```

##Demo Images
![image](https://github.com/bnaveenbharathi/miniblog/assets/144258519/034d2117-d6d5-403f-8bc2-6d8aea23e124)

![image](https://github.com/bnaveenbharathi/miniblog/assets/144258519/749dcb1f-0b72-43c5-80b4-5f3ccc8a21d3)



