from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Simulated student and event data
students = {
    "student1": {"name": "John Doe", "involvement_level": "Participant"},
    "student2": {"name": "Jane Smith", "involvement_level": "Organizer"}
}

event_details = {
    "event_name": "Sample Event",
    "event_date": "September 23, 2023",
    "location": "Virtual"
}

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
    student_id = request.form['student']
    student = students.get(student_id)
    if student:
        return render_template('certificate_preview.html', **event_details, **student)
    else:
        return "Student not found."

@app.route('/download_certificate')
def download_certificate():
    # Generate and serve the certificate as a PDF (you'll need a PDF generation library)
    # For example, you can use Flask-PDFKit or ReportLab for PDF generation.
    # You should customize this part according to your PDF generation method.
    # Once generated, save the PDF to the 'static/certificates/' folder.
    # Replace 'certificate.pdf' with the actual filename.
    certificate_path = 'static/certificates/certificate.pdf'

    return send_file(certificate_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
