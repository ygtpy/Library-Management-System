from models.book import Kitap
from models.member import Uye
from utils.database import Veritabani
from datetime import datetime

class KutuphaneYonetim:
    
    def __init__(self):
        self.vt = Veritabani()
        
        
        
    def kitap_ekle(self):
        try:
            print("\n=== Kitap Ekleme ===")        
            baslik = input("Kitap Başlığı: ")
            yazar = input("Yazar: ")
            isbn = input("ISBN: ")
            sayfa_sayisi = input("Sayfa Sayısı: ")
            kategori = input("Kategori: ")
            
            kitap = Kitap(baslik, yazar, isbn, sayfa_sayisi, kategori)
            kitaplar = self.vt.kitaplari_getir()
            
            
            #isbn kontrolü
            if any(k['isbn'] == isbn for k in kitaplar):
                print("Bu ISBN numarası zaten mevcut!")
                return
            
            kitaplar.append(kitap.sozluk_olustur())
            self.vt_veri_kaydet(self.vt.kitaplar_dosyasi, kitaplar)
            print("Kitap Başarıyla Eklendi!")
            
        except ValueError:
            print("Geçersiz değer girişi!")
            
        except Exception as e:
            print(f"Bir hata oluştu {e}")
            
            
        
    def kitap_sil(self):
        
        try:
            isbn = input("Silinecek Kitabın ISBN Numarsı: ")
            kitaplar = self.vt.kitaplari_getir()
            
            for i,kitap in enumerate(kitaplar):
                if kitap['isbn'] == isbn:
                    if not kitap['musait']:
                        print("Bu kitap şu anda ödünç verilmiş durumda, silinemez!")
                        return
                    del kitaplar[i]
                    self.vt._veri_kaydet(self.vt.kitaplar_dosyasi, kitaplar)
                    print("Kitap başarıyla silindi!")
                    return
            
            print("Kitap bulunamadı!")
        
        except Exception as e:
            print(f"Bir hata oluştu {e}")
            
    
    def kitaplari_listele(self,kategori=None):
        kitaplar = self.vt.kitaplari_getir()
        if not kitaplar:
            print("Henüz kitap kayıtlı değil")
            return
        
        for kitap in kitaplar:
            if kategori and kitap['kategori'] != kategori:
                continue
            print("\n=== Kitap Detayları ===")
            print(f"Başlık: {kitap['baslik']}")
            print(f"Yazar: {kitap['yazar']}")
            print(f"ISBN: {kitap['isbn']}")
            print(f"Sayfa Sayısı: {kitap['sayfa_sayisi']}")
            print(f"Kategori: {kitap['kategori']}")
            print(f"Durum: {'Müsait' if kitap['müsait'] else 'Ödünç Verilmiş'}")
            
            
        
    def kitap_ara(self):
        arama = input("Kitap Adı veya ISBN: ")
        kitaplar = self.vt.kitaplari_getir()
        bulunan= False     
        
        for kitap in kitaplar:
            if arama.lower() in kitap['baslik'].lower() or arama == kitap['isbn']:
                print("\n === Bulunan Kitap ===")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    def menu_goster(self):
        while True:
            print("\n=== Kütüphane Yönetim Sistemi ===")
            print("1. Kitap İşlemleri")
            print("2. Üye İşlemleri")
            print("3. Ödünç İşlemleri")
            print("4. Çıkış")
            
            secim = input("Seçiminiz (1-4): ")
            
            
            if secim == "1":
                self.kitap_menu()
            elif secim == "2":
                self.uye_menu()
            elif secim == "3":
                self.odunc_menu()
            elif secim == "4":
                print("Programdan Çıkılıyor...")
                break
            else:
                print("Geçersiz Seçim")
                
            
    def kitap_menu(self):
        while True:
            print("\n=== Kitap İşlemleri ===")
            print("1. Kitap Ekle")
            print("2. Kitap Sil")
            print("3. Kitapları Listele")
            print("4. Kitap Ara")
            print("5. Ana Menüye Dön")
        
            secim = input("Seçiminiz (1-5): ")
            
    
    def uye_menu(self):
        while True:
            print("\n=== Üye İşlemleri ===")
            print("1. Üye Ekle")
            print("2. Üye Sil")
            print("3. Üyeleri Listele")
            print("4. Üye Ara")
            print("5. Ana Menüye Dön")
            
            secim = input("Seçiminiz (1-5): ") 
            
            
    def odunc_menu(self):
        
        while True:
            print("\n=== Ödünç İşlemleri ===")
            print("1. Kitap Ödünç Ver")
            print("2. Kitap İade Al")
            print("3. Ödünç Alınan Kitapları Listele")
            print("4. Ana Menüye Dön")
            
            secim = input("Seçiminiz (1-4): ")
            
            
            
if __name__ == "__main__":
    sistem = KutuphaneYonetim()
    sistem.menu_goster()
                
            
            
            
            
            
            
            
            
            
            
            
            