from django.db import models
from scraping.utils import from_cyrillic_to_eng

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Location')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta():
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Programming Language')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta():
        verbose_name = 'Programming Language'
        verbose_name_plural = 'Programming languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)