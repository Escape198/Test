from feedback_and_comments.models import FeedBackAndComment

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import redirect, render
from orders.models import Contract, Person


class Show_feedback_list(ListView):
    model = FeedBackAndComment
    template_name = 'feedback_and_comments/admin_feedback.html'
    context_object_name = 'feedbackget'
    paginate_by = 5
    queryset = FeedBackAndComment.objects.filter(DateDel = None, Type = 0).order_by('-Date') ##Type 0 = обратная связь, 1 = комментарий


class Delete_feedback(DeleteView):
    model = FeedBackAndComment
    context_object_name = 'feedback'

    def post(self, request, pk):
        is_delete = FeedBackAndComment.delete_feedback(pk)
        if (is_delete):
            return redirect('admin_feedback')
        return pk


class Update_feedback(UpdateView):
    model = FeedBackAndComment
    template_name = 'feedback_and_comments/admin_feedback.html'
    context_object_name = 'feedback'

    def post(self, request, pk):
        cl = FeedBackAndComment()
        cl= FeedBackAndComment.update_feedback(cl, request, pk)
        return redirect('admin_feedback')
