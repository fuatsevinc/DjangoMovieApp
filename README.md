
# Django Movie 

django ile movie app 


# Django Movie Projesi



## İçindekiler
* [Genel Bilgiler](#genel-bilgiler)
* [Teknolojiler](#teknolojiler)
* [özellikleri](#özellikleri)
* [Kururlrum](#kururlrum)

## Genel Bilgiler
Bu depo, bir Django Projesinin temel kurulumuna sahiptir. Django kullanarak bir projenin temel kurulumunu ayarlamak ve yapılandırmak zor olduğundan. Bu depoyu projeniz için klonlayabilir ve projeleriniz için kullanabilirsiniz.


## Teknolojiler
Proje bu teknolojiler ile oluşturulur:
* Bootstrap 4
* Python 3.10
* Jazzmin 2.5
* Django 4.0

### Özellikleri
1 Kimlik doğrulama, yetkilendirme <br>
2 Üzerine yazılan Django yönetici modülü <br>
3 Giriş yapın ve kaydolun <br>
4 Temel bir sayfa ve temel navigasyon sistemi. <br>
5 İyi ve mobil dostu bir kullanıcı arayüzü. <br>

## Kururlrum

Projeyi yerel olarak çalıştırmak için bu adımları izleyin

1. Depoyu klonla
   ```sh
   git clone https://github.com/tamaraiselvan/Base-django-project-Setup
   ```
2. Sanal bir ortam oluşturun
   ```sh
   python -m venv virtualenviron_name
   ```
3. Ortamı etkinleştir
   ```sh
   virtualenviron_name\Scripts\activate
   ```
4. Requirements.txt dosyasından Requirements yükleyin
   ```sh
   pip install -r requirements.txt
   ```
5. Gereksinimleri yükledikten sonra veritabanını taşıyın
   ```sh
   python manage.py migrate
   ```
6. Taşıma işleminden sonra bir süper kullanıcı hesabı oluşturun
   ```sh
   python manage.py createsuperuser
   ```
7. Sunucuyu sisteminizde yerel olarak çalıştırın
   ```sh
   python manage.py runserver
   ```
8. Tarayıcınızı açın ve yazın
   ```sh
   http://127.0.0.1:8000/
   ```

