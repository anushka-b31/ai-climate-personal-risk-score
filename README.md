GeoFend AI – Personal Climate Risk Analyzer

AI-powered climate risk analysis system that calculates personalized climate risk based on location, age, occupation, and living conditions. GeoFend AI helps users understand their exposure to climate-related hazards and provides a simple risk assessment.

Problem Statement

Climate risks such as extreme heat, flooding, and air pollution do not affect everyone equally. A person’s location, age, occupation, housing conditions, and access to protective facilities can influence their vulnerability.

GeoFend AI aims to provide a simple and accessible way for individuals to understand their personal climate vulnerability and identify the major risks they may face.

Solution

GeoFend AI collects basic information about the user and analyzes different factors to generate a personalized climate risk assessment.

The system considers parameters such as:

* Location
* Age
* Occupation
* Home floor
* Availability of air conditioning
* Drainage conditions

Based on these inputs, the system provides individual risk scores and an overall climate vulnerability assessment.

Key Features

* Personalized climate risk assessment
* Heat risk analysis
* Flood risk analysis
* Air pollution risk analysis
* Overall climate vulnerability score
* Location-based risk evaluation
* Simple and user-friendly interface
* Fast risk calculation
* Easy-to-understand results

How It Works

User Information
       |
       v
Location & Personal Factors
       |
       v
Risk Analysis
       |
       +----------------+
       |                |
       v                v
   Heat Risk       Flood Risk
       |                |
       +--------+-------+
                |
                v
        Air Pollution Risk
                |
                v
     Overall Climate Risk
                |
                v
       Personalized Result

Technology Stack

* Python
* Flask
* HTML
* CSS
* JavaScript
* Jinja Templates
* REST APIs

Project Structure

GeoFend-AI/
│
├── app.py
├── templates/
│   └── index.html
├── README.md
└── requirements.txt

Installation

Clone the repository:

git clone <repository-url>

Move into the project folder:

cd GeoFend-AI

Install the required dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open the local URL displayed by Flask in your browser.

Risk Assessment

GeoFend AI evaluates multiple dimensions of climate vulnerability:

Heat Risk

Estimates vulnerability to high temperatures based on location and personal factors.

Flood Risk

Considers factors such as location, home floor, and drainage conditions.

Air Pollution Risk

Evaluates potential exposure to air pollution based on location and user conditions.

Overall Climate Risk

Combines the individual risk factors into an overall assessment to provide a clearer picture of the user’s climate vulnerability.

Future Improvements

* Integration with real-time weather and climate APIs
* Live air-quality data
* Real-time flood and heat alerts
* Interactive geospatial risk maps
* Machine learning-based prediction
* Location-specific recommendations
* Historical climate trend analysis
* Mobile application
* Personalized emergency preparedness suggestions

Contributors

* Anushka Basak
* Atreyi Som
* Ankita Mandal
* Anusuya Dalapati

Disclaimer

GeoFend AI is an educational and predictive climate-risk assessment tool. Its results are intended for awareness and informational purposes and should not be considered a substitute for official weather, emergency, or government advisories.
