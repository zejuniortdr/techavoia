from typing import Any

from django.db.models import F
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.defaultfilters import linebreaksbr
from django.views.generic import DetailView, ListView, View
from markdownify.templatetags.markdownify import markdownify

from .models import Article


class ArticleCreateView(View):
    def post(self, *args, **kwargs):
        payload = self.request.POST
        article = Article.objects.create(title=payload.get("title"))
        return redirect(article.get_absolute_url())


class ArticleDetailJSONView(View):
    def get(self, *args, **kwargs):
        article = get_object_or_404(Article, slug=kwargs["slug"])
        return JsonResponse(
            {
                "title": article.title,
                "text": linebreaksbr(markdownify(article.text)),
                "summary": article.summary,
            }
        )


class ArticleLikeJSONView(View):
    def get(self, *args, **kwargs):
        article = get_object_or_404(Article, slug=kwargs["slug"])
        article.likes += 1
        article.save(update_fields=["likes"])
        return JsonResponse(
            {
                "slug": article.slug,
                "likes": article.likes,
            }
        )


class ArticleDislikeJSONView(View):
    def get(self, *args, **kwargs):
        article = get_object_or_404(Article, slug=kwargs["slug"])
        article.dislikes += 1
        article.save(update_fields=["dislikes"])
        return JsonResponse(
            {
                "slug": article.slug,
                "dislikes": article.dislikes,
            }
        )


class ArticleListView(ListView):
    model = Article
    template_name = "index.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(public=True).order_by(
            "-date_added", "-ranking", "-views"
        )


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        obj = super().get_object(queryset=queryset)
        queryset.filter(pk=obj.pk).update(views=F("views") + 1)
        obj.refresh_from_db()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = self.object.related.filter(public=True).order_by(
            "-ranking", "-views", "-date_added"
        )
        return context
