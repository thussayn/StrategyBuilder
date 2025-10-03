# data/strategy_elements.py
from typing import Dict, List, Set
from data.strategy_bank_loader import load_strategy_bank
from data.models import get_custom_elements

def get_all_visions(username: str) -> List[str]:
    """يُرجع جميع الرؤى: من البنك + المخصصة للمستخدم."""
    bank_data = load_strategy_bank()
    bank_visions = list(bank_data.keys())
    custom_visions = [item["text"] for item in get_custom_elements(username, "vision")]
    
    # دمج + إزالة التكرار مع الحفاظ على الترتيب
    seen = set()
    all_visions = []
    for v in bank_visions + custom_visions:
        if v and v not in seen:
            all_visions.append(v)
            seen.add(v)
    return all_visions


def get_messages_for_vision(vision: str, username: str) -> List[str]:
    """يُرجع جميع الرسائل المرتبطة برؤية معينة: من البنك + المخصصة."""
    bank_data = load_strategy_bank()
    bank_messages = list(bank_data.get(vision, {}).keys())
    custom_messages = [item["text"] for item in get_custom_elements(username, "message")]
    
    seen = set()
    all_messages = []
    for m in bank_messages + custom_messages:
        if m and m not in seen:
            all_messages.append(m)
            seen.add(m)
    return all_messages


def get_all_objectives(username: str) -> List[str]:
    """يُرجع جميع الأهداف من البنك (كلها) + المخصصة."""
    bank_data = load_strategy_bank()
    bank_objectives: Set[str] = set()
    for vision_dict in bank_data.values():
        for msg_dict in vision_dict.values():
            bank_objectives.update(obj.strip() for obj in msg_dict["objectives"] if obj.strip())
    
    custom_objectives = [item["text"] for item in get_custom_elements(username, "objective") if item["text"].strip()]
    
    # فرز الأهداف من البنك، ثم إضافة المخصصة في النهاية
    all_objectives = sorted(bank_objectives) + custom_objectives
    seen = set()
    unique = []
    for obj in all_objectives:
        clean_obj = obj.strip()
        if clean_obj and clean_obj not in seen:
            unique.append(clean_obj)
            seen.add(clean_obj)
    return unique


def get_all_values(username: str) -> List[str]:
    """يُرجع جميع القيم من البنك (كلها) + المخصصة."""
    bank_data = load_strategy_bank()
    bank_values: Set[str] = set()
    for vision_dict in bank_data.values():
        for msg_dict in vision_dict.values():
            bank_values.update(val.strip() for val in msg_dict["values"] if val.strip())
    
    custom_values = [item["text"] for item in get_custom_elements(username, "value") if item["text"].strip()]
    
    all_values = sorted(bank_values) + custom_values
    seen = set()
    unique = []
    for val in all_values:
        clean_val = val.strip()
        if clean_val and clean_val not in seen:
            unique.append(clean_val)
            seen.add(clean_val)
    return unique

def get_objectives_for_vision_and_message(vision: str, message: str, username: str) -> List[str]:
    """
    يُرجع قائمة الأهداف المرتبطة برؤية ورسالة محددة من بنك الاستراتيجية (Excel).
    لا يُرجع العناصر المخصصة لأنها غير مرتبطة برسالة محددة.
    """
    bank_data = load_strategy_bank()
    objectives_set: Set[str] = set()
    
    if vision in bank_data and message in bank_data[vision]:
        objectives_set.update(obj.strip() for obj in bank_data[vision][message]["objectives"] if obj.strip())
    
    return sorted(list(objectives_set))


def get_values_for_vision_and_message(vision: str, message: str, username: str) -> List[str]:
    """
    يُرجع قائمة القيم المرتبطة برؤية ورسالة محددة من بنك الاستراتيجية (Excel).
    """
    bank_data = load_strategy_bank()
    values_set: Set[str] = set()
    
    if vision in bank_data and message in bank_data[vision]:
        values_set.update(val.strip() for val in bank_data[vision][message]["values"] if val.strip())
    
    return sorted(list(values_set))