# Python-Scrapy
Web Crawler set to extract some text from 
* [onet.pl](https://www.onet.pl) - very popular Polish news web service
* [thehackernews.com](https://thehackernews.com) - hacker news web service

then save them as 
* string( array of text ) 
* into files with .txt extension

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

## e.g. response from onet/spiders/onet_spiders.py
```
6 Kto zastąpi Kaczyńskiego w PiS?
```

## e.g. response from onet/spiders/hackrnews_spiders.py
```
2 header: FinSpy Spyware for Mac and Linux OS Targets Egyptian Organisations
3 len(desc): 991
    Amnesty International today exposed details of a new surveillan
    ce campaign that targeted Egyptian civil society organizations 
    with previously undisclosed versions of FinSpy spyware designed
     to target Linux and macOS systems.  Developed by a German comp
    any , FinSpy is extremely powerful spying software that is bein
    g sold as a legal law enforcement tool to governments around th
    e world  but has also been found  in use by oppressive and dubi
    ous regimes to spy on activists.  FinSpy, also known as FinFish
    er, can target both desktop and mobile operating systems, inclu
    ding Android, iOS, Windows, macOS, and Linux, to gain spying ca
    pabilities, including secretly turning on their webcams and mic
    rophones, recording everything the victim types on the keyboard
    , intercepting calls, and exfiltration of data.   According to 
    the human rights organization Amnesty International , the newly
     discovered campaign is not linked to 'NilePhish,' a hacking gr
    oup known for attacking Egyptian NGOs in a ser
```
