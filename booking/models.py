from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)


class Table(models.Model):
    table = models.IntegerField()
    max_people = models.IntegerField()

    def table_counter(self):
        "Returns the table options"
        if self.max_people < table:
            return "This table is only for 2 people"
        elif self.max_people < table:
            return "Table for 4 but maximum 6 people"
        else:
            return "Please contact us to arrange bigger event"


class Booking(models.Model):
    table_options = models.ForeignKey('Table', on_delete=models.CASCADE)
    guest_list = models.ForeignKey('Guest', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

    def reservation(self):
        if table_options == table_counter:
            return "Booked"
        else:
            return "Please check an other option"
    


