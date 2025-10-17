from django.db import models

class ContactMessage(models.Model):
    FORM_TYPE_CHOICES = [
        ('consultation', 'Consultation'),
        ('modal', 'Modal'),
    ]

    form_type = models.CharField(max_length=20, choices=FORM_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.form_type})"