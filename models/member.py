

class Uye:
    def __init__(self, ad_soyad, uye_no):
        self.ad_soyad = ad_soyad
        self.uye_no = uye_no
        self.odunc_alinan_kitaplar = []
        self.ceza = 0
        
        
    def sozluk_olustur(self):
        return {
            "ad_soyad": self.ad_soyad,
            "uye_no": self.uye_no,
            "odunc_alinan_kitaplar": self.odunc_alinan_kitaplar,
            "ceza": self.ceza
        }
    
    