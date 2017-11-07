from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from login.models import User


class Post(models.Model):
    # Use default id as primary key
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User,
                                   null=True)
    publish_time = models.DateTimeField(_('publish time'),
                                        default=timezone.now)
    last_modified_time = models.DateTimeField(_('last modified time'),
                                              null=True,
                                              blank=True)
    title = models.TextField(_('title'), blank=False)
    slug = models.SlugField(_('slug'), unique=True, null=True, blank=True)
    subtitle = models.TextField(_('subtitle'), blank=True)
    tldr = models.TextField(_('tl;dr'), blank=True)
    content_body = models.TextField(_('content'), blank=False, null=False)

    def __str__(self):
        return self.title

    def make_new_post(self, request, title, content_body):
        self.created_by = request.user
        self.title = title.strip()  # Remove leading and trailing spaces
        self.content_body = content_body
        self.last_modified_time = self.publish_time

    def modify_post(self):
        self.last_modified_time = timezone.now()

    def clean(self):
        if self.title.isspace() or self.content_body.isspace():
            raise ValidationError(message='Title and content cannot be empty')
        super(Post, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Post, self).save(*args, **kwargs)
        self.slug = '{0}/{1}'.format(self.id, slugify(self.title))
        super(Post, self).save(*args, **kwargs)
