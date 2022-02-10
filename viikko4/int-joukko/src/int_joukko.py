

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvastuskoko")  # heitin vaan jotain :D Xddd

        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono
        
    def lisaa(self, n):

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.ljono):
                self.ljono += [0] * self.kasvatuskoko
            return True

        return False

    def poista(self, poistettava):

        for indeksi in range(0, self.alkioiden_lkm):
            if poistettava == self.ljono[indeksi]:
                self.ljono = self.ljono[:indeksi] + self.ljono[indeksi +1:] + [0]
                self.alkioiden_lkm -= 1
                return True

        return False


    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(eka, toka):
        uusi_joukko = IntJoukko()

        for alkio in eka.to_int_list() + toka.to_int_list():
            uusi_joukko.lisaa(alkio)

        return uusi_joukko

    @staticmethod
    def leikkaus(eka, toka):
        uusi_joukko = IntJoukko()

        for alkio in eka.to_int_list() + toka.to_int_list():
            if  eka.kuuluu(alkio) and toka.kuuluu(alkio):
                uusi_joukko.lisaa(alkio)
        
        return uusi_joukko

    @staticmethod
    def erotus(eka, toka):
        uusi_joukko = IntJoukko()

        for alkio in eka.to_int_list():
            if not toka.kuuluu(alkio):
                uusi_joukko.lisaa(alkio)

        return uusi_joukko

    def __str__(self):
        int_list_as_str = [str(int) for int in self.to_int_list()] 

        return "{" + ", ".join(int_list_as_str) + "}"
