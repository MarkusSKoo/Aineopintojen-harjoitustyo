# Testausdokumentti

## Testauksen tavoite

Harjoitustyössä käytettävien testien tavoite on varmistaa, että algoritmit toimivat odotetulla tavalla, jotta niitä voidaan käyttää luotettavasti viestien salaamiseen.

## Yksikkötestaus

Testattavat algoritmit: sieve_of_eratosthenes, miller_rabin, euclidean ja extended_euclidean.

Testaustapa: Pytest.

Kansiossa rsa_salaus testit voidaan toistaa komennolla:

```pytest```

Kattavuusraportit saadaan komennoilla:

```coverage run --branch -m pytest```
```coverage report -m```

Sijainti: tests/prime_utils_test.py

## Testisyötteet ja kattavuus

### sieve_of_eratosthenes

Erathosteneen seula antaa listan alkuluvuista n asti, kun n on 2 tai suurempi. Ensimmäinen testi kokeilee antaako algoritmi oikean tuloksen, kun n on hyvin pieni ja tiedetään varmuudella haluttu paluuarvo. Kolme seuraavaa testiä testaa, että funktio nostaa ValueError, kun syöte on pienempi kuin 2, mutta positiivinen, syöte on 0 ja syöte on negatiivinen. Testisyötteiden 2 ja 3 tarkoitus on tarkistaa palauttaako funktio oikeat alkuluvut pienimmillä mahdollisilla syötteillä, joita testi hyväksyy. Testisyöte 200 tarkoitus on tarkistaa tuottaako funktio listan alkuluvuista oikein suuremmalla n arvolla. Lista alkuluvuista on tarkistettu sivulta:

[Wikipedia - List of prime numbers](https://en.wikipedia.org/wiki/List_of_prime_numbers)

### miller_rabin

Miller-Rabin -algoritmi palauttaa boolean-arvon False jos luku n > 1 ei varmuudella ole alkuluku tai boolean-arvon True, jos luku on todennäköisesti alkuluku. Varmuutta lisää eksponentiaalisesti testikierrosten k kasvattaminen, ja testeissä onkin valittu k arvoksi 40 algoritmin oiken toiminnan varmistamiseksi, paitsi testitapauksissa k = 0 ja k = -1, jolloin nostetaan ValueError, sillä testin suorittamiseksi tarvitaan vähintään yksi kierros.

Testisyöte n = 1, k = 40 tarkoitus on testata, että algoritmi nostaa oikeanlaisen virheilmoituksen, kun n on liian pieni. Testisyöte n = 2, k = 40 tarkoitus on testata, että palautetaan True, kun luku on 2, eikä vahingossa palauteta False luvun parillisuudesta johtuen. Tätä suuremmat parilliset n arvot hylätään automaattisesti, sillä ne eivät varmuudella ole alkulukuja. Parillisia lukuja testataan testillä test_miller_rabin_even_n(), joka kerää listan parillisia lukuja ja testaa algoritmia kaikilla listan luvuilla.

test_miller_rabin_5000() testaa varmistaako miller_rabin luvut alkuluvuiksi aiemmin mainitun sieve_of_eratosthenes() -funktion tuottaman listan perusteella, kun tuotetaan kaikki alkuluvut 5000 asti. Tällä saadaan varmuutta molempien algoritmien oikeanlaiseen toimintaan. On kuitenkin ainakin teoriassa mahdollista, että molemmat funktiot toimisivat väärin, ja paluuarvoina olisi väärä True, siksi testit test_miller_rabin_middle() ja test_miller_rabin_large() testaavat funktiota kovakoodatuilla alkuluvuilla, jotka on kopioitu aiemmin mainitulta Wikipedia-sivulta sekä täältä:

[List of 50000 Primes - The University of Arizona](https://www2.cs.arizona.edu/icon/oddsends/primes.htm)

Testi test_miller_rabin_not_primes() testaa, palauttaako funktio ei-alkuluvuista False, kun tuotetaan lista luvuista, joista poistetaan alkuluvut sieve_of_eratosthenes avulla. Edellä mainitusta syystä test_miller_rabin_big_not_primes() testaa listaa ei-alkuluvuista, joista on kovakoodaamalla poistettu raja-arvojen sisältä kaikki tiedetyt alkuluvut.

Lopuksi test_miller_rabin_2048_primes() testaa algoritmin toimivuutta kahdella erittäin suurella alkuluvulla, joiden koko ylittää reilusti salauksessa tarvittavien alkulukujen koon. Tällä haetaan lisävarmuutta siihen, että algoritmia voidaan käyttää suunniteltua ohjelmaa varten. Luvut on kopioitu täältä:

[Stackoverflow](https://stackoverflow.com/questions/22079315/i-need-2048bit-primes-in-order-to-test-the-upper-limits-of-my-rsa-program)

### euclidean

Algoritmi etsii kahdelle luvulle suurimman yhteisen tekijän. Neljä ensimmäistä testiä testaa palauttaako algoritmi oikean vastauksen yksinkertaisilla, ensin pienillä ja sitten suurilla luvuilla, kun haluttu lopputulos on varmuudella pääteltävissä testisyötteistä.

Testi test_euclidean_large_coprime() testaa For-silmukassa 100 kertaa sieve_of_eratosthenes:illa tuotetuilla, satunnaisesti valituilla alkuluvuilla palauttaako algoritmi tuloksen 1 tai molempien syötteenä olevien lukujen ollessa samat, ko. luvun. For-silmukkaan on kovakoodattu yhdelle kierrokselle valinnaksi sama luku testikattavuutta varten, sillä random.choice ei käytännössä koskaan valitsisi samaa lukua, jolloin ensimmäisen if-haaran toimivuutta ei koskaan testattaisi.

Euclidean toimintaa testataan vielä erikseen samoilla syötteillä, sekä yksinkertaisilla rajatapauksilla, kuten toisen arvon ollessa 0 (tulisi palauttaa toisen luvun itseisarvo), molempien arvojen ollessa 0 (nostaa ValueError) ja negativisilla arvoilla.

### extended_euclidean

Algoritmi laskee kokonaisluvuille a ja b Bezoutin kertoimet x ja y siten, että a * x + b * y = gcd(a, b). Nyt x ja y voivat saada useita eri arvoja, jotka tyydyttäisivät tämän yhtälön, joten testaamisessa on käytetty siksi suurinta yhteistä tekijää euclidean algoritmista. Algoritmia on testattu useilla pienillä luvuilla mukaan lukien alkulukuja ja coprime-lukuja. Lisäksi on testattu algoritmien toimintaa toisen tai molempien arvon ollessa nolla tai negatiivinen, samoilla arvoilla sekä suurilla arvoilla.

## Kattavuusraportti

```
Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
src/rsa_salaus/__init__.py          0      0      0      0   100%
src/rsa_salaus/prime_utils.py      71      0     46      0   100%
tests/__init__.py                   0      0      0      0   100%
tests/prime_utils_test.py         141      0     32      0   100%
---------------------------------------------------------------------------
TOTAL                             212      0     78      0   100%
```

