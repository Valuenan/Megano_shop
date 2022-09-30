from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_users'
    verbose_name = _('users')

