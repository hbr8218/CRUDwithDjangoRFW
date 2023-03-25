from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    highlighted = models.TextField()
    taskName = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=500)
    dueDate = models.DateTimeField(null=False, blank=False)
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    )
    status = models.CharField(max_length=9, choices=STATUS_CHOICES)

    