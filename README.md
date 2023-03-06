# Django-IHA

İlk olarak proje açıldığında sıfırdan Venv oluşturulmalıdır. Projede python 3.11 kullanılmıştır.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/yeni%20venv%20olusturma.jpg?raw=true)

Venv oluşturulduktan sonra requirements.txt de kütüphaneler kurulmalıdır

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/requirements2.jpg?raw=true)

Projede kullanılan kütüphaneler resimdeki gibidir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/requirements.jpg?raw=true)

```
+ pip install django
+ pip install pillow
+ pip install django-filter

yukarıdaki install komutlarını kullanarak aynı kütüphanelerin kurulmasını sağlayabilirsiniz
```

**makemigrations** komutu kullanılarak uygulamadaki model.py deki migration dosyaları oluşturulur.(oluşmamışsa)

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/makemigrations.jpg?raw=true)

**makemigrations** komutu kullanılmadan önce veritabı oluşturulmalıdır. Yoksa çalışmayacaktır.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/database%20olu%C5%9Fturma.jpg?raw=true)


migrate komutu kullanılarak, temel django veritabanı tablolarını(exp:USER) ve migration dosyalarında belirtilen uygulama tablolarını, setting.py de belirtilen veritabanda oluşturur.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/postgresql_setting.jpg?raw=true)

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/migrate.jpg?raw=true)

admin arayüzüne erişmek için **python manage.py createsuperuser** komutu kullanılarak admin oluşturulur.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/createsuperuser.jpg?raw=true)

admin.py, admin kullanıcısının modeldeki veritabanı tabloların erişmesi için izin verir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/admin_py.jpg?raw=true)

**NOT:** Admin sayfasına erişmek için proje çalıştırılmalıdır. Çalıştırıldıktan sonra "/admin" url'sine gidilmelidir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/admin.jpg?raw=true)

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/admin%20aray%C3%BCz%C3%BC.jpg?raw=true)

**python manage.py runserver** komutu kullanılarak proje çalıştırılır. (Migration yapılmamışsa uyarır) 

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/runserver.jpg?raw=true)

Proje ilk belirlenen url("/") olarak login ekranını açar. Alttaki "Yeni bir hesap oluştur" yazısındaki url ile kayıt sayfasına gidilebilir. Admin oluşturduğumuzdan dolayı admin kullanıcısıyla da giriş yapılabilir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/login.jpg?raw=true)

Projenin kayıt sayfasına gitmek için "/register" url'si yazılarak kayıt sayfasına gidilebilinir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/hesap%20olu%C5%9Fturmaca.jpg?raw=true)

Login ekranından giriş yapıldıktan sonra, sistem kullanıcıyı dashboard sayfasına yönlendirecektir. Kayıt yok, bundan dolayı sadece filtreleme gözükecektir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/dashboard_bos.jpg?raw=true)

IHA eklemek istenildiğinde **Kontrol Paneli** sayfasındaki **IHA EKLE** butonuna basılarak iha ekleme sayfasına geçilir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/iha_ekle.jpg?raw=true)

IHA EKLE sayfasında, gerekli Alanlar doğru doldurulmassa kullanıcıya hata bildirilir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/iha_ekle_hata.jpg?raw=true)

IHA eklerken sonuc başarılı olursa, sistem IHA'yı kaydeder ve kullanıcıyı Kontrol Paneline yönlendirir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/dashboard.jpg?raw=true)

Kayıtlı IHA güncellenmek istenirse, karttaki **DÜZENLE** butonuna basılmalıdır.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/dashboard.jpg?raw=true)

**DÜZENLE** butonuna basıldığında IHA Güncelleme sayfasına gidilir.

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/iha_g%C3%BCncelle.jpg?raw=true)

**SİL** butonuna basıldığında IHA SİL sayfasına gidilir. Evet denilirse kayıt veritabanından silinir.
![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/iha%20sil.jpg?raw=true)

Herhangi bir hata olduğunda **404** sayfasıyla karşılaşılır.
![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/404.jpg?raw=true)

Filtreleme seçenekleri kullanılarak istenilen veri kolaylıkla erişilebilir. Bu seçenekler isteğe göre arttılabilir veya azaltılabilinir.
![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/django-filter.jpg?raw=true)

![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/django-filter2.jpg?raw=true)

Sağ üst köşedeki kullanıcıdan **Sign Out** ya da **logout** urlsine gidilerek çıkış yapılır.
![myimage-alt-tag](https://github.com/MTUSTA/Django-IHA/blob/main/ReadmeMD_Image/logout.jpg?raw=true)
