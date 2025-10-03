# StrategyBuilder
StrategyBuilder/
│
├── app.db                # قاعدة بيانات المشروع
├── app.py                # نقطة الدخول الرئيسية للمشروع
├── AppTemplate.zip       # الملف المضغوط الذي يحتوي على مكونات المشروع
├── app_config.json       # إعدادات التطبيق بتنسيق JSON
├── Project Definition.txt # وثيقة تعريف المشروع
│
├── .streamlit            # ملفات إعدادات Streamlit
│   └── config.toml       # إعدادات خاصة بمنصة Streamlit
│
├── .vscode               # إعدادات بيئة التطوير Visual Studio Code
│   └── launch.json       # إعدادات تشغيل المشروع في VS Code
│
├── assets                # مجلد يحتوي على الأصول مثل الصور
│   └── logos             # مجلد يحتوي على شعارات التطبيق
│
├── core                  # الملفات الأساسية في المشروع
│   ├── i18n.py           # ملفات الترجمات (i18n)
│   ├── layout.py         # تصميم الواجهة
│   ├── security.py       # معالجة الأمان
│   ├── theme.py          # إعدادات السمة والتصميم
│   ├── file_utils.py     # لإدارة ملفات اللوجوهات
│   └── __init__.py       # ملف لتحديد المجلد كمكتبة
│   └── __pycache__/      # ملفات بايثون المترجمة
│
├── data                  # ملفات تتعلق بالبيانات والنماذج
│   ├── db.py             # معالجة قاعدة البيانات
│   ├── models.py         # تعريف النماذج
│   ├── seed.py           # تحميل البيانات الأولية (seed data)
│   ├── بنك_الاستراتيجية v2.0.xlsx         # ملف بنك الاستراتيجيات
│   ├── strategy_bank_loader.py # التعامل مع بيانات الاستراتيجيات
│   └── __pycache__/      # ملفات بايثون المترجمة
│
├── features              # خصائص التطبيق المختلفة
│   ├── about.py          # صفحة عن المشروع
│   ├── auth.py           # معالجة المصادقة (Authentication)
│   ├── dashboard_admin.py # لوحة تحكم المسؤول
│   ├── dashboard_editor.py # لوحة تحكم المحرر
│   ├── dashboard_viewer.py # لوحة تحكم المشاهد
│   ├── home.py           # الصفحة الرئيسية
│   ├── strategy_management.py # صفحة إدارة الاستراتيجيات
│   └── __pycache__/      # ملفات بايثون المترجمة
│
├── settings              # ملفات الإعدادات الخاصة بالمشروع
│   ├── config.py         # إعدادات النظام
│   ├── user_settings.py  # إعدادات المستخدم
│   └── __pycache__/      # ملفات بايثون المترجمة
│
├── ui                    # ملفات واجهة المستخدم
│   ├── forms.py          # تعريف النماذج في واجهة المستخدم
│   └── __pycache__/      # ملفات بايثون المترجمة
├── Fonts                 # الخطوط المستخدمة في التصدير
│   ├── Amiri-Bold.ttf
│   ├── Amiri-BoldItalic.ttf
│   ├── Amiri-Italic.ttf
│   ├── Amiri-Regular.ttf
│   ├── NotoNaskhArabic-Bold.ttf
│   ├── NotoNaskhArabic-Medium.ttf
│   ├── NotoNaskhArabic-Regular.ttf
│   ├── NotoNaskhArabic-VariableFont_wght.ttf
│   ├── Tajawal-Black.ttf
│   ├── Tajawal-Bold.ttf
│   ├── Tajawal-ExtraBold.ttf
│   ├── Tajawal-ExtraLight.ttf
│   ├── Tajawal-Light.ttf
│   ├── Tajawal-Medium.ttf
│   └── Tajawal-Regular.ttf
└── users                 # معالجة المستخدمين والمصادقة
    ├── auth_service.py   # خدمة المصادقة للمستخدمين
    └── __pycache__/      # ملفات بايثون المترجمة

