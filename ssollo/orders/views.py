from datetime import datetime, timedelta

from feedback_and_comments.models import FeedBackAndComment
import feedback_and_comments
from orders.forms import OrderForm, Order_update_Form
from orders.models import Contract, Message

from django.shortcuts import redirect, render
from django.db.models import Sum
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView


class Show_orders_list(ListView):
    model = Contract
    template_name = 'orders/admin_orders.html'
    context_object_name = 'orderget'
    queryset = Contract.objects.filter(DateDel = None)
    paginate_by = 4


class Show_order(DetailView):
    model = Contract
    template_name = 'orders/admin_info_order.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        contr = Contract.objects.get(pk=self.kwargs['pk'])
        costcontract = contr.Cost
        ctx = super(Show_order, self).get_context_data(**kwargs)
        return ctx

    def post(self, request, pk):
        if ( request.POST.get('Message') == None):
            cl = FeedBackAndComment()
            cl= FeedBackAndComment.add_comment(pk, request.POST.get('Message_com'))
            # return redirect('admin_order', pk )
        else:
            contract = Contract()
            mes = Message()
            mes= Message.add_message(pk, request.POST.get('Message'))
            # return redirect('admin_order', pk )
        if (request.POST.get('End') != None):
            end = Contract()
            end = Contract.end_order(pk)
        if (request.POST.get('Cancel') != None):
            can = Contract()
            can = Contract.cancel_order(pk)

        return redirect('admin_order', pk )


class Add_order(CreateView):
    form_class = OrderForm
    template_name = 'orders/admin_add_order.html'
    extra_context = {"maxdate": datetime.today() + timedelta(days = 60)}

    def post(self, request):
        form = OrderForm(request.POST)
        if (form.is_valid()):
            cl = Contract()
            cl= Contract.add_order(cl, request)
        return redirect('admin_orders')


class Add_order_client(CreateView):
    template_name = 'cars/carcard.html'

    def post(self, request ,pk):
        cl = Contract()
        cl= Contract.add_order_client(cl, request, pk)
        return redirect('index')


class Update_order(UpdateView):
    model = Contract
    form_class = Order_update_Form
    template_name = 'orders/admin_update_order.html'
    context_object_name = 'order'
    extra_context = {"maxdate": datetime.today() + timedelta(days = 60)}

    def post(self, request, pk):
        form = Order_update_Form(request.POST)
        cl = Contract()
        print(form)
        if (form.is_valid()):
            cl= Contract.update_order(cl, request, pk)
        return redirect('admin_order', pk)

    def get_context_data(self, **kwargs):
        contr = Contract.objects.get(pk=self.kwargs['pk'])
        costcontract = contr.Cost
        ctx = super(Update_order, self).get_context_data(**kwargs)
        return ctx


class Show_messages_list(ListView):
    model = Contract
    template_name = 'orders/admin_messages.html'
    context_object_name = 'orderget'
    queryset = Contract.objects.filter(DateDel = None)
    paginate_by = 5


class Delete_comment(DeleteView):
    model = Contract
    template_name = 'orders/admin_info_order.html'

    def post(self, request, order_id, pk):
        com = FeedBackAndComment.delete_comment(pk)
        return redirect('admin_order', order_id)
