# AI-Powered Health Diagnostic Dashboard

## Overview
The AI-Powered Health Diagnostic Dashboard is an innovative platform designed to assist users in diagnosing health conditions based on their symptoms and medical history. By leveraging artificial intelligence, this application provides personalized health diagnostics and insights, empowering users to take proactive steps in managing their health. The platform is particularly beneficial for individuals seeking quick and preliminary health assessments without immediate access to professional medical consultation.

The dashboard offers a user-friendly interface where users can input symptoms, view their health profile, and receive insights and recommendations. It is built with modern web technologies, ensuring a seamless and responsive user experience.

## Features
- **Symptom Checker**: Allows users to input symptoms and receive a preliminary diagnosis, helping them understand potential health issues.
- **User Profile Management**: Users can view and update their personal information, including age, gender, and medical history.
- **Health Insights**: Provides users with data-driven insights and recommendations to improve their health based on their profile and symptoms.
- **Responsive Design**: Ensures the dashboard is accessible and functional on various devices, including desktops and mobile devices.
- **Simple Navigation**: Intuitive navigation bar for easy access to different sections like Home, Symptom Checker, User Profile, Health Insights, and About.

## Tech Stack
| Technology   | Description                                    |
|--------------|------------------------------------------------|
| Python       | Core programming language                     |
| FastAPI      | Web framework for building APIs               |
| Uvicorn      | ASGI server for running FastAPI applications  |
| Pydantic     | Data validation and settings management       |
| SQLite3      | Lightweight database for storing user data    |
| HTML/CSS/JS  | Frontend technologies for UI/UX               |
| Docker       | Containerization for deployment               |

## Architecture
The project is structured to separate concerns between the frontend and backend, ensuring a clean architecture.

- **Backend**: Built with FastAPI, handling API requests and serving HTML content.
- **Frontend**: Static HTML pages styled with CSS and enhanced with JavaScript for interactivity.
- **Database**: SQLite3 used for storing user data, symptoms, and insights.

### Diagram
```
+-----------------------------------+
|          User Interface           |
| (HTML/CSS/JS served by FastAPI)   |
+-----------------------------------+
                |
                v
+-----------------------------------+
|            FastAPI                |
|  (Handles API requests/responses) |
+-----------------------------------+
                |
                v
+-----------------------------------+
|            SQLite3               |
|   (Stores user data and insights) |
+-----------------------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (optional for container deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-health-diagnostic-dashboard-auto.git
   cd ai-powered-health-diagnostic-dashboard-auto
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit `http://127.0.0.1:8000` to access the dashboard.

## API Endpoints
| Method | Path               | Description                                |
|--------|--------------------|--------------------------------------------|
| GET    | `/`                | Home page                                  |
| GET    | `/diagnosis`       | Symptom Checker page                       |
| GET    | `/profile`         | User Profile page                          |
| GET    | `/insights`        | Health Insights page                       |
| GET    | `/about`           | About page                                 |
| POST   | `/api/diagnose`    | Submit symptoms for diagnosis              |
| GET    | `/api/user/{id}`   | Retrieve user information by ID            |
| PUT    | `/api/user/{id}`   | Update user information by ID              |
| GET    | `/api/insights`    | Retrieve health insights                   |

## Project Structure
```
├── Dockerfile                # Docker configuration for container deployment
├── app.py                    # Main application file with API routes
├── requirements.txt          # Python dependencies
├── start.sh                  # Script to start the application
├── static                    # Static files (CSS, JS)
│   ├── css
│   │   └── style.css         # Main stylesheet for the application
│   └── js
│       └── main.js           # JavaScript for interactivity
└── templates                 # HTML templates for different pages
    ├── about.html            # About page
    ├── diagnosis.html        # Symptom Checker page
    ├── index.html            # Home page
    ├── insights.html         # Health Insights page
    └── profile.html          # User Profile page
```

## Screenshots
*Screenshots of the application interface will be added here to showcase the design and functionality.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t health-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 health-dashboard
   ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive messages.
4. Push your branch and open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Built with Python and FastAPI.