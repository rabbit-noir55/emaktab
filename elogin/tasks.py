import requests
from django.contrib.auth import get_user_model
from celery import shared_task

# Login qilish uchun saytning to‘g‘ri URL manzilini kiriting
LOGIN_URL = "https://login.emaktab.uz/login"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

@shared_task
def auto_login_users():
    User = get_user_model()
    users = User.objects.values_list("login", "password", named=True)  # Faqat kerakli ustunlarni olish
    
    for user in users:
        response = requests.post(LOGIN_URL, data={"login": user.login, "password": user.password}, headers=HEADERS)
        
        if "userfeed" in response.url:
            print(f"✅ {user.login} uchun muvaffaqiyatli login qilindi!")
        else:
            print(f"❌ {user.login} uchun login amalga oshmadi!")
from celery import shared_task

@shared_task
def test_task():
    return "Celery ishlayapti!"
