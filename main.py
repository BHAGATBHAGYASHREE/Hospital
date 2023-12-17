from Hospital.appointment import *
from Hospital.patients import *
from Hospital.doctor import *

def main():
    doctor1 = ExtDoc("Dr. Akriti", "Cardiology🫀", "Cardiology Department", 1500, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])
    doctor2 = ExtDoc("Dr. Bhagyashree", "Orthopedic🦴", "Orthopedic Department", 1300, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])
    doctor3 = ExtDoc("Dr. Riya", "Neurology🧠", "Neurology Department", 2000, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])
    doctor4 = ExtDoc("Dr. Ashlin", "Paediatric👶🏻", "Paediatric Department", 1600, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])
    

    while True:
        print("\nWelcome to the appointment system!")
        patient_name = input("Enter patient name: ")
        patient_age = int(input("Enter patient age: "))
        patient_gender = input("Enter patient gender: ")

        patient = Patient(patient_name, patient_age, patient_gender)
        patient.display_info()
        print("--------------------------------------------")

        print("ID: 1")
        doctor1.display_info()
        print("--------------------------------------------")
        
        print("ID: 2")
        doctor2.display_info()
        print("--------------------------------------------")
        
        print("ID: 3")
        doctor3.display_info()
        print("--------------------------------------------")
        
        print("ID: 4")
        doctor4.display_info()
        print("--------------------------------------------")

        choice = input("\nSelect a doctor by entering their ID: ")
        selected_doctor = None
        if choice == "1":
            selected_doctor = doctor1
        elif choice == "2":
            selected_doctor = doctor2
        elif choice == "3":
            selected_doctor = doctor3
        elif choice == "4":
            selected_doctor = doctor4
        else:
            print("Invalid choice.")
        

        if selected_doctor:
            selected_day = input("Enter preferred day for appointment (e.g., Monday, Tuesday, etc.): ").lower()
            available_times = None

            for availability in selected_doctor.availability:
                if availability.day_of_week == selected_day:
                    available_times = availability.times_available
                    break

            if available_times:
                print(f"Available times on {selected_day.capitalize()}: {', '.join(available_times)}")
                selected_time = input("Select appointment time: ")

                if selected_time in available_times:
                    if check_slot_availability(selected_doctor, selected_day, selected_time):
                        appointment = Appointment(patient_name, selected_doctor.name, selected_day.capitalize(), selected_time, selected_doctor.consultation_fee)
                        appointment.display_info()
                        print("Appointment booked successfully!")
                        
                        for availability in selected_doctor.availability:
                            if availability.day_of_week == selected_day:
                                if selected_time in availability.times_available:
                                    availability.times_available.remove(selected_time)
                                    break
                    else:
                        print("Slot not available. Appointment not booked.")
                else:
                    print("Invalid time selected. Appointment not booked.")
            else:
                print("Doctor not available on the selected day.")
        else:
            print("Invalid choice. Exiting.")

        cancel = input("\nWould you like to cancel an appointment? (yes/no): ").lower()
        if cancel == "yes":
            appointment_day = input("Enter the day of the appointment to cancel: ").lower()
            appointment_time = input("Enter the time of the appointment to cancel: ")

            cancel_successful = cancel_appointment(selected_doctor, appointment_day, appointment_time)
            if not cancel_successful:
                print("Cancellation failed. Please check the entered day and time.")

        repeat = input("\nDo you want to make another appointment? (yes/no): ").lower()
        if repeat != "yes":
            print("Exiting appointment system.")
            break

if __name__ == "__main__":
    main()