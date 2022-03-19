class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

class Operaatio:
    def __init__(self, sovellus, arvo):
        self.arvo = arvo
        self.sovellus = sovellus

    def suorita(self):
        return 0

class Summa(Operaatio):
    def __init__(self, sovellus, arvo):
        super().__init__(sovellus, arvo)

    def suorita(self):
        try:
            return self.sovellus.plus(int(self.arvo()))
        except ValueError:
            pass

class Erotus(Operaatio):
    def __init__(self, sovellus, arvo):
        super().__init__(sovellus, arvo)

    def suorita(self):
        try:
            return self.sovellus.miinus(int(self.arvo()))
        except ValueError:
            pass

class Nollaus(Operaatio):
    def __init__(self, sovellus, arvo):
        super().__init__(sovellus, arvo)

    def suorita(self):
        return self.sovellus.nollaa()

class Kumoa(Operaatio):
    def __init__(self, sovellus, arvo):
        super().__init__(sovellus, arvo)

    def suorita(self):
        pass