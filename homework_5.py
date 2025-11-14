

class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("Первый аргумент должен быть объектом User")

        if not user.is_admin:
            raise PermissionError(
                "Доступ запрещён! Только админ может выполнить эту операцию."
            )

        return func(user, *args, **kwargs)  # выполняем функцию
    return wrapper


@admin_only
def delete_database(user):
    print("База данных удалена!")


if __name__ == "__main__":
    admin = User("Алексей", is_admin=True)
    user = User("Мария", is_admin=False)
    delete_database(admin)

    try:
        delete_database(user)
    except PermissionError as e:
        print(e)
