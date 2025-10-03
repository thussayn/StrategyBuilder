# core/file_utils.py
import os
import streamlit as st
import time

def validate_logo_file(uploaded_file):
    """التحقق من صحة ملف اللوجو"""
    # التحقق من الحجم (5MB)
    max_size = 5 * 1024 * 1024
    if uploaded_file.size > max_size:
        raise ValueError("حجم الشعار يتجاوز الحد المسموح 5MB")
    
    # التحقق من الامتداد
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()
    allowed_extensions = (".png", ".jpg", ".jpeg")
    if file_ext not in allowed_extensions:
        raise ValueError("صيغة الشعار غير صالحة. المسموح: PNG, JPG, JPEG")
    
    return True

def save_logo_file(uploaded_file, username, strategy_id):
    """حفظ ملف اللوجو وإرجاع المسار"""
    try:
        # استخدام assets/logos كمجلد للحفظ
        upload_folder = "assets/logos"
        
        # إنشاء المجلد إذا لم يكن موجوداً
        os.makedirs(upload_folder, exist_ok=True)
        
        # إنشاء اسم فريد للملف
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()
        filename = f"{username}_{strategy_id}_{int(time.time())}{file_ext}"
        file_path = os.path.join(upload_folder, filename)
        
        # حفظ الملف
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
        
    except Exception as e:
        st.error(f"خطأ في رفع الشعار: {str(e)}")
        return None

def delete_logo_file(logo_path):
    """حذف ملف اللوجو"""
    try:
        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)
            return True
    except Exception:
        pass
    return False

def get_logo_url(logo_path):
    """الحصول على رابط اللوجو للعرض"""
    if not logo_path or not os.path.exists(logo_path):
        return None
    
    return logo_path