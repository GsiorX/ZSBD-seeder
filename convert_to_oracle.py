import requests


def convert(filename):
    with open(filename, 'r') as rsql:
        converted_sql = "SET DEFINE OFF;{0}".format(chr(10))
        sql_file = rsql.read().replace("Lao People's Democratic Republic", "Lao People''s Democratic Republic").replace(
            "Cote d'Ivoire", "Cote d''Ivoire").split("INSERT INTO")
        i = 0

        for sql in sql_file:
            if i != 0:
                sql = "INSERT INTO {0}".format(sql)

                if i == 1:
                    sql = "ALTER TABLE C##ZSBD.Translation{0}" \
                          "{1}ADD(FOREIGN KEY (RentRentId) REFERENCES Rent(RentId){0});{0}{0}" \
                          "ALTER USER C##ZSBD quota unlimited on USERS;{0}{0}{2}".format(chr(10), chr(9), sql)

            r = requests.post("http://www.sqlines.com/sqlines_run.php",
                              {"source": sql, "source_type": "MySQL", "target_type": "Oracle"})
            converted_sql += r.text
            i += 1

        # ???
        converted_sql = converted_sql.replace("__SQLINES_MULTI_PART__", "").replace("ROWNUM10", "NUMBER(10")

        with open("converted.sql", "w", encoding="utf-8") as wsql:
            wsql.write(converted_sql)
        wsql.close()
    rsql.close()
