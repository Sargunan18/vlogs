from typing import Any
from django.db import transaction
from django.core.management.base import BaseCommand

from games.models import Category


class Command(BaseCommand):
    help = 'Insert sample Category data'

    def handle(self, *args: Any, **options: Any) -> None:
        # delete existing data and insert sample categories
        with transaction.atomic():
            Category.objects.all().delete()

            names = [
                'sports',
                'technology',
                'science',
                'art',
                'food',
            ]

            for name in names:
                Category.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS('completed inserting categories'))
