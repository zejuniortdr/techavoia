from apps.clients.aistudio import AIStudioClient
from apps.debug.services import log
from celery_worker import app
from django.db.models import Q

from .models import Article


@app.task(ignore_result=True)
def create_content(article_id):
    article = Article.objects.get(id=article_id)
    if article.text or article.summary:
        return

    try:
        ai_studio_client = AIStudioClient()
        article.text = ai_studio_client.create_content(article.title)
        article.summary = ai_studio_client.create_content(
            f"Gere um resumo de uma linha para o texto: {article.text}"
        )
        if article.text and article.summary:
            article.public = True

    except Exception as exc:
        log(f"Exception for article {article_id}: {exc}")
        article.public = False

    article.update_content()


@app.task(ignore_result=True)
def get_related(article_id):
    article = Article.objects.get(id=article_id)
    documents = list(
        Article.objects.values("id", "title", "summary").exclude(
            Q(id=article_id)
            | Q(title__isnull=True)
            | Q(slug__isnull=True)
            | Q(summary__isnull=True)
            | Q(public=False)
        )
    )

    ai_studio_client = AIStudioClient()
    related_ids = ai_studio_client.search_related(article.title, documents)
    article.related.add(*related_ids)
