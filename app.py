from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, "contacts.db")


# Create database table
def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Initialize the database when the application starts
create_table()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Add contact
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()

    if not name or not email or not phone:
        return "Please fill in all fields.", 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO contacts (name, email, phone)
        VALUES (?, ?, ?)
        """,
        (name, email, phone)
    )

    conn.commit()
    conn.close()

    return redirect("/contacts")


# View and search contacts
@app.route("/contacts")
def view_contacts():
    search = request.args.get("search", "").strip()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if search:
        cursor.execute("""
            SELECT id, name, email, phone
            FROM contacts
            WHERE name LIKE ?
               OR email LIKE ?
               OR phone LIKE ?
            ORDER BY id DESC
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))
    else:
        cursor.execute("""
            SELECT id, name, email, phone
            FROM contacts
            ORDER BY id DESC
        """)

    contacts = cursor.fetchall()
    conn.close()

    return render_template(
        "contacts.html",
        contacts=contacts,
        search=search
    )


# Edit contact
@app.route("/edit/<int:contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()

        if not name or not email or not phone:
            conn.close()
            return "Please fill in all fields.", 400

        cursor.execute(
            """
            UPDATE contacts
            SET name = ?, email = ?, phone = ?
            WHERE id = ?
            """,
            (name, email, phone, contact_id)
        )

        conn.commit()
        conn.close()

        return redirect("/contacts")

    cursor.execute(
        """
        SELECT id, name, email, phone
        FROM contacts
        WHERE id = ?
        """,
        (contact_id,)
    )

    contact = cursor.fetchone()
    conn.close()

    if contact is None:
        return "Contact not found.", 404

    return render_template("edit.html", contact=contact)


# Delete contact
@app.route("/delete/<int:contact_id>", methods=["POST"])
def delete_contact(contact_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contacts WHERE id = ?",
        (contact_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/contacts")


# Run locally
if __name__ == "__main__":
    app.run(debug=True)
