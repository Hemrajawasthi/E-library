from django.db import models


# Create your models here.


# class Usertype(models.Model):
#     type = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.type


# class User(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)

    # type = models.OneToOneField(Usertype, on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return self.username


class Semester(models.Model):
    semester = models.CharField(max_length=40)

    def __str__(self):
        return self.semester


class Program(models.Model):
    program_name = models.CharField(max_length=20)
    semester = models.ManyToManyField(Semester)

    def __str__(self):
        return self.program_name


class Subject(models.Model):
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class Note(models.Model):
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjec', default='null')
    file = models.FileField(upload_to='notes', blank=True)
    added_by = models.CharField(max_length=50, null=True)
    date_of_added = models.DateField(auto_now=models.DateField())
    date_of_modified = models.DateField(auto_now=models.DateField())

    def __str__(self):
        return self.added_by


class Syllabus(models.Model):
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects')
    # subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_codes')
    subject_code = models.CharField(max_length=10)
    credit_hrs = models.IntegerField()
    added_by = models.CharField(max_length=50, null=True)
    date_of_added = models.DateField(auto_now=models.DateField())
    date_of_modified = models.DateField(auto_now=models.DateField())

    def __str__(self):
        return str(self.program_name) + " " + str(self.semester)


class OldQuestionPaper(models.Model):
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='sem')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub')
    file = models.FileField(upload_to='oldpaper', blank=True)
    added_by = models.CharField(max_length=50, null=True)
    date_of_added = models.DateField(auto_now=models.DateField())
    date_of_modified = models.DateField(auto_now=models.DateField())

    def __str__(self):
        return self.added_by
