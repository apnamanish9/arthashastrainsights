# INSTRUCTIONS UPDATE 5 — LOGO FIX AND FONT SIZE REDUCTION
# Save as INSTRUCTIONS_UPDATE5_LOGO_FONT.md in:
# D:\Claude code folder\arthashastrainsights\
# Tell Claude Code: "Read INSTRUCTIONS_UPDATE5_LOGO_FONT.md and execute all instructions"

---

## TASK 1 — FIX DOUBLE LOGO ISSUE

The navbar currently shows TWO logos side by side. This needs to be fixed
to show only ONE logo — the circular logo image file only.

### What is happening:
The navbar has both:
1. An img tag showing the logo PNG file
2. A text-based CSS logo or SVG duplicate

### Fix:
In index.html find the navbar/header section.
Look for the brand/logo area and remove the DUPLICATE logo element.

Keep ONLY this structure — one logo image + brand text:

```html
<a href="#home" class="navbar-brand">
  <img src="assets/images/Arthashastrainsights_logo.png" 
       alt="Arthashastra Insights Logo" 
       class="nav-logo">
  <div class="brand-text">
    <span class="brand-name">Arthashastra Insights</span>
    <span class="brand-tagline">Insights from SEBI Registered Research Analyst</span>
  </div>
</a>
```

Remove any duplicate img tag, any SVG logo, any CSS-generated logo,
any ::before or ::after pseudo-element that creates a second logo.
There must be exactly ONE logo image visible in the navbar.

Also check the FOOTER — if it also has a double logo, fix it the same way.
Footer should also show exactly ONE logo image + brand text.

### Logo image path:
The correct logo file is: assets/images/Arthashastrainsights_logo.png
Make sure the img src points to this exact path.

### Logo sizing in navbar CSS:
.nav-logo { 
  height: 110px; 
  width: auto; 
  object-fit: contain;
  display: block;
}

### Logo sizing in footer CSS:
.footer-logo {
  height: 70px;
  width: auto;
  object-fit: contain;
  display: block;
}

---

## TASK 2 — REDUCE FONT SIZE THROUGHOUT WEBSITE BY 2px UNIFORMLY

Reduce EVERY font size in assets/css/style.css by exactly 2px or 
equivalent rem value. Apply this uniformly to ALL elements EXCEPT 
anything related to the logo, brand name, or tagline in the navbar.

### Rules:
- If current size is in px: subtract 2px (e.g. 18px → 16px)
- If current size is in rem: subtract 0.125rem (e.g. 1.125rem → 1rem)
- If current size uses clamp(): reduce all three values by 2px or 0.125rem
- Minimum font size: never go below 12px for any element
- Do NOT change font sizes of these navbar elements:
  - .brand-name / .navbar-brand-name (keep at 40px)
  - .brand-tagline / .navbar-tagline (keep at 14px)
  - .nav-logo img (no font size applicable)

### Specific elements to reduce by 2px:

Body and base:
- body: 18px → 16px

Navigation links:
- .nav-links a, nav a: 16px → 14px

Hero section:
- .hero h1: clamp(2.8rem, 5vw, 4.2rem) → clamp(2.675rem, 4.875vw, 4.075rem)
- .hero p, .hero-subtitle: 1.25rem → 1.125rem
- .hero .cta-buttons a: 1.05rem → 0.925rem
- .slide-quote p: 1.1rem → 0.975rem
- .slide-quote cite: 0.95rem → 0.825rem

Section headings:
- h1: clamp(2.2rem, 4vw, 3.5rem) → clamp(2.075rem, 3.875vw, 3.375rem)
- h2: clamp(1.8rem, 3vw, 2.6rem) → clamp(1.675rem, 2.875vw, 2.475rem)
- h3: clamp(1.3rem, 2vw, 1.8rem) → clamp(1.175rem, 1.875vw, 1.675rem)
- h4: 1.25rem → 1.125rem
- h5: 1.1rem → 0.975rem
- h6: 1rem → 0.875rem

Section content:
- .section-subtitle: 1.1rem → 0.975rem
- .card p: 1rem → 0.875rem
- .card h3: 1.4rem → 1.275rem
- .card-label: 0.9rem → 0.775rem
- .about-bio: 1.1rem → 0.975rem
- .credential-badge: 0.95rem → 0.825rem
- .vm-heading: 1.6rem → 1.475rem
- .vm-text: 1.05rem → 0.925rem
- .why-text: 1.05rem → 0.925rem
- .accordion-header: 1.05rem → 0.925rem
- .accordion-content p: 1rem → 0.875rem
- .grievance-step h4: 1.2rem → 1.075rem
- .grievance-step p: 1rem → 0.875rem
- table: 0.95rem → 0.825rem
- .contact-value: 1.05rem → 0.925rem
- .form-input: 1rem → 0.875rem

Footer:
- footer: 0.95rem → 0.825rem
- .footer-disclosure: 0.88rem → 0.76rem
- .footer-copyright: 0.85rem → 0.73rem

Compliance ticker:
- .compliance-ticker: 0.9rem → 0.78rem

Buttons:
- .btn, button: 1rem → 0.875rem

Legal notes:
- .legal-note: 0.95rem → 0.825rem
- .sebi-badge: 0.9rem → 0.78rem

### Do NOT change these (logo related — keep exactly as is):
- .brand-name: keep 40px
- .brand-tagline: keep 14px
- .nav-logo height: keep 110px
- .footer-logo height: keep 70px

---

## TASK 3 — VERIFY LOGO FILE EXISTS

Check that this file exists in the project:
assets/images/Arthashastrainsights_logo.png

If it does not exist, check for any of these alternative names and 
rename/copy to the correct path:
- Arthashastrainsights_logo.png (root folder) → copy to assets/images/
- assets/images/logo.png → rename to Arthashastrainsights_logo.png
- Any .png file in assets/images/ → verify it is the correct logo

---

## FINAL VERIFICATION

After all changes confirm:
1. Navbar shows exactly ONE logo (the circular PNG image)
2. Footer shows exactly ONE logo
3. No duplicate logo anywhere on the page
4. Brand name "Arthashastra Insights" still 40px (unchanged)
5. Tagline "Insights from SEBI Registered Research Analyst" still 14px (unchanged)
6. Body font reduced from 18px to 16px
7. All other fonts reduced by 2px uniformly
8. No font smaller than 12px anywhere
9. Website still looks good and proportionate
10. Mobile responsive still working

Report all changes made to index.html and assets/css/style.css.
