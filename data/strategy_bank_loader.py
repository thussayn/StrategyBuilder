#strategy_bank_loader.py
import os
import pandas as pd
from typing import Dict, List

# المسار النسبي لملف Excel (يجب أن يكون في مجلد data/)
BANK_FILE_PATH = os.path.join(os.path.dirname(__file__), "بنك_الاستراتيجية v2.0.xlsx")

def load_strategy_bank() -> Dict[str, Dict[str, Dict[str, List[str]]]]:
    """
    يحمّل بنك الاستراتيجية من ملف Excel ويعيده كبنية هرمية:
    {
        "الرؤية 1": {
            "الرسالة 1": {
                "objectives": ["هدف 1", "هدف 2", ..., "هدف 6"],
                "values": ["قيمة 1", "قيمة 2", ..., "قيمة 6"]
            },
            ...
        },
        ...
    }
    """
    if not os.path.exists(BANK_FILE_PATH):
        raise FileNotFoundError(f"لم يتم العثور على ملف بنك الاستراتيجية: {BANK_FILE_PATH}")

    # قراءة ملف Excel
    df = pd.read_excel(BANK_FILE_PATH, sheet_name="بنك الاستراتيجية")

    # التأكد من وجود الأعمدة المطلوبة
    required_columns = ["الرؤية", "الرسالة", "الهدف", "القيمة"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"العمود '{col}' غير موجود في ملف Excel")

    # إزالة الصفوف الفارغة
    df = df.dropna(subset=["الرؤية", "الرسالة", "الهدف", "القيمة"])

    # بناء البنية الهرمية
    strategy_bank = {}

    for _, row in df.iterrows():
        vision = str(row["الرؤية"]).strip()
        message = str(row["الرسالة"]).strip()
        objective = str(row["الهدف"]).strip()
        value = str(row["القيمة"]).strip()

        if vision not in strategy_bank:
            strategy_bank[vision] = {}

        if message not in strategy_bank[vision]:
            strategy_bank[vision][message] = {
                "objectives": [],
                "values": []
            }

        # تجنب التكرار (اختياري)
        if objective not in strategy_bank[vision][message]["objectives"]:
            strategy_bank[vision][message]["objectives"].append(objective)
        if value not in strategy_bank[vision][message]["values"]:
            strategy_bank[vision][message]["values"].append(value)

    return strategy_bank