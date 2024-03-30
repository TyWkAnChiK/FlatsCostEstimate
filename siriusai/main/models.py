from django.db import models

# Create your models here.

class question(models.Model):
    # apartment_type = models.CharField('Тип дома',max_length=50,blank=False)
    metro_station = models.CharField('Ближайшая станция метро',max_length=50,blank=False)
    minutes_to_metro = models.CharField('Время ходьбы до метро',max_length=50,blank=False)
    #region
    number_of_rooms = models.CharField('Количество комнат', max_length=50, blank=False)
    all_area = models.CharField('Вся площадь', max_length=50, blank=False)
    living_area = models.CharField('Жилая площадь',max_length=50,blank=False)
    kitchen_area = models.CharField('Кухонная площадь',max_length=50,blank=False)
    floor = models.CharField('Этаж',max_length=50,blank=False)
    number_of_floors = models.CharField('Количество этажей', max_length=50, blank=False)
    renovation = models.CharField('Ремонт', max_length=50, blank=False)
    renovations = models.CharField(max_length=50,choices=(
        ("Designer", "Дизайнерский"),
        ("Without renovation", "Без ремонта"),
        ("European-style renovation", "Евро-ремонт"),
        ("Cosmetic", "Косметический")
    ), default="Without renovation")

    def __str__(self):
        return self.all_area

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'