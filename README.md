# FirstWeek
# Gümüşhane İkizevler Kent Müzesi Web Uygulaması ve Ziyaretçi Kayıt Sistemi - Öğrenci Projesi

Merhaba! Bu proje, Gümüşhane İkizevler Kent Müzesi için basit bir web uygulaması fikri olarak geliştirildi. Amacım, ziyaretçilerin müzeyle ilgili temel bilgilere ulaşabileceği, belki ileride rezervasyon yapabileceği ve site yöneticilerinin de bazı şeyleri kontrol edebileceği bir yapı oluşturmaktı. Henüz geliştirme aşamasında ve bir öğrenci projesi olduğunu unutmayın :)

## Proje Nasıl Çalışıyor?

Temelde Flask kullanarak birkaç web sayfası oluşturdum. Her sayfa için ayrı bir HTML dosyam var ve `app.py` dosyası da bu sayfalara hangi adreslerden ulaşılacağını belirliyor.

## Proje İçeriği

- **app.py:** Bu ana dosya. Hangi internet adresinin (`/`, `/admin/giris` gibi) hangi sayfayı göstereceğini söylüyor. Şimdilik sadece sayfaları gösteriyor, arka planda pek bir şey yapmıyor.
- **templates/:** Bu klasörde `.html` uzantılı web sayfalarım var.
    - index.html: Müzenin ana sayfası gibi bir şey.
    - admin_giris.html: Yönetici paneline girmek için bir sayfa (amaç sadece göstermek).
    - admin_paneli.html: Yönetici paneli gibi bir yer .
    - kayit_formu.html: Ziyaretçilerin kaydolabileceği bir form (sadece görüntü).
    - listele.html: Kayıtlı ziyaretçilerin listeleneceği bir sayfa (şu an boş).
    - guncelleformu.html: Ziyaretçi bilgilerini güncellemek için bir form (sadece görüntü).
    - filtrele.html: Ziyaretçileri filtrelemek için bir sayfa (boş).
    - kayitli_ziyaretciler.html: Kayıtlı ziyaretçileri gösteren bir sayfa (şu an boş bir liste gönderiyor).
    - kayitli_kullanici.html: Giriş yapan kullanıcının bilgilerini gösterecek bir sayfa (şu an "Boş Alan" yazıyor).
- **static/:** Burada da CSS (sayfaların nasıl görüneceğini ayarlayan dosyalar), JavaScript (sayfalara hareketlilik katan kodlar) ve resimler olabilir. Şu an sadece logo gibi şeyler için bir `img` klasörü var.

## Temel Özellikler (Şimdilik Düşünce Aşamasında)

### Kullanıcı Tarafı İçin

- Belki online rezervasyon yapma imkanı (çalışmıyor).
- Kullanıcıların kaydolabileceği ve giriş yapabileceği bir sistem (henüz çalışmıyor).
- Giriş yapan kullanıcılar kendi bilgilerini görebilecek (şu an sadece "Boş Alan").
- Ziyaret edenler yorum bırakabilecek (basit bir deneme yaptım ama tam değil yorum kısmına giriş yapma şartı eklemeyi denemedim ama beceremedim üstünde çalışacağım.).
- Müzenin konumu gösteren harita.(doğruluğundan emin değilim)

### Yönetici Tarafı İçin (/admin ile başlayan adresler)

- Yöneticiler giriş yapabilecek (ama kimlik kontrolü yok).
- Bir yönetici paneli var.
- Kayıtlı ziyaretçilerin listesi görülebilecek (şu an boş tablo).
- Ziyaretçi bilgileri güncellenebilecek (form var ama işlemiyor).
- Ziyaretçiler silinebilecek (var ama silmiyor).
- Ziyaretçileri filtreleme yapılabilecek (sayfa var ama çalışmıyor).


## Kullandığım Teknolojiler

Python ile Flask (şuanlık sadece yönlendirmeler için).
HTML, CSS, Bootstrap 5 (görünümü daha iyi yapsın diye), JavaScript (birkaç basit şey için), Leaflet (harita için).




