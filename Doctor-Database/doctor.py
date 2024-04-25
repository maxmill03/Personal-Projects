class Doctor:
    def __init__(self, full_name, specialty, information, gender):
        self.full_name = full_name
        full_name_split = full_name.replace(",", "").split()
        self.first_name = full_name_split[0]
        self.last_name = ""
        for word in full_name_split[1:len(full_name_split) - 1]:
            self.last_name += word + " "
        self.specialty = specialty
        self.information = information
        information_split = information.split(", ")
        self.phone_number = information_split[len(information_split) - 1]
        self.facility = information_split[0]
        self.address = ""
        for item in information_split[1:len(information_split) - 2]:
            self.address += item + ", "
        self.address += information_split[len(information_split) - 2]
        self.gender = gender

    def get_name(self):
        return self.full_name

    def get_gender(self):
        return self.gender

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_specialty(self):
        return self.specialty

    def get_information(self):
        return self.information

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_facility(self):
        return self.facility
