from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_risk(city, age, occupation):

    score = 0

    if city.lower() in ["delhi", "mumbai", "kolkata", "chennai"]:
        heat = "High"
        score += 30
    else:
        heat = "Medium"
        score += 20

    if age > 50:
        flood = "High"
        score += 25
    else:
        flood = "Medium"
        score += 15

    if occupation.lower() in ["construction worker", "farmer", "delivery worker"]:
        air = "High"
        score += 30
    else:
        air = "Medium"
        score += 15

    if score > 70:
        level = "High"
        advice = "Avoid outdoor work during extreme weather."
    elif score > 50:
        level = "Moderate"
        advice = "Stay updated on weather alerts and air quality."
    else:
        level = "Low"
        advice = "Maintain regular climate safety habits."

    return score, heat, flood, air, level, advice


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    heat = flood = air = level = advice = None
    city = age = occupation = ""

    if request.method == "POST":

        city = request.form.get("city")
        age = int(request.form.get("age"))
        occupation = request.form.get("occupation")

        score, heat, flood, air, level, advice = calculate_risk(city, age, occupation)

    return render_template(
        "index.html",
        score=score,
        heat=heat,
        flood=flood,
        air=air,
        level=level,
        advice=advice,
        city=city,
        age=age,
        occupation=occupation
    )


if __name__ == "__main__":
    app.run(debug=True)
