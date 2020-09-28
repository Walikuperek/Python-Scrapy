import scrapy


class OnetSpider(scrapy.Spider):
    name = 'hackernews'

    def start_requests(self):
        urls = [
            'https://thehackernews.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        response_arr = self.get_array_of_response(response)

        filename = 'storage.txt'
        with open(filename, 'a') as f:
            for i in range(len(response_arr)):
                f.write('\n')            # make rows
                f.write(str(i))          # write index

                row_to_display = str(response_arr[i])

                if str(i % 2) == '0':    # selects header
                    f.write(' header: ')
                    if row_to_display != 'None':
                        f.write(row_to_display)
                else:                    # selects description
                    f.write(' len(desc): ')
                    s = len(row_to_display)
                    f.write(str(s))

                    counter = 1
                    for k in range(s):
                        if k % 63 == 0:
                            f.write('\n    ')
                            min_len = int(k)
                            max_len = int(63 * counter)
                            if row_to_display != 'None':
                                f.write(row_to_display[min_len:max_len])
                            counter += 1
                    f.write('\n\n')

        self.log('Saved file %s' % filename)

    def get_array_of_response(self, response):
        response_arr = []
        for i in range(20):
            # Get text data for every header and description
            res_h2_home_title = response.xpath('//*[@id="Blog1"]/div[1]/div[' + str(i) + ']/a/div/div[2]/h2/text()').get()
            res_home_desc = response.xpath('//*[@id="Blog1"]/div[1]/div[' + str(i) + ']/a/div/div[2]/div[2]/text()').get()

            # Change type to string and remove whitespaces
            res_h2_home_title = str(res_h2_home_title).strip()
            res_home_desc = str(res_home_desc).strip()
            print(res_h2_home_title)
            print(res_home_desc)

            # append to returned array
            response_arr.append(res_h2_home_title)
            response_arr.append(res_home_desc)

        return response_arr
