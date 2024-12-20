from django.db import models

class Admin(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    date_of_enrollment = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use hashing in practice
    hiring_date = models.DateField()
    expertise = models.TextField()  # Store tags as comma-separated values

    def __str__(self):
        return self.name        


class Semester(models.Model):
    type = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    fees_per_credit_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type} {self.year}"
    

class Course(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    credit_hr = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=20)
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course.name} - {self.semester.type} {self.semester.year} - {self.instructor.name}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} enrolled in {self.course_class.course.name}"


class GradeStudent(models.Model):
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    max_marks = models.IntegerField()
    marks_obtained = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.test_name}"
