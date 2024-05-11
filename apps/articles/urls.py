from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDetailJSONView,
    ArticleDetailView,
    ArticleDislikeJSONView,
    ArticleLikeJSONView,
    ArticleListView,
)

app_name = "myapp"


urlpatterns = [
    path("", ArticleListView.as_view(), name="index"),
    path("novo/", ArticleCreateView.as_view(), name="new"),
    path("<slug:slug>", ArticleDetailView.as_view(), name="detail"),
    path("<slug:slug>/json/", ArticleDetailJSONView.as_view(), name="json"),
    path("<slug:slug>/like/", ArticleLikeJSONView.as_view(), name="like"),
    path("<slug:slug>/dislike/", ArticleDislikeJSONView.as_view(), name="dislike"),
]
