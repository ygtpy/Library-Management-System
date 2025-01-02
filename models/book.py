
from datetime import datetime

class Kitap:
    
    def __init__(self, baslik, yazar, isbn, sayfa_sayisi, kategori):
        self.baslik = baslik
        self.yazar = yazar
        self.isbn = isbn
        self.sayfa_sayisi = sayfa_sayisi
        self.kategori = kategori
        self.musait = True
        self.odunc_alan = None
        self.odunc_tarihi = None
        self.teslim_tarihi = None
        
        
    def sozluk_olustur(self):
        return {
            "baslik": self.baslik,
            "yazar": self.yazar,
            "isbn": self.isbn,
            "sayfa_sayisi": self.sayfa_sayisi,
            "kategori": self.kategori,
            "musait": self.musait,
            "odunc_alan": self.odunc_alan,
            "odunc_tarihi": self.odunc_tarihi,
            "teslim_tarihi": self.teslim_tarihi            
        }
    
    