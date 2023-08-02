from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Used to create Users'
    requires_migrations_checks = True


    def handle(self, *args: Any, **options: Any) -> str | None:
        x = User.objects.filter(is_active = False)
        x.delete()
        print('Users were deleted!')