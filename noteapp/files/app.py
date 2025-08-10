from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('/opt/note_app/notes.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        note = request.form['note']
        timestamp = datetime.datetime.now()
        cursor.execute('INSERT INTO notes (content, timestamp) VALUES (?, ?)', (note, timestamp))
        conn.commit()
        conn.close()
        return redirect('/')  # 🔁 Redirect instead of rendering template again

    cursor.execute('SELECT * FROM notes ORDER BY timestamp DESC')
    notes = cursor.fetchall()
    conn.close()
    return render_template('note_template.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
