# 📓 Note-Taking Web App Deployment with Ansible

## 📖 Overview

This project demonstrates the deployment of a **Python Flask Note-Taking Web Application** on an **AWS EC2 instance** using **Ansible automation**.
The application stores notes in an **SQLite database**, serves them via **NGINX**, and includes a **backup strategy** using an attached EBS volume.

The project is designed to be reusable and fully automated, enabling anyone to quickly provision and configure the application in a cloud environment.

---

## 🚀 Features

* **Automated Deployment** using Ansible roles and playbooks.
* **Flask Web App** for creating and viewing notes with timestamps.
* **SQLite Database** for lightweight local storage.
* **NGINX** as a reverse proxy for better performance.
* **EBS Volume Backup** mounted to `/backup` for storing database backups.
* **Idempotent Setup** – safe to re-run without breaking configurations.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3 (Flask Framework)
* **Configuration Management:** Ansible
* **Database:** SQLite
* **Web Server:** NGINX
* **Cloud Provider:** AWS EC2 (Amazon Linux 2, t2.micro)
* **Storage:** AWS EBS volume for backups

---

## 📂 Project Structure

```
note-taking-app/
├── app.py               # Flask application source code
├── templates/           # HTML templates for the web app
├── static/               # Static files (CSS, JS)
├── roles/
│   └── note_taking_app/
│       ├── tasks/        # Main automation tasks
│       ├── templates/    # Jinja2 templates for configs
│       ├── files/        # Static files for deployment
│       └── meta/         # Role metadata
├── inventory.ini         # Ansible inventory
├── playbook.yml          # Main deployment playbook
└── README.md             # Documentation
```

---

## ⚙️ Prerequisites

Before running the playbook, ensure you have:

1. An AWS EC2 instance (Amazon Linux 2, t2.micro recommended).
2. An attached EBS volume for backups.
3. Ansible installed on your controller machine.
4. Python 3 installed on the EC2 instance (Ansible will handle this if not present).
5. Your SSH key added for EC2 access.

---

## 📥 Installation & Deployment

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/davidahdy/note-taking-app.git
cd note-taking-app
```

### 2️⃣ Update Inventory

Edit `inventory.ini` and add your EC2 server’s IP address:

```ini
[webserver]
your.ec2.ip.address ansible_user=ec2-user ansible_ssh_private_key_file=~/.ssh/your-key.pem
```

### 3️⃣ Run the Playbook

```bash
ansible-playbook -i inventory.ini playbook.yml
```

### 4️⃣ Access the Web App

Open your browser and go to:

```
http://your.ec2.ip.address
```

---

## 💾 Backup Strategy

* A dedicated AWS EBS volume is mounted to `/backup`.
* Database backups are stored automatically at scheduled intervals.
* Backups are timestamped for easy recovery.


