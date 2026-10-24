# 📇 Contact Manager Web Application

A responsive contact management web application built using **Python, Flask, and SQLite**. It helps users organize contact information through a clean dashboard with search, editing, deletion, pagination, dashboard statistics, and CSV export.

## 🚀 Features

* **Add Contacts:** Save names, email addresses, and phone numbers.
* **View Contacts:** Display saved contacts in a structured table.
* **Edit Contacts:** Update existing contact information.
* **Delete Contacts:** Remove contacts after a confirmation prompt.
* **Search Contacts:** Find contacts by name, email address, or phone number.
* **Form Validation:** Validate required fields and basic email and phone number formats.
* **Duplicate Detection:** Prevent duplicate email addresses.
* **Dashboard Statistics:** Display total contacts, contacts with email addresses, and recent contacts.
* **Contact Creation Dates:** Display when contacts were added, when a timestamp is available.
* **Pagination:** Browse contacts across multiple pages.
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
python-contact-management-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── contacts.html
│   └── edit.html
│
└── screenshots/
    ├── add-contact.png
    ├── dashboard.png
    └── pagination.png
```

**Note:** The `screenshots` folder should contain your actual application screenshots. Avoid uploading a database containing personal contact information to a public repository.

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.10 or later
* pip
* Git (optional)

### 1. Clone the Repository

```bash
git clone https://github.com/Manojathirumavalavan/python-contact-management-system.git
```

### 2. Open the Project Directory

```bash
cd python-contact-management-system
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open the Application

Open your browser and visit:

http://127.0.0.1:5000

## 📸 Application Screenshots

### 1. Add Contact Form

The application provides a simple form for entering contact names, email addresses, and phone numbers.

![Add Contact Form](screenshots/add-contact.png)

### 2. Dashboard

The dashboard displays statistics, including total contacts, contacts with email addresses, and contacts added in the last seven days.

![Contact Manager Dashboard](screenshots/dashboard.png)

### 3. Contact List and Pagination

Users can search contacts, view creation dates, edit or delete records, and navigate between pages.

![Contact List and Pagination](screenshots/pagination.png)

## 💡 What I Learned

Building this project helped me practise:

* Developing web applications with Flask.
* Working with SQLite databases.
* Implementing CRUD operations.
* Writing SQL queries for searching and pagination.
* Validating user input.
* Detecting duplicate email addresses.
* Exporting database records to CSV.
* Designing responsive interfaces using HTML and CSS.
* Organizing and documenting a Python project.
* Managing source code using Git and GitHub.

## 🔮 Future Improvements

* Import contacts from CSV.
* Sort contacts by name, email, and creation date.
* Add database backup and restore functionality.
* Improve automated testing and error handling.
* Strengthen application security.
* Improve accessibility and mobile usability.

## 👩‍💻 Developer

**Manoja T.**

Python | Flask | Web Development

* **GitHub Repository:** https://github.com/Manojathirumavalavan/python-contact-management-system
* **GitHub Profile:** https://github.com/Manojathirumavalavan

## 📄 License

No license has been specified yet. An appropriate open-source license can be added if the project is intended for public reuse and redistribution.



