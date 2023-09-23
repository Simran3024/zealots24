from flask import Flask, render_template, request, redirect, flash, send_file

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong and unique secret key

# Sample student data. Replace with your actual data.
students = {
    'event1': ["Student 1", "Student 2", "Student 3"],
    'event2': ["Student 4", "Student 5", "Student 6"]
}

attendance_data = {}  # Dictionary to store attendance data for each event

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/select_event', methods=['POST'])
def select_event():
    selected_event = request.form.get('event')
    if selected_event in students:
        return render_template('attendance_list.html', selected_event=selected_event, students=students[selected_event])
    else:
        flash('Event not found.')
        return redirect('/')

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    selected_event = request.form.get('selected_event')
    attended_students = request.form.getlist('attendance')
    
    if selected_event not in attendance_data:
        attendance_data[selected_event] = []

    attendance_data[selected_event].extend(attended_students)
    flash('Attendance marked successfully.')

    return redirect('/confirmation')

# ... (previous code)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/download/<excel_filename>')
def download_excel(excel_filename):
    return send_file(excel_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
