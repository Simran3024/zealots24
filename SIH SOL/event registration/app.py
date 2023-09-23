from flask import Flask, render_template, request, redirect, url_for
import openpyxl

app = Flask(__name__)

# Helper function to save event details to Excel
def save_event_details(event_details):
    try:
        wb = openpyxl.load_workbook('event_details.xlsx')
        ws = wb.active
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Event Name', 'Event Date', 'Event Description', 'Location', 'Organizer Name', 'Additional Details'])
    
    ws.append(event_details)
    wb.save('event_details.xlsx')

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you can implement user authentication logic
        # For simplicity, we'll assume a valid login for now
        return redirect(url_for('dashboard'))
    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Event Registration Page
@app.route('/event_registration', methods=['GET', 'POST'])
def event_registration():
    if request.method == 'POST':
        event_name = request.form['event-name']
        event_date = request.form['event-date']
        event_description = request.form['event-description']
        event_location = request.form['event-location']
        organizer_name = request.form['organizer-name']
        additional_details = request.form['additional-details']

        event_details = [event_name, event_date, event_description, event_location, organizer_name, additional_details]
        save_event_details(event_details)

        return redirect(url_for('confirmation'))
    
    return render_template('event_details.html')

# Confirmation Page
@app.route('/confirmation', methods=['GET'])
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
