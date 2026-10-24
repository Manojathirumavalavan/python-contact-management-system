# 📇 Contact Manager Web Application

A responsive contact management web application built using Python, Flask, and SQLite. It allows users to organize contact information through a clean dashboard with search, editing, deletion, pagination, and CSV export functionality.

## 🚀 Features

* **Add Contacts:** Save names, email addresses, and phone numbers.
* **View Contacts:** Display saved contacts in a structured table.
* **Edit Contacts:** Update existing contact information.
* **Delete Contacts:** Remove contacts with a confirmation prompt.
* **Search Contacts:** Find contacts by name, email, or phone number.
* **Form Validation:** Validate email formats and phone number inputs.
* **Duplicate Detection:** Prevent duplicate email addresses.
* **Dashboard Statistics:** Display total contacts, contacts with email addresses, and recent contacts.
* **Contact Creation Dates:** Track when contacts were added.
* **Pagination:** Display contacts across multiple pages.
* **CSV Export:** Download contact information as a CSV file.
* **Responsive Interface:** Use the dashboard on desktop and mobile devices.

## 🛠️ Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3
* Jinja2
* Git and GitHub

## 📂 Project Structure

```text
Contact-Manager/
│
├── app.py
├── contacts.db
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    ├── contacts.html
    └── edit.html
```

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.10 or later
* pip
* Git (optional)

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project directory

```bash
cd Contact-Manager
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Flask:

```bash
pip install Flask
```

### 5. Run the application

```bash
python app.py
```

### 6. Open the application

Visit:

```text
http://127.0.0.1:5000
```

## 📸 Screenshots

Add screenshots of your actual running application here.

Recommended screenshots:

1. Contact Manager dashboard
2. Add Contact form
3. Search results
4. Pagination
5. CSV export result

Example Markdown:

```markdown
![Contact Manager Dashboard](screenshots/dashboard.png)
```

## 💡 What I Learned

Building this project helped me practise:

* Developing web applications with Flask.
* Working with SQLite databases.
* Implementing CRUD operations.
* Writing SQL queries for searching and pagination.
* Validating user input.
* Exporting database records to CSV.
* Designing responsive interfaces using HTML and CSS.
* Organizing and documenting a Python project.

## 🔮 Future Improvements

* Contact import from CSV.
* Sorting contacts by name and creation date.
* Automated database backups.
* Improved error handling and application security.
* Additional accessibility improvements.

## 👩‍💻 Developer

**Manoja T.**

Python | Flask | Web Development

GitHub: Add your GitHub profile link here.

Portfolio: Add your portfolio link here.

## 📄 License

This project is available for educational and portfolio purposes. Add a suitable open-source license if you intend to permit reuse and redistribution.

