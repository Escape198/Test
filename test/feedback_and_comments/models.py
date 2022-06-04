from django.db import models
from django.db.models.fields import DateField
from django.contrib import messages

from user_and_company.models import Person

from datetime import date
#import datetime


class FeedBackAndComment(models.Model):
    User=models.ForeignKey('user_and_company.Person', verbose_name='Admin or employee', on_delete=models.PROTECT, blank=True, null=True)
    Contract=models.ForeignKey('orders.Contract', verbose_name='Order', on_delete=models.PROTECT, blank=True, null=True)
    Name=models.CharField('Name', max_length=50, default='')
    Message = models.TextField('Message', blank=True, null=True)
    Status=models.BooleanField('Feedback message status', blank=True, null=True)
    Type=models.BooleanField('Message type', blank=True, null=True)
    PhoneEmail=models.CharField('Phone or email', max_length=12, default='')
    DateDel=models.DateField('Delete date', blank=True, null=True)
    Date=models.DateField('Date', blank=True, null=True)

    def __str__(self):
        return self.Type + self.Message

    class Meta:
        verbose_name='Comment or message'
        verbose_name_plural='Comments or messages'
        ordering = ['-id']

    def add_feedback(feedback, request):
        feedback.Name = request.POST.get('Name')
        feedback.PhoneEmail = request.POST.get('PhoneEmail')
        feedback.Message = request.POST.get('Message')
        feedback.Status = 0
        feedback.Type = 0
        feedback.Date = date.today()
        feedback.save()
        return feedback

    def update_feedback(feedback, request, pk):
        feedback = FeedBackAndComment.objects.get(id=pk)
        print(request.POST.get('Status'))
        if (request.POST.get('Status')== 'on'):
            status = 1
        else:
            status = 0
        feedback.Status = status
        feedback.save()
        return feedback

    def delete_feedback(pk):
        feedback = FeedBackAndComment.objects.get(id=pk)
        feedback.DateDel = date.today()
        feedback.save()
        return True

    def add_comment(id ,comment):
        person_from = 7
        comment = FeedBackAndComment.objects.create(Contract_id=id,Date = datetime.datetime.now(), Message = comment , User_id = person_from, Status = 0, Type = 1)
        comment.save()
        return comment

    def delete_comment(comment):
        k = FeedBackAndComment.objects.filter(id = comment)
        k.delete()
        return True
