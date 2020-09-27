# Python-Scrapy
Web Crawler set to extract some headers from [onet.pl](https://www.onet.pl)
then save them into onet.txt 

### Scrapy package

## Setup
```
pip install scrapy
scrapy startproject project_name
```

## Run
```
scrapy crawl spider_name
```

## Main function
```
def get_array_of_response(self, response):
    response_arr = []
    for i in range(15):
        res = response.xpath('//*[@id="mainPageBody"]/div[3]/div[1]/article/section[1]/div[2]/ul/li[' + str(i) + ']/a/span/text()').get()
        res = str(res)
        res = res.strip()
        print('i: ', i)
        print(res)
        response_arr.append(res)
        print(response_arr)
    return response_arr
```

## response_arr
```
['None', '', 'Ambasadorzy państw poparli społeczność LGBT w Polsce. Powstał list otwarty', 'Ponad milion ofiar koronawirusa', 'Trump unikał płacenia podatków. Zaskakujące dane', 'Jak działał gang Sharksów? Są zeznania', 'Kto zastąpi Kaczyńskiego w PiS?', 'DZIŚ W ONECIE', '"Pancerny Marian" Kaczyńskiego się nie boi', 'Walki o Górski Karabach. Reakcja Rosji', 'Zima będzie ciepła? Ekspert tłumaczy prognozy', 'Europosłowie mieli usta zaklejone taśmą', 'OPINIA', 'Duże protesty na Białorusi. Padły strzały', 'Przywódca Karabachu: straciliśmy część ziemi']
```
