# Openstreetmap DDT

### В файлах direct.txt и reverse.txt хранятся тестовые данные.
### Для тестирования прямого геокодирования тестовые данные представляются в виде:
    место   тест_широта   тест_долгота
#### GET-запрос "/search/место?format=json&limit=1" к nominatim.openstreetmap.org возвращает координаты, которые сравниваются с тест_широта, тест_долгота 
### Для обратного геокодирования:
    широта  долгота   масштаб(zoom)   тест_место
#### GET-запрос "/reverse.php?format=json&lat=широта&lon=долгота&zoom=масштаб" возвращает display_name, который содержит название места по заданным широте и долготе. Если display_name содержит тест_место, то тест считается успешным.

### Usage:
    python3 direct.py
    python3 reverse.py
