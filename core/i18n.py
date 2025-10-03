# core/i18n.py
import streamlit as st

LANGS = {
    "en": {"label": "English", "dir": "ltr"},
    "ar": {"label": "العربية", "dir": "rtl"},
}

_DEF_TEXTS = {
    # === App Structure ===
    "app_title": {"en": "Secure Modular Starter", "ar": "قالب ستريمليت آمن ومنظّم"},
    "language": {"en": "Language", "ar": "اللغة"},
    "theme": {"en": "Theme", "ar": "الثيم"},
    "logout": {"en": "Log out", "ar": "تسجيل الخروج"},
    "home_title": {"en": "Home", "ar": "الصفحة الرئيسية"},
    "about_title": {"en": "About", "ar": "حول"},
    "about_content": {
        "en": "This is the About page of the Secure Modular Starter application.",
        "ar": "هذه هي صفحة حول تطبيق Secure Modular Starter."
    },
    "dashboard": {"en": "Dashboard", "ar": "لوحة التحكم"},
    "settings": {"en": "Settings", "ar": "الإعدادات"},
    "welcome_msg": {"en": "Welcome to your secure starter!", "ar": "مرحبًا بك في القالب الآمن!"},
    "app_title_label": {"en": "App Title", "ar": "عنوان التطبيق"},

    # === Authentication ===
    "login": {"en": "Login", "ar": "تسجيل الدخول"},
    "username": {"en": "Username", "ar": "اسم المستخدم"},
    "password": {"en": "Password", "ar": "كلمة المرور"},
    "remember_me": {"en": "Remember me", "ar": "تذكرني"},
    "login_button": {"en": "Login", "ar": "تسجيل الدخول"},
    "logged_in_success": {"en": "Logged in successfully!", "ar": "تم تسجيل الدخول بنجاح!"},
    "logged_out_success": {"en": "You have been logged out successfully.", "ar": "تم تسجيل الخروج بنجاح."},

    # === User Management ===
    "create_new_user": {"en": "Create New User", "ar": "إنشاء مستخدم جديد"},
    "create_user_button": {"en": "Create User", "ar": "إنشاء مستخدم"},
    "user_created_success": {"en": "User created successfully!", "ar": "تم إنشاء المستخدم بنجاح!"},
    "role": {"en": "Role", "ar": "الدور"},
    "admin": {"en": "Admin", "ar": "مسؤول"},
    "editor": {"en": "Editor", "ar": "محرر"},
    "viewer": {"en": "Viewer", "ar": "مشاهد"},

    # === Settings Form ===
    "save": {"en": "Save", "ar": "حفظ"},
    "cancel": {"en": "Cancel", "ar": "إلغاء"},
    "settings_saved": {"en": "Settings saved successfully!", "ar": "تم حفظ الإعدادات بنجاح!"},
    "must_be_logged_in": {
        "en": "You must be logged in to access settings.",
        "ar": "يجب تسجيل الدخول للوصول إلى الإعدادات."
    },
    "current_theme": {"en": "Current Theme", "ar": "الثيم الحالي"},
    "theme_change_hint": {
        "en": "💡 To change the theme, please use the theme selector in the sidebar.",
        "ar": "💡 لتغيير الثيم، يرجى استخدام محدد الثيم في الشريط الجانبي."
    },
    "back_to_home": {"en": "← Back to Home", "ar": "← العودة للرئيسية"},

    # === Language & Theme Options ===
    "language_selector_label": {"en": "Language", "ar": "اللغة"},
    "theme_selector_label": {"en": "Theme", "ar": "الثيم"},
    "english": {"en": "English", "ar": "الإنجليزية"},
    "arabic": {"en": "Arabic", "ar": "العربية"},
    
    # === الثيمات الجديدة ===
    "modern_light": {"en": "Modern Light", "ar": "فاتح عصري"},
    "professional_dark": {"en": "Professional Dark", "ar": "داكن احترافي"},
    "warm_earth": {"en": "Warm Earth", "ar": "ألوان الأرض"},
    "saudi": {"en": "Saudi", "ar": "سعودي"},
    "soft": {"en": "Soft", "ar": "رقيق"},
    
    # === الثيمات القديمة (للتوافق) ===
    "light": {"en": "Light", "ar": "فاتح"},
    "dark": {"en": "Dark", "ar": "داكن"},

    # === Dashboard Titles ===
    "home_page_title": {"en": "Home Page", "ar": "الصفحة الرئيسية"},
    "home_page_welcome": {"en": "Welcome to the Home page!", "ar": "مرحبًا بك في الصفحة الرئيسية!"},
    "admin_dashboard_title": {"en": "Admin Dashboard", "ar": "لوحة تحكم المسؤول"},
    "admin_dashboard_welcome": {"en": "Welcome, Admin!", "ar": "مرحبًا، أيها المسؤول!"},
    "editor_dashboard_title": {"en": "Editor Dashboard", "ar": "لوحة تحكم المحرر"},
    "editor_dashboard_welcome": {"en": "Welcome, Editor!", "ar": "مرحبًا، أيها المحرر!"},
    "viewer_dashboard_title": {"en": "Viewer Dashboard", "ar": "لوحة تحكم المشاهد"},
    "viewer_dashboard_welcome": {"en": "Welcome, Viewer!", "ar": "مرحبًا، أيها المشاهد!"},

    # === Strategy Management ===
    "strategy_management": {"en": "Strategy Management", "ar": "إدارة الاستراتيجيات"},
    "select_vision": {"en": "Select Vision", "ar": "اختر رؤية"},
    "select_message": {"en": "Select Message", "ar": "اختر رسالة"},
    "strategic_objectives": {"en": "Strategic Objectives", "ar": "الأهداف الاستراتيجية"},
    "strategic_values": {"en": "Strategic Values", "ar": "القيم الاستراتيجية"},
    "strategy_name": {"en": "Strategy Name", "ar": "اسم الاستراتيجية"},
    "strategy_description": {"en": "Description (Optional)", "ar": "الوصف (اختياري)"},
    "save_strategy": {"en": "Save Strategy", "ar": "حفظ الاستراتيجية"},
    "saved_strategies": {"en": "Saved Strategies", "ar": "الاستراتيجيات المحفوظة"},
    "no_saved_strategies": {"en": "No saved strategies yet.", "ar": "لا توجد استراتيجيات محفوظة بعد."},
    
    # === Strategy Builder - Extended ===
    "create_new_strategy": {"en": "Create New Strategy", "ar": "إنشاء استراتيجية جديدة"},
    "preview_and_save": {"en": "Preview & Save", "ar": "معاينة وحفظ"},
    "edit_or_create_vision": {"en": "Edit or create vision:", "ar": "عدّل أو أنشئ رؤية:"},
    "edit_or_create_message": {"en": "Edit or create message:", "ar": "عدّل أو أنشئ رسالة:"},
    "or_add_new_objective": {"en": "Add new objective", "ar": "أضف هدفًا جديدًا"},
    "or_add_new_value": {"en": "Add new value", "ar": "أضف قيمة جديدة"},
    "add_objective": {"en": "Add Objective", "ar": "إضافة هدف"},
    "add_value": {"en": "Add Value", "ar": "إضافة قيمة"},
    "back": {"en": "Back", "ar": "السابق"},
    "save_and_continue": {"en": "Save & Continue", "ar": "حفظ والمتابعة"},
    "strategy_name_required": {"en": "Strategy name is required", "ar": "اسم الاستراتيجية مطلوب"},
    "strategy_saved_success": {"en": "Strategy saved successfully!", "ar": "تم حفظ الاستراتيجية بنجاح!"},
    "export_to_word": {"en": "Export to Word", "ar": "تصدير إلى Word"},
    "export_to_pdf": {"en": "Export to PDF", "ar": "تصدير إلى PDF"},
    "download_word_file": {"en": "Download Word File", "ar": "تنزيل ملف Word"},
    "use_browser_print_for_pdf": {
        "en": "Use your browser's Print → Save as PDF to export this strategy.",
        "ar": "استخدم طباعة المتصفح → حفظ كـ PDF لتصدير هذه الاستراتيجية."
    },
    "edit": {"en": "Edit", "ar": "تعديل"},
    "delete": {"en": "Delete", "ar": "حذف"},
    "view": {"en": "View", "ar": "عرض"},
    "error_deleting_strategy": {"en": "Error deleting strategy.", "ar": "خطأ أثناء حذف الاستراتيجية."},
    "strategy_deleted_success": {"en": "Strategy deleted successfully.", "ar": "تم حذف الاستراتيجية بنجاح."},
    "please_select_vision_first": {"en": "Please select a vision first.", "ar": "يرجى اختيار رؤية أولاً."},
    "back_to_strategy_list": {"en": "Back to Strategy List", "ar": "العودة إلى قائمة الاستراتيجيات"},
    "vision_cannot_be_empty": {"en": "Vision cannot be empty.", "ar": "لا يمكن أن تكون الرؤية فارغة."},
    "message_cannot_be_empty": {"en": "Message cannot be empty.", "ar": "لا يمكن أن تكون الرسالة فارغة."},
    
    # === Strategy Builder - Dialogs ===
    "browse_visions": {"en": "Browse Visions", "ar": "استعراض الرؤى"},
    "browse_messages": {"en": "Browse Messages", "ar": "استعراض الرسائل"},
    "select_vision_from_list": {"en": "Select from available visions", "ar": "اختر من الرؤى المتاحة"},
    "select_message_from_list": {"en": "Select from available messages", "ar": "اختر من الرسائل المتاحة"},
    "confirm_selection": {"en": "Confirm Selection", "ar": "تأكيد الاختيار"},
    "no_visions_available": {"en": "No visions available.", "ar": "لا توجد رؤى متاحة."},
    "no_messages_available": {"en": "No messages available for this vision.", "ar": "لا توجد رسائل متاحة لهذه الرؤية."},
    "update_from_list": {"en": "Update from list", "ar": "تحديث من القائمة"},
    "select_vision_from_list": {"en": "Select a vision from the list", "ar": "اختر رؤية من القائمة"},
    # === Strategy Builder - Objectives ===
    "objectives_linked_to_message": {"en": "Objectives linked to the message", "ar": "الأهداف المرتبطة بالرسالة"},
    "all_bank_objectives": {"en": "All objectives from the bank", "ar": "جميع أهداف البنك"},
    "select_from_linked_objectives": {"en": "Select from linked objectives", "ar": "اختر من الأهداف المرتبطة"},
    "select_from_all_objectives": {"en": "Select from all objectives", "ar": "اختر من جميع الأهداف"},
    "no_linked_objectives": {"en": "No objectives linked to this message.", "ar": "لا توجد أهداف مرتبطة بهذه الرسالة."},
    "selected_objectives": {"en": "Selected Objectives", "ar": "الأهداف المختارة"},
    "no_objectives_selected": {"en": "No objectives selected yet.", "ar": "لم يتم اختيار أي أهداف بعد."},
    "select_strategic_values": {"en": "Select strategic values", "ar": "اختر القيم الاستراتيجية"},

    # === Strategy Builder - Values ===
    "values_linked_to_message": {"en": "Values linked to the message", "ar": "القيم المرتبطة بالرسالة"},
    "all_bank_values": {"en": "All values from the bank", "ar": "جميع القيم من البنك"},
    "select_from_linked_values": {"en": "Select from linked values", "ar": "اختر من القيم المرتبطة"},
    "select_from_all_values": {"en": "Select from all values", "ar": "اختر من جميع القيم"},
    "no_linked_values": {"en": "No values linked to this message.", "ar": "لا توجد قيم مرتبطة بهذه الرسالة."},
    "selected_values": {"en": "Selected Values", "ar": "القيم المختارة"},
    "no_values_selected": {"en": "No values selected yet.", "ar": "لم يتم اختيار أي قيم بعد."},
    
    # === Logo Management ===
    "upload_logo": {"en": "Upload Logo", "ar": "رفع الشعار"},
    "change_logo": {"en": "Change Logo", "ar": "تغيير الشعار"},
    "remove_logo": {"en": "Remove Logo", "ar": "إزالة الشعار"},
    "logo_uploaded_success": {"en": "Logo uploaded successfully!", "ar": "تم رفع الشعار بنجاح!"},
    "logo_removed_success": {"en": "Logo removed successfully!", "ar": "تم إزالة الشعار بنجاح!"},
    "logo_upload_error": {"en": "Error uploading logo", "ar": "خطأ في رفع الشعار"},
    "logo_size_exceeded": {"en": "Logo size exceeds 5MB limit", "ar": "حجم الشعار يتجاوز الحد المسموح 5MB"},
    "invalid_logo_format": {"en": "Invalid logo format. Allowed: PNG, JPG, JPEG", "ar": "صيغة الشعار غير صالحة. المسموح: PNG, JPG, JPEG"},
    "current_logo": {"en": "Current Logo", "ar": "الشعار الحالي"},
    "no_logo_uploaded": {"en": "No logo uploaded", "ar": "لا يوجد شعار مرفوع"},
    "logo_will_appear_in_exports": {"en": "Logo will appear in strategy details and exports", "ar": "سيظهر الشعار في تفاصيل الاستراتيجية وعمليات التصدير"},

    # === Auth Error Messages ===
    "missing_credentials": {"en": "Missing credentials", "ar": "بيانات الاعتماد مفقودة"},
    "user_not_found": {"en": "User not found", "ar": "المستخدم غير موجود"},
    "invalid_password": {"en": "Invalid password", "ar": "كلمة المرور غير صحيحة"},
    "username_password_required": {"en": "Username and password are required", "ar": "اسم المستخدم وكلمة المرور مطلوبان"},
    "username_exists": {"en": "Username already exists", "ar": "اسم المستخدم موجود مسبقًا"},
    "unknown_error": {"en": "An unknown error occurred", "ar": "حدث خطأ غير معروف"},
    "ok": {"en": "OK", "ar": "تم"},

    # === Generic ===
    "yes": {"en": "Yes", "ar": "نعم"},
    "no": {"en": "No", "ar": "لا"},
    "error": {"en": "Error", "ar": "خطأ"},
    "success": {"en": "Success", "ar": "نجاح"},
    "are_you_sure": {"en": "Are you sure?", "ar": "هل أنت متأكد؟"},
    "save_changes": {"en": "Save Changes", "ar": "حفظ التغييرات"},
    "loading": {"en": "Loading...", "ar": "جاري التحميل..."},
    "no_data": {"en": "No data available", "ar": "لا توجد بيانات متاحة"},

}

def get_text(key: str) -> str:
    """استرجاع النص المترجم حسب اللغة الحالية."""
    lang = st.session_state.get("lang", "en")
    if lang not in LANGS:
        lang = "en"  # fallback إلى الإنجليزية إذا كانت اللغة غير مدعومة

    # استرجاع النص من _DEF_TEXTS
    if key in _DEF_TEXTS:
        return _DEF_TEXTS[key].get(lang, _DEF_TEXTS[key].get("en", key))

    # fallback - تسجيل النص المفقود
    print(f"⚠️ Missing translation: {key} (lang: {lang})")
    return f"[{key}]"

def init_language(default: str = "en"):
    """تهيئة اللغة الافتراضية في حالة عدم وجودها في الجلسة."""
    if "lang" not in st.session_state:
        st.session_state.lang = default