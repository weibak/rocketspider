import logging
from django.core.management.base import BaseCommand

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from rocketspiders.gitspider import GitSpider
from rocketspiders.models import Dataspider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl Git"

    def handle(self, *args, **options):
        def crawler_results(signal, sender, item, response, spider):
            Dataspider.save(item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(GitSpider)
        process.start()
