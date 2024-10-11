from flask import Flask, render_template, request
import requests  # pip install requests

app = Flask(__name__)  # Initialize app

# Config
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID=5bdd49e28ba9a9aad7b4e3e13412fa3c'
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']
            icon = data['weather'][0]['icon']

            print(temp, weather, min_temp, max_temp, icon)
            return render_template('index.html', temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp, icon=icon, city_name=city_name)
        else:
            # Handle the case where the city is not found
            error_message = "City not found. Please enter a valid city name."
            return render_template('index.html', error=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
