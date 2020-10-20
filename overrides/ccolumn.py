from faker import Faker
from sqlfaker.column import Column
from sqlfaker.functions import check_type


class CColumn(Column):
    def __init__(self, column_name, n_rows, table_objet, data_target="name", data_type="int", ai=False, not_null=False,
                 **kwargs):

        # Check type of input data
        super().__init__(column_name, n_rows, table_objet, data_target, data_type, ai, not_null)
        check_type(column_name, str)
        check_type(data_target, str)
        check_type(data_type, str)
        check_type(ai, bool)
        check_type(not_null, bool)

        # store all parameters
        self._column_name = column_name
        self._data_type = data_type
        self._ai = ai
        self._not_null = not_null
        self._n_rows = n_rows
        self._data_target = data_target
        self._kwargs = kwargs

        # store own table object
        self._table_object = table_objet

        # store data
        self.data = []

    def generate_data(self, recursive, lang):

        if self._ai:
            # generate incrementing values from 1 to n
            self.data = list(range(1, self._n_rows + 1))

        else:
            # generate data using faker
            self.data = get_fake_data(
                data_target=self._data_target,
                n_rows=self._n_rows,
                lang=lang
            )


def get_fake_data(data_target, n_rows=100, lang="en_EN", **kwargs):
    data_faker = Faker(lang)

    if len(kwargs):
        generator_function = getattr(data_faker, data_target)(**kwargs)
    elif data_target == "":
        generator_function = ""
    else:
        generator_function = getattr(data_faker, data_target)
    return_list = []

    for _ in range(n_rows):
        if data_target == "":
            return_list.append("")
        elif data_target == "simple_profile":
            return_list.append(generator_function()["username"])
        else:
            return_list.append(generator_function())
    return return_list
