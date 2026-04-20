# INSTRUCTIONS — MOBILE RESPONSIVENESS FIX
# Save as INSTRUCTIONS_MOBILE_FIX.md in:
# D:\Claude code folder\arthashastrainsights\
# Tell Claude Code: "Read INSTRUCTIONS_MOBILE_FIX.md and execute all instructions"

---

## ISSUE 1 — VIEWPORT META TAG
In index.html and terms-of-use.html check the viewport
meta tag in <head> section.
Replace any existing viewport meta tag with this exact one:
<meta name="viewport" content="width=device-width,
initial-scale=1.0, minimum-scale=1.0, maximum-scale=5.0,
user-scalable=yes">

---

## ISSUE 2 — PREVENT HORIZONTAL SCROLL
In assets/css/style.css add at the very top:

html {
  overflow-x: hidden;
  scroll-behavior: smooth;
}

body {
  overflow-x: hidden;
  width: 100%;
  max-width: 100vw;
}

* {
  box-sizing: border-box;
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

---

## ISSUE 3 — NAVBAR MOBILE FIX

.site-header, header, nav {
  width: 100%;
  max-width: 100%;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  width: 100%;
  max-width: 100%;
  flex-wrap: nowrap;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
  max-width: 65%;
  overflow: hidden;
}

@media (max-width: 768px) {
  .nav-logo {
    height: 50px !important;
    width: auto;
  }
  .brand-name, .logo-name {
    font-size: 16px !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .brand-tagline, .logo-tagline {
    font-size: 9px !important;
    white-space: nowrap;
  }
}

---

## ISSUE 4 — MOBILE NAV MENU

@media (max-width: 768px) {
  .nav-links {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: #0a0f2e;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 24px;
    z-index: 9998;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .nav-links.active {
    display: flex;
  }
  .nav-links a {
    font-size: 18px !important;
    color: white;
    text-decoration: none;
    padding: 8px 0;
  }
  .hamburger {
    display: flex !important;
    flex-direction: column;
    gap: 5px;
    cursor: pointer;
    z-index: 9999;
    background: none;
    border: none;
    padding: 4px;
  }
  .hamburger span {
    display: block;
    width: 24px;
    height: 2px;
    background: white;
    border-radius: 2px;
    transition: all 0.3s;
  }
}

@media (min-width: 769px) {
  .hamburger {
    display: none !important;
  }
  .nav-links {
    display: flex !important;
  }
}

---

## ISSUE 5 — HERO SECTION MOBILE

@media (max-width: 768px) {
  .hero, #home {
    min-height: 100svh;
    padding: 80px 16px 40px;
  }
  .hero h1, .hero-title {
    font-size: clamp(1.6rem, 6vw, 2.5rem) !important;
    line-height: 1.3;
  }
  .hero p, .hero-subtitle {
    font-size: 0.95rem !important;
    line-height: 1.7;
  }
  .cta-buttons {
    flex-direction: column;
    gap: 12px;
    align-items: center;
  }
  .cta-buttons a, .cta-buttons button {
    width: 100%;
    max-width: 280px;
    text-align: center;
  }
  .slide-quote {
    bottom: 70px;
    padding: 10px 16px;
    font-size: 0.85rem !important;
  }
}

---

## ISSUE 6 — SECTIONS MOBILE PADDING

@media (max-width: 768px) {
  section {
    padding: 50px 16px !important;
  }
  .container {
    padding: 0 16px !important;
    width: 100%;
    max-width: 100%;
  }
  h2 {
    font-size: clamp(1.4rem, 5vw, 2rem) !important;
  }
  h3 {
    font-size: clamp(1.1rem, 4vw, 1.5rem) !important;
  }
}

---

## ISSUE 7 — CARDS MOBILE

@media (max-width: 768px) {
  .services-grid,
  .courses-grid,
  .vm-grid,
  .why-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
  }
  .service-card,
  .course-card {
    min-height: auto !important;
    padding: 24px 16px !important;
  }
}

---

## ISSUE 8 — TABLES MOBILE

@media (max-width: 768px) {
  .grievance-table-section .table-wrap {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
  }
  .grievance-table-section table {
    min-width: 500px;
  }
  .grievance-table-section th,
  .grievance-table-section td {
    font-size: 11px !important;
    padding: 8px 6px !important;
  }
}

---

## ISSUE 9 — FOOTER MOBILE

@media (max-width: 768px) {
  footer .footer-grid,
  footer .footer-columns {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  footer {
    padding: 40px 16px 20px !important;
  }
  .footer-disclosure {
    font-size: 0.75rem !important;
    line-height: 1.6;
  }
}

---

## ISSUE 10 — WHATSAPP AND BACK TO TOP MOBILE

@media (max-width: 768px) {
  .whatsapp-float {
    bottom: 16px !important;
    right: 16px !important;
    width: 50px !important;
    height: 50px !important;
  }
  .back-to-top {
    bottom: 76px !important;
    right: 16px !important;
    width: 40px !important;
    height: 40px !important;
  }
}

---

## ISSUE 11 — COMPLIANCE TICKER MOBILE

@media (max-width: 768px) {
  .ticker-wrap, .compliance-ticker {
    font-size: 0.75rem !important;
    padding: 6px 0 !important;
  }
}

---

## ISSUE 12 — TRADINGVIEW TICKER MOBILE

@media (max-width: 768px) {
  .tradingview-widget-container {
    width: 100% !important;
    overflow: hidden;
  }
}

---

## ISSUE 13 — CONTACT FORM MOBILE

@media (max-width: 768px) {
  .contact-grid,
  .contact-layout {
    grid-template-columns: 1fr !important;
  }
  .form-input,
  .form-select,
  .form-textarea {
    width: 100% !important;
    font-size: 16px !important;
  }
}

---

## ISSUE 14 — ABOUT SECTION MOBILE

@media (max-width: 768px) {
  .about-grid,
  .about-layout {
    grid-template-columns: 1fr !important;
    text-align: center;
  }
  .about-photo,
  .photo-placeholder {
    margin: 0 auto 24px !important;
  }
  .credentials-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

---

## ISSUE 15 — TERMS OF USE PAGE MOBILE

In terms-of-use.html update viewport meta tag same as index.html.

@media (max-width: 768px) {
  .terms-block {
    padding: 16px 0 !important;
  }
  .terms-block h3 {
    font-size: 0.95rem !important;
  }
  .terms-block p,
  .terms-block li {
    font-size: 0.85rem !important;
  }
}

---

## FINAL VERIFICATION

After all changes confirm:
1. Viewport meta tag updated in index.html and terms-of-use.html
2. No horizontal scroll on mobile
3. Navbar hamburger menu works on mobile
4. Hero section fits mobile screen properly
5. All grids stack to single column on mobile
6. Tables scroll horizontally on mobile
7. Footer stacks on mobile
8. WhatsApp button properly positioned on mobile
9. Forms use 16px font to prevent auto-zoom on iOS
10. All sections have proper mobile padding 16px
11. Both index.html and terms-of-use.html are mobile ready

Report all changes made to each file.
