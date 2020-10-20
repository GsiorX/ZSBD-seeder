from sqlfaker.table import Table

from overrides.ccolumn import CColumn


class CTable(Table):
    def add_column_custom(self, column_name, data_target="name", data_type="int", not_null=False, **kwargs):
        self.columns[column_name] = CColumn(
            # add column properties
            column_name=column_name,
            data_type=data_type,
            ai=False,
            not_null=not_null,
            data_target=data_target,
            kwargs=kwargs,

            # auto add table properties
            n_rows=self._n_rows,
            table_objet=self
        )
