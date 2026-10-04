from django.db import models
class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN='open','Open'; IN_PROGRESS='in_progress','In progress'; WAITING='waiting','Waiting'; RESOLVED='resolved','Resolved'
    class Priority(models.TextChoices):
        LOW='low','Low'; MEDIUM='medium','Medium'; HIGH='high','High'; URGENT='urgent','Urgent'
    subject=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    requester_email=models.EmailField()
    assigned_to=models.CharField(max_length=120,blank=True)
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.OPEN,db_index=True)
    priority=models.CharField(max_length=10,choices=Priority.choices,default=Priority.MEDIUM,db_index=True)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self): return f'#{self.pk} {self.subject}'
