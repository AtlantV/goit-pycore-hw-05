# Консольний застосунок CLI (Command Line Interface) складається з 3-x основних елементів:
# 1. Парсер команд. Частина, яка відповідає за розбір введених користувачем
# рядків, виділення з рядка ключових слів та модифікаторів команд.

def parse_input(user_input):         
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower()
    return cmd, *args

# Декоратори для обробки помилок. Повинні обробляти винятки, що виникають у функціях handler, і це винятки 
# KeyError, ValueError, IndexError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and(or) phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."

    return inner

# 2. Функції обробники команд - набір функцій, які ще називають handler, 
# вони відповідають за безпосереднє виконання команд.
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, 
# що вже існує в записнику.
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

# За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.    
@input_error
def phone_username(args, contacts):
    name = args[0] 
    if name in contacts: 
        return f"{name}: {contacts[name]}" 
    else: 
        return f"Contact '{name}' not found."

# За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
def all(contacts):
    if not contacts:  # ← перевірка перед будь-якими діями
        return "No contacts found."
    result = []
    for name, phone in contacts.items(): 
        result.append(f"{name}: {phone}") 
    return "\n".join(result)

# 3. Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних 
# та повернення користувачеві відповіді від функції - handler-а.
def main():
    contacts = {}
    print("Welcome to the assistant bot!\nEnter a command (for username and phone):\n- add\n- change\n- phone\n- all\nor 'exit'/'close' for stop:")
    while True:
        user_input = input("-> ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")
 
if __name__ == "__main__":
    main()