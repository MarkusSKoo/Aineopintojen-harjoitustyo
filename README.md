# Aineopintojen-harjoitustyö: RSA-salaus

## Asennusohjeet:

Kopioi git-repository tietokoneellesi haluamaasi kansioon komentoriviltä komennolla:

```
git clone https://github.com/MarkusSKoo/Aineopintojen-harjoitustyo.git
```

Avaa asennettu kansio komennolla:

```
cd Aineopintojen-harjoitustyo/rsa_salaus
```

Tarkista, että käytössäsi on Python 3.12 tai uudempi komennolla:

```
python3 --version
```

Asenna Python tarvittaessa täältä:

```
https://www.python.org/downloads/
```

Asenna tarvittaessa Poetry. Linus/Mac:
```
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
```

Windows:
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Käynnistä terminaali uudelleen asennuksen jälkeen. Tarkista asennukset:
```
poetry --version
```

rsa_salaus-kansiossa asenna riippuvuudet ja aktivoi virtuaaliympäristö komennolla:
```
poetry install
```

## Ohjelman käynnistäminen:

Varmista, että olet kansiossa:
```
Aineopintojen-harjoitustyo/rsa_salaus
```

Seuraavaksi suorita komentoriviltä komento:
```
poetry run python src/main.py
```

Tämän jälkeen ohjelma antaa sinulle neljä vaihtoehtoa.

Komennolla 1 saat tuotettua RSA-avainparin, joka tulostuu komentoriville. Kopioi nämä talteen. Huomaa, että yksityistä avainta ei ole tarkoitus jakaa, vaan se tulee suojata huolellisesti. Voit jakaa julksien avaimen.

Komennolla 2 voit salata viestin. Syötä käyttäjänimesi ja kirjoita sitten haluamasi viesti. Huomaa, ettei viestin koko saa ylittää salausavaimen kokoa. Lopuksi anna vielä julkinen avain osissa. Komentoriville tulostuu salattu viesti. Kopioi viesti. Voit nyt lähettää salatun viestin yksityisen avaimen haltijalle. Käyttäjätunnus ja viesti ovat merkkijonoja (jotka voivat sisältää numeroita). Julkinen avain muodostuu kahdesta kokonaisluvusta.

Komennolla 3 voit purkaa salatun viestin yksityisellä avaimella. Anna käyttäjänimesi, salattu viesti ja yksityinen avain osissa. Näytölle ilmestyy alkuperäinen, purettu viesti. Käyttäjänimi on merkkijono (joka voi sisältää numeroita). Salattu viesti ja yksityinen avain ovat kokonaislukuja.

Komennolla 4 voit sulkea ohjelman.

## Ohjelman testaaminen

Testit voi suorittaa komennolla:
```
poetry run pytest
```

Kattavuusraportin saa suorittamalla ensin komennon:
```
poetry run coverage run --branch -m pytest
```
ja sitten komennon:
```
poetry run coverage report -m
```


















