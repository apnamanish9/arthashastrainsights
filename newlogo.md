The navbar and footer have duplicate brand text appearing multiple times.
I need you to directly edit the HTML in index.html.

STEP 1 — Show me the current navbar HTML first:
Find the <header> or <nav> tag and print EVERYTHING inside it 
between the opening and closing tag so I can see exactly 
what is there.

STEP 2 — After showing me, replace the ENTIRE navbar/header 
inner content with EXACTLY this clean structure:

<header class="site-header" id="navbar">
  <nav class="navbar">
    <a href="#home" class="navbar-brand">
      <img src="assets/images/Arthashastra_Insights_logo1.png" 
           alt="Arthashastra Insights Logo" 
           class="nav-logo">
      <div class="brand-text">
        <span class="brand-name">Arthashastra Insights</span>
        <span class="brand-tagline">Insights from SEBI Registered 
        Research Analyst</span>
      </div>
    </a>
    <button class="hamburger" id="hamburger" 
            aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-links" id="nav-links">
      <li><a href="#home" class="nav-link active">Home</a></li>
      <li><a href="#about" class="nav-link">About</a></li>
      <li><a href="#services" class="nav-link">Services</a></li>
      <li><a href="#training" class="nav-link">Training</a></li>
      <li><a href="#disclaimer" class="nav-link">Disclaimer</a></li>
      <li><a href="#grievance" class="nav-link">Grievance</a></li>
      <li><a href="#contact" class="nav-link contact-btn">
          Contact</a></li>
      <li>
        <a href="https://www.youtube.com/@Arthashastrainsights" 
           target="_blank" class="nav-yt" 
           aria-label="YouTube Channel">
          <svg width="20" height="20" viewBox="0 0 24 24" 
               fill="#f5a623">
            <path d="M23.498 6.186a3.016 3.016 0 0 
            0-2.122-2.136C19.505 3.545 12 3.545 12 
            3.545s-7.505 0-9.377.505A3.017 3.017 0 0 
            0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 
            5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 
            9.376.505 9.376.505s7.505 0 9.377-.505a3.015 
            3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 
            12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 
            12l-6.273 3.568z"/>
          </svg>
        </a>
      </li>
    </ul>
  </nav>
</header>

STEP 3 — Replace the ENTIRE footer brand section 
(the left column of footer) with EXACTLY this:

<div class="footer-brand">
  <a href="#home">
    <img src="assets/images/Arthashastra_Insights_logo1.png" 
         alt="Arthashastra Insights" 
         class="footer-logo">
  </a>
  <p class="footer-brand-name">Arthashastra Insights</p>
  <p class="footer-brand-tagline">Insights from SEBI Registered 
  Research Analyst</p>
  <p class="footer-brand-sub">A brand by Manish Mishra</p>
  <p class="footer-brand-sub">Independent equity research for 
  informed investors.</p>
</div>

STEP 4 — In assets/css/style.css add/update these styles:

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
}

.nav-logo {
  height: 90px;
  width: auto;
  object-fit: contain;
  flex-shrink: 0;
}

.brand-text {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-size: 28px;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
  font-family: 'Playfair Display', serif;
}

.brand-tagline {
  font-size: 12px;
  color: #f5a623;
  letter-spacing: 0.5px;
  margin-top: 4px;
}

.footer-logo {
  height: 60px;
  width: auto;
  object-fit: contain;
  margin-bottom: 10px;
}

.footer-brand-name {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
  margin: 6px 0 2px 0;
}

.footer-brand-tagline {
  font-size: 11px;
  color: #f5a623;
  margin-bottom: 8px;
}

/* CRITICAL — Remove any old duplicate styles */
/* Delete or comment out any of these if they exist: */
/* .logo-name, .logo-tagline, .site-header .logo-name */
/* .nav-brand-text, .header-brand, .brand-title */
/* Any CSS that creates a second brand name display */

@media(max-width: 768px) {
  .nav-logo { height: 60px; }
  .brand-name { font-size: 18px; }
  .brand-tagline { font-size: 10px; }
}

STEP 5 — CRITICAL CLEANUP:
Search entire index.html for any remaining instances of:
- "Arthashastra Insights" text appearing OUTSIDE the 
  navbar-brand div and footer-brand div
- Any <span class="logo-name"> or <span class="logo-tagline">
- Any duplicate brand text anywhere
DELETE all duplicates found.

After all changes print the final navbar HTML so I can 
verify before testing.
The logo file is confirmed at: 
assets/images/Arthashastrainsights_logo1.png

Do these steps:

STEP 1 — Search and replace logo filename:
In index.html replace ALL instances of any logo filename with:
assets/images/Arthashastrainsights_logo1.png

Replace these filenames wherever found:
- Arthashastra_Insights_logo1.png
- Arthashastrainsights_logo.png  
- Arthashastra_Insights_logo.png
- Any other logo png filename

STEP 2 — Print the COMPLETE current navbar HTML:
Find the opening <header or <nav tag and print 
everything inside it. I need to see exact current code.

Do STEP 2 first before making any other changes.
