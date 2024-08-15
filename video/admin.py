from django.contrib import admin
from .models import Video
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class VideoResource(resources.ModelResource):

    class Meta:
        model = Video  # or 'core.Book'
      


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    pass
