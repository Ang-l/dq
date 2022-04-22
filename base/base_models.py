
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('created'), auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(_('modified'), auto_now=True)
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        abstract = True
