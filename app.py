from flask import Flask, render_template, request, redirect, url_for

from attribute import Attribute
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


@app.route('/add_watch', methods=['GET', 'POST'])
def add_watch():
    if request.method == 'POST':
        kod_produktu = request.form['kod_produktu']
        attribute_ids = request.form.getlist('attribute_ids')

        watch = Watch(kod_produktu=kod_produktu)
        db_session.add(watch)

        for attribute_id in attribute_ids:
            attribute = Attribute.query.get(attribute_id)
            watch.attributes.append(attribute)

        db_session.commit()
        return redirect(url_for('index'))
    else:
        attributes = Attribute.query.all()
        return render_template('add_watch.html', attributes=attributes, attribute_ids=[])  # Dodaj attribute_ids=[]


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
        watch.dla_kogo = request.form.get('dla_kogo')
        watch.rodzaj = request.form.get('rodzaj')
        watch.styl = request.form.get('styl')
        watch.pochodzenie = request.form.get('pochodzenie')
        watch.szkielko = request.form.get('szkielko')
        watch.rodzaj_koperty = request.form.get('rodzaj_koperty')
        watch.szerokosc_koperty = request.form.get('szerokosc_koperty')
        watch.grubosc_koperty = request.form.get('grubosc_koperty')
        watch.typ_paska_bransolety = request.form.get('typ_paska_bransolety')
        watch.kolor_paska_bransolety = request.form.get('kolor_paska_bransolety')
        watch.wodoszczelnosc = request.form.get('wodoszczelnosc')
        watch.gwarancja = request.form.get('gwarancja')
        watch.kolor_tarczy = request.form.get('kolor_tarczy')

        db_session.commit()
        return redirect(url_for('watch', watch_id=watch_id))
    return render_template('edit_watch.html', watch=watch)


@app.route('/attributes')
def attributes():
    attributes = Attribute.query.all()
    return render_template('attributes.html', attributes=attributes)


if __name__ == '__main__':
    app.run(debug=True)
