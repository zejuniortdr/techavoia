from apps.debug.services import log
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64, unique=True, null=True)
    summary = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    public = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    related = models.ManyToManyField("self", null=True, blank=True)
    ranking = models.IntegerField(default=0)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        need_content = False
        self.ranking = self.likes - self.dislikes
        if not self.pk:
            need_content = True
            self.slug = slugify(self.title)
            duplicated_slug = Article.objects.filter(slug=self.slug)
            count = duplicated_slug.count()

            if count:
                self.slug = f"{self.slug}-{count + 1}"

            from .tasks import create_content, get_related

        super().save(*args, **kwargs)

        if need_content:
            create_content.delay(self.pk)
            get_related.delay(self.pk)

    def update_content(self, *args, **kwargs):
        log("16 update content")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})
