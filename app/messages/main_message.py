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
            'uz': f"Afsuski, sizning ma'lumotlaringiz mos kelmaydi yoki allaqachon mavjud.",
            'ru': f"К сожалению, ваши данные не совпадают или уже существуют.",
            'en': f"Unfortunately, your details do not match or already exist."
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
            'uz': '🥳Tabriklaymiz! Endi siz Fbox orqali amalga oshirilgan to\'lovlar haqida xabar olasiz☺️',
            'ru': '🥳Поздравляем! Теперь вы будете получать уведомления о платежах, совершенных через Fbox☺️',
            'en': '🥳Congratulations! You will now be notified about payments made through Fbox☺️'
        }
        return self.message[self.language]

    def fail_end_process_message(self) -> str:
        self.message = {
            'uz': 'Kechirasiz! Siz taqdim etgan mos maʼlumotlarni topa olmadik. Qaytadan urining yoki ro\'yhatdan o\'ting',
            'ru': 'Извините! Мы не смогли найти соответствующие данные, предоставленные вами. Попробуйте еще раз или Авторизуйтесь',
            'en': 'Sorry! We couldn not find any matching data provided by you. Try again or Login'
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

    def help_message(self) -> str:
        self.message = {
            'uz': 'FboxAssistantbot - Bot sizga telegram orqali FBOXda orqali amalga oshirilgan to\'lovlar haqida '
                  'sizni xabardor qiladi.\n'
                  'Siz qilshingiz kerak:\n'
                  '1️⃣ Tizimga kirish /start\n'
                  '2️⃣ Xabar turini tanlash\n'
                  '☎️ To\'liq ma`lumot uchun +(99871) 256 50 09',
            'ru': 'FboxAssistantbot - Уведомлять вас о платежах, совершенных через FBOX в telegram.\n'
                  'Вы должны:\n'
                  '1️⃣ Авторизоваться /start\n'
                  '2️⃣ Выбрит тип уведомления\n'
                  '☎️ По всем вопросам +(99871) 256 50 09',
            'en': 'FboxAssistantbot - Notify you about payments made via FBOX in telegram.\n'
                  'You must:\n'
                  '1️⃣ Log in /start\n'
                  '2️⃣ Select notification type\n'
                  '☎️ For all questions +(99871) 256 50 09'
        }
        return self.message[self.language]

    def user_me_message(self, username: str, is_send: bool, created_date: str, last_updated: str, company: str = None,
                        device: str = None) -> str:
        self.message = {
            'uz': f"-- Foydalanuvchi haqida ma'lumot --\n\n"
                  f"Foydalanuvchi: {username}\n"
                  f"Bildirishnomalarni yuborish: {'✅' if is_send else '🚫'}\n\n"
                  f"Kompaniya: {company}\n"
                  f"Qurilma: {device}\n\n"
                  f"Ishga tushirish sanasi: {created_date}\n"
                  f"Hisob qaydnomasining oxirgi yangilanishi: {last_updated}",
            'ru': f"-- Информация о пользователе --\n\n"
                  f"Имя пользователя: {username}\n"
                  f"Отправлять уведомления: {'✅' if is_send else '🚫'}\n\n"
                  f"Компания: {company}\n"
                  f"Устройство: {device}\n\n"
                  f"Дата запуска: {created_date}\n"
                  f"Последнее обновление аккаунта: {last_updated}",
            'en': f"-- Information about user --\n\n"
                  f"Username: {username}\n"
                  f"Send Notifications: {'✅' if is_send else '🚫'}\n\n"
                  f"Company: {company}\n"
                  f"Device: {device}\n\n"
                  f"Launch date: {created_date}\n"
                  f"The last update an account: {last_updated}",
        }
        return self.message[self.language]

    def user_not_found(self) -> str:
        self.message = {
            'uz': "-- Foydalanuvchi haqida ma'lumot --\n\nFoydalanuvchi topilmadi",
            'ru': "-- Информация о пользователе --\n\nПользователь не найден",
            'en': "-- Information about user --\n\nUser not found"
        }
        return self.message[self.language]

    def monitoring_type_message(self) -> str:
        self.message = {
            'uz': "Kuzatish turini tanlang",
            'ru': "выберите тип наблюдения",
            'en': "select the type of observation"
        }
        return self.message[self.language]

    def notify_status_on_message(self) -> str:
        self.message = {
            'uz': 'Bildirishnoma yoqildi🔔',
            'ru': 'Уведомление Подключено🔔',
            'en': 'Notification Enabled🔔'
        }
        return self.message[self.language]

    def notify_status_off_message(self) -> str:
        self.message = {
            'uz': 'Bildirishnoma o‘chirildi🔕',
            'ru': 'Уведомление Отключено🔕',
            'en': 'Notification Disabled🔕'
        }
        return self.message[self.language]

    def error_on_notify_process_message(self) -> str:
        self.message = {
            'uz': 'Holatni o‘zgartirishda muammo yuz berdi',
            'ru': 'Возникла проблема при изменении статуса',
            'en': 'There was a problem changing the status'
        }
        return self.message[self.language]

    def error_get_ip_address_message(self) -> str:
        self.message = {
            'uz': 'Foydalanuvchi topilmadi yoki ulangan qurilmalari yo\'q.',
            'ru': 'Пользователь не найден или у него нет подключенных устройств.',
            'en': 'The user is not found or has no connected devices.'
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
