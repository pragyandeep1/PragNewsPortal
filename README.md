# Pragyandeep News Portal

Pragyandeep News Portal is a Django-powered web application designed to deliver the latest news articles on various topics such as world news, politics, sports, technology, entertainment, and more. This project demonstrates Django's flexibility and scalability, aiming to provide a dynamic platform for news content management and distribution.

## Features

- **User Authentication**: Secure user registration, login, and password reset functionality.
- **Admin Panel**: Django’s built-in admin interface allows easy management of articles, categories, authors, and users.
- **Category-Based News**: Organizes articles by categories for easy browsing.
- **Search Functionality**: Users can search for news articles by keywords or categories.
- **Responsive Design**: Fully responsive UI, ensuring compatibility with mobile and desktop devices.
- **Comment System**: Users can comment on articles (if enabled).
- **Trending News Section**: Highlights trending or popular articles based on user interaction.
- **SEO Friendly**: Meta tags and proper HTML structure for search engine optimization.
- **Pagination**: Paginated views to enhance site performance and user experience.

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- Virtualenv (optional but recommended)
- PostgreSQL or any other relational database (optional)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pragyandeep-news-portal.git
    cd pragyandeep-news-portal
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    - Update the `settings.py` file to configure the database settings.
    - Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the site at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

- Log in to the admin panel to add, edit, or delete news articles.
- Browse the categories and search for news on the main site.
- Optionally, enable user comments for articles.

## Project Structure

- `news/` - The main app that handles article management and user interactions.
- `accounts/` - Handles user authentication and profile management.
- `templates/` - HTML files for rendering views.
- `static/` - CSS, JavaScript, and images used by the front end.
- `media/` - Directory for user-uploaded files, such as article images.

## Contributing

Feel free to open issues or submit pull requests if you want to contribute to the development of the Pragyandeep News Portal. Please follow the standard Git flow for contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
