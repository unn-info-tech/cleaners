from django.db import models



class RoomTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class FeatureTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    individual_price = models.DecimalField(max_digits=8, decimal_places=2)
    #business_price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='services/')
    room_tags = models.ManyToManyField('RoomTag', related_name='services')
    feature_tags = models.ManyToManyField('FeatureTag', related_name='services')

    def __str__(self):
        return self.name


class ExtraService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='extras/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"



from django.utils import timezone

class Order(models.Model):
    service = models.ManyToManyField(Service, related_name='orders')
    extra_service = models.ManyToManyField(ExtraService, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} - Total: ${self.total_price}"