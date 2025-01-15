from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store registered participants
participants = []

# List of events
events = [
    {"name": "Cultural Night", "description": "Mesmerizing performances", "price": "₹500", "image": "logo.jpg"},
    {"name": "Sports Tournament", "description": "Exciting competitions", "price": "₹300", "image": "logo.jpg"},
    {"name": "Tech Talk", "description": "Innovative discussions", "price": "₹400", "image": "logo.jpg"},
    {"name": "Art Workshop", "description": "Creative painting sessions", "price": "₹250", "image": "logo.jpg"},
    {"name": "Cultural Night", "description": "Mesmerizing performances", "price": "₹500", "image": "logo.jpg"},
    {"name": "Sports Tournament", "description": "Exciting competitions", "price": "₹300", "image": "logo.jpg"},
    {"name": "Tech Talk", "description": "Innovative discussions", "price": "₹400", "image": "logo.jpg"},
    {"name": "Art Workshop", "description": "Creative painting sessions", "price": "₹250", "image": "logo.jpg"},
    {"name": "Cultural Night", "description": "Mesmerizing performances", "price": "₹500", "image": "logo.jpg"},
    {"name": "Sports Tournament", "description": "Exciting competitions", "price": "₹300", "image": "logo.jpg"},
    {"name": "Tech Talk", "description": "Innovative discussions", "price": "₹400", "image": "logo.jpg"},
    {"name": "Art Workshop", "description": "Creative painting sessions", "price": "₹250", "image": "logo.jpg"},
]

# Home Page
@app.route('/')
def home():
    return render_template('home.html', events=events)

# Register Page (Handles Form Submission)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        event = request.form['event']
        participants.append({"name": name, "email": email, "contact": contact, "event": event, "paid": False})
        return redirect(url_for('check_status'))
    return render_template('register.html', events=events)

# Check Status Page
@app.route('/check_status')
def check_status():
    return render_template('check_status.html', participants=participants)

# Handle Payment
@app.route('/pay/<int:participant_id>')
def pay(participant_id):
    participants[participant_id]['paid'] = True
    return redirect(url_for('check_status'))

# Delete Registration
@app.route('/delete/<int:participant_id>')
def delete(participant_id):
    participants.pop(participant_id)
    return redirect(url_for('check_status'))

# Contact Us Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
