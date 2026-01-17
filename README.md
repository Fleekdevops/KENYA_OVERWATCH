# Kenya Overwatch Project

## 1. Project Overview

Kenya Overwatch is a national-scale, AI-powered road safety and public security intelligence system designed to address Kenya's rising rate of accidents, infrastructural hazards, and growing security concerns. The platform utilizes cutting-edge computer vision, IoT sensors, artificial intelligence analytics, and predictive modeling to monitor road activities and public spaces in real-time. The system provides early detection and rapid response capabilities, greatly reducing incidents and improving transportation efficiency.

## 2. Key Features

*   **AI Smart Camera Network:** Utilizing AI detection capabilities to identify overspeeding, dangerous overtaking, lane violations, vehicle breakdowns, stalled or abandoned vehicles, theft, vandalism, suspicious movements, illegal PSV behavior, crowd disturbances, abandoned bags, and illegal activities.
*   **Public Safety Monitoring:** Strategic placement of cameras in public walkways, urban centers, schools, hospitals, and transport hubs.
*   **Emergency & Enforcement Integration:** Automatic alerts sent to NTSA, Traffic police, County emergency units, Ambulance services, and Fire departments to reduce average response time.
*   **Predictive Analytics Engine:** Uses long-term historical data and machine learning to identify dangerous roads, forecast accident patterns, recommend infrastructure redesign, and advise on optimal patrol deployment.
*   **Citizen Companion App:** Allows the public to report incidents, receive verified alerts, check traffic and safety zones, and submit AI-validated videos/photos.

## 3. Architecture

The Kenya Overwatch project is structured as a monorepo, encompassing several distinct but interconnected services:

*   **Backend (FastAPI):** Core API service handling data persistence, business logic, and serving data to the web dashboard and mobile app.
*   **AI Engine:** Contains scripts and models for training and inference of AI algorithms (e.g., YOLOv8).
*   **Edge Agent:** Software deployed on edge devices (e.g., IoT cameras) responsible for video processing, running AI inference locally, and reporting incidents to the backend.
*   **Web Dashboard (Next.js):** The command center interface for operators to monitor live incidents, view maps, and access analytics.
*   **Mobile App (Flutter):** A citizen-facing application for reporting incidents and receiving alerts.
*   **Infrastructure:** Contains configuration files for infrastructure as code (Terraform) and Docker Compose for local development/deployment.
*   **DevOps:** GitHub Actions workflows for continuous integration and deployment.

## 4. Technology Stack

*   **Backend:** Python (FastAPI, SQLAlchemy, PostgreSQL, Psycopg2, Alembic)
*   **AI/ML:** Python (Ultralytics YOLOv8, OpenCV, PyTorch)
*   **Edge Agent:** Python (OpenCV, Requests, Ultralytics YOLOv8)
*   **Web Dashboard:** Next.js, React, TypeScript, Tailwind CSS, Leaflet, SWR
*   **Mobile App:** Flutter, Dart, HTTP, Image Picker
*   **Database:** PostgreSQL
*   **Orchestration:** Docker, Docker Compose
*   **Infrastructure as Code (IaC):** Terraform (placeholder for AWS)
*   **CI/CD:** GitHub Actions

## 5. Setup and Installation (Local Development)

To set up and run the project locally using Docker Compose:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/kenya-overwatch.git
    cd kenya-overwatch
    ```

2.  **Build and run the Docker containers:**
    Make sure you have Docker installed and running.
    ```bash
    docker compose up --build -d
    ```
    This will build the `backend` service, start the `db` (PostgreSQL) service, and run them in detached mode.

3.  **Perform Database Migrations:**
    While the `db` service is running, you need to run the Alembic migrations for the backend.
    ```bash
    docker compose exec backend C:\Users\hani\Desktop\WORKSHOPZ\@FL\KENYA_OVERWATCH\.venv\Scripts\python.exe -m alembic upgrade head
    ```
    *Note: The path to python.exe might need to be adjusted based on your environment inside the docker container if this command fails.*

4.  **Install Web Dashboard dependencies:**
    ```bash
    cd web_dashboard
    npm install
    cd ..
    ```

5.  **Install AI Engine and Edge Agent Python dependencies:**
    It's recommended to create a Python virtual environment for each.
    ```bash
    cd backend
    python -m venv .venv
    .venv/Scripts/activate # On Windows
    # source .venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    deactivate
    cd ..

    cd ai_engine
    python -m venv .venv
    .venv/Scripts/activate # On Windows
    # source .venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    deactivate
    cd ..

    cd edge_agent
    python -m venv .venv
    .venv/Scripts/activate # On Windows
    # source .venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    deactivate
    cd ..
    ```

## 6. Running the Application

After completing the setup:

*   **Backend:** The FastAPI backend will be running inside Docker at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/api/v1/docs`.
*   **Web Dashboard:**
    ```bash
    cd web_dashboard
    npm run dev
    ```
    Access the dashboard at `http://localhost:3000`. (Ensure `NEXT_PUBLIC_API_URL` in `web_dashboard/.env.local` points to your backend).
*   **Edge Agent:**
    ```bash
    cd edge_agent
    .venv/Scripts/activate # On Windows
    # source .venv/bin/activate # On macOS/Linux
    python main.py
    ```
    This will start the edge agent, which will attempt to connect to a video source (defaulting to webcam 0) and send incident reports to the backend. Ensure the backend is running.
*   **AI Engine (Training):**
    ```bash
    cd ai_engine
    .venv/Scripts/activate # On Windows
    # source .venv/bin/activate # On macOS/Linux
    python train.py
    ```
    This will run a placeholder training script for the YOLOv8 model.
*   **Mobile App:**
    To run the Flutter mobile app, you need a Flutter development environment set up.
    ```bash
    cd mobile_app
    flutter pub get
    flutter run
    ```

## 7. Future Enhancements

*   **Authentication and Authorization:** Implement user management and role-based access control for the backend and dashboard.
*   **Real-time Communication:** Integrate WebSockets or GraphQL Subscriptions for real-time incident updates on the dashboard.
*   **Advanced AI Models:** Enhance AI models for more precise object detection, behavior analysis, and predictive capabilities.
*   **Deployment Automation:** Further develop Terraform configurations for full cloud deployment on AWS, Azure, or GCP.
*   **Monitoring and Alerting:** Implement comprehensive monitoring, logging, and alerting solutions.
*   **Military-Grade Hardening:** As per the roadmap, future phases could include military/classified security layers, zero-trust architectures, anti-sabotage/adversarial AI hardening, and defense-grade redundancy.

---
This README provides a comprehensive overview and operational guide for the Kenya Overwatch project MVP.
