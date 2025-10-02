# settings/config.py
import json
import os
from dataclasses import dataclass, asdict

CONFIG_PATH = "app_config.json"

@dataclass
class AppConfig:
    app_title: str = "Secure Modular Starter"
    default_language: str = "en"
    default_theme: str = "modern_light"  # ✅ غيرها إلى ثيم موجود
    allowed_themes: tuple = ("modern_light", "professional_dark", "warm_earth")  # ✅ حدّث القائمة
    logo_path: str = ""
    
    @staticmethod
    def load():
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            return AppConfig(**data)
        cfg = AppConfig()
        cfg.save()
        return cfg

    def save(self):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, ensure_ascii=False, indent=2)

    def update(self, **kwargs):
        for k,v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        self.save()
