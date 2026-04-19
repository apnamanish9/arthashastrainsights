# INSTRUCTIONS UPDATE 3 — VISUAL ENHANCEMENTS
# Save as INSTRUCTIONS_UPDATE3.md in:
# D:\Claude code folder\arthashastrainsights\
# Tell Claude Code: "Read INSTRUCTIONS_UPDATE3.md and execute all instructions"

---

## TASK 1 — HERO SECTION: ROTATING BACKGROUND WITH QUOTES

Replace the current static hero background with a full-screen 
image slideshow that auto-rotates every 5 seconds with smooth 
fade transition.

Use 4 high-quality UNSPLASH image URLs (no download needed — 
use direct URLs):

IMAGE 1 — Stock chart / trading screen:
https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1920&q=80

IMAGE 2 — Gold coins / wealth:
https://images.unsplash.com/photo-1610375461246-83df859d849d?w=1920&q=80

IMAGE 3 — Green nature / growth:
https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1920&q=80

IMAGE 4 — City / financial district:
https://images.unsplash.com/photo-1486325212027-8081e485255e?w=1920&q=80

Each background image must have:
- A dark overlay (rgba(0,0,0,0.65)) so text stays readable
- A famous quote displayed at the bottom of the hero section
- Quote fades in with the image

QUOTES for each image (in same order as images):
1. "The stock market is a device for transferring money from 
   the impatient to the patient." — Warren Buffett

2. "Gold is money. Everything else is credit." 
   — J.P. Morgan

3. "In investing, what is comfortable is rarely profitable." 
   — Robert Arnott

4. "The four most dangerous words in investing are: 
   'This time it's different.'" — Sir John Templeton

Quote styling:
- Position: bottom center of hero, above the SEBI badge strip
- Font: italic, 16px, white, opacity 0.9
- Attribution: 13px, gold (#f5a623), not italic
- Fade in/out with background transition
- Background: subtle dark gradient behind quote text

SLIDESHOW IMPLEMENTATION:
- Use CSS transitions for smooth fade (opacity 0 to 1, duration 1.5s)
- Auto-rotate every 6 seconds using JavaScript setInterval
- Add 4 small dot indicators at bottom of hero showing current slide
- Dots: inactive = white 30% opacity, active = gold (#f5a623)
- No pause on hover needed

---

## TASK 2 — WHATSAPP FLOATING BUTTON

Add a WhatsApp floating button that:
- Is ALWAYS fixed at bottom-right of screen (position: fixed)
- Does NOT move when user scrolls
- Stays on top of all content (z-index: 9999)
- Links to: https://wa.me/919480322410
- Opens in new tab
- Has tooltip on hover: "Chat on WhatsApp"

Button design:
- Circle button, 56px diameter
- Background: #25D366 (WhatsApp green)
- WhatsApp SVG icon inside (white, 28px)
- Box shadow: 0 4px 12px rgba(37,211,102,0.4)
- Positioned: bottom 24px, right 24px
- On hover: slightly scale up (transform: scale(1.1))
- Pulse animation: subtle green glow pulse every 3 seconds 
  to draw attention

WhatsApp SVG icon to use:
<svg viewBox="0 0 24 24" fill="white" width="28" height="28">
  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
</svg>

---

## TASK 3 — LIVE MARKET TICKER BELOW HERO

Add a live scrolling ticker bar immediately BELOW the hero section
(before the About section).

Style:
- Full width, dark background (#0d1117)
- Gold text (#f5a623) for index names
- White text for prices
- Green (#22c55e) for positive change
- Red (#ef4444) for negative change
- Continuous left-scroll animation (CSS animation, no pause)
- Font: monospace or Inter, 13px, bold for values

Since live data requires an API key, implement it this way:

PRIMARY METHOD — TradingView Widget (FREE, no API key needed):
Embed the TradingView ticker tape widget which shows live Indian 
market data automatically. Add this inside a div below the hero:

<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" 
    src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" 
    async>
  {
    "symbols": [
      {"proName": "NSE:NIFTY","title": "Nifty 50"},
      {"proName": "NSE:BANKNIFTY","title": "Bank Nifty"},
      {"proName": "NSE:CNXIT","title": "Nifty IT"},
      {"proName": "NSE:CNXPHARMA","title": "Nifty Pharma"},
      {"proName": "NSE:CNXAUTO","title": "Nifty Auto"},
      {"proName": "NSE:CNXFMCG","title": "Nifty FMCG"},
      {"proName": "NSE:CNXMETAL","title": "Nifty Metal"},
      {"proName": "NSE:CNXREALTY","title": "Nifty Realty"},
      {"proName": "NSE:CNXENERGY","title": "Nifty Energy"},
      {"proName": "MCX:GOLD1!","title": "Gold"},
      {"proName": "MCX:SILVER1!","title": "Silver"},
      {"proName": "MCX:CRUDEOIL1!","title": "Crude Oil"}
    ],
    "showSymbolLogo": true,
    "colorTheme": "dark",
    "isTransparent": false,
    "displayMode": "adaptive",
    "locale": "en"
  }
  </script>
</div>

Wrap this in a section with:
- id="market-ticker"
- No padding/margin so it sits flush below hero
- Full width 100%

---

## TASK 4 — SERVICE CARDS: UNIQUE BACKGROUND IMAGES

In the Services section, each service card should have its own 
unique stock market related background image with dark overlay.

Use these Unsplash image URLs as card backgrounds:

CARD 1 — Swing Trading Research:
Background: https://images.unsplash.com/photo-1642790551116-18a150d248d3?w=800&q=80
(Stock chart candlesticks)

CARD 2 — Momentum Trading Research:
Background: https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80
(Trading screens with momentum)

CARD 3 — Long Term Investing Research:
Background: https://images.unsplash.com/photo-1604594849809-dfedbc827105?w=800&q=80
(Growth/investment theme)

Card styling with background images:
- background-image with dark overlay: linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.72))
- background-size: cover
- background-position: center
- All text in white
- Card border: 1px solid rgba(245,166,35,0.3)
- On hover: border becomes gold, slight scale 1.02
- Minimum height: 320px
- Padding: 32px

Same treatment for TRAINING / COURSES cards:

COURSE CARD 1 — Swing Trading Masterclass:
Background: https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&q=80
(Charts and analysis)

COURSE CARD 2 — Momentum Trading Course:
Background: https://images.unsplash.com/photo-1569025690938-a00729c9e1f9?w=800&q=80
(Fast movement / energy)

COURSE CARD 3 — Long Term Investing Framework:
Background: https://images.unsplash.com/photo-1559526324-593bc073d938?w=800&q=80
(Growth and future)

---

## TASK 5 — VISION AND MISSION SECTION

Add a new section between Training and Disclaimer sections.
Section id="vision-mission"
Background: #1a2456 (deep blue)

Layout: Two columns side by side on desktop, stacked on mobile.
Add thin gold vertical divider between columns on desktop.

LEFT COLUMN — VISION:
Icon: Eye SVG (outline, gold, 36px)
Heading: "Our Vision" (gold, 22px, Playfair Display)
Content:
"To become a trusted and transparent research partner for investors, 
empowering them to make informed financial decisions through 
disciplined, data-driven insights and ethical practices."

RIGHT COLUMN — MISSION:
Icon: Target/Bullseye SVG (outline, gold, 36px)  
Heading: "Our Mission" (gold, 22px, Playfair Display)
Content:
"To provide unbiased, research-backed investment insights aligned 
with regulatory standards set by SEBI. We simplify complex market 
data into actionable insights that are easy to understand and 
implement, helping clients achieve their financial goals."

Section padding: 80px top and bottom.
Add this section to the navbar as "Vision" anchor link OR 
include it under the existing nav without separate nav link
(keep navbar clean — do not add new nav item for this).

---

## TASK 6 — WHY CHOOSE US SECTION (LUXURY MINIMAL STYLE)

Add a "Why Choose Us" section immediately AFTER the Vision/Mission section.
Section id="why-choose-us"

BACKGROUND: Plain white (#ffffff) — clean luxury look
Section padding: 100px top and bottom

SECTION HEADER (centered):
Title: "Why Choose Us" 
  - Font size: 32px
  - Font weight: 600
  - Color: #111827
  - Letter spacing: 0.5px
Subtitle: "Built on discipline, research, and regulatory integrity"
  - Font size: 15px
  - Color: #6B7280
  - Margin top: 10px
  - Letter spacing: 0.3px
Space below header before columns: 60px

LAYOUT: 4 columns horizontal on desktop (max-width 1200px centered)
On tablet (768px): 2x2 grid
On mobile: single column

GAP between columns: 60px
Optional subtle vertical divider between columns: 1px solid #E5E7EB

EACH COLUMN has exactly 3 elements in this order:
① Icon (28px, outline style, color #9CA3AF)
② Title (12-14px, ALL CAPS, letter-spacing: 2px, color: #6B7280, margin-top: 14px)
③ Main text (17px, font-weight: 500, color: #111827, margin-top: 10px)

COLUMN 1 — CREDIBILITY:
Icon: Shield outline SVG
Title: CREDIBILITY
Text: SEBI Registered Analyst

COLUMN 2 — EXPERTISE:
Icon: Line chart / trending up outline SVG  
Title: EXPERTISE
Text: Technical & Fundamental Analysis

COLUMN 3 — PROCESS:
Icon: Gear/Settings outline SVG
Title: PROCESS
Text: Data-Driven Insights

COLUMN 4 — TRUST:
Icon: Handshake outline SVG
Title: TRUST
Text: Transparent & Ethical Practices

HOVER EFFECT on each column (subtle only):
- Icon color changes from #9CA3AF to #6B7280
- Text color deepens slightly
- Column moves up 2px (transform: translateY(-2px))
- Transition: all 0.2s ease
- NO scaling, NO glow, NO animations

Use these clean SVG icons inline (outline style, stroke not fill):

Shield icon:
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" 
  stroke="#9CA3AF" stroke-width="1.5" stroke-linecap="round" 
  stroke-linejoin="round">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>

Chart/Trending Up icon:
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" 
  stroke="#9CA3AF" stroke-width="1.5" stroke-linecap="round" 
  stroke-linejoin="round">
  <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
  <polyline points="17 6 23 6 23 12"/>
</svg>

Gear/Settings icon:
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" 
  stroke="#9CA3AF" stroke-width="1.5" stroke-linecap="round" 
  stroke-linejoin="round">
  <circle cx="12" cy="12" r="3"/>
  <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>
</svg>

Handshake icon:
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" 
  stroke="#9CA3AF" stroke-width="1.5" stroke-linecap="round" 
  stroke-linejoin="round">
  <path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 0C1.46 6.7 1.33 10.28 4 13l8 8 8-8c2.67-2.72 2.54-6.3.42-8.42z"/>
</svg>

---

## TASK 7 — UPDATE CSS FOR ALL NEW SECTIONS

In assets/css/style.css add/update styles for:

1. Hero slideshow:
.hero-slide { position: absolute; inset: 0; opacity: 0; 
  transition: opacity 1.5s ease; background-size: cover; 
  background-position: center; }
.hero-slide.active { opacity: 1; }
.slide-quote { position: absolute; bottom: 120px; left: 50%; 
  transform: translateX(-50%); text-align: center; 
  background: rgba(0,0,0,0.4); padding: 16px 32px; 
  border-radius: 8px; max-width: 700px; width: 90%; }
.slide-dots { position: absolute; bottom: 80px; left: 50%; 
  transform: translateX(-50%); display: flex; gap: 8px; }
.slide-dot { width: 8px; height: 8px; border-radius: 50%; 
  background: rgba(255,255,255,0.3); cursor: pointer; 
  transition: background 0.3s; }
.slide-dot.active { background: #f5a623; }

2. WhatsApp button:
.whatsapp-float { position: fixed; bottom: 24px; right: 24px; 
  z-index: 9999; width: 56px; height: 56px; background: #25D366; 
  border-radius: 50%; display: flex; align-items: center; 
  justify-content: center; box-shadow: 0 4px 12px rgba(37,211,102,0.4); 
  text-decoration: none; transition: transform 0.2s; }
.whatsapp-float:hover { transform: scale(1.1); }
@keyframes whatsapp-pulse { 
  0% { box-shadow: 0 4px 12px rgba(37,211,102,0.4); }
  50% { box-shadow: 0 4px 20px rgba(37,211,102,0.7); }
  100% { box-shadow: 0 4px 12px rgba(37,211,102,0.4); } }
.whatsapp-float { animation: whatsapp-pulse 3s infinite; }

3. Why Choose Us:
.why-choose-us { background: #ffffff; padding: 100px 0; }
.why-grid { display: grid; grid-template-columns: repeat(4,1fr); 
  gap: 60px; max-width: 1200px; margin: 60px auto 0; 
  padding: 0 40px; }
.why-item { text-align: center; cursor: default; 
  transition: transform 0.2s ease; }
.why-item:hover { transform: translateY(-2px); }
.why-item:hover svg { stroke: #6B7280; }
.why-item:hover .why-text { color: #030712; }
.why-title { font-size: 12px; letter-spacing: 2px; 
  color: #6B7280; text-transform: uppercase; margin-top: 14px; }
.why-text { font-size: 17px; font-weight: 500; color: #111827; 
  margin-top: 10px; }
.why-divider { width: 1px; background: #E5E7EB; }
@media(max-width:768px) { 
  .why-grid { grid-template-columns: repeat(2,1fr); gap: 40px; }
  .why-divider { display: none; } }
@media(max-width:480px) { 
  .why-grid { grid-template-columns: 1fr; } }

4. Vision Mission:
.vision-mission { background: #1a2456; padding: 80px 0; }
.vm-grid { display: grid; grid-template-columns: 1fr 1px 1fr; 
  gap: 60px; max-width: 1000px; margin: 0 auto; padding: 0 40px; 
  align-items: center; }
.vm-divider { background: rgba(245,166,35,0.3); }
@media(max-width:768px) { 
  .vm-grid { grid-template-columns: 1fr; }
  .vm-divider { display: none; } }

---

## TASK 8 — UPDATE JS (assets/js/main.js)

Add hero slideshow JavaScript:

const slides = document.querySelectorAll('.hero-slide');
const dots = document.querySelectorAll('.slide-dot');
let current = 0;

function goToSlide(n) {
  slides[current].classList.remove('active');
  dots[current].classList.remove('active');
  current = (n + slides.length) % slides.length;
  slides[current].classList.add('active');
  dots[current].classList.add('active');
}

setInterval(() => goToSlide(current + 1), 6000);

dots.forEach((dot, i) => {
  dot.addEventListener('click', () => goToSlide(i));
});

// Initialize first slide
if(slides.length > 0) {
  slides[0].classList.add('active');
  if(dots.length > 0) dots[0].classList.add('active');
}

---

## FINAL VERIFICATION
After all changes confirm:
1. Hero rotates through 4 images with quotes automatically
2. Dot indicators show and change with slides
3. WhatsApp button fixed at bottom-right on ALL scroll positions
4. TradingView live ticker shows below hero with Indian indices
5. Service cards (3) each have unique background images
6. Course cards (3) each have unique background images
7. Vision & Mission section present between Training and Disclaimer
8. Why Choose Us section present with 4-column luxury layout
9. All hover effects working (subtle only)
10. Mobile responsive for all new sections
11. No broken image links
12. WhatsApp links to wa.me/919480322410

Report all changes made to each file.
