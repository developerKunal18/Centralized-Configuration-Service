🧠 Why This Is Important

Without centralized config:
User Service     → config.py
Order Service    → config.py
Payment Service  → config.py

Changing one setting means updating every service.

With centralized config:
Services
    ↓
Configuration Service
    ↓
Shared Settings

👉 Used by:
Spring Cloud Config
Kubernetes ConfigMaps
Consul
AWS Parameter Store

🛠 Tech Stack
Python
Flask
JSON Storage

📂 Project Structure
config-service/
├── app.py
├── config.json
└── README.md
