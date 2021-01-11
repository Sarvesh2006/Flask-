import requests
from flask import *
from flask import render_template
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError


location = TextField("Location")
submit = SubmitField("Submit")


class Weather(Form):
    location = TextField(
        "Location", validators=[validators.required(), validators.length(max=20)])
    submit = SubmitField("Submit")


class Result():
    api_key = 'fed28c90f1a04868d21243536e5194af'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = f'location'
    complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=fed28c90f1a04868d21243536e5194af&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidiy = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]
    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidiy = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))

    else:
        print('City not found')


app = Flask(__name__)
app.secret_key = 'sarvesh@23'


@app.route('/', methods=['GET', 'POST'])
def home():
    input = Weather()
    if input.validate() == False:
        flash('Location is required.')
    return render_template('homepage.html', input=input)


@app.route('/success', methods=['GET', 'POST'])
def result():
    result = Result()
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
