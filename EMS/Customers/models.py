from django.db import models

# Create your models here.
class register(models.Model):
    book_id=models.BigIntegerField(primary_key=True)
    event_id=models.BigIntegerField()
    booked_date=models.DateField()
    p_name=models.CharField(max_length=90)
    p_email=models.CharField(max_length=90)
    p_phone=models.BigIntegerField()

class events(models.Model):
    event_id=models.BigIntegerField(primary_key=True)
    event_name=models.CharField(max_length=90)
    event_date=models.DateField()
    org_email=models.CharField(max_length=90)
    org_phone=models.BigIntegerField()
    event_desc=models.TextField()
    event_type=models.CharField(max_length=90)
    event_loc=models.CharField(max_length=90)
    event_status=models.CharField(max_length=90)
    max_seats=models.BigIntegerField()