class DoctorAvailability:
    def __init__(self, day_of_week, times_available):
        self.day_of_week = day_of_week.lower()
        self.times_available = times_available


class ExtDoc:
    def __init__(self, name, specialization, department, consultation_fee, availability):
        self.name = name
        self.specialization = specialization
        self.department = department
        self.consultation_fee = consultation_fee
        self.availability = availability

    def display_info(self):
        print(f"Doctor Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Department: {self.department}")
        print(f"Consultation Fee: Rs.{self.consultation_fee}")
        print("Available Days and Times:")
        for availability in self.availability:
            print(f"{availability.day_of_week.capitalize()}: {', '.join(availability.times_available)}")