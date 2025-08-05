# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma toteuttaa 2048-bittisen RSA-salauksen, joka myös tuottaa mainitun pituisia salausavaimia. Käyttäjä voi antaa salattavaksi sen pituisen tekstin kuin avaimen pituus sallii.

Ohjelman toiminnallisuus on jaoteltu tiedostoittain. prime_utils.py sisältää keskeiset funktiot alkulukujen tuottamiseen ja suurimman yhteisen tekijän löytämiseen kahdelle kokonaisluvulle. keygen.py käyttää näitä funktioita alkulukujen tuottamiseen, avainparien tuottamiseen alkuluvuista ja lopuksi RSA-avainparien tuottamiseen, jonka aikana alkulukuja ei enää tallenneta testikäyttöä lukuunottamatta. rsa_crypt.py käsittelee viestien salaamisen ja purkamisen kutsumalla keygen.py:ssä olevaa generate_rsa_keys() -funktiota.

## Saavutetut aika- ja tilavaativuudet

Algoritmien aikavaativuudet ovat:

- Miller-Rapid: O(k n^3)
- Eukleideen algoritmi: O(log b)
- Sieve of Eratosthenes: O(n log log n)

En ole vielä tehnyt tarkkoja analyyseja, mutta uskoisin päässeeni aikavaatimuksiin kiitettävästi. Päivitän tämän myöhemmin.

## Suorituskyky- ja O-analyysivertailu

Toistaiseksi ohjelmaan on luotu vain yksi suorituskykytesti. generate_rsa_keys() -funktio suoriutuu tehtävästä alle 4 sekunnissa. Lisää suorituskykytestejä tulossa myöhemmin.

## Työn mahdolliset puutteet ja parannusehdotukset

Tällä hetkellä ohjelmalla ei ole vielä rajapintaa käyttäjän kanssa lainkaan, mutta kaikki vaadittavat funktiot ja algoritmit viestien salaamista ja purkamista varten ovat valmiina.

Yksikkötestit ovat mielestäni jo varsin kattavia, mutta suorituskykytestejä ja muita testaustapoja (kuten päästä päähän) on vielä tarkoitus luoda lisää.

## Laajojen kielimallien käyttö

Olen käyttänyt työssäni apuna OpenAI GPT-4-mallia työn perustana olevien algoritmien toiminnan ymmärtämiseen. Olen pyytänyt ChatGPT:tä selittämään asioita ja samalla antanut eksplisiittiset ohjeet, etten halua mitään valmista ratkaisua tai koodia.

## Lähteet

### Algoritmit:

- [RSA - Wikipedia](https://fi.wikipedia.org/wiki/RSA)
- [Miller–Rabin primality test - Wikipedia](https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)
- [Sieve of Eratosthenes - Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Extended Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)

### Alkuluvut:

- [Wikipedia - List of prime numbers](https://en.wikipedia.org/wiki/List_of_prime_numbers)
- [List of 50000 Primes - The University of Arizona](https://www2.cs.arizona.edu/icon/oddsends/primes.htm)
- [Carmichael number - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_number)
- [rfc-editor](https://www.rfc-editor.org/rfc/rfc3526#page-3)

