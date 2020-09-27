import scrapy


class OnetSpider(scrapy.Spider):
    name = "spider"

    def start_requests(self):
        urls = [
            'https://www.onet.pl'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        response_arr = self.get_array_of_response(response)

        filename = 'onet.txt'
        with open(filename, 'a') as f:
            f.write(str(response_arr))
        self.log('Saved file %s' % filename)

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
