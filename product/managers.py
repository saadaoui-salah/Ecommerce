from django.db import models
from django.db.models import Avg

class QuerySets(models.QuerySet):
    def calculate_percentage(self, star):
        if self.count() > 0:
            return (self.filter(stars=star).count() / self.count()) * 100
        else:
            return 0

    def get_1_star_percentage(self):
        return self.calculate_percentage(1)

    def get_2_star_percentage(self):
        return self.calculate_percentage(2)
    
    def get_3_star_percentage(self):
        return self.calculate_percentage(3)

    def get_4_star_percentage(self):
        return self.calculate_percentage(4)

    def get_5_star_percentage(self):
        return self.calculate_percentage(5)

    def get_avg_rating(self):
        rating = self.values('stars').aggregate(Avg('stars'))['stars__avg']
        if not rating is None:
            return rating.__round__()
        return 0

    def get_details(self):
        return self.values(
            'id', 'name', 'details', 'price',
            'image', 'discount__percentage'
        )

class ReviewManager(models.Manager):
    def get_queryset(self):
        return QuerySets(self.model, using=self._db)
    
    def calculate_percentage(self):
        return self.get_queryset().calculate_percentage()

    def get_1_star_percentage(self):
        return self.get_queryset().get_1_star_percentage()

    def get_2_star_percentage(self):
        return self.get_queryset().get_2_star_percentage()

    def get_3_star_percentage(self):
        return self.get_queryset().get_3_star_percentage()

    def get_4_star_percentage(self):
        return self.get_queryset().get_4_star_percentage()

    def get_5_star_percentage(self):
        return self.get_queryset().get_5_star_percentage()

    def get_avg_rating(self):
        return self.get_queryset().get_avg_rating()

class ProductManager(models.Manager):
    def get_queryset(self) :
        return QuerySets(self.model, using=self._db)

    def get_details(self):
        return self.get_queryset().get_details()
