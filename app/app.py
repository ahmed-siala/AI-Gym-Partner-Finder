from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Sample data for users (same as before)
users = [
    {"name": "Ahmed", "gender": "Male", "age": 24, "country": "Tunisia", "city": "Tunis", "img": "594cdde419dde7e4942afb2eedb4e24d.jpg"},
    {"name": "Mariem", "gender": "Female", "age": 22, "country": "Tunisia", "city": "Sousse", "img": "225756e0d3a991443ee7736f1ccdf709.jpg"},
    {"name": "Yassine", "gender": "Male", "age": 27, "country": "Tunisia", "city": "Sfax", "img": "79c36d360329c964c247ca526b66885e.jpg"},
    {"name": "Fatma", "gender": "Female", "age": 21, "country": "Tunisia", "city": "Bizerte", "img": "99f0541ed4be448e537fa4df490ca332.jpg"},
    {"name": "Anis", "gender": "Male", "age": 29, "country": "Tunisia", "city": "Nabeul", "img": "6ee79e0d05ce0bb444dbde1d8987345f.jpg"},
    {"name": "Rania", "gender": "Female", "age": 26, "country": "Tunisia", "city": "Monastir", "img": "1b12902a2632d94d1d0c4097318f7642.jpg"},
    {"name": "Ramy", "gender": "Male", "age": 25, "country": "Tunisia", "city": "Sfax", "img": "63a16417-603a-4496-8963-af2d7e928712.jpg"},
    {"name": "Emna", "gender": "Female", "age": 23, "country": "Tunisia", "city": "Kairouan", "img": "e744ef8c8202bec30fd590a3b0c7756a.jpg"},
    {"name": "Mohaimen", "gender": "Male", "age": 21, "country": "Tunisia", "city": "Sfax", "img": "Screenshot 2025-04-28 015653.png"},
    {"name": "Kmar", "gender": "Female", "age": 20, "country": "Tunisia", "city": "Sfax", "img": "Screenshot 2025-04-28 014538.png"}
]

@app.route('/')
def home():
    return render_template('gym.html', users=users)

@app.route('/foundyourfriends', methods=['GET'])
def foundyourfriends():
    # Pass all users to found_friends.html, no filtering by city
    return render_template('found_friends.html', friends=users)

@app.route('/find_gym_partners', methods=['GET'])
def find_gym_partners():
    # Get the city from the URL parameter
    city = request.args.get('city', default='Sfax', type=str)
    
    # Filter users based on the selected city
    filtered_users = [user for user in users if user['city'] == city]
    
    return render_template('ai_found_gym_partner.html', city=city, friends=filtered_users)

@app.route('/signin')
def signin():
    return render_template('signinPage.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/createanaccount')
def createanaccount():
    return render_template('create_an_account.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(debug=True)
