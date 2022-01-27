from kirjanpito import Kirjanpito
from kirjanpito import kirjanpito as defaulf_kirjanpito


class Pankki:

    def __init__(self, kirjanpito=defaulf_kirjanpito):
        self._kirjanpito = kirjanpito

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True
pankki = Pankki()