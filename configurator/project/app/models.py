from django.db import models

EXIT_VALUE_HANDLER_CHOICES = [
    # first is the one we store
    # second is the one we save
    ("logging", "logging"),
]

STDERR_HANDLER_CHOICES = [
    ("pythonTraceback", "python traceback"),
    ("logging", "logging"),
]

# Create your models here.
class Process(models.Model):
    title = models.CharField(max_length=256)
    abstract_description  = models.TextField(blank=True)
    image_id = models.CharField(max_length=256)
    working_dir = models.CharField(max_length=1024)
    command_to_execute = models.CharField(max_length=1024)
    exit_value_handler = models.CharField(max_length=64, choices=EXIT_VALUE_HANDLER_CHOICES)
    stderr_handler = models.CharField(max_length=64, choices=STDERR_HANDLER_CHOICES)

    class Meta:
        verbose_name_plural =  "Processes"
        ordering = ["title"]

    def __str__(self):
        return self.title

INPUT_USE_AS_CHOICES = [
    ("commandLineArgument", "command line argument"),
    ("file", "file"),
]

INPUT_TYPE_CHOICES = [
    ("bbox", "bounding box"),
    ("double", "double"),
    ("string", "string"),
    ("quakeml", "quakeml"),
    ("xml", "xml"),
    ("json", "json"),
    ("geotiff", "geotiff"),
    ("geojson", "geojson"),
]

class ProcessInput(models.Model):
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    abstract_description = models.TextField(blank=True)
    use_as = models.CharField(max_length=64, choices=INPUT_USE_AS_CHOICES)
    input_type = models.CharField(max_length=64, choices=INPUT_TYPE_CHOICES)
    schema = models.CharField(max_length=1024, null=True, blank=True)
    command_line_flag = models.CharField(max_length=256, null=True, blank=True)
    path = models.CharField(max_length=1024, null=True, blank=True)
    default_value = models.CharField(max_length=256, null=True, blank=True)
    allowed_values = models.CharField(max_length=1024, null=True, blank=True)
    crs = models.CharField(max_length=1024, null=True, blank=True)
    sort_order = models.IntegerField()

    class Meta:
        ordering = ["process", "sort_order"]

    def __str__(self):
        return self.title

OUTPUT_READ_FROM_CHOICES = [
    ("file", "file"),
    ("stdout", "stdout"),
]
OUTPUT_TYPE_CHOICES = [
    ("quakeml", "quakeml"),
    ("json", "json"),
    ("shapefile", "shapefile"),
]

class ProcessOutput(models.Model):
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    abstract_description = models.TextField(blank=True)
    read_from = models.CharField(max_length=64, choices=OUTPUT_READ_FROM_CHOICES)
    path = models.CharField(max_length=1024, null=True, blank=True)
    output_type = models.CharField(max_length=64, choices=OUTPUT_TYPE_CHOICES)
    schema = models.CharField(max_length=1024, null=True, blank=True)
    sort_order = models.IntegerField()

    class Meta:
        ordering = ["process", "sort_order"]

    def __str__(self):
        return self.title
