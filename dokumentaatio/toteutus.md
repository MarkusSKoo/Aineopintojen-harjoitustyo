# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma toteuttaa 2048-bittisen RSA-salauksen, joka myös tuottaa mainitun pituisia salausavaimia. Käyttäjä voi antaa salattavaksi sen pituisen tekstin kuin avaimen pituus sallii.

Ohjelman toiminnallisuus on jaoteltu tiedostoittainseuraavasti:

prime_utils.py sisältää keskeiset funktiot alkulukujen tuottamiseen ja suurimman yhteisen tekijän löytämiseen kahdelle kokonaisluvulle.

keygen.py käyttää näitä funktioita alkulukujen tuottamiseen, avainparien tuottamiseen alkuluvuista ja lopuksi RSA-avainparien tuottamiseen, jonka paluuarvoina alkulukuja ei enää palauteta testikäyttöä lukuunottamatta. Ensimmäinen funktio tuottaa satunnaisen parittoman 1024 bittisen (tai suuremman) luvun. Seuraavaksi tarkistetaan onko luku jaollinen millään pienellä alkuluvulla. Tämä säästää huomattavasti aikaa mahdollisten alkulukujen suodattamisessa, sillä seuraavaksi suoritettava Miller-Rabin on jo raskaampi algoritmi. Miller-Rabinin testin läpäistyään meillä on todennäköinen oikeankokoinen alkuluku. Avainparin tuottava funktio tuottaa kaksi alkulukua p ja q, ja varmistaa, että ne ovat eri lukuja. Lopuksi tuotetaan varsinainen RSA-avain generate_rsa_keys() -funktiolla, jossa N = p * q. Julkinen avain muodostuu luvuista N ja e, jossa 1 < e < (p - 1) * (q - 1) ja suurin yhteinen tekijä gcd(e, (p - 1) * (q - 1)) == 1. Yksityinen avain muodostuu luvuista N ja d, jossa d toteuttaa (d * e) % ((p - 1) * (q - 1)) == 1. Funktio palauttaa siis tuplen julkinen avain (N, e), yksityinen avain (N, d).

rsa_crypt.py käsittelee viestien salaamisen ja purkamisen kutsumalla keygen.py:ssä olevaa generate_rsa_keys() -funktiota tuottaen salauksessa käytettävän avaimen. Funktio encrypt ottaa parametreina käyttäjänimen, salattavan viestin ja julkisen avaimen. Funktio palauttaa tuplena käyttäjänimen ja salatun viestin. Funktio decrypt ottaa parametreina käyttäjänimen, salatun viestin ja yksityisen avaimen ja palauttaa tuplena käyttäjänimen ja puretun viestin.

## Saavutetut aika- ja tilavaativuudet

- Miller-Rabin: Aikavaativuus O(k log^3 N) jossa k = kierrosten määrä ja N testattava luku. Tilavaatimus O(log N)
- Eukleideen algoritmi: Aikavaativuus O(log min(a, b)), tilavaativuus O(1)
- Laajennettu Eucleideen algoritmi: Aikavaativuus O(log min(a, b)), tilavaativuus O(1)
- Sieve of Eratosthenes: Aikavaativuus O(n log log n), tilavaatimus O(n)
- Encryption: Aikavaativuus O(log e), tilavaativuus O(1)
- Decryption: Aikavaativuus O(log d), Tilavaativuus O(1)

## Suorituskyky- ja O-analyysivertailu

Suorituskykytesteissä salausavaimen luonnille on asetettu aikarajaksi 3 sekuntia, mikä vastaa Eucleideen ja Miller-Rabinin vaativuutta. Viestin salaamisen ja purkamisen yhdistelmään eli ns. roundtrip aikavaatimukseksi on asetettu 1 sekunti. Viestin salaamiseen yksinään, kuten myös viestin purkamiseen yksinään on asetettu 0.2 sekunnin raja kummallekin, tämä toteutuu modulaarisen exponenttiin korottamisen ansiosta (pow-metodi). Lopuksi 100 viestin peräkkäiselle roundtrip-testille on asetettu 5 sekunnin raja, joka demonstroi algoritmien skaalautuvuutta odotetusti.

## Työn mahdolliset puutteet ja parannusehdotukset

Tällä hetkellä rajapinta käyttäjälle main.py tiedosto sisältää kaksi apufunktiota syötteiden validointia varten. Kyseisten funktioiden koodi ei ole kaikista esteettisintä, mutta ne toimivat odotetusti, tekevät muista funktioista siistimpiä ja ratkaisevat Pylintin antaman varoituksen too manby instances. En ole halunnut ohjelmoida näitä apufunktioita enää uudestaan, koska ne toimivat testattaessa odotetusti, mutta koodia pystyisi varmasti siistimään luettavampaan muotoon.

Tämän lisäksi ohjelma ei oikein tee mitään hyödyllistä käytäjänimellä, muuta kuin tulostaa sen näytölle muoden syötteiden yhteydessä. Tämä on toki siinä mielesä oleellista, että useita salauksia/purkuja peräkkäin suoritettaessa se helpottaa luettavuutta ja erittelyä. Käyttäjänimi olisi erittäin hyödyllinen datan organisointia varten tallennettaessa viestejä tietokantaan, mutta tällaista ominaisuutta ei tehtävänannossa erikseen vaadittu, enkä lopulta tätä toteuttanut. Tällainen voisi kuitenkin olla hyödyllinen, jos projektia haluaisi käyttää kurssin ulkopuolella osana laajempaa projektia.

Työ on dokumentoitu ja kommentoitu suomeksi. Kuitenkin virheviestien käsitteleminen tuntui luontevammalta englanniksi ja toisaalta käyttöliittymä on taas täysin suomeksi toteutettu. Tätä olisi voinut yhdenmukaistaa ja pitää kaiken ohjelman kommentoinnin ja virheviestien käsittelyn englanniksi. Kurssi on kuitenkin suomenkielinen ja työtä arvoivat muut opiskelijat ja kurssin henkilökunta, joten pitäydyin suomen kielessä, mutta varsinaisessa tuotantotyössä dokumentointi ja koodin kommentointi olisivat todennäköisimmin enlganniksi ja siten yhteneväisempi.

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






