📍 Geo-Fencing Alert System
This project implements a Geo-Fencing Alert System with real-time location tracking, entry/exit alerts, SMS/Email notifications, role-based login, and data export functionality. It includes a live map-based dashboard to visualize movements relative to defined geofence zones.

✅ Features
🌍 Live map with real-time tracking (Leaflet.js)

🔒 Login authentication (Admin/Viewer roles)

🛡 Define polygonal geofences

🚨 Alerts for geofence entry/exit

📧 Email alerts via SendGrid

📱 SMS alerts via Twilio

📄 Logs all events to CSV

📤 Export logs (CSV)

🖥 Simple dashboard UI

⚡ Real-time updates with Flask-SocketIO

📂 Folder Structure
csharp
Copy
Edit
geo-fencing/
├── app.py                  # Flask backend
├── templates/
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── main.js             # Frontend JavaScript
├── logs/
│   └── alerts.csv          # Alert logs
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
🚀 Installation
1. Clone Repository
bash
Copy
Edit
git clone <repository-url>
cd geo-fencing
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Setup API Keys
Replace:

SENDGRID_API_KEY (for email alerts)

TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM, TO_PHONE (for SMS alerts)

4. Run Server
bash
Copy
Edit
python app.py
5. Access Dashboard
Navigate to:

cpp
Copy
Edit
http://127.0.0.1:5000
6. Login Credentials
Username	Password	Role
admin	admin123	Admin
viewer	view123	Viewer

🧩 Dependencies
Flask

Flask-SocketIO

Eventlet

Shapely

SendGrid

Twilio

Leaflet.js

Turf.js (frontend)

🗺 How to Use
Login as Admin or Viewer.

View live location updates on the map.

Define Geofence via code or integrate with Leaflet Draw.

Trigger entry/exit alerts on boundary crossing.

View logs in dashboard and export as CSV.

Admin can logout and export data.

✅ To Do / Future Enhancements
Export logs as PDF

Database integration (MongoDB/PostgreSQL)

Geofence drawing via frontend

Multiple user/device tracking

Mobile app integration

📜 License
This project is open-source and for educational/demo purposes.
