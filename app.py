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
    data = {
        'kod_produktu': request.form['kod_produktu'],
        'proba': request.form['proba'],
        'grawer': 'grawer' in request.form,  # Sprawdzenie czy klucz 'grawer' istnieje w formularzu
        'dla_kogo': request.form['dla_kogo'],
        'rodzaj': request.form['rodzaj'],
        'styl': request.form['styl'],
        'pochodzenie': request.form['pochodzenie'],
        'szkielko': request.form['szkielko'],
        'rodzaj_koperty': request.form['rodzaj_koperty'],
        'szerokosc_koperty': request.form['szerokosc_koperty'],
        'grubosc_koperty': request.form['grubosc_koperty'],
        'typ_paska_bransolety': request.form['typ_paska_bransolety'],
        'kolor_paska_bransolety': request.form['kolor_paska_bransolety'],
        'wodoszczelnosc': request.form['wodoszczelnosc'],
        'mechanizm': request.form['mechanizm'],
        'gwarancja': request.form['gwarancja'],
        'kolor_tarczy': request.form['kolor_tarczy']
    }

    watch = Watch(**data)
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
        watch.kod_produktu = request.form.get('kod_produktu')
        watch.proba = request.form.get('proba')
        watch.grawer = bool(request.form.get('grawer'))
        # Update the remaining attributes here

        db_session.commit()
        return redirect(url_for('watch', watch_id=watch_id))
    return render_template('edit_watch.html', watch=watch)


if __name__ == '__main__':
    app.run(debug=True)
