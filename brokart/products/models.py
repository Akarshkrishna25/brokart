from django.db import models

# product structure
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'), (DELETE,'delete'))
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def __str__(self)->str:
    return self.title

