from datetime import datetime
class remainder:
    def remember_event():
        date_event = {}
        while True:
            choice = input('Do you want to remember something(yes/no): ')
            if choice.lower() == 'yes':
                date = input('Enter the important date: ')
                event = input('Enter the event for the date: ')
                date_event[date] =event
                print('Sucessfully Remembered')
            elif choice.lower() == 'no':
                break
            else:
                print('Invalid choice. Please enter yes or no.')
        return date_event
    
    def check_event(date_event):
        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        keys = list(date_event.keys())
        values = list(date_event.values())
        for value in keys:
            if  current_date == value:
                print(f'The event for {value} is : {date_event[value]}')
        
rem= remainder
date_and_event =rem.remember_event()
# print(date_and_event)
rem.check_event(date_and_event)