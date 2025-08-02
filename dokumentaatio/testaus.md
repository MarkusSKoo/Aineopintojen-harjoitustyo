# Testausdokumentti

## Testauksen tavoite

Harjoitustyössä käytettävien testien tavoite on varmistaa, että algoritmit toimivat odotetulla tavalla, jotta niitä voidaan käyttää luotettavasti viestien salaamiseen.

## Yksikkötestaus

Testattavat tiedostot: prime_utils.py, keygen.py

Testaustapa: Pytest.

Kansiossa rsa_salaus testit voidaan toistaa komennolla:

```pytest```

Kattavuusraportit saadaan komennoilla:

```coverage run --branch -m pytest src tests; coverage report -m```

## Testisyötteet

### sieve_of_eratosthenes

Erathosteneen seula antaa listan alkuluvuista n asti, kun n on 2 tai suurempi. Ensimmäinen testi kokeilee antaako algoritmi oikean tuloksen, kun n on hyvin pieni ja tiedetään varmuudella haluttu paluuarvo. Kolme seuraavaa testiä testaa, että funktio nostaa ValueError, kun syöte on pienempi kuin 2, mutta positiivinen, syöte on 0 ja syöte on negatiivinen. Testisyötteiden 2 ja 3 tarkoitus on tarkistaa palauttaako funktio oikeat alkuluvut pienimmillä mahdollisilla syötteillä, joita testi hyväksyy. Testisyöte 200 tarkoitus on tarkistaa tuottaako funktio listan alkuluvuista oikein suuremmalla n arvolla. Lista alkuluvuista on tarkistettu sivulta:

[Wikipedia - List of prime numbers](https://en.wikipedia.org/wiki/List_of_prime_numbers)

### miller_rabin

Miller-Rabin -algoritmi palauttaa boolean-arvon False jos luku n > 1 ei varmuudella ole alkuluku tai boolean-arvon True, jos luku on todennäköisesti alkuluku. Varmuutta lisää eksponentiaalisesti testikierrosten k kasvattaminen, ja testeissä onkin valittu k arvoksi 40 algoritmin oiken toiminnan varmistamiseksi, paitsi testitapauksissa k = 0 ja k = -1, jolloin nostetaan ValueError, sillä testin suorittamiseksi tarvitaan vähintään yksi kierros.

Testisyöte n = 1, k = 40 tarkoitus on testata, että algoritmi nostaa oikeanlaisen virheilmoituksen, kun n on liian pieni. Testisyöte n = 2, k = 40 tarkoitus on testata, että palautetaan True, kun luku on 2, eikä vahingossa palauteta False luvun parillisuudesta johtuen. Tätä suuremmat parilliset n arvot hylätään automaattisesti, sillä ne eivät varmuudella ole alkulukuja. Parillisia lukuja testataan testillä test_miller_rabin_even_n(), joka kerää listan parillisia lukuja ja testaa algoritmia kaikilla listan luvuilla.

test_miller_rabin_5000() testaa varmistaako miller_rabin luvut alkuluvuiksi aiemmin mainitun sieve_of_eratosthenes() -funktion tuottaman listan perusteella, kun tuotetaan kaikki alkuluvut 5000 asti. Tällä saadaan varmuutta molempien algoritmien oikeanlaiseen toimintaan. On kuitenkin ainakin teoriassa mahdollista, että molemmat funktiot toimisivat väärin, ja paluuarvoina olisi väärä True, siksi testit test_miller_rabin_middle() ja test_miller_rabin_large() testaavat funktiota kovakoodatuilla alkuluvuilla, jotka on kopioitu aiemmin mainitulta Wikipedia-sivulta sekä täältä:

[List of 50000 Primes - The University of Arizona](https://www2.cs.arizona.edu/icon/oddsends/primes.htm)

Testi test_miller_rabin_not_primes() testaa, palauttaako funktio ei-alkuluvuista False, kun tuotetaan lista luvuista, joista poistetaan alkuluvut sieve_of_eratosthenes avulla. Edellä mainitusta syystä test_miller_rabin_big_not_primes() testaa listaa ei-alkuluvuista, joista on kovakoodaamalla poistettu raja-arvojen sisältä kaikki tiedetyt alkuluvut.

Carmichaelsin luvut ovat lukuja, jotka vaikuttavat alkuluvuilta ja tietyissä testeissä käyttäytyvät, kuten alkuluvut, mutta eivät ole alkulukuja. Testi test_miller_rabin_carmichael() testaa algoritmin toimintaa 7 ensimmäisellä carmichaelin luvulla, lähde:

[Carmichael number - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_number)

Lopuksi test_miller_rabin_2048_primes() testaa algoritmin toimivuutta muutamalla erittäin suurella verifioidulla alkuluvulla, joiden koko ylittää reilusti salauksessa tarvittavien alkulukujen koon. Tällä haetaan lisävarmuutta siihen, että algoritmia voidaan käyttää suunniteltua ohjelmaa varten. Samojen lukujen tuloja testataan myös, jotta voidaan varmistaa algoritmin hylkäävän suuret komposiittiluvut. Luvut on kopioitu täältä:

[rfc-editor](https://www.rfc-editor.org/rfc/rfc3526#page-3)

### euclidean

Algoritmi etsii kahdelle luvulle suurimman yhteisen tekijän. Neljä ensimmäistä testiä testaa palauttaako algoritmi oikean vastauksen yksinkertaisilla, ensin pienillä ja sitten suurilla luvuilla, kun haluttu lopputulos on varmuudella pääteltävissä testisyötteistä.

Testi test_euclidean_large_coprime() testaa For-silmukassa 100 kertaa sieve_of_eratosthenes:illa tuotetuilla, satunnaisesti valituilla alkuluvuilla palauttaako algoritmi tuloksen 1 tai molempien syötteenä olevien lukujen ollessa samat, ko. luvun. For-silmukkaan on kovakoodattu yhdelle kierrokselle valinnaksi sama luku testikattavuutta varten, sillä random.choice ei käytännössä koskaan valitsisi samaa lukua, jolloin ensimmäisen if-haaran toimivuutta ei koskaan testattaisi.

Euclidean toimintaa testataan vielä erikseen samoilla syötteillä, sekä yksinkertaisilla rajatapauksilla, kuten toisen arvon ollessa 0 (tulisi palauttaa toisen luvun itseisarvo), molempien arvojen ollessa 0 (nostaa ValueError) ja negativisilla arvoilla.

### extended_euclidean

Algoritmi laskee kokonaisluvuille a ja b Bezoutin kertoimet x ja y siten, että a * x + b * y = gcd(a, b). Nyt x ja y voivat saada useita eri arvoja, jotka tyydyttäisivät tämän yhtälön, joten testaamisessa on käytetty siksi suurinta yhteistä tekijää euclidean algoritmista. Algoritmia on testattu useilla pienillä luvuilla mukaan lukien alkulukuja ja coprime-lukuja. Lisäksi on testattu algoritmien toimintaa toisen tai molempien arvon ollessa nolla tai negatiivinen, samoilla arvoilla sekä suurilla arvoilla.

## Yksikkötestaus: keygen

### generate_1024bit_number

Tämän funktion toimintaa testataan tuottamalla 1024 bittiä pitkä numero, jonka pituus testataan bit_length() -metodilla. Sen jälkeen tarkistetaan onko luku parillinen. Sitten generoidaan kaksi erillistä lukua ja vertaillaan, etteivät ne ole samat. Näillä testeillä varmistetaan, että funktio tuottaa oikeanpituisia, parittomia ja satunnaisia lukuja.

### check_primality_sieve

Alkuseulonnan tarkoitus on tehdä alkulukujen löytämisestä nopeampaa. Useimmat luvut eivät ole alkulukuja ja suurin osa saadaan kiinni seulomalla luvun jaollisuus pienillä alkuluvuilla. Funktion toimintaa testataan suurilla alkuluvuilla, jotta varmistutaan, että näitä ei hylätä aiheettomasti. Seuraavaksi testataan muutamia alkulukujen kertomia, jotta seula ei päästä näitä läpi. Lopuksi tarkastellaan vielä rajatapaukset, jotta ValueError nousee odotetusti.

### generate_prime

Funktio tuottaa 1024 bittiä pitkiä alkulukuja. Sen toimintaa testataan tuottamalla luku, jonka pituus tarkastetaan .bit_length() -metodilla. Tämän jälkeen luku annetaan miller_rabinille tarkasteltavaksi ja vahvistettavaksi. miller_rabinin toimintaa on testattu aiemmin, joten sitä ei testata tässä kohtaa uudestaan.

### generate_keypair

Funktio tuottaa avainlukuparin, joista kummatkin ovat 1024 bittiä pitkiä. Lukujen tulee olla eri lukuja, tämä tarkistetaan vertailuoperaattorilla. Generoinnin nopeutta tarkistetaan time.time() -metodilla, tässä hyväksyttäväksi aikarajaksi on asetettu 4 sekuntia. Molempien lukujen koko tarkastetaan .bit_length() -metodilla, jonka jälkeen luvut annetaan miller_rabinin tarkastettavaksi. Koska generate_keypair() -funktio ei käytännössä koskaan tuota kahta samaa lukua avainparille, testikattavuudesta jää while True-silmukasta ajamatta uusintakierros. Tätä varten on mockattu test_generate_keypair_mocked, jonka tarkoitus on testata while-silmukan oikeanlaista toimintaa.

### class TestGenerateRsaKeys

Tämä luokka testaa generate_rsa_keys() -funktion toimintaa. Huomaa, että funktion debug-tila on oletuksena False, koska rsa-avainparin muodostuksessa käytettävät alkuluvut p ja q tulee hävittää turvallisuussyistä. Debug-tilan ollessa päällä nämä palautetaan funktion returns-arvoissa vain testaamiskäyttöä varten. Funktiota tulee tällöin kutsua generate_rsa_keys(debug=True), eikä käyttäjälle anneta mahdollisuutta suorittaa tällaista kutsua tai edes tietoa tällaisesta mahdollisuudesta.

Testi test_rsa_keypair_return_format() varmistaa, että funktio palauttaa debug-tilassa oikean määrän oikeanlaisia arvoja. Testi test_rsa_keypair_math() varmistaa, että funktion palauttamat arvot ovat matemaattisesti oikein. n tulee olla sama sekä julkisessa, että yksityisessä avaimessa. n tulee olla p:n ja q:n tulo. p ja q tulee olla eri arvot, kummankin koon tulee olla 1024 bittiä ja niiden tulee olla alkulukuja (varmistetaan Miller-Rabinilla). e:n ja phi_n (eli (p - 1) * (q - 1)) suurin yhteinen tekijä tulee olla 1. d tulee olla väliltä [1, phi_n - 1]

Testi test_keypair_return_format_mocked() varmistaa, että funktio palauttaa oikean määrän oikeanlaisia arvoja, kun debug-tila ei ole päällä, eli kuten se tuotantokäytössä olisi. Näistä arvoista puuttuu p ja q, eikä niistä siten voida päätellä funktion matemaattisen toiminnan oikeellisuutta. Nämä on tarkoituskin jättää pois, sillä p:n ja q:n arvoilla salaus pystyttäisiin murtamaan. Tässä testissä keskitytään tarkistamaan paluuarvojen oikeellisuus tuotantokäytössä. Sekä yksityisen, että julkisen avaimen sisältämä n tulee olla sama, pituudeltaan 2048 bittiä. Lisäksi tämän testin mockauksen tarkoituksena on tarkistaa funktion eri haarojen toiminta, sillä for-luupissa kutsuttu euclidean palauttaa lähes varmasti 1 ensimmäisellä alkiolla 11939 ja katkaisee silmukan suorittamisen. Näin silmukka ei koskaan etene seuraavalle kierrokselle, eikä alla olevaan else-haaraan. Else-haaran sisältämä while-silmukka on tarkoitus toimia fallback-metodina for-silmukalle.

## Kattavuusraportti

```
Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
src/rsa_salaus/__init__.py          0      0      0      0   100%
src/rsa_salaus/keygen.py           47      0     20      0   100%
src/rsa_salaus/prime_utils.py      71      0     46      0   100%
tests/__init__.py                   0      0      0      0   100%
tests/keygen_test.py              102      0      6      0   100%
tests/prime_utils_test.py         155      0     38      0   100%
---------------------------------------------------------------------------
TOTAL                             375      0    110      0   100%
(rsa-salaus-py3.12) markuskauhanen@Markus-MacBook-Pro rsa_salaus % 
```

