from django.db import models

class City(models.Model):
    City_Name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.City_Name}"

class Course(models.Model):
    Course_Name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Course_Name}"

class Student_Data(models.Model):
    Stud_Name=models.CharField(max_length=100)
    Stud_Age=models.IntegerField(default=None)
    Stud_Phno=models.BigIntegerField()
    Stud_City=models.ForeignKey(City,on_delete=models.CASCADE)
    Stud_Course = models.ForeignKey(Course, on_delete=models.CASCADE)

