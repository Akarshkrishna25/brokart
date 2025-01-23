from django.db import models

# Customer.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live')(DELETE,'delete'))
    name=models.CharField(max_lenght=200)
    address=models.CharField()
    user=models.OneToOneField(user,on_delete=models.CASCADE, related_name='Customer_profile')
    phone=models.IntegerField(max_lenght=200)

    image=models.CharField(upload_to='/media')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def __str__(self)->str:
    return self.title
