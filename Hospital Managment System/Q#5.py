
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Patient(Person):
    def __init__(self, name, age, address, patient_id, medical_history):
        super().__init__(name, age, address)
        self.patient_id = patient_id
        self.medical_history = medical_history
        self.prescriptions = []

class Doctor(Person):
    def __init__(self, name, age, address, employee_id, specialty):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.specialty = specialty
        self.assigned_patients = []

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient Name : {patient.name} Age: {patient.age} Address: {patient.address}")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor Name : {doctor.name} Age: {doctor.age} Address: {doctor.address}")

    def schedule_appointment(self, patient, doctor):
        self.appointments.append((patient, doctor))
        doctor.assigned_patients.append(patient)

    def manage_patient_records(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print("Patient Records:")
                print(f"Name: {patient.name}")
                print(f"Age: {patient.age}")
                print(f"Address: {patient.address}")
                print(f"Medical History: {patient.medical_history}")
                print(f"Prescriptions: {patient.prescriptions}")
                return
        print("Patient not found.")

person = Person("hassan","15","Saddar Rawalpindi")
patient = Patient(person.name,person.age,person.address,"PAT-112","Blood Cancer")
doctor = Doctor("Amjad Khan",35,"Double road RWP","Dr-45","Cancer Specialist")
hospital = Hospital()
hospital.add_patient(patient)
hospital.add_doctor(doctor)
hospital.schedule_appointment(patient,doctor)
hospital.manage_patient_records("PAT-112")
