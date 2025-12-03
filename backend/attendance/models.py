from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SportKind(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Trainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CourseTemplate(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(SportKind, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    timeslot = models.CharField(max_length=10)  # e.g., "18:00-19:00"
    weekday = models.CharField(max_length=10)   # e.g., "Monday"
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.sport.name}) on {self.weekday} at {self.timeslot}"


class TrainerCourse(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    course_template = models.ForeignKey(CourseTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trainer} assigned to {self.course_template}"


class DateDimension(models.Model):
    full_date = models.DateField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    calendar_week = models.IntegerField()
    weekday_name = models.CharField(max_length=10)
    is_holiday = models.BooleanField(default=False)
    is_weekend = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_date)


class CourseEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.ForeignKey(DateDimension, on_delete=models.PROTECT)
    sport = models.ForeignKey(SportKind, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    timeslot = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} on {self.date.full_date} at {self.timeslot}"


class Attendance(models.Model):
    event = models.ForeignKey(CourseEvent, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sick = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.event} ({'Sick' if self.sick else 'Present'})"


class EnrolledSportType(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sport = models.ForeignKey(SportKind, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} enrolled in {self.sport}"


class EnrolledCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    template = models.ForeignKey(CourseTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} enrolled in {self.template}"
