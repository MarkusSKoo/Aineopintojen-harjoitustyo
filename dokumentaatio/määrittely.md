# Määrittelydokumentti

## Harjoitustyön aihe
Opinto-ohjelma: Tietojenkäsittelytiede, kandidaatin tutkinto
Ohjelmointikieli: ohjelma toteutetaan Pythonilla ja dokumentoidaan suomeksi. Pystyn vertaisarvioimaan Pythonilla ohjelmoituja, suomeksi tai englanniksi dokumentoituja sovelluksia.
Ohjelma toteuttaa RSA-salauksen, jossa algoritmi salaa ja purkaa tekstin käyttäen julkista ja yksityistä avainta. Lisäksi tavoitteena on tuottaa avaimia, joiden pituus on vähintään 2048 bittiä.

## Algoritmit

Ohjelman toteutus vaatii useita algoritmejä, joista alkuselvitysten perusteella tulen käsittelemään ainakin seuraavia:
-Miller-Rapid-testi sen määrittelemiseksi, onko luku todennäköisesti alkuluku
-Eukleideen algoritmi
-Laajennettu Eukleideen algoritmi
-Sieve of Eratosthenes

## Ratkaistava ongelma

Ohjelman haasteena on alkulukujen generointi, joka ymmärtääkseni on varsin monimutkainen toimenpide. Näitä tarvitaan salausparien muodostamiseen viestien salaamista varten.

## Syötteet

Syötteinä käytetään käyttäjänimeä ja salattavaa/purettavaa viestiä.
Salattava viesti salataan julkista avainta käyttäen ja puretaan yksityisellä avaimella.

