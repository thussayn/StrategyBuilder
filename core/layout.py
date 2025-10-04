# core/layout.py
import streamlit as st
from .i18n import LANGS

def _is_rtl(lang: str) -> bool:
    return LANGS.get(lang, {}).get("dir") == "rtl"

def app_header(title: str, lang: str = "en"):
    is_rtl = _is_rtl(lang)
    direction = "rtl" if is_rtl else "ltr"
    text_align = "right" if is_rtl else "left"
    
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:.75rem;background:var(--panel);padding:1rem;border-radius:var(--radius);direction:{direction};text-align:{text_align};">
            <div style="width:12px;height:12px;background:var(--brand);border-radius:50%"></div>
            <h2 style="margin:0;">{title}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

def app_footer(lang: str = "en"):
    is_rtl = _is_rtl(lang)
    direction = "rtl" if is_rtl else "ltr"
    text_align = "right" if is_rtl else "left"
    
    st.markdown(
        f"""
        <hr/>
        <div style="opacity:.7;font-size:.9rem;direction:{direction};text-align:{text_align};">
            [جميع الحقوو ق محفوظة © 2025 - Basic Systems Co.](https://basicsystems.sa) |
        </div>
        """,
        unsafe_allow_html=True,
    )