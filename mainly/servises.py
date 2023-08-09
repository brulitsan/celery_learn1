from django.core.mail import send_mail


def send(user_mail):
    send_mail(
        'вы подписались на рассылку',
        "мы будем присылать вам много спама",
        'matveytulaevm.ama@gmail.com',
        [user_mail],
        fail_silently=False,
    )