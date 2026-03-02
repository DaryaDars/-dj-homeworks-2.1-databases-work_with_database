
import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def add_arguments(self, parser):
        # parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        pass

    def handle(self, *args, **options):
        csv_file_path = 'phones.csv'
        try:
            with open('phones.csv', 'r') as file:
                phones = list(csv.DictReader(file, delimiter=';'))

                for phone_data in phones:
                    # TODO: Добавьте сохранение модели
                    # Преобразование данных и создание объекта Phone
                    phone = Phone(
                        name=phone_data['name'],
                        price=phone_data['price'],
                        image=phone_data['image'],
                        release_date=phone_data['release_date'],
                        lte_exists=phone_data['lte_exists'],
                        # slug=slugify(phone_data['name'])
                    )

                    # Сохранение объекта Phone в базе данных
                    phone.save()

                    self.stdout.write(self.style.SUCCESS(f'Successfully imported phone: {phone.name}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {csv_file_path}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
