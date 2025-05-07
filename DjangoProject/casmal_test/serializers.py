# serializers.py
from collections import OrderedDict

from rest_framework import serializers
from .models import Experiment, Dataset
from .utils import camel_to_snake, snake_to_camel

import re
from rest_framework import serializers

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

class CamelCaseModelSerializer(serializers.ModelSerializer):
    """
    自动将字段重命名为 camelCase，并用 `source` 指回原模型字段。
    """
    def get_fields(self):
        original_fields = super().get_fields()
        new_fields = OrderedDict()
        for name, field in original_fields.items():
            camel_name = to_camel_case(name)
            if camel_name != name:
                field.source = name
            new_fields[camel_name] = field
        return new_fields


# class CamelCaseModelSerializer(serializers.ModelSerializer):
#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         return {snake_to_camel(k): v for k, v in ret.items()}
#
#     def to_internal_value(self, data):
#         camel_to_snake_data = {
#             camel_to_snake(k): v for k, v in data.items()
#         }
#         return super().to_internal_value(camel_to_snake_data)


class DatasetSerializer(CamelCaseModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'


class ExperimentSerializer(CamelCaseModelSerializer):
    datasets = DatasetSerializer(many=True)

    class Meta:
        model = Experiment
        fields = '__all__'
