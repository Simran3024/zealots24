from flask import Flask, render_template, request, redirect, url_for
import openpyxl

app = Flask(__name__)

# Function to check if user credentials are valid
def is_valid_credentials(email, password):
    try:
        # Load the Excel workbook
        wb = openpyxl.load_workbook('user_data.xlsx')

        # Select the default sheet (usually named 'Sheet')
        sheet = wb.active

        # Iterate through rows and check for a matching email and password
        for row in sheet.iter_rows(values_only=True):
            if row[0] == email and row[1] == password:
                return True

        # If no matching credentials found
        return False
    except Exception as e:
        print(e)
        return False

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if is_valid_credentials(email, password):
            return "Login successful!"
        else:
            return "Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
