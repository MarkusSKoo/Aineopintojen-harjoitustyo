# Määrittelydokumentti

## Harjoitustyön aihe

- Opinto-ohjelma: Tietojenkäsittelytiede, kandidaatin tutkinto
- Ohjelmointikieli: ohjelma toteutetaan Pythonilla ja dokumentoidaan suomeksi. Pystyn vertaisarvioimaan Pythonilla ohjelmoituja, suomeksi tai englanniksi dokumentoituja sovelluksia.
- Ohjelma toteuttaa RSA-salauksen, jossa algoritmi salaa ja purkaa tekstin käyttäen julkista ja yksityistä avainta. Lisäksi tavoitteena on tuottaa avaimia, joiden pituus on vähintään 2048 bittiä.

## Algoritmit

Ohjelman toteutus vaatii useita algoritmejä, joista alkuselvitysten perusteella tulen käsittelemään ainakin seuraavia:

- Miller-Rapin-testi sen määrittelemiseksi, onko luku todennäköisesti alkuluku: O(k n^3)
- Eukleideen algoritmi kahden luvun suurimman yhteisen tekijän löytämiseen: O(log b)
- Laajennettu Eukleideen algoritmi
- Sieve of Eratosthenes, algoritmilla määritellän alkuluvut valittuun numeroon asti: O(n log log n)

## Ratkaistava ongelma

Ohjelman haasteena on alkulukujen generointi, joka ymmärtääkseni on varsin monimutkainen toimenpide. Näitä tarvitaan salausparien muodostamiseen viestien salaamista varten.

## Syötteet

Syötteinä käytetään käyttäjänimeä ja salattavaa/purettavaa viestiä.

Salattava viesti salataan julkista avainta käyttäen ja puretaan yksityisellä avaimella.

## Työssä käytettävät lähteet

- [RSA - Wikipedia](https://fi.wikipedia.org/wiki/RSA)
- [Miller–Rabin primality test - Wikipedia](https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)
- [Sieve of Eratosthenes - Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Extended Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)


