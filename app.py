from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

API_KEY = "8e9f88befce22ee1d518c610cc52ffcd"


@app.route("/", methods=["GET", "POST"])
def home():

    risk_score = None
    risk_level = ""
    risk_color = "blue"
    heat_risk = ""
    flood_risk = ""
    air_risk = ""
    ai_analysis = ""
    climate_insight = ""
    season = ""
    temperature = ""

    city = ""
    age = ""
    occupation = ""

    if request.method == "POST":

        city = request.form.get("city") or ""
        age = int(request.form.get("age") or 0)
        occupation = request.form.get("occupation") or ""

        city_lower = city.lower()

        risk_score = 0

        # AGE RISK
        if age > 50:
            risk_score += 3
        elif age >= 30:
            risk_score += 2
        else:
            risk_score += 1


        # HEAT RISK
        if city_lower in ["delhi", "jaipur", "nagpur", "ahmedabad"]:
            heat_risk = "High"
            risk_score += 3
        elif city_lower in ["mumbai", "kolkata", "chennai"]:
            heat_risk = "Moderate"
            risk_score += 2
        else:
            heat_risk = "Low"
            risk_score += 1


        # FLOOD RISK
        if city_lower in ["mumbai", "kolkata", "chennai", "guwahati"]:
            flood_risk = "High"
            risk_score += 3
        elif city_lower in ["delhi", "patna"]:
            flood_risk = "Moderate"
            risk_score += 2
        else:
            flood_risk = "Low"
            risk_score += 1


        # AIR POLLUTION RISK
        if city_lower in ["delhi", "kanpur", "lucknow"]:
            air_risk = "High"
            risk_score += 3
        elif city_lower in ["mumbai", "kolkata", "chennai"]:
            air_risk = "Moderate"
            risk_score += 2
        else:
            air_risk = "Low"
            risk_score += 1


        # LIMIT SCORE
        if risk_score > 10:
            risk_score = 10


        # FINAL RISK LEVEL
        if risk_score <= 3:
            risk_level = "Low"
            risk_color = "green"
        elif risk_score <= 6:
            risk_level = "Moderate"
            risk_color = "orange"
        else:
            risk_level = "High"
            risk_color = "red"


        # AI ANALYSIS
        if risk_level == "High":
            ai_analysis = "Your profile indicates significant exposure to climate risks based on regional environmental conditions."
        elif risk_level == "Moderate":
            ai_analysis = "Moderate climate vulnerability detected based on geographic and demographic factors."
        else:
            ai_analysis = "Low climate vulnerability detected based on your location and demographic profile."


        # CLIMATE INSIGHT
        if heat_risk == "High":
            climate_insight = "Your region experiences frequent heatwaves and rising summer temperatures."
        elif flood_risk == "High":
            climate_insight = "Your city has historically experienced flooding during monsoon seasons."
        elif air_risk == "High":
            climate_insight = "Air quality levels in your region frequently exceed recommended health limits."
        else:
            climate_insight = "Your region currently shows relatively lower climate vulnerability."


        # WEATHER API CALL
        try:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(weather_url)
            data = response.json()

            temperature = data["main"]["temp"]

        except:
            temperature = "Unavailable"


        # SEASON CALCULATION
        month = datetime.datetime.now().month

        if month in [12, 1, 2]:
            season = "Winter"
        elif month in [3, 4, 5]:
            season = "Summer"
        elif month in [6, 7, 8, 9]:
            season = "Monsoon"
        else:
            season = "Autumn"


    return render_template(
        "index.html",
        risk_score=risk_score,
        risk_level=risk_level,
        risk_color=risk_color,
        heat_risk=heat_risk,
        flood_risk=flood_risk,
        air_risk=air_risk,
        ai_analysis=ai_analysis,
        climate_insight=climate_insight,
        season=season,
        temperature=temperature,
        city=city,
        age=age,
        occupation=occupation
    )


if __name__ == "__main__":
    app.run(debug=True)
