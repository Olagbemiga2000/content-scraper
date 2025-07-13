import streamlit as st

# Config de la page
st.set_page_config(page_title="Content Scraper", layout="centered")

# Titre principal
st.title("🧠 CONTENT SCRAPER – Prompt Optimizer (EN/FR)")
st.markdown("Transforme un prompt simple en prompt **SEO-ready**, adapté à chaque plateforme.")

# Sélecteurs
lang = st.selectbox("Language / Langue :", ["English", "Français"])
platform = st.selectbox("Target Platform / Plateforme :", ["Instagram", "TikTok", "LinkedIn", "Blog", "YouTube Shorts"])
user_prompt = st.text_area("Your basic prompt / Ton prompt de base :", placeholder="Ex : Post about a perfume...")

# Fonction d'optimisation
def optimize_prompt(prompt, lang, platform):
    if lang == "Français":
        return f"""🎯 Objectif : Créer un contenu optimisé SEO pour {platform}  
🎯 Format : Accroche + avantages + preuve sociale + appel à l'action  

✅ Prompt optimisé :  
“Crée un contenu {platform} pour promouvoir : {prompt}.  
Structure : Hook émotionnel, 3 bénéfices clairs, preuve sociale, appel à l’action.  
Ajoute des hashtags SEO liés à la niche.”"""
    else:
        return f"""🎯 Goal: Create SEO-optimized content for {platform}  
🎯 Format: Hook + benefits + social proof + CTA  

✅ Optimized Prompt:  
“Write a {platform} content to promote: {prompt}.  
Structure: Emotional hook, 3 key benefits, social proof, strong call-to-action.  
Add SEO-relevant hashtags.”"""

# Affichage du résultat
if st.button("🚀 Optimize / Optimiser"):
    if user_prompt:
        result = optimize_prompt(user_prompt, lang, platform)
        st.success("✅ Prompt optimized!")
        st.code(result, language="markdown")
    else:
        st.warning("Please enter a basic prompt.")
