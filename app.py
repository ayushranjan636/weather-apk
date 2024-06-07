from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# OpenWeatherMap API key
api_key = 'f82c09f037dcf68401060c2f2b1a45de'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}'
    response = requests.get(api_url)
    data = response.json()

    if data['cod'] == '404':
        return render_template('index.html', error='No City Found')

    weather = data['weather'][0].get('main', 'No Data')
    temp_fahrenheit = data['main'].get('temp', 'No Data')
    temp_celsius = round((temp_fahrenheit - 32) * 5 / 9, 2) if isinstance(temp_fahrenheit, (int, float)) else 'No Data'

    return render_template('index.html', city=city, weather=weather, temp=temp_celsius)

if __name__ == '__main__':
    app.run(debug=True)
