

# ERP Library Management System

This is a Library Management System built using the Frappe framework. It is designed to manage library operations like book inventory, lending, and tracking.

## Features
- Manage book details, including title, author, and ISBN
- Track book loans and returns
- Manage user accounts for librarians and borrowers
- Generate reports on library activity

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/samikshakhadka/ERP_Library.git
   ```
2. Set up the environment by following the [Frappe framework installation guide](https://frappeframework.com/docs/v13/user/en/installation).
3. Create a new site and install the app:
   ```bash
   bench new-site library.local
   bench --site library.local install-app erp_library
   ```

4. Run the development server:
   ```bash
   bench start
   ```

## Usage
Once the app is running, you can access it through your browser at `localhost:8000` and log in with the credentials you set during setup.

## Contributing
Feel free to open issues or submit pull requests for improvements.



