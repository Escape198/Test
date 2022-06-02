from feedback_and_comments.models import FeedBackAndComment
from cars.models import Category

from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView


def index(request):
    catalogget = Category.objects.all()

    context = {
        'catalogget': catalogget,
    }
    return render(request, 'main/index.html', context=context)
def contact(request):
    return render(request, 'main/contact.html')
def Rentcondition(request):
    return render(request, 'main/Rentcondition.html')


class Add_feedback(CreateView):

    def post(self, request):
        cl = FeedBackAndComment()
        cl= FeedBackAndComment.add_feedback(cl, request)
        return redirect('index')
