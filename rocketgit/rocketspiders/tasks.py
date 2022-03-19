import logging
from django_rq import job

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from rocketspiders.gitspider import GitSpider
from rocketspiders.models import Dataspider

logger = logging.getLogger(__name__)


@job
def run_git_spider():

    def crawler_results(signal, sender, item, response, spider):
        Dataspider.objects.update_or_create(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(GitSpider)
    process.start()
