# LOGIN_MESSAGE = {
#     'uz': 'Ajoyib! Endi muvaffaqiyatli avtorizatsiya qilish uchun "Login" va "Parol" ni kiritishingiz kerak',
#     'ru': 'Отлично! Теперь вам нужно ввести "Логин" и "Пароль" для успешной авторизации',
#     'en': 'Great! Now you need to enter "Login" and "Password" for successful authorization'
# }
#
# LOGIN_USERNAME_MESSAGE = {
#     'uz': 'Iltimos, Login kiriting',
#     'ru': 'Пожалуйста, введите Логин',
#     'en': 'Please, enter your Login'
# }
#
# LOGIN_PASSWORD_MESSAGE = {
#     'uz': 'Iltimos, Parol kiriting',
#     'ru': 'Пожалуйста, введите Пароль',
#     'en': 'Please, enter your Password'
# }


class MainMessages:
    def __init__(self, language: str = 'ru'):
        self.language = language
        self.message = None

    def hello_message(self, username: str) -> str:
        self.message = {
            'uz': f'{username} Xush kelibsiz 😊! Ushbu bot Fbox orqali amalga oshirilgan to\'lovlar haqida sizni xabardor qiladi\n\n'
                  f'BUning uchun siz tizimga kirishingiz kerak',
            'ru': f'{username} Добро пожаловать 😊! Этот бот будет уведомлять вас о платежах, совершенных через Fbox\n\n'
                  f'Чтобы иметь доступ необходимо авторизоваться',
            'en': f'{username} Welcome 😊! This bot will notify you about payments made through Fbox\n\n'
                  f'To have access you need to log in'
        }
        return self.message[self.language]

    def login_message(self) -> str:
        self.message = {
            'uz': 'Ajoyib! Endi muvaffaqiyatli avtorizatsiya qilish uchun "Login" va "Parol" ni kiritishingiz kerak',
            'ru': 'Отлично! Теперь вам нужно ввести "Логин" и "Пароль" для успешной авторизации',
            'en': 'Great! Now you need to enter "Login" and "Password" for successful authorization'
        }
        return self.message[self.language]

    def login_success_message(self):
        self.message = {
            'uz': f"Tabriklaymiz, siz muvaffaqiyatli avtorlashdingiz",
            'ru': f"Поздравляем, вы успешно авторизовались",
            'en': f"Congratulations, you have successfully authorized"
        }
        return self.message[self.language]

    def login_fail_message(self):
        self.message = {
            'uz': f"Kechirasiz, maʼlumotlaringiz mos emas.",
            'ru': f"К сожалению, ваши данные не совпадают.",
            'en': f"Unfortunately, your details do not match."
        }
        return self.message[self.language]

    def invalid_phone_message(self):
        self.message = {
            'uz': f"Iltimos, telefon raqamini kiritish o'rniga kontaktni jo`nating.",
            'ru': f"Пожалуйста, поделитесь контактом вместо ввода номера телефона.",
            'en': f"Please, Share contact instead of entering a phone number."
        }
        return self.message[self.language]

    def login_username_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, Login kiriting',
            'ru': 'Пожалуйста, введите Логин',
            'en': 'Please, enter your Login'
        }
        return self.message[self.language]

    def login_password_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, Parol kiriting',
            'ru': 'Пожалуйста, введите Пароль',
            'en': 'Please, enter your Password'
        }
        return self.message[self.language]

    def login_phone_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, Telefon raqam kiriting',
            'ru': 'Пожалуйста, введите Телефон номер',
            'en': 'Please, enter your Phone Number'
        }
        return self.message[self.language]

    def login_inn_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, INN kiriting',
            'ru': 'Пожалуйста, введите ИНН',
            'en': 'Please enter INN'
        }
        return self.message[self.language]

    def error_choose_one_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, variantlardan birini tanlang!',
            'ru': 'Пожалуйста, выберите один из вариантов!',
            'en': 'Please choose one of Option!'
        }
        return self.message[self.language]

    def ask_device_serial_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, qurilmaning seriya raqamini kiriting!',
            'ru': 'Пожалуйста, введите серийный номер устройства!',
            'en': 'Please, Enter the device serial number!'
        }
        return self.message[self.language]

    def success_end_process_message(self) -> str:
        self.message = {
            'uz': '✅Tabriklaymiz! Endi siz Fbox orqali amalga oshirilgan to\'lovlar haqida xabar olasiz☺️',
            'ru': '✅Поздравляем! Теперь вы будете получать уведомления о платежах, совершенных через Fbox☺️',
            'en': '✅Congratulations! You will now be notified about payments made through Fbox☺️'
        }
        return self.message[self.language]

    def fail_end_process_message(self) -> str:
        self.message = {
            'uz': 'Kechirasiz! Siz taqdim etgan mos maʼlumotlarni topa olmadik. Qayta urinib koʼring!',
            'ru': 'Извините! Мы не смогли найти соответствующие данные, предоставленные вами. Попробуйте еще раз!',
            'en': 'Sorry! We couldn not find any matching data provided by you. Try again!'
        }
        return self.message[self.language]

    def ask_company_inn_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, kompaniyangizning INN (soliq to\'lovchining identifikatsiya raqami) ni kiriting.',
            'ru': 'Пожалуйста, введите ИНН вашей компании (идентификационный номер налогоплательщика)',
            'en': 'Please, enter your Company INN (Taxpayer Identification Number)'
        }
        return self.message[self.language]

    def user_exists_message(self) -> str:
        self.message = {
            'uz': 'Foydalanuvchi allaqachon mavjud.',
            'ru': 'Пользователь уже существует.',
            'en': 'User already exists.'
        }
        return self.message[self.language]

    def transaction_message(self, is_status: bool, data: dict, obj, date: str) -> str:
        success_status = {
            'uz': 'muvaffaqiyatli',
            'ru': 'Успешно',
            'en': 'Success'
        }

        fail_status = {
            'uz': 'Muvaffaqiyatsiz',
            'ru': 'Неудача',
            'en': 'Fail'
        }

        status = success_status[self.language] if is_status else fail_status[self.language]

        self.message = {
            'uz': f"✅Holati: {status}\n\n "
                  f"№ Xabar: {obj.id}\n"
                  f"⏱Vaqt: {date}\n\n",
            'ru': f"✅Статус: {status}\n\n "
                  f"№ Сообщения: {obj.id}\n"
                  f"⏱Время: {date}\n\n",
            'en': f"✅Status: {status}\n\n "
                  f"№ Message: {obj.id}\n"
                  f"⏱Date: {date}\n\n"
        }
        return self.message[self.language]
