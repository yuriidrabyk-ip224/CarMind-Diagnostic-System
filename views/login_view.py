import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, parent, on_success):
        # Встановлюємо темний фон для всього екрана (автомобільна стилістика)
        super().__init__(parent, bg="#1A1A1A")
        self.on_success = on_success

        # Логотип/Назва додатка
        tk.Label(self, text="CarMind", font=("Arial", 36, "bold"),
                 bg="#1A1A1A", fg="#007AFF").pack(pady=(80, 40))

        # Контейнер для полів введення (щоб додати відступи)
        form_frame = tk.Frame(self, bg="#1A1A1A")
        form_frame.pack(fill="x", padx=40)

        # Поле Email
        tk.Label(form_frame, text="Email Address", bg="#1A1A1A",
                 fg="#8E8E93", font=("Arial", 10)).pack(anchor="w")
        self.email_entry = tk.Entry(form_frame, font=("Arial", 12), bg="#2C2C2E",
                                    fg="white", insertbackground="white", bd=0)
        self.email_entry.pack(pady=(5, 20), fill="x", ipady=8)
        # Додаємо лінію підкреслення для стилю
        tk.Frame(form_frame, height=1, bg="#3A3A3C").pack(fill="x", pady=(0, 20))

        # Поле Password
        tk.Label(form_frame, text="Password", bg="#1A1A1A",
                 fg="#8E8E93", font=("Arial", 10)).pack(anchor="w")
        self.password_entry = tk.Entry(form_frame, show="*", font=("Arial", 12),
                                       bg="#2C2C2E", fg="white", insertbackground="white", bd=0)
        self.password_entry.pack(pady=(5, 5), fill="x", ipady=8)
        tk.Frame(form_frame, height=1, bg="#3A3A3C").pack(fill="x", pady=(0, 30))

        # Кнопка входу (акцентна синя)
        login_btn = tk.Button(self, text="Sign In", bg="#007AFF", fg="white",
                              font=("Arial", 12, "bold"), command=self.login,
                              relief="flat", cursor="hand2", activebackground="#0051A8")
        login_btn.pack(pady=10, padx=40, fill="x", ipady=10)

        # Додаткова кнопка (імітація реєстрації)
        tk.Button(self, text="Create an account", bg="#1A1A1A", fg="#007AFF",
                  font=("Arial", 10), relief="flat", cursor="hand2").pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Проста валідація для MVP
        if email and password:
            print(f"Login attempt: {email}")
            self.on_success()
        else:
            # Можна додати візуальне попередження, але для лаби виведемо в консоль
            print("Error: Please enter both email and password")