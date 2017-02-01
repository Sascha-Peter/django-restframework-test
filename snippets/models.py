"""Define models for the snippet app."""
from django.db import models
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [lexer for lexer in get_all_lexers() if lexer[1]]
LANGUAGE_CHOICES = sorted([(lexer[1][0], lexer[0]) for lexer in LEXERS])
STYLE_CHOICES = sorted((style, style) for style in get_all_styles())


class Snippet(models.Model):
    """Define model for snippets."""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        default='python',
        max_length=100
    )
    style = models.CharField(
        choices=STYLE_CHOICES,
        default='friendly',
        max_length=100
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='snippets',
        on_delete=models.CASCADE
    )
    highlighted = models.TextField()

    class Meta:
        """Define meta information for model."""

        ordering = ('created',)

    def save(self, *args, **kwargs):
        """Custom save method to make use of the pygments library.

        Creates a highlighted HTML representation of the code snippet after
        saving.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
