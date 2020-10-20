from sqlfaker.column import Column
from sqlfaker.database import Database
from faker import Faker
from sqlfaker.functions import check_type
from sqlfaker.table import Table
from convert_to_oracle import convert

fake = Faker()


class CTable(Table):
    def add_column_custom(self, column_name, data_target, data_type="int", not_null=False):
        self.columns[column_name] = CColumn(
            # add column properties
            column_name=column_name,
            data_type=data_type,
            ai=False,
            not_null=not_null,
            data_target=data_target,

            # auto add table properties
            n_rows=self._n_rows,
            table_objet=self
        )


# TODO get rid of ifs
def get_fake_data(data_target, n_rows=100, lang="en_EN"):
    return_list = []
    if data_target == "gender":
        for _ in range(n_rows):
            return_list.append(fake.bothify(text="?", letters="MF"))
    elif data_target == "date":
        for _ in range(n_rows):
            return_list.append(fake.date())
    elif data_target == "height":
        for _ in range(n_rows):
            return_list.append(fake.random_int(min=150, max=210))
    elif data_target == "first_name":
        for _ in range(n_rows):
            return_list.append(fake.first_name())
    elif data_target == "last_name":
        for _ in range(n_rows):
            return_list.append(fake.last_name())
    elif data_target == "name":
        for _ in range(n_rows):
            return_list.append(fake.name())
    elif data_target == "words":
        for _ in range(n_rows):
            words = fake.words(nb=3)
            return_list.append(" ".join(words))
    elif data_target == "word":
        for _ in range(n_rows):
            return_list.append(fake.word())
    elif data_target == "number":
        for _ in range(n_rows):
            return_list.append(fake.random_int(min=30, max=360))
    elif data_target == "float":
        for _ in range(n_rows):
            return_list.append(
                fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=200000, max_value=9999999))
    elif data_target == "paragraph":
        for _ in range(n_rows):
            return_list.append(fake.paragraph(nb_sentences=3, variable_nb_sentences=True))
    elif data_target == "promo":
        for _ in range(n_rows):
            return_list.append(
                fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=0, max_value=1))
    elif data_target == "genre":
        for _ in range(n_rows):
            return_list.append(
                fake.word(ext_word_list=["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama",
                                         "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery",
                                         "Romance", "Science Fiction", "Thriller", "War", "Western"]))
    elif data_target == "country":
        for _ in range(n_rows):
            result = fake.country()
            if result == "Lao People's Democratic Republic":
                return_list.append("Lao People''s Democratic Republic")
            elif result == "Cote d'Ivoire":
                return_list.append("Cote d''Ivoire")
            else:
                return_list.append(result)
    elif data_target == "boolean":
        for _ in range(n_rows):
            return_list.append(fake.pyint(min_value=0, max_value=1))
    elif data_target == "rate":
        for _ in range(n_rows):
            return_list.append(fake.pyint(min_value=0, max_value=10))
    elif data_target == "email":
        for _ in range(n_rows):
            return_list.append(fake.ascii_safe_email())
    elif data_target == "login":
        for _ in range(n_rows):
            return_list.append(fake.simple_profile()["username"])
    elif data_target == "password":
        for _ in range(n_rows):
            return_list.append(fake.password())
    elif data_target == "freeshit":
        for _ in range(n_rows):
            return_list.append(fake.random_int(min=0, max=5))
    elif data_target == "0-2":
        for _ in range(n_rows):
            return_list.append(fake.random_int(min=0, max=3))
    elif data_target == "language":
        for _ in range(n_rows):
            return_list.append(fake.language_name())
    # elif data_target == "auto_increment":
    #     for i in range(n_rows):
    #         return_list.append("NULL")
    else:
        for _ in range(n_rows):
            return_list.append(data_target)
    return return_list


class CColumn(Column):
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


# add database
my_db = CDatabase(db_name="C##ZSBD")

# add tables
my_db.add_table(table_name="CrewMember", n_rows=1000)
my_db.add_table(table_name="Genre", n_rows=1000)
my_db.add_table(table_name="Country", n_rows=1000)
my_db.add_table(table_name="Award", n_rows=1000)
my_db.add_table(table_name="Job", n_rows=1000)
my_db.add_table(table_name="Customer", n_rows=1000)
my_db.add_table(table_name="Translation", n_rows=1000)
my_db.add_table(table_name="Language", n_rows=1000)
my_db.add_table(table_name="Movie", n_rows=1000)
my_db.add_table(table_name="Rent", n_rows=1000)
my_db.add_table(table_name="Role", n_rows=1000)
my_db.add_table(table_name="Rate", n_rows=1000)
my_db.add_table(table_name="Genre_Movie", n_rows=1000)
my_db.add_table(table_name="Movie_Award", n_rows=1000)
my_db.add_table(table_name="Country_Movie", n_rows=1000)
my_db.add_table(table_name="CrewMember_Award", n_rows=1000)
my_db.add_table(table_name="CrewMember_Job", n_rows=1000)
my_db.add_table(table_name="CrewMember_Movie", n_rows=1000)

# add columns to CrewMember table

my_db.tables["CrewMember"].add_primary_key(column_name="CrewMemberId")
my_db.tables["CrewMember"].add_column_custom(column_name="Name", data_target="first_name", data_type="varchar(255)")
my_db.tables["CrewMember"].add_column_custom(column_name="Surname", data_target="last_name", data_type="varchar(255)")
my_db.tables["CrewMember"].add_column_custom(column_name="Gender", data_target="gender", data_type="char(1)")
my_db.tables["CrewMember"].add_column_custom(column_name="BirthDate", data_target="date", data_type="date")
my_db.tables["CrewMember"].add_column_custom(column_name="Height", data_target="height", data_type="number(10)")

my_db.tables["Movie"].add_primary_key(column_name="MovieId")
my_db.tables["Movie"].add_column_custom(column_name="Title", data_target="words", data_type="varchar(255)")
my_db.tables["Movie"].add_column_custom(column_name="PremiereDate", data_target="date", data_type="date")
my_db.tables["Movie"].add_column_custom(column_name="Duration", data_target="number", data_type="number(10)")
my_db.tables["Movie"].add_column_custom(column_name="Budget", data_target="float", data_type="float(10)")
my_db.tables["Movie"].add_column_custom(column_name="Description", data_target="paragraph", data_type="varchar(255)")
my_db.tables["Movie"].add_column_custom(column_name="Studio", data_target="word", data_type="varchar(255)")
my_db.tables["Movie"].add_column_custom(column_name="Promo", data_target="promo", data_type="float(10)")

my_db.tables["Genre"].add_primary_key(column_name="GenreId")
my_db.tables["Genre"].add_column_custom(column_name="Name", data_target="genre", data_type="varchar(255)")

my_db.tables["Role"].add_primary_key(column_name="RoleId")
my_db.tables["Role"].add_column_custom(column_name="Name", data_target="name", data_type="varchar(255)")

my_db.tables["Country"].add_primary_key(column_name="CountryId")
my_db.tables["Country"].add_column_custom(column_name="Name", data_target="country", data_type="varchar(255)")

my_db.tables["Award"].add_primary_key(column_name="AwardId")
my_db.tables["Award"].add_column_custom(column_name="Name", data_target="country", data_type="varchar(255)")
my_db.tables["Award"].add_column_custom(column_name="Category", data_target="word", data_type="varchar(255)")
my_db.tables["Award"].add_column_custom(column_name="DeliveryDate", data_target="date", data_type="date")
my_db.tables["Award"].add_column_custom(column_name="IsWinner", data_target="boolean", data_type="number")

my_db.tables["Job"].add_primary_key(column_name="JobId")
my_db.tables["Job"].add_column_custom(column_name="Name", data_target="name", data_type="varchar(255)")

my_db.tables["Rate"].add_primary_key(column_name="RateId")
my_db.tables["Rate"].add_column_custom(column_name="Value", data_target="rate", data_type="number(10)")
my_db.tables["Rate"].add_column_custom(column_name="Title", data_target="words", data_type="varchar(255)")
my_db.tables["Rate"].add_column_custom(column_name="Description", data_target="paragraph", data_type="varchar(255)")
my_db.tables["Rate"].add_column_custom(column_name="RateDate", data_target="date", data_type="date")
my_db.tables["Rate"].add_column_custom(column_name="Verified", data_target="boolean", data_type="number")
my_db.tables["Rate"].add_column_custom(column_name="Views", data_target="number", data_type="number(10)")

my_db.tables["Customer"].add_primary_key(column_name="CustomerId")
my_db.tables["Customer"].add_column_custom(column_name="Email", data_target="email", data_type="varchar(255)")
my_db.tables["Customer"].add_column_custom(column_name="Login", data_target="login", data_type="varchar(255)")
my_db.tables["Customer"].add_column_custom(column_name="Password", data_target="password", data_type="varchar(255)")
my_db.tables["Customer"].add_column_custom(column_name="RegistrationDate", data_target="date", data_type="date")
my_db.tables["Customer"].add_column_custom(column_name="BirthDate", data_target="date", data_type="date")
my_db.tables["Customer"].add_column_custom(column_name="FreeMovies", data_target="freeshit", data_type="number(10)")
my_db.tables["Customer"].add_column_custom(column_name="EmailVerified", data_target="boolean", data_type="number")

my_db.tables["Rent"].add_primary_key(column_name="RentId")
my_db.tables["Rent"].add_column_custom(column_name="RentDate", data_target="date", data_type="date")
my_db.tables["Rent"].add_column_custom(column_name="Price", data_target="float", data_type="float(10)")
my_db.tables["Rent"].add_column_custom(column_name="Quality", data_target="freeshit",
                                       data_type="number(10)")  # TODO to enum?
my_db.tables["Rent"].add_column_custom(column_name="Period", data_target="number", data_type="number(10)")
my_db.tables["Rent"].add_column_custom(column_name="Promo", data_target="promo", data_type="float(10)")

my_db.tables["Translation"].add_primary_key(column_name="TranslationId")
my_db.tables["Translation"].add_column_custom(column_name="Type", data_target="0-2",
                                              data_type="number(10)")  # TODO to enum?
my_db.tables["Translation"].add_column_custom(column_name="TranslationDate", data_target="date", data_type="date")
my_db.tables["Translation"].add_column_custom(column_name="Author", data_target="name", data_type="varchar(255)")
my_db.tables["Translation"].add_column_custom(column_name="Copyright", data_target="word", data_type="varchar(255)")
my_db.tables["Translation"].add_column_custom(column_name="RentRentId", data_target="", data_type="number(10)")

my_db.tables["Language"].add_primary_key(column_name="LanguageId")
my_db.tables["Language"].add_column_custom(column_name="Name", data_target="language", data_type="varchar(255)")

# Foreign keys - intermediate tables
my_db.tables["Genre_Movie"].add_foreign_key(column_name="GenreGenreId", target_table="Genre", target_column="GenreId")
my_db.tables["Genre_Movie"].add_foreign_key(column_name="MovieMovieId", target_table="Movie", target_column="MovieId")
my_db.tables["Movie_Award"].add_foreign_key(column_name="MovieMovieId", target_table="Movie", target_column="MovieId")
my_db.tables["Movie_Award"].add_foreign_key(column_name="AwardAwardId", target_table="Award", target_column="AwardId")
my_db.tables["Country_Movie"].add_foreign_key(column_name="CountryCountryId", target_table="Country",
                                              target_column="CountryId")
my_db.tables["Country_Movie"].add_foreign_key(column_name="MovieMovieId", target_table="Movie", target_column="MovieId")
my_db.tables["CrewMember_Award"].add_foreign_key(column_name="CrewMemberCrewMemberId", target_table="CrewMember",
                                                 target_column="CrewMemberId")
my_db.tables["CrewMember_Award"].add_foreign_key(column_name="AwardAwardId", target_table="Award",
                                                 target_column="AwardId")
my_db.tables["CrewMember_Job"].add_foreign_key(column_name="CrewMemberCrewMemberId", target_table="CrewMember",
                                               target_column="CrewMemberId")
my_db.tables["CrewMember_Job"].add_foreign_key(column_name="JobJobId", target_table="Job", target_column="JobId")
my_db.tables["CrewMember_Movie"].add_foreign_key(column_name="CrewMemberCrewMemberId", target_table="CrewMember",
                                                 target_column="CrewMemberId")
my_db.tables["CrewMember_Movie"].add_foreign_key(column_name="MovieMovieId", target_table="Movie",
                                                 target_column="MovieId")

# Foreign keys
my_db.tables["Movie"].add_foreign_key(column_name="TranslationTranslationId", target_table="Translation",
                                      target_column="TranslationId")
my_db.tables["Role"].add_foreign_key(column_name="MovieMovieId", target_table="Movie", target_column="MovieId")
my_db.tables["Role"].add_foreign_key(column_name="CrewMemberCrewMemberId", target_table="CrewMember",
                                     target_column="CrewMemberId")
my_db.tables["Country"].add_foreign_key(column_name="CrewMemberCrewMemberId", target_table="CrewMember",
                                        target_column="CrewMemberId")
my_db.tables["Rate"].add_foreign_key(column_name="MovieMovieId", target_table="Movie", target_column="MovieId")
my_db.tables["Rate"].add_foreign_key(column_name="CustomerCustomerId", target_table="Customer",
                                     target_column="CustomerId")
my_db.tables["Rent"].add_foreign_key(column_name="CustomerCustomerId", target_table="Customer",
                                     target_column="CustomerId")
my_db.tables["Rent"].add_foreign_key(column_name="MovieMovieId", target_table="Movie", target_column="MovieId")
# my_db.tables["Translation"].add_foreign_key(column_name="RentRentId", target_table="Rent", target_column="RentId")

my_db.generate_data()
my_db.export_sql("generated.sql")

convert('generated.sql')
