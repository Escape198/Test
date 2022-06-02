from django.shortcuts import render


def admin_start(request):
    return render(request, 'my_admin/start_admin.html')
