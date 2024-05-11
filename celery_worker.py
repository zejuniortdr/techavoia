from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Defina a variável de ambiente padrão do Django para o arquivo de configurações do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('techavoia')

# Usando uma string aqui significa que o trabalhador não precisa serializar
# o objeto de configuração para filas filhas.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carregue módulos de tarefas de todos os aplicativos registrados
app.autodiscover_tasks()
