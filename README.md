
# CeleryMonitor

Aplikacja śłuży do monitorowania stron internetowych w zadanych interwałach czasowych. Łatwa do modernizacji. Napisana w Django. Wykorzystuje ona Celery do zarządzania koeljką zadań oraz jej pakietami do Django umożliwiającymi jej większą kompatybiliność:
- django-celery-beat
- django-celery-results


## Tech Stack

**Server:** Django, Django Rest Framework, Celery, RabbitMQ
**Database** PostgreSQL



## Features

- Możliwość zdefiniowania, edycji, usunięcia monitorowanej strony internetowej.
- Możliwość ustawienia interwału czasowego dla każdej monitorowanej strony
  - 1 minuta;
  - 5 minut;
  - 15 minut;
  - 30 minut;
  - 60 minut;
- Zapisywanie problemów związanych z działaniem monitorowanej strony w bazie danych - "Kod odpowiedzi"
- Wykrywanie zmian w zadanej stronie - "Suma kontrolna"
- Możliwość podejrzenia historii awarii dla każdej monitorowanej strony
  - przejrzysty sposob oglądania od kiedy do kiedy była awaria
  - podział na stony
  - sortowana od najnowszych zdarzeń
- Możliwość wykorzystania admina django do zarządzania danymi które aplikacja zbiera.
- Widok do sprawdzenia wszystkich stron, które aktualnie mają problemy.
- Wykorzystanie prostego Boostrapa
- REST API
- Dana strona może zostać dodana tylko raz dla danego interwału poprzez webową.

## Deployment

Aby zdeployować projkt na serwerze potrzeba dokonąc następujące zmiany w budowię projektu:
- zainstalować PostgreSQL na serwerze, jeżeli jeszcze go nie ma 

- stworzyć podkatalog settings o strukturze:
```bash
settings/
    __init__.py
    base.py
    local.py
    pro.py
```
gdzie Base.py, to stary plik settings.py, ale ze zmieniną nazwą.

- dostosowac stałą 'BASE_DIR' w pliku base.py

- w pliku 'local.py' oraz 'pro.py' zaimportować cały 'base.py' - w dwóch plikahc powinny być nadpisane tylko specyficzne dla nich elementy, reszta wspólna

- w pliku 'local.py' nalezy dac ustawienia
```bash
DEBUG = True 

DATABASE = {...}
```
Ustawiamy opcję DEBUG na True, po to byśmy mogli TYLKO W ŚRODOWISKU LOKALNYM debugować. Database należy uzupełnić odpowiednimi informacjami w zależności od użytej przez nas bazy danych.

- w pliku 'pro.py' 
```bash
DEBUG = False 
Admins = (...)

ALLOWED_HOSTS = [...]

DATABASE = {...}
```
    - Po to aby utrudnić możliwość wyciekania niepotrzebnych informacji dla osób postronnych. 
    - Pole DATABASE odpowiendio uzupełnić.
    - ADMINS służy do informowania odpowienich osobw  tej sekcji o awariach
    - ALLOWED_HOSTS służy do kontroli łączπących sie hostów. '*' pozwala każdem hostowi sie połaćzyć

- Z pliku 'base.py'  'DEBUG' i 'DATABASE' - są już niepotrzebne w nim.

- Utworzenie zmiennej srodowiskowej 'DJANGO_SETTINGS_MODULE' w powłoce komendą:
```bash
export DJANGO_SETTINGS_MODULE=CeleryMonitor.settings.pro
By móc łatwiej korzystać z aplikacji - nie dodawać --settings przy większosći poleceń z 'manage.py'
```

- użycie komendy 
```bash 
python manage.py check
```
służacej do sprawdzenia poprawności projektu. Można ozyć opcji '--deply' by sprawdzić tylko aplikacje dla środowiska produkcyjnego.

- Instalacje i konfuguracja uWSGI w tym stworzenie struktury danych:
```bash
config/
    uwsgi.ini
logs/
```

- zainstalowanie i skonfigurowanie NGINX

- udostępnienie zasobów statycznych oraz multimedialnych. Służy do tego komenda:
```bash
python manage.py collectstatic
```
Oraz odpowiedni skonfugurowanie serwera pod to. SŁuża do tego komendu:
```bash
STATIC_ROOT
STATIC_URL
MEDIA_ROOT
MEDIA_URL
```

- dobrym pomysłem będzie skonfigurowanie też SSL/TLS by korzystać z protokołu HTTPS - szyfropwanej wersji HTTP. Daje to większe bezpieczeństwo, w szczególności, jeżeli dodamy opcje logowania do aplikacji. Większość usatwień będzie w NGINXie, a w Django należy ustawić:
```bash
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
```
w pliku 'pro.py'. Służa one do przekierwoania do HTTPS oraz stworzenia bezpiecznego cookie by zabezpieczyć przed atakiem CSRF.



## Run Locally

Komenda do uruchomienia Django

```bash
  python manage.py  runserver
```
Komenda do uruchomienia serwera Celery 

```bash
  celery -A CeleryMonitoring worker -l info
```
Komenda do uruchomienia serwera Celery beat

```bash
celery -A CeleryMonitoring beat -l info
```
## REST API

Lista wszystkich monitorowanych stron:

```bash
GET /websitesApi/
```

Dodanie nowej strony do monitorowania:

```bash
POST /websitesApi/
```
Format JSONA do Dodania strony
```JSON
{
    "name": "WebName",
    "urlAddress": "url",
    "intervals": "05",
    "isWorking": false
}
```

Obsługiwane formaty interwałów:
- '01' co 1 minute
- '05' co 5 minut
- '15' co 15 minut
- '30' co 30 minut
- '60' co 60 minut

Informacje tylko o jednej stronie bazując na jej 'id':

```bash
GET /websitesApi/id
```
Lub
```bash
GET GET /notworkingApi/id
```

Lista wszystkich NIE DZIAŁAJĄCYCH stron:

```bash
GET /notworkingApi/
```

Lista wszystkich logów sprawdzeń stron:

```bash
GET /eventsApi/
```


Informacje tylko o jednego logu bazując na jego 'id':

```bash
GET /eventsApi/id
```
