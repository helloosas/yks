import customtkinter as ctk
import json
from tkinter import messagebox
import time # Zamanlayıcı için eklendi
import os # PLAN_DOSYASI yolu için

# Plan verisi için dosya adı
PLAN_DOSYASI = "plan_verisi.json"

# 14 Günlük Detaylı Çalışma Planı Şablonu
PLAN_TEMPLATE = [
    {
        "date": "2025-06-07", "day_of_week": "Cuma", "day_number": 1,
        "tasks": [
            {"id": "d1t1", "subject": "TYT Matematik", "topic": "Temel Kavramlar, Sayı Basamakları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d1t2", "subject": "TYT Fizik", "topic": "Madde ve Özellikleri (Özkütle, Hacim, Dayanıklılık)", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d1t3", "subject": "AYT Matematik", "topic": "Fonksiyonlar (Tanım, Değer Bulma, Grafik Okuma)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d1t4", "subject": "AYT Kimya", "topic": "Modern Atom Teorisi (Orbital, Kuantum Sayıları)", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d1t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-08", "day_of_week": "Cumartesi", "day_number": 2,
        "tasks": [
            {"id": "d2t1", "subject": "TYT Matematik", "topic": "Bölme-Bölünebilme, OBEB-OKEK", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d2t2", "subject": "TYT Kimya", "topic": "Atom ve Periyodik Sistem", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d2t3", "subject": "AYT Matematik", "topic": "Fonksiyonlar (Bileşke, Ters)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d2t4", "subject": "AYT Fizik", "topic": "Vektörler, Kuvvet ve Denge", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d2t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Dün ve Bugünün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-09", "day_of_week": "Pazar", "day_number": 3,
        "tasks": [
            {"id": "d3t1", "subject": "TYT Matematik", "topic": "Rasyonel Sayılar, Basit Eşitsizlikler", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d3t2", "subject": "TYT Biyoloji", "topic": "Canlıların Ortak Özellikleri, Temel Bileşenler", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d3t3", "subject": "AYT Matematik", "topic": "Polinomlar", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d3t4", "subject": "AYT Biyoloji", "topic": "Sinir Sistemi", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d3t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-10", "day_of_week": "Pazartesi", "day_number": 4,
        "tasks": [
            {"id": "d4t1", "subject": "TYT Matematik", "topic": "Mutlak Değer, Üslü Sayılar", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d4t2", "subject": "TYT Fizik", "topic": "Isı, Sıcaklık ve Genleşme", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d4t3", "subject": "AYT Matematik", "topic": "Parabol", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d4t4", "subject": "AYT Kimya", "topic": "Gazlar", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d4t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-11", "day_of_week": "Salı", "day_number": 5,
        "tasks": [
            {"id": "d5t1", "subject": "TYT Matematik", "topic": "Köklü Sayılar", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d5t2", "subject": "TYT Kimya", "topic": "Maddenin Halleri, Karışımlar", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d5t3", "subject": "AYT Matematik", "topic": "Trigonometri (Birim Çember, Özdeşlikler)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d5t4", "subject": "AYT Fizik", "topic": "Newton'un Hareket Yasaları", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d5t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-12", "day_of_week": "Çarşamba", "day_number": 6,
        "tasks": [
            {"id": "d6t1", "subject": "TYT Matematik", "topic": "Problemler (Sayı, Kesir)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d6t2", "subject": "TYT Biyoloji", "topic": "Hücre ve Organelleri", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d6t3", "subject": "AYT Matematik", "topic": "Trigonometri (Teoremler, Grafikler)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d6t4", "subject": "AYT Biyoloji", "topic": "Endokrin Sistem", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d6t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-13", "day_of_week": "Perşembe", "day_number": 7,
        "tasks": [
            {"id": "d7t1", "subject": "TYT Matematik", "topic": "Kümeler ve Mantık", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d7t2", "subject": "TYT Fizik", "topic": "Optik (Aynalar)", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d7t3", "subject": "AYT Matematik", "topic": "Logaritma", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d7t4", "subject": "AYT Kimya", "topic": "Çözeltiler", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d7t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Hafta 1 Genel Tekrarı", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-14", "day_of_week": "Cuma", "day_number": 8,
        "tasks": [
            {"id": "d8t1", "subject": "TYT Matematik", "topic": "Fonksiyonlar (TYT Düzeyi)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d8t2", "subject": "TYT Kimya", "topic": "Asitler, Bazlar, Tuzlar", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d8t3", "subject": "AYT Matematik", "topic": "Diziler", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d8t4", "subject": "AYT Fizik", "topic": "Bir Boyutta Hareket (Atışlar)", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d8t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-15", "day_of_week": "Cumartesi", "day_number": 9,
        "tasks": [
            {"id": "d9t1", "subject": "TYT Matematik", "topic": "Permütasyon, Kombinasyon, Olasılık", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d9t2", "subject": "TYT Biyoloji", "topic": "Sınıflandırma", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d9t3", "subject": "AYT Matematik", "topic": "Limit ve Süreklilik", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d9t4", "subject": "AYT Biyoloji", "topic": "Duyu Organları", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d9t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-16", "day_of_week": "Pazar", "day_number": 10,
        "tasks": [
            {"id": "d10t1", "subject": "TYT Matematik", "topic": "İstatistik (Veri Analizi)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d10t2", "subject": "TYT Fizik", "topic": "Elektrik Akımı (Basit Devreler)", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d10t3", "subject": "AYT Matematik", "topic": "Türev (Alma Kuralları, Geometrik Yorum)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d10t4", "subject": "AYT Kimya", "topic": "Kimyasal Tepkimelerde Hız ve Denge", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d10t5", "subject": "Tekrar ve Soru Çözümü", "topic": "Günün Konuları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-17", "day_of_week": "Pazartesi", "day_number": 11,
        "tasks": [
            {"id": "d11t1", "subject": "TYT Matematik", "topic": "Genel Tekrar ve Deneme Soruları", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d11t2", "subject": "TYT Kimya", "topic": "Kimya Her Yerde", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d11t3", "subject": "AYT Matematik", "topic": "İntegral (Alma Kuralları, Belirli İntegral)", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d11t4", "subject": "AYT Fizik", "topic": "İş, Güç, Enerji", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d11t5", "subject": "Tekrar ve Soru Çözümü", "topic": "AYT Matematik Genel Tekrar", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-18", "day_of_week": "Salı", "day_number": 12,
        "tasks": [
            {"id": "d12t1", "subject": "TYT Deneme Sınavı", "topic": "Tamamı", "estimated_time_min": 165, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d12t2", "subject": "TYT Deneme Analizi", "topic": "Hata Analizi", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d12t3", "subject": "AYT Biyoloji", "topic": "Sistemler Genel Tekrar", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d12t4", "subject": "AYT Kimya", "topic": "Dengeler Genel Tekrar", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d12t5", "subject": "Tekrar", "topic": "AYT Fen Konu Tekrarı", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-19", "day_of_week": "Çarşamba", "day_number": 13,
        "tasks": [
            {"id": "d13t1", "subject": "AYT Deneme Sınavı (Sayısal)", "topic": "Tamamı", "estimated_time_min": 180, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d13t2", "subject": "AYT Deneme Analizi", "topic": "Hata Analizi", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d13t3", "subject": "TYT Fizik Hızlı Tekrar", "topic": "Tüm Konular Özet", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d13t4", "subject": "TYT Kimya Hızlı Tekrar", "topic": "Tüm Konular Özet", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d13t5", "subject": "TYT Biyoloji Hızlı Tekrar", "topic": "Tüm Konular Özet", "estimated_time_min": 90, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    },
    {
        "date": "2025-06-20", "day_of_week": "Cuma", "day_number": 14, # Düzeltildi: Perşembe -> Cuma
        "tasks": [
            {"id": "d14t1", "subject": "Son Tekrarlar", "topic": "Zayıf Hissedilen AYT Konuları", "estimated_time_min": 180, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d14t2", "subject": "Formül Tekrarları", "topic": "Tüm Dersler Önemli Formüller", "estimated_time_min": 120, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d14t3", "subject": "Sınav Stratejileri ve Motivasyon", "topic": "Son Hazırlıklar", "estimated_time_min": 60, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0},
            {"id": "d14t4", "subject": "Dinlenme", "topic": "Erken Yatış ve Zihinsel Hazırlık", "estimated_time_min": 0, "status": "Bekliyor", "time_spent_min": 0, "notes": "", "pomodoro_sessions": 0}
        ]
    }
]


class StudyApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("YKS Pro Çalışma Takip Uygulaması")
        self.geometry("1000x750")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.plan_data = self.load_plan_data()
        self.current_day_index = self.find_initial_day_index()

        # Pomodoro Zamanlayıcı Ayarları
        self.pomodoro_work_duration_seconds = 25 * 60
        self.pomodoro_break_duration_seconds = 5 * 60
        self.timer_id = None  # self.after ID'sini tutmak için
        self.time_left_seconds = self.pomodoro_work_duration_seconds
        self.is_timer_running = False
        self.is_timer_paused = False
        self.current_pomodoro_task_id = None
        self.current_pomodoro_cycle = "work" # "work" veya "break"

        # --- Ana Çerçeve ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # --- Üst Çerçeve (Gün Bilgisi ve Navigasyon) ---
        self.header_nav_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_nav_frame.pack(pady=10, padx=10, fill="x")

        self.prev_button = ctk.CTkButton(self.header_nav_frame, text="❮ Önceki Gün", command=self.prev_day, width=120)
        self.prev_button.pack(side="left", padx=(0, 20))

        self.day_label = ctk.CTkLabel(self.header_nav_frame, text="", font=ctk.CTkFont(size=24, weight="bold"))
        self.day_label.pack(side="left", expand=True, fill="x")

        self.next_button = ctk.CTkButton(self.header_nav_frame, text="Sonraki Gün ❯", command=self.next_day, width=120)
        self.next_button.pack(side="right", padx=(20, 0))

        # --- Orta Çerçeve (Görevler ve Zamanlayıcı) ---
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Görevler için Kaydırılabilir Çerçeve (Sol Taraf)
        self.tasks_scrollable_frame = ctk.CTkScrollableFrame(self.content_frame, width=600, corner_radius=10)
        self.tasks_scrollable_frame.pack(side="left", fill="both", expand=True, padx=(0,10))
        self.task_widgets_map = {} # task_id -> {"frame": frame, "check_var": var, ...}

        # Zamanlayıcı ve Notlar Çerçevesi (Sağ Taraf)
        self.timer_notes_frame = ctk.CTkFrame(self.content_frame, width=350, corner_radius=10)
        self.timer_notes_frame.pack(side="right", fill="both", expand=False)
        self.timer_notes_frame.pack_propagate(False) # Boyutun sabit kalması için

        # Zamanlayıcı Ekranı
        self.timer_display_label = ctk.CTkLabel(self.timer_notes_frame, text="25:00", font=ctk.CTkFont(size=60, weight="bold"))
        self.timer_display_label.pack(pady=(30,10))
        
        self.active_task_label = ctk.CTkLabel(self.timer_notes_frame, text="Bir görev seçin", font=ctk.CTkFont(size=14), wraplength=330)
        self.active_task_label.pack(pady=5)

        self.pomodoro_cycle_label = ctk.CTkLabel(self.timer_notes_frame, text="Çalışma Zamanı", font=ctk.CTkFont(size=16))
        self.pomodoro_cycle_label.pack(pady=5)

        self.timer_controls_frame = ctk.CTkFrame(self.timer_notes_frame, fg_color="transparent")
        self.timer_controls_frame.pack(pady=10)

        self.start_pause_button = ctk.CTkButton(self.timer_controls_frame, text="Başlat", command=self.toggle_timer_start_pause, width=100)
        self.start_pause_button.pack(side="left", padx=5)
        self.start_pause_button.configure(state="disabled") # Başlangıçta pasif

        self.reset_button = ctk.CTkButton(self.timer_controls_frame, text="Sıfırla", command=self.reset_timer, width=100)
        self.reset_button.pack(side="left", padx=5)
        self.reset_button.configure(state="disabled")

        # Not Alanı (Basit bir Textbox)
        self.notes_label = ctk.CTkLabel(self.timer_notes_frame, text="Görev Notları:", font=ctk.CTkFont(size=16, weight="bold"))
        self.notes_label.pack(pady=(20,5), anchor="w", padx=20)
        self.notes_textbox = ctk.CTkTextbox(self.timer_notes_frame, height=150, wrap="word", font=ctk.CTkFont(size=13))
        self.notes_textbox.pack(pady=5, padx=20, fill="both", expand=True)
        self.notes_textbox.configure(state="disabled") # Başlangıçta pasif
        self.save_note_button = ctk.CTkButton(self.timer_notes_frame, text="Notu Kaydet", command=self.save_current_task_note)
        self.save_note_button.pack(pady=10, padx=20)
        self.save_note_button.configure(state="disabled")


        # --- Alt Çerçeve (Yardım vb.) ---
        self.bottom_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.bottom_frame.pack(pady=10, padx=10, fill="x")
        
        self.help_button = ctk.CTkButton(self.bottom_frame, text="Bir Konu Hakkında Yardım İste", command=self.show_help_message)
        self.help_button.pack(side="left", padx=10)

        self.total_time_label = ctk.CTkLabel(self.bottom_frame, text="Bugün Toplam Çalışılan: 0dk", font=ctk.CTkFont(size=14))
        self.total_time_label.pack(side="right", padx=10)


        self.update_display()
        self.update_timer_display_text() # Zamanlayıcıyı başlangıç değeriyle göster


    def load_plan_data(self):
        try:
            with open(PLAN_DOSYASI, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Yeni alanlar yoksa ekle (eski plan dosyaları için)
                for day in data:
                    for task in day["tasks"]:
                        task.setdefault("notes", "")
                        task.setdefault("pomodoro_sessions", 0)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            with open(PLAN_DOSYASI, "w", encoding="utf-8") as f:
                json.dump(PLAN_TEMPLATE, f, ensure_ascii=False, indent=4)
            return PLAN_TEMPLATE

    def save_plan_data(self):
        try:
            with open(PLAN_DOSYASI, "w", encoding="utf-8") as f:
                json.dump(self.plan_data, f, ensure_ascii=False, indent=4)
        except IOError:
            messagebox.showerror("Hata", "Plan dosyasına kaydedilemedi.")

    def find_initial_day_index(self):
        for i, day_plan in enumerate(self.plan_data):
            if any(task['status'] != 'Tamamlandı' for task in day_plan['tasks']):
                return i
        return len(self.plan_data) - 1

    def format_time_display(self, minutes):
        if minutes == 0: return "0dk"
        hours = int(minutes // 60)
        mins = int(minutes % 60)
        if hours > 0: return f"{hours}s {mins}d" # "sa" yerine "s", "dk" yerine "d"
        return f"{mins}d"

    def format_seconds_to_mm_ss(self, seconds_total):
        minutes = seconds_total // 60
        seconds = seconds_total % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_display(self):
        current_day_data = self.plan_data[self.current_day_index]
        self.day_label.configure(text=f"Gün {current_day_data['day_number']}: {current_day_data['date']} ({current_day_data['day_of_week']})")

        for widget_id, widget_dict in self.task_widgets_map.items():
            widget_dict["frame"].destroy()
        self.task_widgets_map = {}

        day_total_spent_min = 0

        for task in current_day_data["tasks"]:
            day_total_spent_min += task.get("time_spent_min", 0)

            task_outer_frame = ctk.CTkFrame(self.tasks_scrollable_frame, corner_radius=8, border_width=1)
            task_outer_frame.pack(fill="x", pady=(5,0), padx=5)
            
            # Tıklanabilir başlık çerçevesi
            header_frame = ctk.CTkFrame(task_outer_frame, fg_color="transparent", corner_radius=0)
            header_frame.pack(fill="x", padx=5, pady=3)
            header_frame.bind("<Button-1>", lambda event, t=task: self.select_task_for_timer(t))


            check_var = ctk.StringVar(value="on" if task["status"] == "Tamamlandı" else "off")
            checkbox = ctk.CTkCheckBox(header_frame,
                                       text="", # Metni ayrı label'a taşıyacağız
                                       variable=check_var, onvalue="on", offvalue="off",
                                       command=lambda t=task, v=check_var: self.toggle_task_status(t,v),
                                       width=20)
            checkbox.pack(side="left", padx=(0,5))
            
            task_title_text = f"{task['subject']}: {task['topic']}"
            task_title_label = ctk.CTkLabel(header_frame, text=task_title_text, font=ctk.CTkFont(size=14), anchor="w", wraplength=400)
            task_title_label.pack(side="left", expand=True, fill="x")
            task_title_label.bind("<Button-1>", lambda event, t=task: self.select_task_for_timer(t))


            # Detaylar Çerçevesi (Süre, Pomodoro Sayısı)
            details_frame = ctk.CTkFrame(task_outer_frame, fg_color="transparent", corner_radius=0)
            details_frame.pack(fill="x", padx=10, pady=(0,5))
            details_frame.bind("<Button-1>", lambda event, t=task: self.select_task_for_timer(t))


            time_info_text = f"Tahmini: {self.format_time_display(task['estimated_time_min'])} | Çalışılan: {self.format_time_display(task['time_spent_min'])}"
            time_info_label = ctk.CTkLabel(details_frame, text=time_info_text, font=ctk.CTkFont(size=12), anchor="w")
            time_info_label.pack(side="left")

            pomodoro_info_text = f"Pomodoro: {task.get('pomodoro_sessions', 0)}"
            pomodoro_info_label = ctk.CTkLabel(details_frame, text=pomodoro_info_text, font=ctk.CTkFont(size=12))
            pomodoro_info_label.pack(side="right")
            
            # Aktif görev vurgusu
            if self.current_pomodoro_task_id == task["id"]:
                task_outer_frame.configure(border_color="dodgerblue", border_width=2) # Vurgu rengi
            else:
                 task_outer_frame.configure(border_color=("gray70", "gray30")) # Varsayılan kenarlık


            self.task_widgets_map[task["id"]] = {
                "frame": task_outer_frame, 
                "task_data": task, 
                "check_var": check_var,
                "time_label": time_info_label,
                "pomodoro_label": pomodoro_info_label
            }

        self.total_time_label.configure(text=f"Bugün Toplam Çalışılan: {self.format_time_display(day_total_spent_min)}")
        self.prev_button.configure(state="normal" if self.current_day_index > 0 else "disabled")
        self.next_button.configure(state="normal" if self.current_day_index < len(self.plan_data) - 1 else "disabled")


    def select_task_for_timer(self, task_data):
        if self.is_timer_running and not self.is_timer_paused:
            if messagebox.askyesno("Zamanlayıcı Aktif", "Başka bir görev için zamanlayıcı çalışıyor.\nDuraklatıp bu göreve geçmek ister misiniz?"):
                self.pause_timer() # Önceki zamanlayıcıyı duraklat
            else:
                return # Geçiş yapma

        self.current_pomodoro_task_id = task_data["id"]
        self.active_task_label.configure(text=f"{task_data['subject']}: {task_data['topic']}")
        
        # Notları yükle
        self.notes_textbox.configure(state="normal")
        self.notes_textbox.delete("1.0", "end")
        self.notes_textbox.insert("1.0", task_data.get("notes", ""))
        self.save_note_button.configure(state="normal")
        
        self.reset_timer_logic(reset_cycle_to_work=True) # Yeni görev için zamanlayıcıyı çalışmaya ayarla
        self.start_pause_button.configure(state="normal", text="Başlat")
        self.reset_button.configure(state="normal")
        self.update_display() # Seçili görevi vurgulamak için


    def toggle_task_status(self, task_data, check_var):
        new_status = "Tamamlandı" if check_var.get() == "on" else "Bekliyor"
        task_data["status"] = new_status
        
        # Eğer görev tamamlandıysa ve bu görev için zamanlayıcı çalışıyorsa, durdur.
        if new_status == "Tamamlandı" and self.current_pomodoro_task_id == task_data["id"] and self.is_timer_running:
            self.stop_timer_completely()
            messagebox.showinfo("Görev Tamamlandı", f"'{task_data['topic']}' görevi tamamlandı. Zamanlayıcı durduruldu.")

        self.save_plan_data()
        self.update_display() # Gerekirse arayüzü yenile (özellikle toplam süre için)

    def toggle_timer_start_pause(self):
        if not self.current_pomodoro_task_id:
            messagebox.showwarning("Görev Seçilmedi", "Lütfen önce bir görev seçin.")
            return

        if self.is_timer_running:
            if self.is_timer_paused:
                self.resume_timer()
            else:
                self.pause_timer()
        else:
            self.start_timer()

    def start_timer(self):
        if not self.current_pomodoro_task_id: return
        self.is_timer_running = True
        self.is_timer_paused = False
        self.start_pause_button.configure(text="Duraklat")
        self.countdown()

    def pause_timer(self):
        self.is_timer_paused = True
        self.start_pause_button.configure(text="Devam Et")
        if self.timer_id:
            self.after_cancel(self.timer_id)

    def resume_timer(self):
        self.is_timer_paused = False
        self.start_pause_button.configure(text="Duraklat")
        self.countdown()
        
    def stop_timer_completely(self):
        """Zamanlayıcıyı tamamen durdurur ve sıfırlar, seçili görevi kaldırır."""
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.is_timer_running = False
        self.is_timer_paused = False
        self.time_left_seconds = self.pomodoro_work_duration_seconds
        self.current_pomodoro_cycle = "work"
        self.pomodoro_cycle_label.configure(text="Çalışma Zamanı")
        self.update_timer_display_text()
        self.start_pause_button.configure(text="Başlat", state="disabled" if not self.current_pomodoro_task_id else "normal")
        self.reset_button.configure(state="disabled" if not self.current_pomodoro_task_id else "normal")
        # Aktif görevi de temizleyebiliriz veya kullanıcı yeni bir görev seçene kadar kalabilir.
        # self.current_pomodoro_task_id = None
        # self.active_task_label.configure(text="Bir görev seçin")
        # self.notes_textbox.delete("1.0", "end")
        # self.notes_textbox.configure(state="disabled")
        # self.save_note_button.configure(state="disabled")


    def reset_timer_logic(self, reset_cycle_to_work=True):
        """Zamanlayıcıyı mevcut döngüye göre veya çalışmaya sıfırlar (mantıksal)"""
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.is_timer_running = False
        self.is_timer_paused = False

        if reset_cycle_to_work:
            self.current_pomodoro_cycle = "work"
            self.time_left_seconds = self.pomodoro_work_duration_seconds
            self.pomodoro_cycle_label.configure(text="Çalışma Zamanı")
        elif self.current_pomodoro_cycle == "work":
            self.time_left_seconds = self.pomodoro_work_duration_seconds
            self.pomodoro_cycle_label.configure(text="Çalışma Zamanı")
        else: # break
            self.time_left_seconds = self.pomodoro_break_duration_seconds
            self.pomodoro_cycle_label.configure(text="Mola Zamanı")

        self.update_timer_display_text()
        self.start_pause_button.configure(text="Başlat")


    def reset_timer(self):
        if not self.current_pomodoro_task_id: return
        self.reset_timer_logic(reset_cycle_to_work=True)
        self.start_pause_button.configure(state="normal") # Reset sonrası başlatılabilir olmalı


    def countdown(self):
        if self.is_timer_running and not self.is_timer_paused:
            self.update_timer_display_text()

            if self.time_left_seconds > 0:
                self.time_left_seconds -= 1
                self.timer_id = self.after(1000, self.countdown)
            else: # Süre bitti
                task = self.get_task_by_id(self.current_pomodoro_task_id)
                if not task:
                    self.stop_timer_completely()
                    return

                if self.current_pomodoro_cycle == "work":
                    task["time_spent_min"] = task.get("time_spent_min", 0) + (self.pomodoro_work_duration_seconds // 60)
                    task["pomodoro_sessions"] = task.get("pomodoro_sessions", 0) + 1
                    self.save_plan_data()
                    self.update_task_widget_display(task["id"]) # İlgili görevin etiketlerini güncelle
                    self.update_total_time_today()


                    messagebox.showinfo("Mola Zamanı!", f"Çalışma seansı bitti. Şimdi {self.pomodoro_break_duration_seconds // 60} dakika mola!")
                    self.current_pomodoro_cycle = "break"
                    self.time_left_seconds = self.pomodoro_break_duration_seconds
                    self.pomodoro_cycle_label.configure(text="Mola Zamanı")
                else: # Mola bitti
                    messagebox.showinfo("Çalışma Zamanı!", "Mola bitti. Yeni çalışma seansına başla!")
                    self.current_pomodoro_cycle = "work"
                    self.time_left_seconds = self.pomodoro_work_duration_seconds
                    self.pomodoro_cycle_label.configure(text="Çalışma Zamanı")
                
                # Eğer görev bu pomodoro ile tamamlandıysa kullanıcıya sor
                if task["status"] != "Tamamlandı" and task["time_spent_min"] >= task["estimated_time_min"]:
                    if messagebox.askyesno("Görev Süresi Doldu", f"'{task['topic']}' görevinin tahmini süresini doldurdunuz. Tamamlandı olarak işaretlensin mi?"):
                        task["status"] = "Tamamlandı"
                        self.save_plan_data()
                        if self.task_widgets_map.get(task["id"]):
                             self.task_widgets_map[task["id"]]["check_var"].set("on")


                self.update_timer_display_text() # 00:00 göster, sonra yeni döngü için başlat
                self.start_timer() # Otomatik olarak yeni döngüyü başlat

    def update_timer_display_text(self):
        self.timer_display_label.configure(text=self.format_seconds_to_mm_ss(self.time_left_seconds))

    def update_task_widget_display(self, task_id):
        """Belirli bir görevin UI'daki etiketlerini günceller."""
        if task_id in self.task_widgets_map:
            widget_dict = self.task_widgets_map[task_id]
            task_data = widget_dict["task_data"]
            
            time_info_text = f"Tahmini: {self.format_time_display(task_data['estimated_time_min'])} | Çalışılan: {self.format_time_display(task_data['time_spent_min'])}"
            widget_dict["time_label"].configure(text=time_info_text)
            
            pomodoro_info_text = f"Pomodoro: {task_data.get('pomodoro_sessions', 0)}"
            widget_dict["pomodoro_label"].configure(text=pomodoro_info_text)

    def update_total_time_today(self):
        current_day_data = self.plan_data[self.current_day_index]
        day_total_spent_min = sum(task.get("time_spent_min", 0) for task in current_day_data["tasks"])
        self.total_time_label.configure(text=f"Bugün Toplam Çalışılan: {self.format_time_display(day_total_spent_min)}")


    def get_task_by_id(self, task_id):
        for day_plan in self.plan_data:
            for task in day_plan["tasks"]:
                if task["id"] == task_id:
                    return task
        return None
        
    def save_current_task_note(self):
        if self.current_pomodoro_task_id:
            task = self.get_task_by_id(self.current_pomodoro_task_id)
            if task:
                task["notes"] = self.notes_textbox.get("1.0", "end-1c") # -1c sondaki newline'ı alır
                self.save_plan_data()
                messagebox.showinfo("Not Kaydedildi", f"'{task['topic']}' görevi için notlar kaydedildi.")
            else:
                messagebox.showerror("Hata", "Not kaydedilecek aktif görev bulunamadı.")
        else:
            messagebox.showwarning("Görev Seçilmedi", "Lütfen önce not eklemek için bir görev seçin.")


    def show_help_message(self):
        active_task_topic = "bir konu"
        if self.current_pomodoro_task_id:
            task = self.get_task_by_id(self.current_pomodoro_task_id)
            if task:
                active_task_topic = f"'{task['subject']} - {task['topic']}'"
        else: # Aktif pomodoro görevi yoksa, güncel gündeki ilk bekleyen görevi al
            current_day_data = self.plan_data[self.current_day_index]
            for task_in_day in current_day_data["tasks"]:
                if task_in_day["status"] == "Bekliyor" or task_in_day["status"] == "Devam Ediyor":
                    active_task_topic = f"'{task_in_day['subject']} - {task_in_day['topic']}'"
                    break
        
        message = (
            f"Merhaba! Şu an {active_task_topic} konusu üzerinde çalışmayı düşünüyor olabilirsin.\n\n"
            "Bu konu veya plandaki herhangi bir konu hakkında:\n"
            "- Anlamadığın bir noktayı sormak,\n"
            "- Konu anlatımı istemek,\n"
            "- Örnek soru çözümü görmek,\n"
            "için doğrudan bana (yapay zeka asistanına) bu sohbet ekranından yazabilirsin.\n\n"
            "Uygulamadaki görevi seçerek 'Çalışmaya Başla' butonu ile Pomodoro zamanlayıcısını kullanabilir, notlarını girebilirsin."
        )
        messagebox.showinfo("Yardım ve Destek", message)

    def prev_day(self):
        if self.is_timer_running and not self.is_timer_paused :
             if not messagebox.askyesno("Zamanlayıcı Aktif", "Zamanlayıcı çalışırken gün değiştirmek zamanlayıcıyı durduracaktır. Devam etmek istiyor musunuz?"):
                return
        self.stop_timer_completely() # Gün değiştirirken zamanlayıcıyı sıfırla
        # Notlar ve aktif görev etiketini de temizle
        self.active_task_label.configure(text="Bir görev seçin")
        self.notes_textbox.delete("1.0", "end")
        self.notes_textbox.configure(state="disabled")
        self.save_note_button.configure(state="disabled")
        self.current_pomodoro_task_id = None


        if self.current_day_index > 0:
            self.current_day_index -= 1
            self.update_display()

    def next_day(self):
        if self.is_timer_running and not self.is_timer_paused :
             if not messagebox.askyesno("Zamanlayıcı Aktif", "Zamanlayıcı çalışırken gün değiştirmek zamanlayıcıyı durduracaktır. Devam etmek istiyor musunuz?"):
                return
        self.stop_timer_completely()
        self.active_task_label.configure(text="Bir görev seçin")
        self.notes_textbox.delete("1.0", "end")
        self.notes_textbox.configure(state="disabled")
        self.save_note_button.configure(state="disabled")
        self.current_pomodoro_task_id = None


        if self.current_day_index < len(self.plan_data) - 1:
            self.current_day_index += 1
            self.update_display()
            
    def on_closing(self):
        """Pencere kapatılırken çağrılır."""
        if self.is_timer_running and not self.is_timer_paused:
            if messagebox.askyesno("Çıkış Onayı", "Aktif bir zamanlayıcı çalışıyor. Yine de çıkmak istediğinize emin misiniz? (Çalışılan süre kaydedilmeyecek)"):
                self.destroy()
            else:
                return # Kapatma
        else:
            self.destroy()


if __name__ == "__main__":
    app = StudyApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing) # Kapatma butonuna basıldığında on_closing'i çağır
    app.mainloop()
