from flask import Flask,render_template,request
import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=014093f04f1d04c9e512539a36d4aaa9&q='
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather',methods=['GET','POST'])
def weather():
        city=request.form['city_name']
        url=api_address + city
        json_data=requests.get(url).json()
        desc=json_data['weather'][0]['main']
        temp_k=float(json_data['main']['temp'])
        temp_c=temp_k-273.15
        t1=float(json_data['main']['temp_min'])
        t2=t1-273.15
        t3=float(json_data['main']['temp_max'])
        t4=t3-273.15
        name=json_data['name']
        return render_template("weather.html",temp_min=round(t2,2),temp_max=round(t4,2),main=desc,temp=round(temp_c,2),name=name)

@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

if __name__=='__main__':
    app.run(debug=True)    