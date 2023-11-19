import scrapy


class WorldPopulationSpider(scrapy.Spider):
    name = "world_population"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        rows = response.xpath('//div[@class="content prose max-w-none prose-h1:text-2xl prose-h1:font-medium prose-h2:text-lg prose-h2:font-bold prose-a:text-sky-600 prose-a:no-underline hover:prose-a:text-sky-500 prose-li:my-0 prose-h1:xl:text-3xl prose-h2:xl:text-xl"]/table/tr')

        for row in rows:
                
            country = row.xpath('.//td[6]/text()').get()
            if country is None:
                country = row.xpath('.//td[6]/a/text()').get()
            gdp = row.xpath('.//td[7]/text()').get()
            yield {
                'country name': country,
                'gdp': gdp
            }

