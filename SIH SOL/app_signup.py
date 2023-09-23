from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Define a function to write data to a CSV file
def write_to_csv(data):
    with open('user_data.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

@app.route('/')
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate and sanitize input as needed.

        # Write data to CSV file
        write_to_csv([email, password])

        # Redirect the user to a thank-you page or wherever you like.
        return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "Thank you for signing up!"

if __name__ == '__main__':
    app.run(debug=True)
