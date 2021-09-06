## 3 Feladat: Alfanumerikus mező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Alfanumerikus mezőapp-ot az 
[https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Alfanumerikus mező app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

A cél a mező validáció tesztelése:

* Helyes kitöltés esete:
    * title: abcd1234
    * Nincs validációs hibazüzenet

* Illegális karakterek esete:
    * title: teszt233@
    * Only a-z and 0-9 characters allewed.

* Tul rövid bemenet esete:
    * title: abcd
    * Title should be at least 8 characters; you entered 4.

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k3.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(