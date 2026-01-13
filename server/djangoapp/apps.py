from django.apps import AppConfig


class DjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoapp'
    
    def ready(self):
        """Initialize sample data when Django starts"""
        from .restapis import init_sample_data
        init_sample_data()
