from django.db import models
from django.contrib.auth import get_user_model


class Todo(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="todos", on_delete=models.CASCADE)
    task = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.task
