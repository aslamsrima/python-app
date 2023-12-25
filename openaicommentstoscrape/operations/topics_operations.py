from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def topics_operation():
    process = CrawlerProcess(get_project_settings())
    process.crawl('topics')
    process.start() # the script will block here until the crawling is finished

    pass