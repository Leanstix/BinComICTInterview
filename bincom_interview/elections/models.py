from django.db import models

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    state_id = models.IntegerField()
    polling_unit_name = models.CharField(max_length=255, null=True)
    polling_unit_description = models.TextField(null=True)

class AnnouncedPuResult(models.Model):
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=10)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class LGA(models.Model):
    lga_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(null=True, blank=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=255)