from .models import Log

def log(text):
    Log.objects.create(text=text)
