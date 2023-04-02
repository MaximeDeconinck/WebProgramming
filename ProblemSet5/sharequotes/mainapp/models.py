from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quote(models.Model):
    content = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} - {self.person}"