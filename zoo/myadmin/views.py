from django.shortcuts import render

def show_admin_main_page(request):
    return render(request, "myadmin/main_page.html")
