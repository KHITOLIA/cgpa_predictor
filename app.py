from flask import Flask, render_template, redirect, request
import numpy as np
import pickle

with open('pipe1.pkl', 'rb') as file:
    pipe = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cgpa', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        sleep_hours = request.form['sleep_hours']
        attendance = request.form['attendance']
        previous_sem_cgpa = request.form['previous_sem_cgpa']
        total_study_hours = request.form['total_study_hours']
        total_screen_time = request.form['total_screen_time']

        prediction = np.round(pipe.predict([[age, gender, sleep_hours, attendance, previous_sem_cgpa, total_study_hours, total_screen_time]])[0], 2)
        return render_template('predict.html', prediction = prediction)
    return render_template('predict.html')



if __name__ == '__main__':
    app.run(debug=True)

    
