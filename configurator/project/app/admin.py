import json
import pathlib
from django.contrib import admin, messages
from django.utils.html import format_html
from django.urls import reverse
from django.conf import settings
from . import models
from .views import process_to_json
from .utils import pluralize

class ProcessInputInline(admin.TabularInline):
    model = models.ProcessInput

class ProcessOutputInline(admin.TabularInline):
    model = models.ProcessOutput

def export_json_to_folder(modeladmin, request, queryset):
    export_base_path = pathlib.Path(settings.CONFIGURATION_EXPORT_FOLDER)
    export_base_path.mkdir(parents=True, exist_ok=True)

    export_count = 0
    for inst in queryset:
        result = process_to_json(inst)
        result_name = export_base_path / f"{inst.title}.json"
        if result_name.exists():
            result_name.unlink()

        with result_name.open("wt") as outfile:
            json.dump(result, outfile, indent=4)
        export_count += 1

    messages.add_message(request, messages.INFO, f"{pluralize(export_count, 'file')} exported")


class ProcessAdmin(admin.ModelAdmin):
    inlines = [
        ProcessInputInline,
        ProcessOutputInline,
    ]

    actions = [
        export_json_to_folder,
    ]

    list_display = [
        "title", "image_id", "working_dir", "command_to_execute", "actions_to_trigger"
    ]


    def actions_to_trigger(self, obj):
        url = reverse("process-json", args=(obj.pk,))
        html = f"""
        <a target="_blank" href="{url}">json</a>
        """
        return format_html(html)



admin.site.register(models.Process, ProcessAdmin)
