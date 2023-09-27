import uuid

from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email addres"), unique=True)
    avatar = models.FileField(
        _('Avatar'),
        default=None,
        null=True,
        blank=True,
        upload_to='avatars/'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('users/photo_2023-09-26_22-16-42.jpg')


    def save(self, *args, **kwargs):
        if not self.pk and not self.username:
            self.username = str(uuid.uuid4())

        super().save(*args, **kwargs)
