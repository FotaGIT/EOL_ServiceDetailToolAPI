from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class CvpHuNonprodCa(models.Model):
    created_on                  = models.DateTimeField()
    modified_on                 = models.DateTimeField(blank=True, null=True)
    certificate_creation_date   = models.DateTimeField(blank=True, null=True)
    certificate_expiration_date = models.DateTimeField(blank=True, null=True)
    certificate_revocation_date = models.DateTimeField(blank=True, null=True)
    certificate_serial_number   = models.CharField(primary_key=True, max_length=60)
    certificate                 = models.TextField(blank=True, null=True)
    private_key                 = models.TextField(blank=True, null=True)
    common_name                 = models.CharField(max_length=50, blank=True, null=True)
    is_revoked                  = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'CVP_HU_NONPROD_CA'


class CvpTcuNonprodPvevCa(models.Model):
    created_on                  = models.DateTimeField()
    modified_on                 = models.DateTimeField(blank=True, null=True)
    certificate_creation_date   = models.DateTimeField(blank=True, null=True)
    certificate_expiration_date = models.DateTimeField(blank=True, null=True)
    certificate_revocation_date = models.DateTimeField(blank=True, null=True)
    certificate_serial_number   = models.CharField(primary_key=True, max_length=60)
    certificate                 = models.TextField(blank=True, null=True)
    private_key                 = models.TextField(blank=True, null=True)
    common_name                 = models.CharField(max_length=50, blank=True, null=True)
    is_revoked                  = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'CVP_TCU_NONPROD_PVEV_CA'

