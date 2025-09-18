# program to manage timesheets


import datetime
import json
from typing import List, Dict, Any     

class Timesheet:
    def __init__(self, employee_id: str):
        self.employee_id = employee_id
        self.entries: List[Dict[str, Any]] = []

    def add_entry(self, date: str, hours: float, description: str):
        entry = {
            "date": date,
            "hours": hours,
            "description": description
        }
        self.entries.append(entry)

    def get_entries(self) -> List[Dict[str, Any]]:
        return self.entries

    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(self.entries, file)

    def load_from_file(self, filename: str):
        with open(filename, 'r') as file:
            self.entries = json.load(file)  

    def total_hours(self) -> float:
        return sum(entry['hours'] for entry in self.entries)    

    def __str__(self):
        return f"Timesheet for Employee ID: {self.employee_id}, Total Hours: {self.total_hours()}"


def main():
    employee_id = input("Enter Employee ID: ")
    timesheet = Timesheet(employee_id)

    while True:
        date = input("Enter date (YYYY-MM-DD) or 'exit' to finish: ")
        if date.lower() == 'exit':
            break
        hours = float(input("Enter hours worked: "))
        description = input("Enter description of work done: ")
        timesheet.add_entry(date, hours, description)

    print(timesheet)
    filename = f"{employee_id}_timesheet.json"
    timesheet.save_to_file(filename)
    print(f"Timesheet saved to {filename}")

if __name__ == "__main__":
    main()



