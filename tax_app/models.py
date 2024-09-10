from django.db import models

class Income(models.Model):
    income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.income}"
