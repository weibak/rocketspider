import logging
from django.core.management.base import BaseCommand


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl GIT"

    def handle(self, *args, **options):
        run_git_spider.delay()
