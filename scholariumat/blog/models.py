from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from django_extension.db.models import TimeStampedModel, TitleDescriptionModel

from products.models import ProductBase
from blog.utils import markdown_to_html


class Article(ProductBase):
    text = models.TextField()
    text_hidden = models.TextField(blank=True)
    text_2 = models.TextField(blank=True)
    references = models.TextField(blank=True)
    date_publish = models.DateField(null=True, blank=True)
    priority = models.PositiveSmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog', [self.slug])

    class Meta:
        verbose_name_plural = "Artikel"
        verbose_name = "Artikel"
        ordering = ['-date_publish']


class MarkdownArticle(ProductBase):
    text = models.TextField()
    priority = models.PositiveSmallIntegerField(default=0)
    article = models.OneToOneField(Article, on_delete=models.SET_NULL, null=True, blank=True)

    def create_article(self):
        text, text_hidden, text_2, references = markdown_to_html(self.text)
        if self.article:
            art = self.article
            art.name = self.name
            art.slug = self.slug
            art.text = text
            art.text_hidden = text_hidden
            art.text_2 = text_2
            art.references = references
            art.priority = self.priority
        elif Article.objects.filter(slug=self.slug).exists():
            raise ValidationError('Artikel-slug existiert bereits.')
        else:
            art = Article.objects.create(slug=self.slug, name=self.name, text=text,
                                         text_hidden=text_hidden, text_2=text_2,
                                         references=references, priority=self.priority)
            self.article = art
        art.save()
        print('%s erfolgreich gespeichert.' % self.name)

    def save(self, *args, **kwargs):
        self.create_article()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Markdown Artikel"
        verbose_name = "Markdown Artikel"
