from django.db import models


# Create your models here.


class Usertype(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    # type = models.OneToOneField(Usertype, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Semester(models.Model):
    semester = models.CharField(max_length=40)

    def __str__(self):
        return self.semester


class Program(models.Model):
    program_name = models.CharField(max_length=20)
    semester = models.ManyToManyField(Semester)

    def __str__(self):
        return self.program_name


class Course(models.Model):
    program_name = models.OneToOneField(Program, on_delete=models.CASCADE)
    semester = models.OneToOneField(Semester, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    credit_hrs = models.IntegerField()

    def __str__(self):
        return self.course_name


class Note(models.Model):
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='notes', blank=True)
    # course_code = models.OneToOneField(Course, on_delete=models.CASCADE)
    added_by = models.CharField(max_length=50, null=True)
    date_of_added = models.DateField(auto_now=models.DateField())
    date_of_modified = models.DateField(auto_now=models.DateField())

    def __str__(self):
        return self.name
#
## class Syalabus(models.Model):
#     program_name = models.OneToOneField(Program, on_delete=models.CASCADE)
#     semester = models.OneToOneField(Semester, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     course_code = models.OneToOneField(Course, on_delete=models.CASCADE)
#     added_by = models.CharField(max_length=50, null=True)
#     date_of_added = models.DateField(auto_now=models.DateField())
#     date_of_modified = models.DateField(auto_now=models.DateField())
#
#     def __str__(self):
#         return self.name
#
#
# class OldQuestionPaper(models.Model):
#     program_name = models.OneToOneField(Program, on_delete=models.CASCADE)
#     semester = models.OneToOneField(Semester, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     course_code = models.OneToOneField(Course, on_delete=models.CASCADE)
#     added_by = models.CharField(max_length=50, null=True)
#     date_of_added = models.DateField(auto_now=models.DateField())
#     date_of_modified = models.DateField(auto_now=models.DateField())
#
#     def __str__(self):
#         return self.name
