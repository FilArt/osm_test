# osm_test

### В файлах direct.txt и reverse.txt хранятся тестовые данные.
### Для тестирования прямого геокодирования тестовые данные представляются в виде:
    место   тест_широта   тест_долгота
#### GET запрос к nomanatim.openstreetmap search/место/ возвращает координаты, которые сравниваются с тест_широта, тест_долгота 
### Для обратного геокодирования:
    широта  долгота   масштаб(zoom)   тест_место
#### GET запрос возвращает display_name, который содержит название места по данным широты и долготы, которое сравнивается с тест_место

### Usage:
    python3 direct.py
    python3 reverse.py
