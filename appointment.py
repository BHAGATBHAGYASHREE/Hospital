class Appointment:
    def __init__(self, patient_name, doctor_name, appointment_day, appointment_time, consultation_fee):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_day = appointment_day
        self.appointment_time = appointment_time
        self.consultation_fee = consultation_fee

    def display_info(self):
        print("\nAppointment Details:")
        print(f"Patient Name: {self.patient_name}")
        print(f"Doctor: {self.doctor_name}")
        print(f"Appointment Day: {self.appointment_day}")
        print(f"Appointment Time: {self.appointment_time}")
        print(f"Consultation Fee: Rs.{self.consultation_fee}")


def check_slot_availability(doctor, appointment_day, appointment_time):
    for availability in doctor.availability:
        if availability.day_of_week == appointment_day:
            if appointment_time in availability.times_available:
                return True
    return False


def cancel_appointment(doctor, appointment_day, appointment_time):
    for availability in doctor.availability:
        if availability.day_of_week == appointment_day:
            if appointment_time not in availability.times_available:
                availability.times_available.append(appointment_time)
                availability.times_available.sort()
                print("Appointment canceled successfully.")
                return True
    print("Appointment cancellation failed. Slot not found or already canceled.")
    return False