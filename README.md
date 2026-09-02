GeoFend AI – Personal Climate Risk Analyzer

GeoFend AI is an AI-powered climate risk assessment system designed to help individuals understand how vulnerable they may be to different climate-related hazards.

The system analyzes personal and environmental factors such as location, age, occupation, home floor, air-conditioning availability, and drainage conditions to generate a personalized climate risk assessment.

Problem Statement

Climate change affects people differently depending on where they live and their personal circumstances. Extreme heat, flooding, and air pollution can create serious risks, especially for people living in vulnerable locations or conditions.

However, climate information is often presented at a general level and does not explain how these risks may affect an individual.

GeoFend AI addresses this gap by converting basic personal and location information into a simple, understandable climate risk assessment.

Solution

GeoFend AI provides a personalized assessment of three major climate-related risks:

* Heat Risk – evaluates potential vulnerability to extreme temperatures.
* Flood Risk – considers factors such as location, home floor, and drainage conditions.
* Air Pollution Risk – evaluates potential exposure to poor air quality.

These factors are combined to provide an overall climate vulnerability assessment, helping users understand their major areas of risk.

Key Features

Personalized Risk Assessment

The system uses individual information instead of providing the same climate-risk result to everyone.

Heat Risk Analysis

Identifies potential vulnerability to extreme heat based on location and personal factors.

Flood Risk Analysis

Considers environmental and housing-related factors such as drainage and the floor on which the user lives.

Air Pollution Risk

Provides an assessment of potential exposure to air pollution based on location-related risk factors.

Overall Climate Risk

Combines multiple risk factors into a single, easy-to-understand assessment.

Simple User Interface

The application is designed to make climate-risk information easy to understand, even for users without technical knowledge.

How It Works

The system follows a simple five-step process:

1. Enter Information

The user provides basic details such as:

* Location
* Age
* Occupation
* Home floor
* AC availability
* Drainage conditions

2. Analyze Risk Factors

GeoFend AI evaluates the user’s information against different climate-risk factors.

3. Calculate Individual Risks

The system calculates separate assessments for:

* Heat
* Flood
* Air pollution

4. Generate Overall Assessment

The individual risk factors are combined to determine the user’s overall climate vulnerability.

5. Display Results

The final results are presented in a simple format so that users can quickly understand their climate risks.

Technology Stack

Backend

* Python
* Flask

Frontend

* HTML
* CSS
* JavaScript
* Jinja Templates

Data & APIs

* REST APIs
* Location and climate-related data sources

Project Structure

GeoFend-AI/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
│
└── README.md

Installation

1. Clone the Repository

git clone <repository-url>

2. Open the Project Folder

cd GeoFend-AI

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

python app.py

5. Open the Application

Open the local Flask URL shown in the terminal, usually:

http://127.0.0.1:5000/

Example Assessment

A user provides information about their location and living conditions.

GeoFend AI analyzes these inputs and produces results such as:

Heat Risk: High
Flood Risk: Medium
Air Pollution Risk: High
Overall Climate Vulnerability: High

The purpose is not just to provide a score, but to help the user understand which climate risks are most relevant to them.

Future Enhancements

GeoFend AI can be expanded into a more advanced real-time climate intelligence platform.

Planned improvements include:

* Real-time weather data integration
* Live air-quality monitoring
* Real-time flood alerts
* Interactive geospatial climate-risk maps
* Machine learning-based risk prediction
* Historical climate trend analysis
* Location-specific recommendations
* Personalized emergency preparedness guidance
* Mobile application
* Real-time climate notifications

Impact

GeoFend AI aims to make climate-risk information more personal, accessible, and actionable.

Instead of asking:

“Is my city at risk?”

GeoFend AI helps answer:

“How vulnerable am I, and what climate risks should I be aware of?”

This approach can support better climate awareness, preparedness, and decision-making at an individual level.

Contributors

* Anushka Basak
* Atreyi Som
* Ankita Mandal
* Anusuya Dalapati

Disclaimer

GeoFend AI is an educational and predictive climate-risk assessment tool intended for awareness and informational purposes. Its results should not be considered a replacement for official weather forecasts, government advisories, emergency warnings, or professional risk assessments.
