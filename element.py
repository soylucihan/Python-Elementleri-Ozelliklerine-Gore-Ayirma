#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Main():
    def __init__(self):
        self.Al = Dosya()
        self.Yaz = Dosya()
        self.liste = self.Al.DosyadanOku("semboller.txt")
        self.Yaz.DosyayaYaz("sonuc.txt", self.liste)

class Element():
    
    def __init__(self, z, sembol, ad, grup):
        self.z = z
        self.sembol = sembol
        self.ad = ad
        self.grup = grup

    def turYazdir(self):
        return "Element"

    def ozellikYazdir(self,flag,tur):
        if flag == False:
            self.yazi = "{0:>10} {1:>13} {2:>15} {3:>15} {4:>15}".format(tur, self.z, self.sembol, self.ad, self.grup)
            return self.yazi
        else:
            self.yazi = "{0:>7} {1:>18} {2:>15} {3:>15} {4:>15}".format(tur, self.z, self.sembol, self.ad, self.grup)
            return self.yazi

class AlkaliMetal(Element):
    def turYazdir(self):
        return "Alkali Metal"
class GecisMetali(Element):
    def turYazdir(self):
        return "Gecis Metali"
class Diger(Element):
    pass
class Dosya():
    def __init__(self):
        pass

    def DosyadanOku(self,yazi):
        self.yazi = yazi
        self.file = open(self.yazi,"r", encoding='utf-8-sig')
        self.liste2 = self.file.readlines()
        self.file.close()
        return self.liste2

    def DosyayaYaz(self, dosyaAdi, liste):
        self.dosyaAdi = dosyaAdi
        self.yazi=""
        self.liste = liste
        self.sayac = 0
        self.z = []
        self.sembol = []
        self.ad = []
        self.grup = []

        for satir in self.liste:
            self.z.append(satir.split()[0])
            self.sembol.append(satir.split()[1])
            self.ad.append(satir.split()[2])
            self.grup.append(satir.split()[3])
        self.sonuclar = open(self.dosyaAdi, "w", encoding='utf-8-sig')
        for i in self.grup:
            if i == "1A":
                self.element = AlkaliMetal(self.z[self.sayac], self.sembol[self.sayac], self.ad[self.sayac], self.grup[self.sayac])
                self.tur = self.element.turYazdir()
                self.yazi= self.element.ozellikYazdir(False, self.tur)
                if self.yazi is not None:
                    self.sonuclar.write(self.yazi)
                    self.sonuclar.write("\n")
            elif "B" in i:
                self.element = GecisMetali(self.z[self.sayac], self.sembol[self.sayac], self.ad[self.sayac]
                                                        , self.grup[self.sayac])
                self.tur = self.element.turYazdir()
                self.yazi= self.element.ozellikYazdir(False, self.tur)
                if self.yazi is not None:
                    self.sonuclar.write(self.yazi)
                    self.sonuclar.write("\n")
            else:
                self.element = Diger(self.z[self.sayac], self.sembol[self.sayac], self.ad[self.sayac], self.grup[self.sayac])
                self.tur = self.element.turYazdir()
                self.yazi= self.element.ozellikYazdir(True, self.tur)
                if self.yazi is not None:
                    self.sonuclar.write(self.yazi)
                    self.sonuclar.write("\n")
            self.sayac += 1
if __name__ == '__main__':
    run = Main()