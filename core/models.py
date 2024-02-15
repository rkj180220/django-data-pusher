from django.db import models
import uuid

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.AutoField(primary_key=True, unique=True)
    account_name = models.CharField(max_length=100)
    app_secret_token = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.account_name

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField(blank=False)
    http_method = models.CharField(max_length=10, choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT')])
    headers = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.account.account_name} - {self.url}"
