import datetime
import json
import re

from typing import List, Union


class FilterBuilder:
    def __init__(self):
        self.filters = []

    def _add_value_filter(self, allowed_types, operator, field, value, allow_list):
        self._verify_field_is_string(field)

        type_check_value = value
        if isinstance(value, list) and allow_list:
            self._verify_list_of_single_type(value, allowed_types)
            type_check_value = value[0]

        if not isinstance(type_check_value, allowed_types):
            raise TypeError(f'value must be a {allowed_types}')

        if isinstance(value, list):
            value = [v.isoformat() if isinstance(v, datetime.datetime) else v for v in value]
        elif isinstance(value, datetime.datetime):
            value = value.isoformat()
        else:
            value = self._toJson(value)

        # python surrounds datetime values in a list with single quotes
        if isinstance(type_check_value, datetime.datetime):
            value = re.sub("'", '', f'{value}')

        constructed_filter = re.sub(r'\s', '', f'{operator}({field},{value})')
        self.filters.append(constructed_filter)

    def equals(self, field: str, value: Union[list, bool, int, float, str, datetime.datetime]):
        types = (bool, int, float, str, datetime.datetime)
        self._add_value_filter(types, 'equals', field, value, allow_list=True)

    def less_than(self, field: str, value: Union[int, float, datetime.datetime]):
        types = (int, float, datetime.datetime)
        self._add_value_filter(types, 'less-than', field, value, allow_list=False)

    def less_or_equal(self, field: str, value: Union[int, float, datetime.datetime]):
        types = (int, float, datetime.datetime)
        self._add_value_filter(types, 'less-or-equal', field, value, allow_list=False)

    def greater_than(self, field: str, value: Union[int, float, datetime.datetime]):
        types = (int, float, datetime.datetime)
        self._add_value_filter(types, 'greater-than', field, value, allow_list=False)

    def greater_or_equal(self, field: str, value: Union[int, float, datetime.datetime]):
        types = (int, float, datetime.datetime)
        self._add_value_filter(types, 'greater-or-equal', field, value, allow_list=False)

    def contains(self, field: str, value: Union[str, list]):
        types = (str,)
        self._add_value_filter(types, 'contains', field, value, allow_list=True)

    def contains_any(self, field: str, value: Union[str, list]):
        types = (str,)
        self._add_value_filter(types, 'contains-any', field, value, allow_list=True)

    def contains_all(self, field: str, value: Union[str, list]):
        types = (str,)
        self._add_value_filter(types, 'contains-all', field, value, allow_list=True)

    def ends_with(self, field: str, value: str):
        types = (str,)
        self._add_value_filter(types, 'ends-with', field, value, allow_list=False)

    def starts_with(self, field: str, value: str):
        types = (str,)
        self._add_value_filter(types, 'starts-with', field, value, allow_list=False)

    def any(self, field: str, value: List[Union[str, bool, int, float, datetime.datetime]]):
        if type(value) is not list:
            raise TypeError('value must be a list')
        types =(bool, int, float, str, datetime.datetime)
        self._add_value_filter(types, 'any', field, value, allow_list=True)

    def has(self, field: str):
        self._verify_field_is_string(field)
        self.filters.append(f'has({field})')

    def _verify_field_is_string(self, field):
        if not isinstance(field, str):
            raise TypeError('field must be a string')

    def _verify_list_of_single_type(self, value, allowed_types):
        if not value:  # if list is empty, we cannot determine the type
            raise ValueError('value cannot be an empty list')

        first_type = type(value[0])

        if first_type not in allowed_types:
            raise TypeError(f'Items in list must be one of the following types: {allowed_types}')

        if not all(isinstance(v, first_type) for v in value):
            raise TypeError('All items in value must be of the same type')

    def _toJson(self, value):
        return json.dumps(value, separators=(',', ':'))

    def build(self):
        return ','.join(self.filters)
