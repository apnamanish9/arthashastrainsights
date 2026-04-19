# INSTRUCTIONS UPDATE 4 — FONT SIZE, LOGO, GRIEVANCE & TICKER FIXES
# Save as INSTRUCTIONS_UPDATE4.md in:
# D:\Claude code folder\arthashastrainsights\
# Tell Claude Code: "Read INSTRUCTIONS_UPDATE4.md and execute all instructions"

---

## TASK 1 — INCREASE FONT SIZE ACROSS ENTIRE WEBSITE

In assets/css/style.css make these font size increases globally:

### Base font size:
Change html/body base font from whatever it currently is to 18px.
body { font-size: 18px; line-height: 1.7; }

### Navigation links:
.nav-links a, nav a { font-size: 16px; }

### Hero section:
.hero h1, .hero-title { font-size: clamp(2.8rem, 5vw, 4.2rem); }
.hero p, .hero-subtitle { font-size: 1.25rem; line-height: 1.8; }
.hero .cta-buttons a, .hero button { font-size: 1.05rem; }
.slide-quote p { font-size: 1.1rem; }
.slide-quote cite, .slide-quote span { font-size: 0.95rem; }

### Section headings:
h1 { font-size: clamp(2.2rem, 4vw, 3.5rem); }
h2 { font-size: clamp(1.8rem, 3vw, 2.6rem); }
h3 { font-size: clamp(1.3rem, 2vw, 1.8rem); }
h4 { font-size: 1.25rem; }
h5 { font-size: 1.1rem; }
h6 { font-size: 1rem; }

### Section subtitles / descriptions:
.section-subtitle, .section-desc { font-size: 1.1rem; line-height: 1.8; }

### Card content:
.card p, .service-card p, .course-card p { font-size: 1rem; line-height: 1.75; }
.card h3, .service-card h3, .course-card h3 { font-size: 1.4rem; }
.card-label, .card-meta { font-size: 0.9rem; }

### About section:
.about-bio, .about-text p { font-size: 1.1rem; line-height: 1.85; }
.credential-badge { font-size: 0.95rem; }

### Vision Mission:
.vm-heading { font-size: 1.6rem; }
.vm-text, .vm-content p { font-size: 1.05rem; line-height: 1.8; }

### Why Choose Us:
.why-title { font-size: 13px; letter-spacing: 2px; }
.why-text { font-size: 1.05rem; font-weight: 500; }

### Disclaimer accordion:
.accordion-header { font-size: 1.05rem; }
.accordion-content p, .accordion-body { font-size: 1rem; line-height: 1.8; }

### Grievance section:
.grievance-step h4 { font-size: 1.2rem; }
.grievance-step p { font-size: 1rem; }
table { font-size: 0.95rem; }
th { font-size: 0.95rem; }

### Contact section:
.contact-label { font-size: 0.9rem; }
.contact-value { font-size: 1.05rem; }
.form-label { font-size: 0.95rem; }
.form-input, .form-select, .form-textarea { font-size: 1rem; }

### Footer:
footer { font-size: 0.95rem; }
.footer-disclosure { font-size: 0.88rem; line-height: 1.7; }
.footer-copyright { font-size: 0.85rem; }

### Compliance ticker (top scrolling bar):
.compliance-ticker, .ticker-text { font-size: 0.9rem; }

### Buttons globally:
.btn, button { font-size: 1rem; padding: 12px 28px; }

### Form elements:
input, select, textarea { font-size: 1rem; padding: 12px 16px; }

### Legal note / disclaimer boxes:
.legal-note, .disclaimer-box, .warning-box { font-size: 0.95rem; line-height: 1.75; }

### SEBI badge strip in hero:
.sebi-badge, .hero-badge { font-size: 0.9rem; }

---

## TASK 2 — DOUBLE THE LOGO SIZE AND BRAND NAME

In the navbar/header section of index.html and in assets/css/style.css:

### Logo image:
Find the navbar logo img tag and change:
- height from whatever it currently is → 110px
- width: auto (maintain aspect ratio)
- Do NOT stretch or distort the logo

### Brand name "Arthashastra Insights":
Find the navbar brand name text and change:
- font-size to 40px
- font-weight: 700
- color: white
- letter-spacing: 0.5px

### Tagline "Insights from SEBI Registered Research Analyst":
Find the navbar tagline/subtitle text and change:
- font-size to 14px
- color: #f5a623 (gold)
- letter-spacing: 0.5px
- font-weight: 400

### Navbar height adjustment:
Since logo is larger, increase navbar min-height to 90px
and add more padding: padding: 12px 40px
Make sure navbar still works on mobile — on mobile set logo height to 65px
and brand name font-size to 22px on screens below 768px.

### CSS for navbar brand specifically:
.navbar-brand img, .nav-logo { height: 110px; width: auto; }
.brand-name, .navbar-brand-name { font-size: 40px; font-weight: 700; }
.brand-tagline, .navbar-tagline { font-size: 14px; color: #f5a623; }
@media(max-width: 768px) {
  .navbar-brand img, .nav-logo { height: 65px; }
  .brand-name, .navbar-brand-name { font-size: 22px; }
  .brand-tagline, .navbar-tagline { font-size: 11px; }
}

---

## TASK 3 — GRIEVANCE SECTION: CHANGE RESPONSE TIME

In index.html find the Grievance Redressal section.
Find this exact text or similar:
"Response within: 10 business days"
or
"10 business days"
in the context of Step 1 / direct contact / email response time.

Change it to: "Response within: 7 business days"

Also find the resolution timeline table in grievance section:
Find "Level 1 | Manish Mishra (RA) | 10 business days"
Change to: "Level 1 | Manish Mishra (RA) | 7 business days"

Search for any other mention of "10 business days" in the 
grievance context and change all to "7 business days".

---

## TASK 4 — FIX TRADINGVIEW TICKER WITH CORRECT SYMBOLS

In index.html find the TradingView ticker tape widget script.
Replace the entire symbols array with this exact correct list:

{
  "symbols": [
    {"proName": "NSE:NIFTY", "title": "Nifty 50"},
    {"proName": "NSE:BANKNIFTY", "title": "Bank Nifty"},
    {"proName": "BSE:SENSEX", "title": "Sensex"},
    {"proName": "NSE:CNXAUTO", "title": "Nifty Auto"},
    {"proName": "NSE:CNXFINANCE", "title": "Nifty Financial"},
    {"proName": "NSE:CNXMETAL", "title": "Nifty Metal"},
    {"proName": "NSE:CNXPHARMA", "title": "Nifty Pharma"},
    {"proName": "NSE:CNXIT", "title": "Nifty IT"},
    {"proName": "NSE:CNXPSUBANK", "title": "PSU Bank"},
    {"proName": "NSE:NIFTY_HEALTHCARE", "title": "Healthcare"},
    {"proName": "NSE:NIFTY_INDIA_MFG", "title": "India Mfg"},
    {"proName": "NSE:NIFTYJR", "title": "Nifty Next 50"},
    {"proName": "NSE:CNXINFRA", "title": "Nifty Infra"},
    {"proName": "NSE:CNXFMCG", "title": "Nifty FMCG"},
    {"proName": "NSE:CNXMEDIA", "title": "Nifty Media"},
    {"proName": "NSE:CNXSERVICE", "title": "Nifty Services"},
    {"proName": "NSE:CNXREALTY", "title": "Nifty Realty"},
    {"proName": "NSE:CNXCOMMODITIES", "title": "Commodities"},
    {"proName": "NSE:NIFTY_IND_DIGITAL", "title": "Digital India"},
    {"proName": "NSE:CNXENERGY", "title": "Nifty Energy"},
    {"proName": "NSE:NIFTY_IND_DEFENCE", "title": "Defence"},
    {"proName": "NSE:NIFTY200MOMENTM30", "title": "Momentum 30"},
    {"proName": "NSE:NIFTYMIDSML400", "title": "MidSmall 400"},
    {"proName": "NSE:CNXSMALLCAP", "title": "Smallcap"},
    {"proName": "NSE:NIFTYSMLCAP250", "title": "Smallcap 250"},
    {"proName": "NSE:NIFTYMIDCAP150", "title": "Midcap 150"},
    {"proName": "NSE:CNXPSE", "title": "PSE"},
    {"proName": "MCX:CRUDEOIL1!", "title": "Crude Oil"},
    {"proName": "MCX:NATURALGAS1!", "title": "Natural Gas"},
    {"proName": "MCX:GOLD1!", "title": "Gold"},
    {"proName": "MCX:SILVER1!", "title": "Silver"}
  ],
  "showSymbolLogo": true,
  "colorTheme": "dark",
  "isTransparent": false,
  "displayMode": "adaptive",
  "locale": "en"
}

Make sure the complete script tag for the TradingView widget 
looks exactly like this — replace whatever is currently there:

<div class="tradingview-widget-container" style="width:100%">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" 
    src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" 
    async>
  {
    "symbols": [
      {"proName": "NSE:NIFTY", "title": "Nifty 50"},
      {"proName": "NSE:BANKNIFTY", "title": "Bank Nifty"},
      {"proName": "BSE:SENSEX", "title": "Sensex"},
      {"proName": "NSE:CNXAUTO", "title": "Nifty Auto"},
      {"proName": "NSE:CNXFINANCE", "title": "Nifty Financial"},
      {"proName": "NSE:CNXMETAL", "title": "Nifty Metal"},
      {"proName": "NSE:CNXPHARMA", "title": "Nifty Pharma"},
      {"proName": "NSE:CNXIT", "title": "Nifty IT"},
      {"proName": "NSE:CNXPSUBANK", "title": "PSU Bank"},
      {"proName": "NSE:NIFTY_HEALTHCARE", "title": "Healthcare"},
      {"proName": "NSE:NIFTY_INDIA_MFG", "title": "India Mfg"},
      {"proName": "NSE:NIFTYJR", "title": "Nifty Next 50"},
      {"proName": "NSE:CNXINFRA", "title": "Nifty Infra"},
      {"proName": "NSE:CNXFMCG", "title": "Nifty FMCG"},
      {"proName": "NSE:CNXMEDIA", "title": "Nifty Media"},
      {"proName": "NSE:CNXSERVICE", "title": "Nifty Services"},
      {"proName": "NSE:CNXREALTY", "title": "Nifty Realty"},
      {"proName": "NSE:CNXCOMMODITIES", "title": "Commodities"},
      {"proName": "NSE:NIFTY_IND_DIGITAL", "title": "Digital India"},
      {"proName": "NSE:CNXENERGY", "title": "Nifty Energy"},
      {"proName": "NSE:NIFTY_IND_DEFENCE", "title": "Defence"},
      {"proName": "NSE:NIFTY200MOMENTM30", "title": "Momentum 30"},
      {"proName": "NSE:NIFTYMIDSML400", "title": "MidSmall 400"},
      {"proName": "NSE:CNXSMALLCAP", "title": "Smallcap"},
      {"proName": "NSE:NIFTYSMLCAP250", "title": "Smallcap 250"},
      {"proName": "NSE:NIFTYMIDCAP150", "title": "Midcap 150"},
      {"proName": "NSE:CNXPSE", "title": "PSE"},
      {"proName": "MCX:CRUDEOIL1!", "title": "Crude Oil"},
      {"proName": "MCX:NATURALGAS1!", "title": "Natural Gas"},
      {"proName": "MCX:GOLD1!", "title": "Gold"},
      {"proName": "MCX:SILVER1!", "title": "Silver"}
    ],
    "showSymbolLogo": true,
    "colorTheme": "dark",
    "isTransparent": false,
    "displayMode": "adaptive",
    "locale": "en"
  }
  </script>
</div>

---

## FINAL VERIFICATION
After all changes confirm:
1. Body base font is 18px
2. All headings are larger — h1 clamp 2.2-3.5rem, h2 clamp 1.8-2.6rem
3. Navbar logo height is 110px on desktop, 65px on mobile
4. Brand name "Arthashastra Insights" is 40px on desktop, 22px on mobile
5. Tagline "Insights from SEBI Registered Research Analyst" is 14px gold
6. Grievance Step 1 shows "Response within: 7 business days"
7. Grievance table Level 1 shows "7 business days"
8. TradingView widget has all 31 symbols listed above
9. No mention of "10 business days" remains in grievance section
10. Website still mobile responsive after font size increases

Report all files changed and confirm all 10 checks above.
