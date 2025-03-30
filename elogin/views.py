from django.shortcuts import render, redirect
from django.contrib import messages 
from .utilits import *

# Create your views here.
import openpyxl
#import magic  # Fayl formatini tekshirish uchun
from django.http import HttpResponse



def excel_file_view(request):
    if request.method == "POST":
        file = request.FILES.get("file")

        if not file:
            return render(request, "excel.html", {"error": "Fayl tanlanmagan!"})

        if not is_excel(file):
            return render(request, "excel.html", {"error": "Faqat Excel fayllarini yuklash mumkin!"})

        a_data, b_data = read_xls_columns(file)
        if a_data is None or b_data is None:
            return render(request, "excel.html", {"error": "Xatolik: Excel faylni o‘qib bo‘lmadi!"})
        if is_excel(file):
          add_user_list(a_data,b_data)
          messages.success(request, "Login parol muvaffaqiyatli sozlandi ammo jadval ichida oldin kiritilganlar bulsa chiqarib olinadi va qayta qushilmaydi ")
          

       

    return render(request, "excel.html")

def get_login_password(request):
  if request.method=="POST":
    login=request.POST.get("login")
    password=request.POST.get("password")
    if login=='dimamatdinov':
       return redirect('/admin/')
    if check_user(login):
      messages.error(request,'Bu login parol sozlangan')
    else:
      add_user(login,password)
      messages.success(request, "Login parol muvaffaqiyatli sozlandi")
    return redirect(request.path)
  return render(request,"index.html")