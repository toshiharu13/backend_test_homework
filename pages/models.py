from django.db import models


class Arm(models.Model):
    name_arm = models.CharField(max_length=30)
    id_arm = models.AutoField(primary_key=True)
    ip_arm = models.GenericIPAddressField(null=True)
    dt_version_arm = models.CharField(max_length=30, blank=True)
    os_version_arm = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name_arm

