class ValidateCountry:
    def __init__(self, country):
        self.country = country

    def validate_country(self, country):
        if self.country == "Argentina":
            return True
        else:
            return False