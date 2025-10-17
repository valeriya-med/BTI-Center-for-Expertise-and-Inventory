from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import ContactMessage

def index(request):
    return render(request, 'main/index.html')

def submit_form(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            message_text = request.POST.get('message', '').strip()

            ContactMessage.objects.create(
                form_type='consultation',
                name=name,
                email=email,
                phone=phone,
                message=message_text
            )

            return JsonResponse({'status': 'ok', 'message': 'Дякуємо! Ваша форма успішно відправлена.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Сталася помилка: {str(e)}'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Невірний метод запиту'}, status=400)


def submit_modal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        ContactMessage.objects.create(
            form_type='modal',
            name=name,
            phone=phone
        )

        whatsapp_number = '+380934242711'
        text = f"Нова заявка з сайту:\nІм'я: {name}\nТелефон: {phone}"
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={text.replace(' ', '%20').replace('\n','%0A')}"

        return redirect(whatsapp_url)

    return redirect('/')
