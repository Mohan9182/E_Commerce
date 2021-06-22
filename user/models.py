from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.category