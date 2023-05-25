from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from watch import Watch


def add_sample_watch():
    engine = create_engine('sqlite:///watches.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tworzenie przykładowego zegarka
    sample_watch = Watch(
        kod_produktu='ZEG003',
        proba='18k',
        grawer=True,
        dla_kogo='Mężczyzna',
        rodzaj='Mechaniczny',
        styl='Elegancki',
        pochodzenie='Szwajcaria',
        szkielko='Szkło szafirowe',
        rodzaj_koperty='Stal nierdzewna',
        szerokosc_koperty='40 mm',
        grubosc_koperty='10 mm',
        typ_paska_bransolety='Skórzany',
        kolor_paska_bransolety='Czarny',
        wodoszczelnosc='100 m',
        mechanizm='Automatyczny',
        gwarancja='2 lata',
        kolor_tarczy='Biały'
    )

    # Dodawanie zegarka do bazy danych
    session.add(sample_watch)
    session.commit()

    print("Przykładowy zegarek został dodany do bazy danych.")


if __name__ == '__main__':
    add_sample_watch()
