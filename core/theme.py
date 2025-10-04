import streamlit as st
import time
from .i18n import LANGS

THEMES = {
    "modern_light": {
        "--brand": "#3B82F6",
        "--bg": "#FFFFFF",
        "--panel": "#F8FAFC", 
        "--text": "#1E293B",
        "--muted": "#64748B",
        "--accent": "#10B981",
        "--tab-bg": "#F1F5F9",
        "--tab-text": "#475569",
        "--tab-active-bg": "#3B82F6",
        "--tab-active-text": "#FFFFFF",
        "--tab-hover-bg": "#E2E8F0",
        "--tab-hover-text": "#334155",
        "--input-bg": "#FFFFFF",
        "--input-text": "#1E293B",
        "--input-border": "#CBD5E1",
        "--input-focus-border": "#3B82F6",
        "--input-focus-bg": "#FFFFFF",
        "--dropdown-bg": "#FFFFFF",
        "--dropdown-text": "#1E293B",
        "--dropdown-hover-bg": "#F1F5F9",
        "--dropdown-hover-text": "#1E293B",
        "--dropdown-border": "#CBD5E1",
        "--checkbox-bg": "#FFFFFF",
        "--checkbox-border": "#CBD5E1",
        "--checkbox-checked-bg": "#3B82F6",
        "--radio-bg": "#FFFFFF",
        "--radio-border": "#CBD5E1",
        "--radio-checked-bg": "#3B82F6",
        "--slider-bg": "#E2E8F0",
        "--slider-progress": "#3B82F6",
        "--slider-handle": "#3B82F6",
    },
    "professional_dark": {
        "--brand": "#6366F1",
        "--bg": "#0F172A",
        "--panel": "#1E293B",
        "--text": "#F1F5F9",
        "--muted": "#94A3B8",
        "--accent": "#F59E0B",
        "--tab-bg": "#1E293B",
        "--tab-text": "#CBD5E1",
        "--tab-active-bg": "#6366F1",
        "--tab-active-text": "#FFFFFF",
        "--tab-hover-bg": "#334155",
        "--tab-hover-text": "#F1F5F9",
        "--input-bg": "#1E293B",
        "--input-text": "#F1F5F9",
        "--input-border": "#475569",
        "--input-focus-border": "#6366F1",
        "--input-focus-bg": "#1E293B",
        "--dropdown-bg": "#1E293B",
        "--dropdown-text": "#F1F5F9",
        "--dropdown-hover-bg": "#334155",
        "--dropdown-hover-text": "#F1F5F9",
        "--dropdown-border": "#475569",
        "--checkbox-bg": "#1E293B",
        "--checkbox-border": "#475569",
        "--checkbox-checked-bg": "#6366F1",
        "--radio-bg": "#1E293B",
        "--radio-border": "#475569",
        "--radio-checked-bg": "#6366F1",
        "--slider-bg": "#334155",
        "--slider-progress": "#6366F1",
        "--slider-handle": "#6366F1",
    },
    "warm_earth": {
        "--brand": "#D97706",
        "--bg": "#FEF7ED",
        "--panel": "#FDE68A",
        "--text": "#451A03",
        "--muted": "#92400E",
        "--accent": "#65A30D",
        "--tab-bg": "#FDE68A",
        "--tab-text": "#78350F",
        "--tab-active-bg": "#D97706",
        "--tab-active-text": "#FFFFFF",
        "--tab-hover-bg": "#FCD34D",
        "--tab-hover-text": "#451A03",
        "--input-bg": "#FFFFFF",
        "--input-text": "#451A03",
        "--input-border": "#D97706",
        "--input-focus-border": "#B45309",
        "--input-focus-bg": "#FFFFFF",
        "--dropdown-bg": "#FFFFFF",
        "--dropdown-text": "#451A03",
        "--dropdown-hover-bg": "#FEF3C7",
        "--dropdown-hover-text": "#451A03",
        "--dropdown-border": "#D97706",
        "--checkbox-bg": "#FFFFFF",
        "--checkbox-border": "#D97706",
        "--checkbox-checked-bg": "#D97706",
        "--radio-bg": "#FFFFFF",
        "--radio-border": "#D97706",
        "--radio-checked-bg": "#D97706",
        "--slider-bg": "#FDE68A",
        "--slider-progress": "#D97706",
        "--slider-handle": "#D97706",
    },
    "saudi": {
        "--brand": "#0B4F32",
        "--bg": "#082E1F",
        "--panel": "#0B3A26",
        "--text": "#E0F0E9",
        "--muted": "#A0C9B8",
        "--accent": "#4CAF50",
        "--tab-bg": "#0D422D",
        "--tab-text": "#B0D8CA",
        "--tab-active-bg": "#0B4F32",
        "--tab-active-text": "#FFFFFF",
        "--tab-hover-bg": "#105A38",
        "--tab-hover-text": "#E0F0E9",
        "--input-bg": "#0C3528",
        "--input-text": "#E0F0E9",
        "--input-border": "#1A5A42",
        "--input-focus-border": "#4CAF50",
        "--input-focus-bg": "#0C3528",
        "--dropdown-bg": "#0B3A26",
        "--dropdown-text": "#E0F0E9",
        "--dropdown-hover-bg": "#105A38",
        "--dropdown-hover-text": "#FFFFFF",
        "--dropdown-border": "#1A5A42",
        "--checkbox-bg": "#0C3528",
        "--checkbox-border": "#1A5A42",
        "--checkbox-checked-bg": "#0B4F32",
        "--radio-bg": "#0C3528",
        "--radio-border": "#1A5A42",
        "--radio-checked-bg": "#0B4F32",
        "--slider-bg": "#1A5A42",
        "--slider-progress": "#4CAF50",
        "--slider-handle": "#0B4F32",
    },
    "soft": {
        "--brand": "#E91E63",
        "--bg": "#FFF9F9",
        "--panel": "#FFECEC",
        "--text": "#5A3E4A",
        "--muted": "#A87C89",
        "--accent": "#FF6B6B",
        "--tab-bg": "#FFE0E0",
        "--tab-text": "#7A5C68",
        "--tab-active-bg": "#E91E63",
        "--tab-active-text": "#FFFFFF",
        "--tab-hover-bg": "#FFD1D1",
        "--tab-hover-text": "#5A3E4A",
        "--input-bg": "#FFFFFF",
        "--input-text": "#5A3E4A",
        "--input-border": "#F8BBD0",
        "--input-focus-border": "#E91E63",
        "--input-focus-bg": "#FFFFFF",
        "--dropdown-bg": "#FFFFFF",
        "--dropdown-text": "#5A3E4A",
        "--dropdown-hover-bg": "#FFF0F0",
        "--dropdown-hover-text": "#5A3E4A",
        "--dropdown-border": "#F8BBD0",
        "--checkbox-bg": "#FFFFFF",
        "--checkbox-border": "#F8BBD0",
        "--checkbox-checked-bg": "#E91E63",
        "--radio-bg": "#FFFFFF",
        "--radio-border": "#F8BBD0",
        "--radio-checked-bg": "#E91E63",
        "--slider-bg": "#FFE0E0",
        "--slider-progress": "#E91E63",
        "--slider-handle": "#E91E63",
    }    
}

def _dir_class(lang: str) -> str:
    return "html-rtl" if LANGS.get(lang, {}).get("dir") == "rtl" else "html-ltr"

def apply_theme(theme_key: str, lang: str):

    # ✅ تحميل فونت عربي أنيق: Tajawal
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;600;700&display=swap');
    </style>
    """, unsafe_allow_html=True)

    theme = THEMES.get(theme_key, THEMES["modern_light"]).copy()
    
    rtl_langs = {code for code, info in LANGS.items() if info.get("dir") == "rtl"}
    is_rtl = lang in rtl_langs
    direction = "rtl" if is_rtl else "ltr"
    text_align = "right" if is_rtl else "left"
    sidebar_position = "right: 0; left: auto;" if is_rtl else "left: 0; right: auto;"
    
    # ✅ تحديد الفونت حسب اللغة
    font_family = "'Tajawal', sans-serif" if lang == "ar" else "sans-serif"
    
    theme_vars = "; ".join([f"{k}: {v}" for k, v in theme.items()])
    
    css_template = """

    <style>
    /* Theme: {theme_key}, Lang: {lang}, Time: {timestamp} */
    :root {{
        --radius: 14px;
        --pad: 1rem;
        {theme_vars}
    }}
    
    /* ========== الأنماط الأساسية ========== */
    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stHeader"], [data-testid="stSidebarContent"] {{
        direction: {direction} !important;
        text-align: {text_align} !important;
        font-family: {font_family} !important;
    }}
    
    [data-testid="stSidebar"] {{
        {sidebar_position}
    }}
    
    body, .main, [data-testid="stAppViewContainer"] {{
        background: var(--bg) !important;
        color: var(--text) !important;
    }}
    
    section[data-testid="stSidebar"] > div {{
        background: var(--panel) !important;
        color: var(--text) !important;
    }}
    
    .block-container {{
        padding-top: 2rem;
    }}
    
    /* ========== تحسينات النصوص العامة ========== */
    .stMarkdown, .stText, .stAlert, .stDataFrame {{
        color: var(--text) !important;
        border-radius: var(--radius);
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: var(--text) !important;
    }}
    
    a {{
        color: var(--accent) !important;
    }}
    
    /* ========== تحسينات Text Inputs ========== */
    .stTextInput > div > div > input {{
        background: var(--input-bg) !important;
        color: var(--input-text) !important;
        border: 1px solid var(--input-border) !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        text-align: {text_align} !important;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: var(--input-focus-border) !important;
        background: var(--input-focus-bg) !important;
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--input-focus-border), transparent 90%) !important;
        outline: none !important;
    }}
    
    .stTextInput > div > div > input::placeholder {{
        color: var(--muted) !important;
        opacity: 0.7;
    }}
    
    .stTextInput label {{
        color: var(--text) !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    /* ========== تحسينات Text Areas ========== */
    .stTextArea > div > div > textarea {{
        background: var(--input-bg) !important;
        color: var(--input-text) !important;
        border: 1px solid var(--input-border) !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        text-align: {text_align} !important;
        resize: vertical;
        min-height: 100px;
    }}
    
    .stTextArea > div > div > textarea:focus {{
        border-color: var(--input-focus-border) !important;
        background: var(--input-focus-bg) !important;
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--input-focus-border), transparent 90%) !important;
        outline: none !important;
    }}
    
    .stTextArea label {{
        color: var(--text) !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    /* ========== تحسينات Dropdowns (Selectboxes) ========== */
    .stSelectbox > div > div {{
        background: var(--dropdown-bg) !important;
        color: var(--dropdown-text) !important;
        border: 1px solid var(--dropdown-border) !important;
        border-radius: var(--radius) !important;
        padding: 0.1rem 0.2rem !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        text-align: {text_align} !important;
    }}
    
    .stSelectbox > div > div:hover {{
        background: var(--dropdown-hover-bg) !important;
        border-color: var(--input-focus-border) !important;
    }}
    
    .stSelectbox > div > div:focus-within {{
        border-color: var(--input-focus-border) !important;
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--input-focus-border), transparent 90%) !important;
    }}
    
    .stSelectbox label {{
        color: var(--text) !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    /* ⚡️ حل نهائي: فرض لون النص على كل العناصر داخل الـ selectbox */
    .stSelectbox [data-baseweb="select"] * {{
        color: var(--dropdown-text) !important;
        background: var(--dropdown-bg) !important;
    }}
    
    .stSelectbox [data-baseweb="select"] > div {{
        color: var(--dropdown-text) !important;
    }}
    
    .stSelectbox [data-baseweb="select"] span {{
        color: var(--dropdown-text) !important;
    }}
    
    /* ========== قائمة الـ dropdown المفتوحة ========== */
    [data-baseweb="popover"] {{
        background: var(--dropdown-bg) !important;
        border: 1px solid var(--dropdown-border) !important;
        border-radius: var(--radius) !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15) !important;
        font-family: {font_family} !important; /* ⚡️ تطبيق الفونت هنا */

    }}
    
    [data-baseweb="menu"] {{
        background: var(--dropdown-bg) !important;
        font-family: {font_family} !important; /* ⚡️ تطبيق الفونت هنا */

    }}
    
    [data-baseweb="menu"] li {{
        background: var(--dropdown-bg) !important;
        color: var(--dropdown-text) !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.2s ease !important;
        font-family: {font_family} !important; /* ⚡️ تطبيق الفونت هنا */
    }}
    
    [data-baseweb="menu"] li * {{
        color: inherit !important;
        font-family: {font_family} !important; /* ⚡️ تطبيق الفونت هنا */
    }}
    
    [data-baseweb="menu"] li:hover {{
        background: var(--dropdown-hover-bg) !important;
        color: var(--dropdown-hover-text) !important;
        font-family: {font_family} !important; /* ⚡️ تطبيق الفونت هنا */
    }}
    
    /* ========== تحسينات Number Inputs ========== */
    .stNumberInput > div > div > input {{
        background: var(--input-bg) !important;
        color: var(--input-text) !important;
        border: 1px solid var(--input-border) !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        text-align: {text_align} !important;
    }}
    
    .stNumberInput > div > div > input:focus {{
        border-color: var(--input-focus-border) !important;
        background: var(--input-focus-bg) !important;
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--input-focus-border), transparent 90%) !important;
        outline: none !important;
    }}
    
    .stNumberInput label {{
        color: var(--text) !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    /* ========== تحسينات Checkboxes - نسخة نهائية تضمن ظهور العلامة ✓ عند الضغط ========== */

    /* المربع نفسه */
    .stCheckbox [data-baseweb="checkbox"] {{
        background: var(--checkbox-bg) !important;
        border: 1px solid var(--checkbox-border) !important;
        border-radius: 4px !important;
        width: 20px !important;
        height: 20px !important;
        flex-shrink: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
        transition: all 0.2s ease !important;
    }}

    .stCheckbox [data-baseweb="checkbox"]:hover {{
        border-color: var(--input-focus-border) !important;
        background: color-mix(in srgb, var(--checkbox-bg), white 90%) !important;
    }}

    /* ✅ حل مضمون: استخدام :checked بدلاً من aria-checked */
    .stCheckbox [data-baseweb="checkbox"]:checked {{
        background: var(--checkbox-checked-bg) !important;
        border-color: var(--checkbox-checked-bg) !important;
    }}

    /* ✅ حل إضافي: استخدام [aria-checked="true"] مع !important */
    .stCheckbox [data-baseweb="checkbox"][aria-checked="true"] {{
        background: var(--checkbox-checked-bg) !important;
        border-color: var(--checkbox-checked-bg) !important;
    }}

    /* العلامة الداخلية (✓) */
    .stCheckbox [data-baseweb="checkbox"] svg {{
        color: white !important;
        width: 12px !important;
        height: 12px !important;
        stroke-width: 3px !important;
        fill: currentColor !important;
    }}

    /* حل أخير: فرض على العلامة أن تظهر دائمًا */
    .stCheckbox [data-baseweb="checkbox"] svg path {{
        fill: white !important;
        stroke: white !important;
    }}

    /* ========== تحسينات Radio Buttons ========== */
    .stRadio {{
        color: var(--text) !important;
    }}
    
    .stRadio [data-baseweb="radio"] {{
        background: var(--radio-bg) !important;
        border: 1px solid var(--radio-border) !important;
    }}
    
    .stRadio [data-baseweb="radio"]:hover {{
        border-color: var(--input-focus-border) !important;
    }}
    
    .stRadio [data-baseweb="radio"][aria-checked="true"] {{
        background: var(--radio-checked-bg) !important;
        border-color: var(--radio-checked-bg) !important;
    }}
    
    .stRadio span {{
        color: var(--text) !important;
        font-weight: 500 !important;
    }}
    
    /* ========== تحسينات Sliders ========== */
    .stSlider [data-baseweb="slider"] {{
        background: var(--slider-bg) !important;
        border-radius: 20px !important;
    }}
    
    .stSlider [data-baseweb="slider"] > div > div {{
        background: var(--slider-progress) !important;
    }}
    
    .stSlider [data-baseweb="thumb"] {{
        background: var(--slider-handle) !important;
        border: 2px solid white !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2) !important;
    }}
    
    .stSlider label {{
        color: var(--text) !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    /* ========== تحسينات التابات (Tabs) ========== */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px;
        padding: 4px;
        background: var(--tab-bg) !important;
        border-radius: var(--radius);
        margin-bottom: 1rem;
        border: 1px solid var(--muted);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        height: 3rem;
        white-space: pre-wrap;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        background-color: var(--tab-bg) !important;
        color: var(--tab-text) !important;
        font-weight: 500;
        transition: all 0.3s ease !important;
        border: 1px solid transparent !important;
        margin: 2px !important;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: var(--tab-active-bg) !important;
        color: var(--tab-active-text) !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
        border: 1px solid var(--tab-active-bg) !important;
        transform: translateY(-1px);
    }}
    
    .stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {{
        background: var(--tab-hover-bg) !important;
        color: var(--tab-hover-text) !important;
        border: 1px solid var(--muted) !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }}
    
    .stTabs [data-baseweb="tab"] span,
    .stTabs [data-baseweb="tab"] div {{
        color: inherit !important;
        font-weight: inherit !important;
    }}
    
    .stTabs [data-baseweb="tab"]:focus {{
        outline: 2px solid var(--accent) !important;
        outline-offset: 2px;
    }}
    
    /* ========== تحسينات الأزرار ========== */
    .stButton > button {{
        border-radius: var(--radius) !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.25s ease !important;
        min-height: 2.75rem !important;
        border: none !important;
        color: white !important;
        background: var(--brand) !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15) !important;
    }}

    .stButton > button:hover {{
        background: color-mix(in srgb, var(--brand), white 10%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    }}

    .stButton > button:active {{
        transform: translateY(0) !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2) !important;
    }}

    .stButton > button:focus {{
        outline: 2px solid var(--accent) !important;
        outline-offset: 2px !important;
    }}

    /* أزرار غير أولية */
    .stButton > button[kind="secondary"] {{
        background: var(--panel) !important;
        color: var(--text) !important;
        border: 1px solid var(--muted) !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08) !important;
    }}

    .stButton > button[kind="secondary"]:hover {{
        background: var(--bg) !important;
        border-color: var(--brand) !important;
        color: var(--text) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1) !important;
    }}

    .stButton > button:not([kind="primary"]) {{
        background: var(--panel) !important;
        color: var(--text) !important;
        border: 1px solid var(--muted) !important;
    }}

    .stButton > button:not([kind="primary"]):hover {{
        background: var(--bg) !important;
        border-color: var(--brand) !important;
        color: var(--text) !important;
    }}
    
    /* ========== تحسينات الـ Sidebar ========== */
    .stSidebar .stButton button,
    .stSidebar .stMarkdown,
    .stSidebar .stSelectbox label,
    .stSidebar .stTextInput label,
    .stSidebar .stNumberInput label,
    .stSidebar .stCheckbox span,
    .stSidebar .stRadio span {{
        color: var(--text) !important;
    }}
    
    .stSidebar .stSelectbox > div > div,
    .stSidebar .stTextInput > div > div > input,
    .stSidebar .stNumberInput > div > div > input,
    .stSidebar .stTextArea > div > div > textarea {{
        color: var(--text) !important;
        background: var(--input-bg) !important;
        border-color: var(--input-border) !important;
    }}
    
    /* ========== تحسينات الـ Alerts والرسائل ========== */
    .stAlert {{
        background: var(--panel) !important;
        color: var(--text) !important;
        border: 1px solid var(--muted) !important;
        border-radius: var(--radius) !important;
    }}
    
    .stSuccess {{
        background: rgba(16, 185, 129, 0.1) !important;
        border-color: var(--accent) !important;
    }}
    
    .stWarning {{
        background: rgba(245, 158, 11, 0.1) !important;
        border-color: var(--accent) !important;
    }}
    
    .stError {{
        background: rgba(239, 68, 68, 0.1) !important;
        border-color: #EF4444 !important;
    }}
    
    .stInfo {{
        background: rgba(59, 130, 246, 0.1) !important;
        border-color: var(--brand) !important;
    }}
    
    /* ========== تحسينات الجداول ========== */
    .stDataFrame {{
        background: var(--panel) !important;
        color: var(--text) !important;
        border-radius: var(--radius) !important;
        border: 1px solid var(--muted) !important;
    }}
    
    .dataframe table {{
        color: var(--text) !important;
    }}
    
    .dataframe th {{
        background: var(--tab-bg) !important;
        color: var(--tab-text) !important;
        font-weight: 600 !important;
    }}
    
    .dataframe td {{
        background: var(--panel) !important;
        color: var(--text) !important;
        border-color: var(--muted) !important;
    }}
    
    /* ========== تحسينات إضافية ========== */
    .stProgress > div > div > div {{
        background: var(--brand) !important;
    }}
    
    .stExpander {{
        background: var(--panel) !important;
        border: 1px solid var(--muted) !important;
        border-radius: var(--radius) !important;
    }}
    
    .stExpander summary {{
        color: var(--text) !important;
        font-weight: 600 !important;
    }}
    
    .stExpander div {{
        color: var(--text) !important;
    }}
    
    /* ⚡️ حل أخير: فرض على جميع عناصر الـ checkbox أن تظهر العلامة ✓ بشكل واضح */
    [data-testid="stCheckbox"] [data-baseweb="checkbox"] svg * {{
        fill: white !important;
        stroke: white !important;
        color: white !important;
    }}
    
    </style>
    """
    # تحديد الفونت حسب اللغة
    font_family = "'Tajawal', sans-serif" if lang == "ar" else "sans-serif"
    
    css = css_template.format(
        theme_key=theme_key,
        lang=lang,
        timestamp=time.time(),
        theme_vars=theme_vars,
        direction=direction,
        text_align=text_align,
        sidebar_position=sidebar_position,
        font_family=font_family
    )
    

    st.markdown(css, unsafe_allow_html=True)


def apply_navigation_fix():
    """حل إضافي لمشاكل الـ navigation - تطبيق عالمي"""
    fix_css = """
    <style>
    /* حلول إضافية لضمان وضوح النص في جميع العناصر */
    
    /* التأكد من وضوح النص في التابات */
    .stTabs [data-baseweb="tab"] {
        font-weight: 500 !important;
        text-shadow: 0 1px 1px rgba(0,0,0,0.05);
    }
    
    /* تحسين contrast للنص في التاب النشط */
    .stTabs [aria-selected="true"] {
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        font-weight: 600 !important;
    }
    
    /* تحسين النصوص في الـ inputs */
    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea {
        color: inherit !important;
    }
    
    /* تحسين النصوص في الـ checkboxes و radios */
    .stCheckbox span, 
    .stRadio span {
        color: inherit !important;
        font-weight: 500 !important;
    }
    
    /* تحسين contrast للنصوص في الثيمات الداكنة */
    [data-testid="stAppViewContainer"] * {
        color-scheme: light dark;
    }
    
    /* ========== تطبيق فونت Tajawal على كل العناصر العربية ========== */
    [data-testid="stAppViewContainer"] * {{
        font-family: {font_family} !important;
    }}

    /* تأكد من تطبيق الفونت على الـ inputs والـ buttons والـ labels */
    .stTextInput label,
    .stTextArea label,
    .stNumberInput label,
    .stSelectbox label,
    .stCheckbox span,
    .stRadio span,
    .stButton > button,
    h1, h2, h3, h4, h5, h6,
    .stMarkdown, .stText, .stAlert, .stDataFrame {{
        font-family: {font_family} !important;
    }}

    /* حل أخير: فرض على جميع العناصر أن تستخدم Tajawal عند اللغة العربية */
    html[dir="rtl"] * {{
        font-family: 'Tajawal', sans-serif !important;
    }}
    
    /* حل أخير: فرض على جميع عناصر الـ app أن تستخدم Tajawal عند اللغة العربية */
    [data-testid="stAppViewContainer"] * {
    font-family: 'Tajawal', sans-serif !important;
    }
    
    /* حل أخير: فرض على جميع عناصر الـ dropdown أن تستخدم Tajawal عند اللغة العربية */
    [data-baseweb="popover"] * {
        font-family: 'Tajawal', sans-serif !important;
    }
    </style>
    """
    st.markdown(fix_css, unsafe_allow_html=True)

    