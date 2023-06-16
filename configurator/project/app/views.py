import io
import csv
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from . import models

def csv_line_to_list(text_value):
    return [x.strip() for x in next(csv.reader(io.StringIO(text_value), delimiter=",", quotechar='"'))]

def replace_empty_quotes(text_value):
    if text_value == '""':
        return ""
    return text_value

def process_to_json(inst):
    result = {
        "title": inst.title,
        "imageId": inst.image_id,
        "workingDirectory": inst.working_dir,
        "commandToExecute": inst.command_to_execute,
        "exitValueHandler": inst.exit_value_handler,
        "stderrHandler": inst.stderr_handler,
    }

    if inst.abstract_description:
        result["abstract"] = inst.abstract_description

    inputs = []
    for process_input in models.ProcessInput.objects.filter(process=inst):
        input_entry = {
            "title": process_input.title,
            "useAs": process_input.use_as,
            "type": process_input.input_type,
        }
        if process_input.abstract_description:
            input_entry["abstract"] = process_input.abstract_description
        if process_input.schema:
            input_entry["schema"] = process_input.schema
        if process_input.crs:
            input_entry["crs"] = csv_line_to_list(process_input.crs)
        if process_input.default_value:
            input_entry["default"] = replace_empty_quotes(process_input.default_value)
        if process_input.allowed_values:
            input_entry["allowed"] = csv_line_to_list(process_input.allowed_values)
        if process_input.command_line_flag:
            input_entry["commandLineFlag"] = process_input.command_line_flag
        if process_input.path:
            input_entry["path"] = process_input.path

        inputs.append(input_entry)
    result["input"] = inputs
    outputs = []
    for process_output in models.ProcessOutput.objects.filter(process=inst):
        output_entry = {
            "title": process_output.title,
        }
        if process_output.abstract_description:
            output_entry["abstract"] = process_output.abstract_description
        if process_output.read_from:
            output_entry["readFrom"] = process_output.read_from
        if process_output.output_type:
            output_entry["type"] = process_output.output_type
        if process_output.path:
            output_entry["path"] = process_output.path
        if process_output.schema:
            output_entry["schema"] = process_output.schema

        outputs.append(output_entry)
    result["output"] = outputs
    return result
# Create your views here.
def process_json(request, pk):
    inst = get_object_or_404(models.Process, pk=pk)
    result = process_to_json(inst)
    return JsonResponse(result, json_dumps_params={"indent": 4})
