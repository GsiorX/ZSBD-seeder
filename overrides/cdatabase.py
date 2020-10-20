from sqlfaker.database import Database
from sqlfaker.functions import check_type
from overrides.ctable import CTable


class CDatabase(Database):
    def add_table(self, table_name, n_rows):
        # raise error if types do not match
        check_type(n_rows, int)
        check_type(table_name, str)
        if n_rows < 1:
            raise ValueError("n_rows must be at least 1 but was {}".format(
                str(n_rows)
            ))

        self.tables[table_name] = CTable(
            table_name=table_name,
            db_object=self,
            n_rows=n_rows
        )
