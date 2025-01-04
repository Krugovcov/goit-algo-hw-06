from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, number):
        if not isinstance(number, str) or not number.isdigit() or len(number) != 10:
            raise ValueError("The phone number must be a string of 10 digits")
        super().__init__(number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
            phone = Phone(number)
            self.phones.append(phone)

    def remove_phone(self, number):
            for phone in self.phones:
                if phone.value == number:
                    self.phones.remove(phone)
                    return True
            return False

    def edit_phone(self, old_number, new_number):
            try:
                Phone(new_number)
            except ValueError:
                raise ValueError("invalid new number")
            if self.remove_phone(old_number):
                self.add_phone(new_number)
                return True
            else:
                raise ValueError(f"Old number {old_number} not found")
    
    def find_phone(self, number):
        for phone in self.phones:
                if phone.value == number:
                    return phone
        return None
                    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Record with name  {name} not found.")

    def __str__(self):
        if not self.data:
            return "The address book is empty."
        return "\n".join(str(record) for record in self.data.values())
    
try:
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    
    phone_to_find = "5555555555"
    found_phone = john_record.find_phone(phone_to_find)

        
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
except ValueError as e:
    print(f"Error: {e}")
