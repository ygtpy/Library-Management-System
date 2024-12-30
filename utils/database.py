import json
import os

class Veritabani:
    
    def __init__(self):
        self.kitaplar_dosyasi = "data/books.json"
        self.uyeler_dosyasi = "data/members.json"
        self._dosyalari_olustur()
        
    
    def _dosyalari_olustur(self):
        os.makedirs("data",exist_ok=True)
        
        if not os.path.exists(self.kitaplar_dosyasi):
            self._veri_kaydet(self.kitaplar_dosyasi, [])
        if not os.path.exists(self.uyeler_dosyasi):
            self._veri_kaydet(self.uyeler_dosyasi, [])
            
   
    def _veri_kaydet(self,dosya_yolu, veri):
        with open(dosya_yolu, 'w', encoding='utf-8')as f:
            json.dump(veri, f, indent=4, ensure_ascii=False)
        
   
    def _veri_oku(self, dosya_yolu):
        with open(dosya_yolu ,'r', encoding= 'utf-8')as f:
            return json.load(f)
        
    
    def kitaplari_getir(self):
        return self._veri_oku(self.kitaplar_dosyasi)
    
    
    def uyeler_getir(self):
        return self._veri_oku(self.uyeler_dosyasi)
        