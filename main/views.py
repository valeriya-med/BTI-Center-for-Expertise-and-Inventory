from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .models import ContactMessage


def index(request):
    return render(request, 'index.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_text = request.POST.get('message')

        ContactMessage.objects.create(
            form_type='consultation',
            name=name,
            email=email,
            phone=phone,
            message=message_text
        )

        email_message = EmailMessage(
            subject=f"Нова заявка з консультації від {name}",
            body=f"Ім'я: {name}\nEmail: {email}\nТелефон: {phone}\nПовідомлення:\n{message_text}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_RECEIVER_EMAIL],
        )
        email_message.send(fail_silently=False)

        return JsonResponse({
            'status': 'ok',
            'message': 'Дякуємо! Ваша форма успішно відправлена.'
        })
    return JsonResponse({
        'status': 'error',
        'message': 'Сталася помилка. Спробуйте ще раз.'
    }, status=400)



def submit_modal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # Зберігаємо у базі
        ContactMessage.objects.create(
            form_type='modal',
            name=name,
            phone=phone
        )

        # Відправка листа адміністратору
        email_message = EmailMessage(
            subject=f"Нова заявка з модальної форми від {name}",
            body=f"Ім'я: {name}\nТелефон: {phone}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_RECEIVER_EMAIL],
        )
        email_message.send(fail_silently=False)

        # Повертаємо красиве повідомлення для користувача
        return JsonResponse({
            'status': 'ok',
            'message': 'Дякуємо! Ваша заявка успішно надіслана. Ми з вами зв’яжемося найближчим часом.'
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Сталася помилка. Будь ласка, спробуйте ще раз.'
    }, status=400)
