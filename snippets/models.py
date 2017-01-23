"""Define models for the snippet app."""
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

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

    class Meta:
        """Define meta information for model."""

        ordering = ('created',)
