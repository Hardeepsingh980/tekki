from django.core.management.base import BaseCommand, CommandError
from subscription.models import UserSubscription
import datetime
from django.utils import timezone




class Command(BaseCommand):
    help = 'Get Payment'


    def handle(self, *args, **options):
        start_date = timezone.now()
        end_date = start_date + datetime.timedelta(days=0)

        userSubscriptions = UserSubscription.objects.filter(updated_at__range=(start_date, end_date))

        for i in userSubscriptions:
            # Write Payment Logic
            self.stdout.write(self.style.SUCCESS(f'Payment Done For {i.user}'))    

        self.stdout.write(self.style.SUCCESS('Successfully closed poll '))