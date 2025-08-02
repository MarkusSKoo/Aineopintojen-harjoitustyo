Tällä viikolla sain luotua loput tarvittavat funktiot RSA-avainparin luomiseen sekä viestien salaamiseen ja purkamiseen. Lisäksi olen saanut varsin kattavasti laadittua testejä ja päässyt jo testaamaan, että salattava ja purettava viesti vastaavat toisiaan. Tämä oli mielenrauhan kannalta varsin oleellista.

Testikattavuuden nostamiseksi mockaaminen osoittautui varsin haastavaksi, sillä en ole tehnyt sitä aiemmin. Erityisesti haasteeksi osoittautui Euclidean algoritmin mockaaminen, sillä päästäkseni generate_rsa_keys() -funktiossa jälimmäiseen while-silmukkaan, mutta saadakseni sitten while-silmukasta oikeita paluuarvoja, minun tuli luoda tähän apufunktio.

Toinen haaste oli löytää Miller-Rabinin testifunktioille verifioituja, suuria alkulukuja. Aiemmin käyttämäni stackoverflow:n keskustelufoorumilta kopioimani luvut eivät tietysti täytä oikeassa tuotannossa vaadittavia laatuvaatimuksia.

Vielä ratkaisematon haaste on mockata generate_rsa_keys() -funktion ensimmäiseen silmukkaan mielekkäitä arvoja, sillä kahden 1024 bittiä pitkän alkuluvun tulo saattaa jäädä 2047 bittiä pitkäksi, mutta ei aina. Nyt testit menevät toisinaan 100% läpi, eli silmukka toistaa vähintään yhden kierroksen, muttei aina.

Seuraavaksi keskityn testausmetodien monipuolistamiseen ja pääohjelman toiminnan kehittämiseen, jotta rajapinta käyttäjän kanssa saadaan kuntoon ja ohjelmalla pystytään oikeasti ajamaan syötteitä käyttäjän toimesta.

Käytin tällä viikolla projektin kehittämiseen 18 tuntia.
