import scrapy


class OnetSpider(scrapy.Spider):
    name = 'onet_spider'

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
            for i in range(len(response_arr)):
                f.write('\n')
                f.write(str(i))
                f.write(' ')
                if str(response_arr[i]) != 'None':
                    f.write(str(response_arr[i]))

        self.log('Saved file %s' % filename)

    def get_array_of_response(self, response):
        response_arr = []
        for i in range(20):
            # Get text data for every header and description
            res = response.xpath('//*[@id="mainPageBody"]/div[3]/div[1]/article/section[1]/div[2]/ul/li[' + str(i) + ']/a/span/text()').get()

            # Change type to string and remove whitespaces
            res = str(res)
            res = res.strip()

            # append to returned array
            response_arr.append(res)

        return response_arr
