# INSTRUCTIONS UPDATE 2 FOR CLAUDE CODE
# Save this file as INSTRUCTIONS_UPDATE2.md in:
# D:\Claude code folder\arthashastrainsights\
# Then tell Claude Code: "Read INSTRUCTIONS_UPDATE2.md and execute all instructions"

---

## TASK 1 — NAVBAR BRANDING TEXT CHANGE
Find the navbar/header on ALL HTML pages where it currently shows:
  "Arthashastra Insights"
  "SEBI REGISTERED RESEARCH ANALYST"

Change the tagline/subtitle text from:
  "SEBI REGISTERED RESEARCH ANALYST"
To:
  "Insights from SEBI Registered Research Analyst"

Apply this change consistently across all HTML pages in the navbar header section.

---

## TASK 2 — ENLARGE NAVBAR BRAND FONTS
In assets/css/style.css find the navbar brand name and tagline styles.

For the main brand name "Arthashastra Insights":
- Set font-size to 20px (or 1.25rem)
- Set font-weight to 700 (bold)
- Make sure it is prominent and clearly visible

For the tagline "Insights from SEBI Registered Research Analyst":
- Set font-size proportionately — approximately 11px or 0.7rem
- Set font-weight to 500
- Set letter-spacing to 0.5px
- Keep it visible but secondary to the main brand name

For the navbar logo image:
- Increase the logo size proportionately
- Set height to approximately 55px to 60px (from whatever it currently is)
- Maintain aspect ratio (width: auto)
- Make sure logo, brand name and tagline all look balanced together

These elements should be PROMINENT and immediately noticeable when someone visits the site.

---

## TASK 3 — REPLACE "AT A GLANCE" SECTION COMPLETELY
Find the section on index.html (homepage) called "At a Glance" or 
"Stats" or similar section that shows:
- Years of Research
- Stocks Analysed  
- Sectors Covered
- Subscribers
or any similar statistics cards.

DELETE that entire section completely.

Replace it with a single clean prominent banner/section that says:

  "12+ Years of Stock Market Wisdom"

Style this as:
- Full width section
- Dark navy background (#0a0f2e) with gold (#f5a623) accent
- Large centered text — font size 2.5rem to 3rem
- "12+" in gold color, rest of text in white
- Subtitle below in smaller text (1rem, light gray):
  "Combining institutional discipline from banking with deep market 
   expertise in Equity, F&O and Commodities"
- Add a thin gold horizontal line above and below this section
- Padding: 40px top and bottom

---

## TASK 4 — ADD YOUTUBE CHANNEL LINK
Add the YouTube channel link https://www.youtube.com/@Arthashastrainsights
in the following places:

1. NAVBAR — Add a YouTube icon link in the navbar (top right area, 
   before or after the Contact Us button):
   - Use YouTube SVG icon or unicode ▶ symbol
   - Color: gold (#f5a623) 
   - Link: https://www.youtube.com/@Arthashastrainsights
   - Opens in new tab (target="_blank")
   - Tooltip: "Watch on YouTube"

2. FOOTER on ALL pages — In the social media / connect section of footer:
   - Add YouTube link with label "YouTube Channel"
   - Link: https://www.youtube.com/@Arthashastrainsights
   - Opens in new tab
   - Use YouTube icon or ▶ symbol

3. ABOUT PAGE (about.html) — Add a dedicated "Watch My Analysis" section 
   or button:
   - Text: "Watch Free Market Analysis on YouTube"
   - Button style: gold background, dark text
   - Link: https://www.youtube.com/@Arthashastrainsights
   - Opens in new tab

4. HOME PAGE (index.html) — Add YouTube link in hero section or 
   below hero as a secondary CTA:
   - Text: "▶ Watch Free Analysis on YouTube"
   - Style as outlined/ghost button in gold
   - Link: https://www.youtube.com/@Arthashastrainsights
   - Opens in new tab

---

## TASK 5 — IMPORTANT LEGAL CLARIFICATION THROUGHOUT SITE
This is a critical compliance correction. 

CURRENT INCORRECT IMPRESSION:
The site currently implies "Arthashastra Insights" is a SEBI Registered 
Research Analyst firm/entity.

CORRECT FACTS:
- Arthashastra Insights is NOT a SEBI registered firm or company
- Manish Mishra is the individual who holds SEBI Research Analyst 
  registration (INH000024620) as a PART-TIME Research Analyst
- The registration is in the name of MANISH MISHRA as an individual
- Arthashastra Insights is the trading name / brand under which 
  Manish Mishra operates

Apply these corrections across ALL pages:

FIND and REPLACE these phrases wherever they appear:

WRONG: "Arthashastra Insights is a SEBI Registered Research Analyst"
RIGHT: "Manish Mishra (trading as Arthashastra Insights) is a SEBI 
        Registered Research Analyst (Reg. No. INH000024620)"

WRONG: "We are SEBI Registered"
RIGHT: "Manish Mishra is SEBI Registered as an Individual Research 
        Analyst (Reg. No. INH000024620)"

WRONG: "Our SEBI Registration"
RIGHT: "SEBI Registration of Manish Mishra"

WRONG: "Arthashastra Insights (SEBI RA Reg. No. INH000024620)"
RIGHT: "Manish Mishra (SEBI RA Reg. No. INH000024620), operating 
        under the brand Arthashastra Insights"

In the FOOTER disclaimer on ALL pages, update the SEBI disclosure line to:
"Manish Mishra, SEBI Registered Research Analyst (Part-Time), 
 Reg. No. INH000024620, operating under the brand name 
 Arthashastra Insights. Arthashastra Insights is not a SEBI 
 registered entity. Registration is held by Manish Mishra as 
 an individual."

In the DISCLAIMER page (disclaimer.html):
Add a prominent section at the top:
"IMPORTANT CLARIFICATION: Arthashastra Insights is a brand name 
 operated by Manish Mishra, who is registered with SEBI as an 
 Individual Part-Time Research Analyst vide Registration No. 
 INH000024620. Arthashastra Insights as an entity is NOT 
 registered with SEBI. All research and analysis is conducted 
 by Manish Mishra in his individual capacity as a SEBI Registered 
 Research Analyst."

In the ABOUT page (about.html):
Update the credentials section to clearly state:
"SEBI Registered Research Analyst (Individual, Part-Time)
 Registration No. INH000024620
 Registration held by: Manish Mishra
 Brand Name: Arthashastra Insights"

In the SERVICES page (services.html):
Add at the top of the page before any service description:
"All research services are provided by Manish Mishra in his 
 individual capacity as a SEBI Registered Research Analyst 
 (Reg. No. INH000024620). Arthashastra Insights is the brand 
 name under which these services are offered."

In INVESTOR CHARTER (investor-charter.html):
Update the header to read:
"Investor Charter — Manish Mishra
 SEBI Registered Research Analyst (Individual)
 Reg. No. INH000024620
 Brand: Arthashastra Insights"

In GRIEVANCE REDRESSAL (grievance-redressal.html):
Update the header and all references:
"Grievance Redressal — Manish Mishra
 SEBI Registered Research Analyst (Individual, Part-Time)
 Reg. No. INH000024620"

---

## TASK 6 — SCROLLING TICKER UPDATE
Update the scrolling compliance ticker on ALL pages to reflect 
the correct individual registration:

"Manish Mishra | SEBI Registered Research Analyst (Individual, Part-Time) | 
Reg. No. INH000024620 | Arthashastra Insights is a brand name, not a SEBI 
registered entity | Investments in securities market are subject to market 
risk. Read all related documents carefully before investing. | Registration 
granted by SEBI and certification from NISM in no way guarantee performance 
or assurance of returns | Past performance is not indicative of future results 
| NISM Certificate No.: 202400095615 |"

---

## FINAL VERIFICATION
After all changes confirm:
1. Navbar shows "Arthashastra Insights" at font-size 20px prominently
2. Navbar tagline shows "Insights from SEBI Registered Research Analyst"
3. Logo is enlarged proportionately (height ~55-60px)
4. "At a Glance" stats section is completely removed from homepage
5. "12+ Years of Stock Market Wisdom" section exists on homepage
6. YouTube link https://www.youtube.com/@Arthashastrainsights appears 
   in navbar, footer, about page and home page
7. No page incorrectly states "Arthashastra Insights is SEBI Registered"
8. All pages correctly state Manish Mishra is the individual SEBI RA
9. Footer on all pages has updated individual RA disclosure
10. Scrolling ticker updated with correct text

Report all files changed with summary of changes made.
