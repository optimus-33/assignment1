from django.db import models

# Create your models here.
class Accounts(models.Model):
    acc_id = models.BigIntegerField(default=202305040001)
    holder_name = models.TextField(max_length=50)
    acc_balance = models.IntegerField(default=0)
    loan_amt = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.holder_name