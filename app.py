from flask import Flask, render_template, request, redirect, url_for
from database import db_session
from watch import Watch

app = Flask(__name__)


@app.route('/')
def index():
    watches = Watch.query.all()
    return render_template('index.html', watches=watches)


@app.route('/watch/<watch_id>')
def watch(watch_id):
    watch = Watch.query.get(watch_id)
    return render_template('watch.html', watch=watch)


@app.route('/add_watch', methods=['POST'])
def add_watch():
    watch = Watch(**request.form)
    db_session.add(watch)
    db_session.commit()
    return redirect(url_for('index'))


@app.route('/delete_watch/<watch_id>', methods=['POST'])
def delete_watch(watch_id):
    watch = Watch.query.get(watch_id)
    db_session.delete(watch)
    db_session.commit()
    return redirect(url_for('index'))


@app.route('/edit_watch/<watch_id>', methods=['GET', 'POST'])
def edit_watch(watch_id):
    watch = Watch.query.get(watch_id)
    if request.method == 'POST':
        for key, value in request.form.items():
            setattr(watch, key, value)
        db_session.commit()
        return redirect(url_for('watch', watch_id=watch_id))
    return render_template('edit_watch.html', watch=watch)


if __name__ == '__main__':
    app.run(debug=True)
