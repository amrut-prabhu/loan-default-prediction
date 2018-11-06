from django.db import models
import csv

# Create your models here.


class Entity(models.Model):
    state = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=50)
    school_type = models.CharField(max_length=50)
    debt        = models.FloatField()
    household_income = models.FloatField()
    poverty_rate = models.FloatField()
    unemployment_rate = models.FloatField()
    location    = models.CharField(max_length=50)

    def __str__(self):
        return self.state+ " - "+self.degree_type+" - "+ self.school_type+" - "+ str(self.debt)+" - "+ str(self.household_income)+" - " + str(self.poverty_rate) + " - "+ str(self.unemployment_rate)+" - "+self.location



'''

#with open(path) as file:
    reader = csv.reader(file)
    for row in reader:
        created = Entity.objects.get_or_create(
            state = row[0] ,
            degree_type = row[1] ,
            school_type = row[2],
            debt= row[3] ,
            household_income= row[4] ,
            poverty_rate  = row[5] ,
            unemployment_rate = row[6],
            location = row[7]
        )
        
'''


