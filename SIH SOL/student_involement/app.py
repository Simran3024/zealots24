from flask import Flask, render_template

app = Flask(__name__)

# Sample event data. Replace with your actual data.
events = {
    'event1': {
        'students': [
            {'name': 'Student 1', 'level': 'Participant'},
            {'name': 'Student 2', 'level': 'Organizer'},
            {'name': 'Student 3', 'level': 'Winner'},
        ],
    },
    'event2': {
        'students': [
            {'name': 'Student 4', 'level': 'Participant'},
            {'name': 'Student 5', 'level': 'Participant'},
            {'name': 'Student 6', 'level': 'Organizer'},
        ],
    },
}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', events=events)

@app.route('/involvement_levels/<event_name>')
def involvement_levels(event_name):
    if event_name in events:
        event = events[event_name]
        return render_template('involvement_levels.html', event_name=event_name, students=event['students'])
    else:
        return 'Event not found'

if __name__ == '__main__':
    app.run(debug=True)
