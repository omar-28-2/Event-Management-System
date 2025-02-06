# Event Management System (Ticketawy)

![Technology](https://img.shields.io/badge/Built%20with-Python%20%7C%20Django-green)

## 📋 Project Description

The **Event Management System (Ticketawy)** is a web-based platform designed to streamline the event planning and management process. It automates event registration, user authentication, vendor coordination, and feedback collection, ensuring a seamless experience for administrators, users, and vendors. By integrating modern technologies, the system minimizes manual errors, enhances efficiency, and optimizes usability.

## 🎯 Features

- **User Authentication & Role-Based Access Control:** Secure login for admins, users, and vendors.
- **Event Creation & Management:** Organizers can create, edit, and manage events with ease.
- **Vendor Service Integration:** Vendors can register and offer their services for events.
- **Event Registration & Tracking:** Users can register for events, receive notifications, and track event status.
- **Feedback Collection:** Attendees can submit feedback to improve future events.
- **Scalability & Security:** Designed for handling large numbers of users and events securely.

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Django (Python)
- **Database:** Firebase (for secure data storage)
- **Version Control:** GitHub ([Repository](https://github.com/omar-28-2/Event-Management-System))

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Django 4.0+
- Firebase Authentication & Database
- Git (for version control)

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/omar-28-2/Event-Management-System.git
   cd Event-Management-System
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate  # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Firebase Configuration:**
   - Configure Firebase authentication and database.
   - Add the Firebase credentials file (`serviceAccountKey.json`) to the project.

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the System:**
   - Open `http://127.0.0.1:8000/` in your browser.

## 📌 Future Enhancements

- **Advanced Analytics:** Implement insights and performance metrics for events.
- **Payment Gateway Integration:** Enable online ticket sales and vendor payments.
- **Accessibility Features:** Improve inclusivity with better UI/UX support for diverse users.

## 📚 References

- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [GitHub Repository](https://github.com/omar-28-2/Event-Management-System)

## 👥 Team Members

- Omar Elhossiny
- Marwan Ibrahim
- Mohamed Amir
- Yousef Yehia
- Zeyad Shawky

---

This **Event Management System** was developed as part of the **CSCI 313 Software Engineering** course under the guidance of **Dr. Mohamed ElGazar** and **TA Ahmed Jamal**.

---

**🚀 Happy Event Management!**

