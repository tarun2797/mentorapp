from django.db import models

# Create your models here.
class college(models.Model):  #model object in django
    name=models.CharField(max_length=128)
    location=models.CharField(max_length=64)
    acronym=models.CharField(max_length=8)
    contact=models.EmailField()


    def __str__(self):
        return self.acronym

class Student(models.Model):
    name=models.CharField(max_length=128)
    dob=models.DateField(null=True,blank=True)
    email=models.EmailField()
    db_folder=models.CharField(max_length=50)
    dropped_out=models.BooleanField(default=False)
    college=models.ForeignKey(college,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class MockTest1(models.Model):
    problem1 = models.IntegerField()
    problem2 = models.IntegerField()
    problem3 = models.IntegerField()
    problem4 = models.IntegerField()

    total = models.IntegerField()

    students = models.OneToOneField(Student,on_delete=models.CASCADE)

    def __str__(self):
        return f"student {self.student.name} marks"

class Teacher(models.Model):
    name = models.CharField(max_length=28)
    email = models.EmailField()
    college = models.ForeignKey(college, on_delete=models.CASCADE)

