from django.db import models

class Account(models.Model):
    account_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Transfer(models.Model):
    origin_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="from_user")
    destination_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="to_user")
    type = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.amount} {self.currency} from: {self.origin_account} to: {self.destination_account} reference: {self.reference}"