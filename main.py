from models.book import Kitap
from models.member import Uye
from utils.database import Veritabani
from datetime import datetime, timedelta

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
            self.vt._veri_kaydet(self.vt.kitaplar_dosyasi, kitaplar)
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
            print(f"Durum: {'Müsait' if kitap['musait'] else 'Ödünç Verilmiş'}")
            
            
        
    def kitap_ara(self):
        arama = input("Kitap Adı veya ISBN: ")
        kitaplar = self.vt.kitaplari_getir()
        bulunan= False     
        
        for kitap in kitaplar:
            if arama.lower() in kitap['baslik'].lower() or arama == kitap['isbn']:
                print("\n === Bulunan Kitap Bilgileri ===")
                print(f"Başlık: {kitap['baslik']}")
                print(f"Yazar: {kitap['yazar']}")
                print(f"ISBN: {kitap['isbn']}")
                print(f"Durum: {'Müsait' if kitap['musait'] else 'Ödünç Verilmiş'}")
                bulunan= True
            
            if not bulunan:
                print("Kitap Bulunamadı")
                
                
    def uye_ara(self):
        arama = input("Üye No: ")
        uyeler = self.vt.uyeler_getir()
        bulunan = False
        
        for uye in uyeler:
            if arama == uye['uye_no']:
                print("\n === Bulunan Üye Bilgileri ===")
                print(f"Adı ve Soyadı: {uye['ad_soyad']}")
                print(f"Üye Numarası: {uye['uye_no']}")
                print(f"Ödünç Alınan Kitaplar: {uye['odunc_alinan_kitaplar']}")
                print(f"Ceza Durumu: {uye['ceza']} TL")
                bulunan = True
        if not bulunan:
            print("Üye Bulunamadı")
            
    def uye_ekle(self):
        try:
            print("\n=== Üye Ekleme ===")
            ad_soyad = input("Ad Soyad: ")
            uyeler = self.vt.uyeler_getir()
            
                
            # Otomatik üye numarası oluşturma
            if not uyeler:
                uye_no = "M1"
            else:
                son_uye_no = max(int(uye['uye_no'][1:]) for uye in uyeler)
                uye_no = f"M{son_uye_no + 1}"
                
            
            uye = Uye(ad_soyad, uye_no)
            uyeler.append(uye.sozluk_olustur())
            self.vt._veri_kaydet(self.vt.uyeler_dosyasi, uyeler)
            print(f"Üye başarıyla eklendi! Üye Numarası: {uye_no}")
            
        except Exception as e:
            print(f"Bir hata oluştu {e}")
            
        
    def uye_sil(self):
        
        try:
            uye_no = input("Silinecek Üyenin Numarası: ")
            uyeler = self.vt.uyeler_getir()
            
            for i, uye in enumerate(uyeler):
                if uye['uye_no'] == uye_no:
                    if uye['odunc_alinan_kitaplar']:
                        print("Üyenin iade etmediği kitaplar var, silinemez!")
                        return
                    del uyeler[i]
                    self.vt._veri_kaydet(self.vt.uyeler_dosyasi, uyeler)
                    print("Üye başarıyla silindi! ")
                    return
            
            print("Üye bulunamadı!")
            
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            
            
    def uyeleri_listele(self):
        uyeler = self.vt.uyeler_getir()
        if not uyeler:
            print("Henüz kayıtlı üye bulunmamaktadır.")
            return
        
        if not isinstance(uyeler, list):
            print("Üye bilgileri doğru bir şekilde alınamadı. Lütfen kontrol edin.")
            return
                    
        for uye in uyeler:
            print("\n==== Üye Detayları ====")
            print(f"Ad Soyad: {uye['ad_soyad']}")
            print(f"Üye No: {uye['uye_no']}")
            print(f"Ödünç Alınan Kitap Sayısı: {len(uye['odunc_alinan_kitaplar'])}")
            print(f"Ceza Durumu: {uye['ceza']} TL")
            
            
    def odeme_islemi(self):
        try:
            uye_no = input("Ödeme yapacak üyenin numarasını giriniz: ")
            uyeler = self.vt.uyeler_getir()
            uye_bulundu = False
            
            for uye in uyeler:
                if uye['uye_no'] == uye_no:
                    uye_bulundu = True
                    if uye['ceza'] > 0:
                        print(f"{uye['ad_soyad']} adlı üyenin {uye['ceza']} TL borcu bulunmaktadır.")
                        while True:
                            try:
                                odenecek_tutar = int(input("Ödemek istediğiniz tutarı giriniz: "))
                                if odenecek_tutar <= 0:
                                    print("Lütfen geçerli bir tutar giriniz!")
                                    continue
                                if odenecek_tutar > uye['ceza']:
                                    print("Ödeme tutarı borçtan büyük olamaz!")
                                    continue
                                # Ödeme 
                                uye['ceza'] -= odenecek_tutar
                                self.vt._veri_kaydet(self.vt.uyeler_dosyasi, uyeler)
                                print(f"Ödeme başarılı! Kalan borç: {uye['ceza']} TL")
                                break
                            except ValueError:
                                print("Lütfen sayısal bir değer giriniz!")
                    else:
                        print(f"{uye['ad_soyad']} adlı üyenin borcu bulunmamaktadır.")
                    break
            
            if not uye_bulundu:
                print("Üye bulunamadı!")
                
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
                
    def kitap_odunc_ver(self):
        
        try:
            isbn = input("Ödünç Verilecek Kitabın ISBN Numarası: ")
            uye_no = input("Üye Numarası: ")
            
            kitaplar = self.vt.kitaplari_getir()
            uyeler = self.vt.uyeler_getir()
            
            #Kitap ve Üye kontrolü
            kitap = None
            uye = None
            
            for k in kitaplar:
                if k['isbn'] == isbn:
                    kitap = k
                    break
            
            for u in uyeler:
                if u['uye_no'] == uye_no:
                    uye = u
                    break
    
            if not kitap or not uye:
                print("Kitap veya üye bulunamadı!")
                return
            
            if not kitap['musait']:
                print("Kitap zaten ödünç verilmiş!")
                return
            
            if len(uye['odunc_alinan_kitaplar']) >= 3:
                print("Bir üye en fazla 3 kitap ödünç alabilir! ")
                return
            
            if uye['ceza'] > 5:
                print(f"Üyenin {uye['ceza']} TL cezası bulunmaktadır!")
                return
            
            
            # ödünç verme işlemi
            kitap['musait'] = False
            kitap['odunc_alan'] = uye_no
            kitap['odunc_tarihi'] = datetime.now().strftime("%Y-%m-%d")
            kitap['teslim_tarihi'] = (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")
            
            uye['odunc_alinan_kitaplar'].append(isbn)
            
            self.vt._veri_kaydet(self.vt.kitaplar_dosyasi, kitaplar)
            self.vt._veri_kaydet(self.vt.uyeler_dosyasi, uyeler)
            
            print("Kitap başarıyla ödünç verildi!")
            print(f"Teslim Tarihi: {kitap['teslim_tarihi']}")
            
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
        
    
    
    def kitap_iade_al(self):
        try:
            isbn = input("İade Edilecek Kitabın ISBN Numarası: ")
            
            kitaplar = self.vt.kitaplari_getir()
            uyeler = self.vt.uyeler_getir()
            
            #kitap kontrolü
            kitap = None
            for k in kitaplar:
                if k['isbn'] == isbn:
                    kitap = k
                    break
                
            if not kitap:
                print("Kitap bulunamadı!")
                return
            
            if kitap['musait']:
                print("Bu kitap zaten kütüphanede!")
                return
            
            # üye bulma
            uye = None
            for u in uyeler:
                if f"M{int(u['uye_no'][1:])}" == f"M{int(kitap['odunc_alan'][1:])}":
                    uye = u 
                    break
                
            if not uye:
                print("Kitabı ödünç alan üye bulunamadı!")
                return
            
            # gecikme kontrolü
            teslim_tarihi = datetime.strptime(kitap['teslim_tarihi'], "%Y-%m-%d")
            bugun = datetime.now()
            
            if bugun > teslim_tarihi:
                gecikme_gun = (bugun - teslim_tarihi).days
                ceza = gecikme_gun * 5 #Günlük 5 tl ceza
                uye['ceza'] = uye.get('ceza', 0) + ceza
                print(f"Gecikme Cezası: {ceza} TL")
                
            # iade işlemi 
            kitap['musait'] = True
            kitap['odunc_alan'] = None
            kitap['odunc_tarihi'] = None
            kitap['teslim_tarihi'] = None
            
            if 'odunc_alinan_kitaplar' in uye:
                uye['odunc_alinan_kitaplar'].remove(isbn)
            
            self.vt._veri_kaydet(self.vt.kitaplar_dosyasi, kitaplar)
            self.vt._veri_kaydet(self.vt.uyeler_dosyasi, uyeler)
            
            print("Kitap başarıyla iade alındı!")
            
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            
            
    def odunc_listele(self):
        try:
            kitaplar = self.vt.kitaplari_getir()
            uyeler = self.vt.uyeler_getir()
        
            odunc_kitaplar = [k for k in kitaplar if not k['musait']]
            
            if not odunc_kitaplar:
                print("Henüz ödünç verilen kitap yok.")
                return
            
            for kitap in odunc_kitaplar:
                try:    
                    uye = next((u for u in uyeler if 
                           u['uye_no'] == kitap['odunc_alan'] or
                           f"M{int(u['uye_no'][1:])}" == f"M{int(kitap['odunc_alan'][1:])}"
                           ), None)
                    
                    print("\n === Ödünç Kitap Detayları ===")
                    print(f"Kitap: {kitap['baslik']}")
                    
                    if uye:
                        print(f"Ödünç Alan Üye: {uye['ad_soyad']}")
                    else:
                        print(f"Ödünç Alan Üye No: {kitap['odunc_alan']} (Üye bilgisi bulunamadı)")
                        
                    print(f"Teslim Tarihi: {kitap['teslim_tarihi']}")
                    
                except Exception as e:
                    print(f"Kitap detayları gösterilirken hata oluştu: {e}")
                    
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
        
        
    
    def menu_goster(self):
        while True:
            print("\n=== Kütüphane Yönetim Sistemi ===")
            print("1. Kitap İşlemleri")
            print("2. Üye İşlemleri")
            print("3. Ödünç İşlemleri")
            print("4. Çıkış")
            
            secim = input("Seçiminiz (1-4): ")
            
            
            if secim == '1':
                self.kitap_menu()
            elif secim == '2':
                self.uye_menu()
            elif secim == '3':
                self.odunc_menu()
            elif secim == '4':
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
            
            
            if secim == '1':
                self.kitap_ekle()
            elif secim == '2':
                self.kitap_sil()
            elif secim == '3':
                self.kitaplari_listele()
            elif secim == '4':
                self.kitap_ara()
            elif secim == '5':
                break
            else:
                print("Geçersiz Seçim")
                
            
    
    def uye_menu(self):
        while True:
            print("\n=== Üye İşlemleri ===")
            print("1. Üye Ekle")
            print("2. Üye Sil")
            print("3. Üyeleri Listele")
            print("4. Üye Ara")
            print("5. Ceza Ödeme")
            print("6. Ana Menüye Dön")
            
            secim = input("Seçiminiz (1-5): ") 
            
            if secim == '1':
                self.uye_ekle()
            elif secim == '2':
                self.uye_sil()
            elif secim == '3':
                self.uyeleri_listele()
            elif secim == '4':
                self.uye_ara()
            elif secim == '5':
                self.odeme_islemi()
            elif secim == '6':
                break
            else:
                print("Geçersiz seçim!")
            
            
    def odunc_menu(self):
        
        while True:
            print("\n=== Ödünç İşlemleri ===")
            print("1. Kitap Ödünç Ver")
            print("2. Kitap İade Al")
            print("3. Ödünç Alınan Kitapları Listele")
            print("4. Ana Menüye Dön")
            
            secim = input("Seçiminiz (1-4): ")
            
            if secim == "1":
                self.kitap_odunc_ver()
            elif secim == "2":
                self.kitap_iade_al()
            elif secim == "3":
                self.odunc_listele()
            elif secim == "4":
                break
            else:
                print("Geçersiz seçim!")
            
            
if __name__ == "__main__":
    sistem = KutuphaneYonetim()
    sistem.menu_goster()
                
            
            
            
            
            
            
            
            
            
            
            
            