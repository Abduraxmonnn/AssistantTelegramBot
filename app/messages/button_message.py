class ButtonMessages:
    def __init__(self, language: str = 'ru'):
        self.language = language
        self.message = None

    def type_monitoring_device_message(self) -> str:
        self.message = {
            'uz': 'Qurilma kuzatuvi',
            'ru': 'Наблюдения за устройством',
            'en': 'Device Monitoring'
        }
        return self.message[self.language]

    def type_monitoring_company_message(self) -> str:
        self.message = {
            'uz': 'Kompaniya kuzatuvi',
            'ru': 'Наблюдение за компанией',
            'en': 'Company Observation'
        }
        return self.message[self.language]

    def type_monitoring_placeholder_message(self) -> str:
        self.message = {
            'uz': 'Kuzatuv turini tanlang',
            'ru': 'Выберите тип наблюдения',
            'en': 'Select the type of observation'
        }
        return self.message[self.language]

    def notify_status_on_btn_message(self) -> str:
        self.message = {
            'uz': 'Bildirishnoma yoqish✅',
            'ru': 'Подключить уведомление✅',
            'en': 'Enable notification✅'
        }
        return self.message[self.language]

    def notify_status_off_btn_message(self) -> str:
        self.message = {
            'uz': 'Bildirishnomani o‘chirish🚫',
            'ru': 'Отключить уведомление🚫',
            'en': 'Disable notification🚫'
        }
        return self.message[self.language]

    def send_contact_message(self) -> str:
        self.message = {
            'uz': 'Kontaktni yuboring',
            'ru': 'Отправить контакт',
            'en': 'Send contact'
        }
        return self.message[self.language]

    def login_message(self) -> str:
        self.message = {
            'uz': 'Tizimga kirish',
            'ru': 'Авторизоваться',
            'en': 'Login'
        }
        return self.message[self.language]

    def back_to_monitoring_type_message(self) -> str:
        self.message = {
            'uz': 'Kuzatish turini tanlashga qaytish⬅️',
            'ru': 'Вернуться к выбору типа наблюдения⬅️',
            'en': 'Back to select observation type⬅️'
        }
        return self.message[self.language]
