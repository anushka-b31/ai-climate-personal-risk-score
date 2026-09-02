GeoFend-AI – Personal Climate Risk Analyzer

AI-powered climate risk analysis system that calculates personalized climate risk based on location, age, occupation, and living conditions. GeoFend AI helps users understand their exposure to climate-related hazards and provides a simple and easy-to-understand risk assessment.

Problem Statement

Climate risks such as extreme heat, flooding, and air pollution do not affect everyone equally. A person’s location, age, occupation, housing conditions, and access to protective facilities can influence their vulnerability.

This project aims to provide an accessible way for individuals to understand their personal climate vulnerability and identify the major environmental risks they may face.

Solution

GeoFend AI collects basic information about the user and analyzes different personal and environmental factors to generate a personalized climate risk assessment.

The system considers key parameters including:

* Location
* Age
* Occupation
* Home Floor
* Availability of Air Conditioning
* Drainage Conditions

Based on these inputs, GeoFend AI evaluates different climate-related risks and provides individual risk scores along with an overall climate vulnerability assessment.

Features

* Personalized climate risk assessment
* Heat risk analysis
* Flood risk analysis
* Air pollution risk analysis
* Overall climate vulnerability score
* Location-based risk evaluation
* Fast risk calculation
* Simple and user-friendly interface
* Easy-to-understand risk results
* Personalized climate vulnerability insights

Tech Stack

Frontend:

* HTML
* CSS
* Jinja Templates

Backend:

* Python
* Flask

APIs:

* REST APIs
* Requests

Risk Assessment

Heat Risk

Evaluates a user’s vulnerability to extreme heat based on location and personal factors.

Flood Risk

Considers factors such as location, home floor, and drainage conditions to estimate potential flood vulnerability.

Air Pollution Risk

Evaluates potential exposure to air pollution based on location and user-related conditions.

Overall Climate Risk

Combines the individual risk factors to provide an overall assessment of the user’s climate vulnerability.

Installation and Setup

1. Clone the repository

git clone <repository-url>

2. Move into the project folder

cd GeoFend-AI

3. Install the required packages

pip install -r requirements.txt

4. Run the application

python app.py

5. Open the local URL displayed by Flask in your browser.

Example Assessment

The system can provide results such as:

* Heat Risk: High
* Flood Risk: Medium
* Air Pollution Risk: Medium
* Overall Climate Risk: High

The assessment helps users understand which climate-related factors may require greater attention.

Future Improvements

* Integration with real-time weather APIs
* Live air-quality data
* Real-time heat and flood alerts
* Interactive geospatial risk maps
* Machine learning-based climate prediction
* Location-specific recommendations
* Historical climate trend analysis
* Personalized emergency preparedness suggestions
* Mobile application

Contributors

* Anushka Basak – Frontend Development + Backend Development
* Atreyi Som – Development + Research
* Ankita Mandal – Development + Research
* Anusuya Dalapati – Development + Documentation

Disclaimer

GeoFend AI is an educational and predictive climate-risk assessment tool. Its results are intended for awareness and informational purposes and should not be considered a substitute for official weather forecasts, emergency alerts, or government advisories.
