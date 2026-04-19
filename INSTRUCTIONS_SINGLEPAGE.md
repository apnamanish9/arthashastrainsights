# INSTRUCTIONS — REBUILD AS SINGLE PAGE WEBSITE
# Save this file as INSTRUCTIONS_SINGLEPAGE.md in:
# D:\Claude code folder\arthashastrainsights\
# Then tell Claude Code: "Read INSTRUCTIONS_SINGLEPAGE.md and execute all instructions"

---

## OVERVIEW
Rebuild the entire website as a single page (index.html only).
Delete all other HTML pages. Keep only:
- index.html (single page with all sections)
- assets/css/style.css
- assets/js/main.js
- assets/images/Arthashastrainsights_logo.png
- robots.txt
- sitemap.xml

Delete these files completely:
- about.html
- services.html
- stock-picks.html
- disclaimer.html
- grievance-redressal.html
- investor-charter.html
- terms-of-use.html
- contact.html

---

## DESIGN SYSTEM
- Colors: Dark navy (#0a0f2e) primary, Gold (#f5a623) accent, 
  White (#ffffff) text, Deep blue (#1a2456) for alternate sections
- Font: Google Fonts — Inter for body, Playfair Display for headings
- Fully mobile responsive
- Smooth scroll between sections
- Clean, premium, trustworthy look
- No clutter — crisp and minimal content

---

## STRUCTURE OF index.html
Build these sections in this exact order on one single HTML page:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — COMPLIANCE TICKER (top of page)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scrolling marquee bar at very top. Gold text on dark background.
Content (repeat twice for smooth scroll):
"Manish Mishra | SEBI Registered Research Analyst (Individual, Part-Time) | 
Reg. No. INH000024620 | NISM Certificate No.: 202400095615 | 
Investments in securities market are subject to market risk. 
Read all related documents carefully before investing. | 
Past performance is not indicative of future results. |"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — STICKY NAVBAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sticky navbar with:
- Left: Logo (height 55px) + Brand name "Arthashastra Insights" 
  (font-size 20px, bold, white) + tagline below brand name: 
  "Insights from SEBI Registered Research Analyst" (font-size 11px, gold)
- Right: navigation anchor links to each section on same page:
  Home | About | Services | Training | Disclaimer | Grievance | Contact
- YouTube icon link: https://www.youtube.com/@Arthashastrainsights 
  (gold color, opens new tab)
- Hamburger menu on mobile
- Active section highlight as user scrolls

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — HERO (id="home")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dark navy background with subtle candlestick pattern (CSS/SVG).
Content:
- Heading: "Data-Driven Research. Disciplined Investing."
- Subheading: "12+ years of stock market wisdom in Equity, 
  F&O and Commodities — shared with clarity and compliance."
- Two CTA buttons: 
  "View Services" (gold, scrolls to #services)
  "▶ Watch on YouTube" (outlined gold, opens YouTube channel)
- Below buttons — SEBI badge strip:
  "Manish Mishra | SEBI RA Reg. No. INH000024620 | 
   Investments subject to market risk"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — ABOUT (id="about")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alternate background (#1a2456).
Layout: Two columns on desktop, stacked on mobile.
Left column — Photo placeholder (round, 180px, gold border, 
  text "Your Photo" centered inside).
Right column — Content:

Heading: "Manish Mishra"
Subheading: "SEBI Registered Research Analyst (Individual, Part-Time)"

Short bio (keep crisp — 3 sentences max):
"With 12+ years in equity, F&O and commodities markets, I bring 
institutional discipline from my banking career at SBI to retail 
investors. An MBA Finance graduate from NMIMS, I specialise in 
Nifty options, swing trading and momentum strategies. My approach 
is rooted in technical analysis, systematic risk management 
and strict SEBI compliance."

Credentials — 4 small badges in a row:
- MBA Finance — NMIMS
- Former SBI Manager  
- SEBI RA — INH000024620
- NISM Certified — 202400095615

Important legal note box (amber/gold border box):
"IMPORTANT: Arthashastra Insights is a brand name. The SEBI Research 
Analyst registration (Reg. No. INH000024620) is held by Manish Mishra 
as an Individual Part-Time Research Analyst. Arthashastra Insights 
as an entity is not registered with SEBI."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — SERVICES (id="services")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dark navy background.
Section heading: "Research Services"
Subheading: "All research is provided by Manish Mishra in his 
individual capacity as SEBI RA (INH000024620)"

Three cards side by side (stack on mobile):

CARD 1 — Swing Trading Research
- Holding period: 5–20 days
- Instruments: Equities (NSE/BSE)
- Basis: Technical analysis, price action, volume
- Includes: Entry, Target, Stop Loss, Rationale

CARD 2 — Momentum Trading Research  
- Holding period: 2–10 days
- Instruments: Mid & Small cap equities
- Basis: Momentum burst, volume breakouts, relative strength
- Includes: Entry, Target, Stop Loss, Rationale

CARD 3 — Long Term Investing Research
- Holding period: 1–3 years
- Instruments: Large & Mid cap equities
- Basis: Fundamental analysis, business quality, valuations
- Includes: Research rationale and entry zones

Disclaimer box below cards (red/amber border):
"Research reports are for informational and educational purposes only. 
These are NOT buy/sell recommendations. SEBI registration does not 
guarantee returns. Investments are subject to market risk. 
Past performance is not indicative of future results."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — TRAINING / COURSES (id="training")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alternate background (#1a2456).
Section heading: "Trading Education"
Subheading: "Learn the methodology, not just the calls"

Three course cards:

CARD 1 — Swing Trading Masterclass
Short description: Master price action, support/resistance 
and trade management for swing trades.

CARD 2 — Momentum Trading Course
Short description: Learn to identify momentum bursts, 
volume breakouts and high-probability setups.

CARD 3 — Long Term Investing Framework
Short description: Fundamental analysis, business evaluation 
and portfolio construction for long-term wealth.

Note below cards (italic, small text):
"All courses are purely educational in nature and do not 
constitute investment advice or research recommendations."

YouTube CTA box below note:
"Watch free market insights and educational content on our YouTube channel"
Button: "▶ Visit YouTube Channel" 
Link: https://www.youtube.com/@Arthashastrainsights (opens new tab)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — DISCLAIMER (id="disclaimer")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dark navy background.
Section heading: "Disclaimer & Legal"

Show full disclaimer content in a clean readable layout.
Use accordion/expandable panels for each sub-section to keep it neat.
Keep language but make it specific to Manish Mishra / Arthashastra Insights.

Sub-sections as expandable accordions:

1. General Disclaimer
"Registration granted by SEBI and certification from NISM in no way 
guarantee performance of the intermediary or provide any assurance 
of returns to investors. Investments in securities market are subject 
to market risks. Read all related documents carefully before investing."

2. Research Analyst Disclosure
"Manish Mishra (SEBI RA Reg. No. INH000024620) operates under the 
brand name Arthashastra Insights. Arthashastra Insights is NOT a 
SEBI registered entity. All research is conducted by Manish Mishra 
in his individual capacity as a part-time SEBI Registered Research Analyst."

3. No Guarantee of Returns
"We do not propose or guarantee consistent and stable returns. 
Rewards in the market can be unpredictable. Even experienced traders 
face prolonged periods of losses. No representation is made as to 
returns generated by any client."

4. Educational Content
"Any content published on YouTube or social media by Arthashastra 
Insights / Manish Mishra is purely for educational and illustrative 
purposes and should not be treated as recommendations or investment 
advice. Securities quoted are for illustration only."

5. Limitation of Liability
"Manish Mishra and Arthashastra Insights take no responsibility for 
any investment decisions made based on research published. Users are 
solely responsible for their own investment decisions. Please consult 
a SEBI registered investment adviser before investing."

6. Privacy & Terms
"By visiting this website you agree to these terms. Governing 
jurisdiction: Courts of Bangalore, Karnataka, India."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8 — GRIEVANCE REDRESSAL (id="grievance")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alternate background (#1a2456).
Section heading: "Grievance Redressal"
Subheading: "Manish Mishra | SEBI RA Reg. No. INH000024620"

Three step process shown as timeline:

STEP 1 — Contact Us Directly
Email: apnamanish9@gmail.com
Subject: "Grievance — [Your Name]"
Response within: 10 business days

STEP 2 — SEBI SCORES Portal
If unresolved: https://scores.sebi.gov.in
SEBI Toll Free: 1800 266 7575
SEBI Email: sebi@sebi.gov.in

STEP 3 — ODR Portal
Online Dispute Resolution: https://smartodr.in
Resolution within 45 days

Resolution timeline table:
| Level | Authority | Timeline |
|-------|-----------|----------|
| Level 1 | Manish Mishra (RA) | 10 business days |
| Level 2 | SEBI SCORES | 30 calendar days |
| Level 3 | ODR Portal | 45 calendar days |

Grievance form below table:
Fields: Name, Email, Phone, 
Nature of Grievance (dropdown: 
  Non-receipt of research report | 
  Quality of research | 
  Billing dispute | 
  Misconduct | Other),
Description (textarea),
Submit button

Form action: https://formspree.io/f/REPLACE_WITH_REAL_FORMSPREE_ID
Hidden fields:
  <input type="hidden" name="_replyto" value="apnamanish9@gmail.com">
  <input type="hidden" name="_subject" value="Grievance - Arthashastra Insights">

Complaints data table (SEBI mandated):
| Sr | Month-Year | Received | Resolved | Pending |
|----|------------|----------|----------|---------|
| 1  | Apr 2025   | Nil      | Nil      | Nil     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 9 — CONTACT (id="contact")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dark navy background.
Section heading: "Get In Touch"

Two column layout (stack on mobile):

Left column — Contact info cards:
- Email: apnamanish9@gmail.com
- Phone: +91 9480322410
- WhatsApp: wa.me/919480322410 (click to chat)
- Address: GF-06, Winds Of Change, Judicial Layout, 
  Thalaghattapura, Bangalore - 560062, Karnataka
- YouTube: https://www.youtube.com/@Arthashastrainsights
- Business Hours: Mon–Fri 9AM–6PM IST, Sat 9AM–1PM IST

Right column — Contact form:
Fields: Name, Email, Phone, 
Subject (dropdown: 
  General Inquiry | 
  Research Services | 
  Trading Courses | 
  YouTube / Content | Other),
Message (textarea),
Submit button

Form action: https://formspree.io/f/REPLACE_WITH_REAL_FORMSPREE_ID
Hidden fields:
  <input type="hidden" name="_replyto" value="apnamanish9@gmail.com">
  <input type="hidden" name="_subject" value="Contact - Arthashastra Insights">

Important note above form:
"For research service enquiries only. Arthashastra Insights cannot 
provide personalised investment advice or stock tips via email/phone. 
For complaints please use the Grievance section above."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 10 — FOOTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dark navy, full width.
Content:

Left: Logo + 
"Arthashastra Insights" 
"A brand by Manish Mishra"

Center: Quick navigation links (anchor links to all sections)

Right: Social / contact
- apnamanish9@gmail.com
- +91 9480322410
- YouTube channel link

Full width SEBI disclosure bar above copyright line:
"Manish Mishra | SEBI Registered Research Analyst (Individual, Part-Time) | 
Reg. No. INH000024620 | NISM Cert. No.: 202400095615 | 
GF-06, Winds Of Change, Judicial Layout, Thalaghattapura, 
Bangalore - 560062, Karnataka | 
Arthashastra Insights is a brand name and NOT a SEBI registered entity. 
Investments in securities market are subject to market risk. 
Read all related documents carefully before investing."

Copyright line:
"© 2025 Arthashastra Insights. All Rights Reserved. | 
Manish Mishra, SEBI RA INH000024620"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLOATING ELEMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. WhatsApp floating button (bottom right):
   Link: https://wa.me/919480322410
   Green WhatsApp color, fixed position

2. Back to top button (bottom right, above WhatsApp):
   Shows after scrolling 300px down

3. Cookie consent banner (bottom, dismissible):
   "This website uses cookies for analytics. By continuing you 
   accept our cookie policy."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECHNICAL REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Single file: index.html (all sections on one page)
- Smooth scroll to all anchor sections
- Navbar active link updates as user scrolls (Intersection Observer)
- Mobile hamburger menu working
- Accordion JS for disclaimer section
- Form validation before submit
- Real fetch() POST to Formspree (no fake simulations)
- All CSS in assets/css/style.css
- All JS in assets/js/main.js
- Meta tags: title, description, keywords, og:title, og:description, 
  canonical, author
- Page title: "Arthashastra Insights | Manish Mishra | SEBI Registered Research Analyst"
- Favicon: assets/images/Arthashastrainsights_logo.png
- No broken links
- No placeholder X values anywhere
- No @arthashastrainsights.com emails — only apnamanish9@gmail.com

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL FOLDER STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
arthashastrainsights/
├── index.html          (single page — all sections)
├── robots.txt
├── sitemap.xml         (update to single URL)
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── Arthashastrainsights_logo.png

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
After building confirm:
1. Only index.html exists — all other HTML files deleted
2. All 9 sections present with correct IDs for anchor navigation
3. Zero instances of @arthashastrainsights.com
4. Zero instances of XXX placeholders
5. Zero instances of Mumbai or Maharashtra in address
6. SEBI reg no INH000024620 correct everywhere
7. Phone +91 9480322410 correct everywhere
8. Address Bangalore correct everywhere
9. YouTube link working in navbar, hero, training section, footer
10. Both forms pointing to Formspree
11. WhatsApp button present
12. Mobile responsive confirmed
13. Disclaimer accordion working
14. Navbar smooth scroll working

Report all files created/deleted/modified.
