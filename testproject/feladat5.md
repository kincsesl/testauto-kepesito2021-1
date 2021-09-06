## 5 Feladat: Bingo

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Bingo app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Bingoapp tesztelését.

Az applikáció indulo bingo táblája minden frissítésnél véletlenszerűen változik!

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

A feladatod az alábbi tesztesetek lefejlesztése:
* Az applikáció helyesen megjelenik:
    * A bingo tábla 25 darab cellát tartalmaz
    * A számlista 75 számot tartalmaz
    
* Bingo számok ellenőzrzése:
    * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
    * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már
    * kihúzott számok közül kerültek-e ki
    
* Új játékot tudunk indítani
    * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    * új bingo szelvényt kapunk más számokkal.


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k5.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(