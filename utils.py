class Utils:
    def __init__(self):
        pass  

    def year_validation(self, year : int) -> bool:
        if len(str(year)) != 4 or year <= 0 or type(year) != int:
            print("The year should be a valid 4 digits number.")
            return False
        else:
            return True
        