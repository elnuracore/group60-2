
import random
from abc import ABC, abstractmethod



class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password


    def deposit(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"
        self._balance += amount
        return self._balance

    def withdraw(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"
        if amount > self._balance:
            return "Недостаточно средств!"
        self._balance -= amount
        return self._balance


    def get_balance(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        return self._balance

    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            return "Старый пароль неверный"
        self.__password = new_password
        return "Пароль изменён"


    def reset_pin(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return new_pin


    def __generate_pin(self):
        return str(random.randint(1000, 9999))



class NotificationSender(ABC):

    @abstractmethod
    def send(self, message, recipient):
        pass



class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    def send(self, message, recipient):
        return f"Email sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"



class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"



class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"



class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        result = self.account.get_balance(password)
        if isinstance(result, int):   # значит пароль верный
            print(self.notifier.send(f"Успешный вход: {self.username}", "system"))
            return True
        return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        if self.account.get_balance(password) == "Неверный пароль!":
            return "Неверный пароль!"


        withdrawal = self.account.withdraw(amount, password)
        if withdrawal == "Недостаточно средств!":
            return "Недостаточно средств!"
        if withdrawal == "Неверный пароль!":
            return "Неверный пароль!"

        recipient_account._balance += amount

        print(self.notifier.send(f"Перевод {amount} отправлен", "system"))

        print(self.notifier.send(f"Получено {amount} от {self.username}", "system"))

        return f"Перевод успешен. Новый баланс: {self.account._balance}"



if __name__ == "__main__":
    print("=== Тест BankAccount ===")
    john = BankAccount("John", 200, "secret")

    print(john.deposit(50, "secret"))
    print(john.withdraw(100, "secret"))
    print(john.get_balance("secret"))
    print(john.change_password("wrong", "new"))
    print(john.change_password("secret", "new"))
    new_pin = john.reset_pin("new")
    print(new_pin)
    print(john.get_balance(new_pin))

    print("\n=== Тест NotificationSender ===")
    email = EmailSender()
    print(email.send("Привет", "test@mail.ru"))
    print(email.get_service())
    sms = SmsSender()
    print(sms.get_service())

    print("\n=== Тест UserAuth ===")
    john2 = BankAccount("John", 150, "pass")
    alice = BankAccount("Alice", 50, "alice123")

    notifier = SmsSender()
    auth = UserAuth("john_doe", john2, notifier)

    print(auth.login("pass"))
    print(auth.login("pass"))

    result = auth.transfer(70, "pass", alice)
    print(result)
    print("John balance:", john2._balance)
    print("Alice balance:", alice._balance)
