# Python-Scrapy
Web Crawler set to extract some headers from [onet.pl](https://www.onet.pl) - very popular Polish news web service
then save them as string(array of headers) into onet.txt

### PIP dependency:
* Scrapy - Web Scrapping Framework

## Setup
```
pip install scrapy
scrapy startproject project_name
```

## Run
```
scrapy crawl spider_name
```

## e.g. response_array saved as <string>string into 'onet.txt'</string>
```
['None', '', 'Ambasadorzy państw poparli społeczność LGBT w Polsce. Powstał list otwarty', 'Ponad milion ofiar koronawirusa', 'Trump unikał płacenia podatków. Zaskakujące dane', 'Jak działał gang Sharksów? Są zeznania', 'Kto zastąpi Kaczyńskiego w PiS?', 'DZIŚ W ONECIE', '"Pancerny Marian" Kaczyńskiego się nie boi', 'Walki o Górski Karabach. Reakcja Rosji', 'Zima będzie ciepła? Ekspert tłumaczy prognozy', 'Europosłowie mieli usta zaklejone taśmą', 'OPINIA', 'Duże protesty na Białorusi. Padły strzały', 'Przywódca Karabachu: straciliśmy część ziemi']
```
