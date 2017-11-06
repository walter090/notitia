from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from login.models import User


class Post(models.Model):
    # Use default id as primary key
    created_by = models.ForeignKey(User,
                                   null=True)
    publish_time = models.DateTimeField(_('publish time'),
                                        default=timezone.now)
    last_modified_time = models.DateTimeField(_('last modified time'),
                                              null=True)
    title = models.CharField(_('title'), max_length=200, blank=False)
    subtitle = models.CharField(_('subtitle'), max_length=400, blank=True)
    content_body = models.TextField(_('content'), blank=False, null=False)

    def __str__(self):
        return self.title

    def make_new_post(self, request, title, content_body):
        self.created_by = request.user
        self.title = title
        self.content_body = content_body

    def modify_post(self):
        self.last_modified_time = timezone.now()

    def clean(self):
        if self.title.isspace() or self.content_body.isspace():
            raise ValidationError
        super(Post, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Post, self).save(*args, **kwargs)
