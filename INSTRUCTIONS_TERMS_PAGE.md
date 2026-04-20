# INSTRUCTIONS — CREATE SEPARATE TERMS OF USE PAGE
# Save as INSTRUCTIONS_TERMS_PAGE.md in:
# D:\Claude code folder\arthashastrainsights\
# Tell Claude Code: "Read INSTRUCTIONS_TERMS_PAGE.md and execute all instructions"

---

## TASK 1 — CREATE NEW FILE terms-of-use.html

Create a new file called terms-of-use.html in the root project folder.

This should be a complete standalone HTML page with the same 
navbar, footer, ticker and styling as index.html.

Copy the navbar, footer, compliance ticker, CSS links and JS links 
exactly from index.html and use them in this new page.

The page content between navbar and footer should be:

---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Use | Arthashastra Insights</title>
  <meta name="description" content="Terms of Use for Arthashastra 
  Insights - Manish Mishra, SEBI Registered Research Analyst 
  INH000024620">
  <meta name="author" content="Manish Mishra">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" href="assets/images/Arthashastrainsights_logo1.png">
  <!-- Copy same Google Fonts link from index.html -->
</head>
<body>

  <!-- Copy EXACT compliance ticker from index.html -->
  <!-- Copy EXACT navbar/header from index.html -->

  <!-- PAGE HERO -->
  <section class="page-hero" style="background: #1a2456; 
    padding: 60px 0 40px; text-align: center;">
    <div class="container">
      <nav class="breadcrumb" style="margin-bottom: 16px; 
        font-size: 14px; color: rgba(255,255,255,0.6);">
        <a href="index.html" style="color: #f5a623; 
          text-decoration: none;">Home</a>
        <span style="margin: 0 8px;">›</span>
        <span style="color: white;">Terms of Use</span>
      </nav>
      <h1 style="font-size: clamp(1.8rem, 3vw, 2.8rem); 
        color: white; font-family: 'Playfair Display', serif;
        margin-bottom: 12px;">Terms of Use</h1>
      <p style="color: rgba(255,255,255,0.7); font-size: 1rem;">
        Please read carefully before using any content on this 
        website or subscribing to our services.</p>
    </div>
  </section>

  <!-- TERMS CONTENT -->
  <section style="background: #0a0f2e; padding: 60px 0;">
    <div class="container" style="max-width: 900px; 
      margin: 0 auto; padding: 0 24px;">

      <div style="background: rgba(245,166,35,0.1); 
        border-left: 4px solid #f5a623; padding: 16px 20px; 
        border-radius: 4px; margin-bottom: 40px;">
        <p style="color: #f5a623; font-weight: 600; 
          margin: 0 0 4px 0;">Arthashastra Insights | 
          Manish Mishra | SEBI RA INH000024620</p>
        <p style="color: rgba(255,255,255,0.7); 
          font-size: 0.9rem; margin: 0;">
          Last Updated: April 2025</p>
      </div>

      <!-- Section 1 -->
      <div class="terms-block">
        <h3>1. Acceptance of Terms</h3>
        <p>By visiting or using www.arthashastrainsights.com, 
        you agree to be bound by these Terms of Use. We reserve 
        the right to modify these terms at any time. Continued 
        use of the website constitutes acceptance of any revised 
        terms. Please review this page periodically.</p>
      </div>

      <!-- Section 2 -->
      <div class="terms-block">
        <h3>2. Registration Terms</h3>
        <p>By registering for any service, you certify that all 
        information provided is accurate and complete. Arthashastra 
        Insights reserves the right to deny access to the website 
        or any service without notice if: (a) there is any 
        unauthorized access or misuse by you; (b) you attempt to 
        assign or transfer any rights granted under this agreement; 
        (c) you violate any terms of this agreement; or (d) for 
        any other reason deemed appropriate.</p>
      </div>

      <!-- Section 3 -->
      <div class="terms-block">
        <h3>3. Intellectual Property & Copyright</h3>
        <p>All content on www.arthashastrainsights.com including 
        research reports, analysis, recommendations, methodologies, 
        and design is the exclusive intellectual property of Manish 
        Mishra operating as Arthashastra Insights. Nothing in this 
        agreement transfers any ownership rights to you.</p>
        <p>You agree not to reproduce, redistribute, rebroadcast, 
        or republish any content or recommendations from this website 
        by any means without prior written permission. Unauthorized 
        use may result in legal action including claims for actual 
        and punitive damages under Indian law. You may not rent, 
        lease, sublicense, distribute, copy, store, or time-share 
        any content from this website without explicit written 
        authorization.</p>
      </div>

      <!-- Section 4 -->
      <div class="terms-block">
        <h3>4. Disruption of Service</h3>
        <p>Arthashastra Insights shall not be liable for any loss 
        resulting directly or indirectly from delays, disruptions, 
        or interruptions due to equipment failures, connectivity 
        issues, weather, strikes, acts of God, or other causes 
        beyond our reasonable control.</p>
      </div>

      <!-- Section 5 -->
      <div class="terms-block">
        <h3>5. Prohibited Activities</h3>
        <p>Users are strictly prohibited from:</p>
        <ul>
          <li>Soliciting or promoting personal services or 
          third-party financial services to other users</li>
          <li>Copying or distributing research content without 
          explicit permission</li>
          <li>Using website content or community for resale or 
          redistribution</li>
          <li>Providing stock market services including advisory, 
          brokerage, training, or research using content from 
          this website</li>
          <li>Any activity that violates SEBI regulations or 
          applicable Indian law</li>
        </ul>
        <p>Violation of these terms will result in immediate 
        termination of access without refund.</p>
      </div>

      <!-- Section 6 -->
      <div class="terms-block">
        <h3>6. Limitation of Liability</h3>
        <p>Use of this website is entirely at your own risk. 
        All content is provided on an "as is" basis. Arthashastra 
        Insights and Manish Mishra make no warranties regarding 
        accuracy, completeness, timeliness, or fitness for any 
        particular purpose.</p>
        <p>Arthashastra Insights, Manish Mishra, and any associated 
        persons shall not be liable for any direct, indirect, 
        incidental, special, or consequential damages arising from 
        use of or inability to use this website, including any 
        reliance on research content published herein.</p>
      </div>

      <!-- Section 7 -->
      <div class="terms-block">
        <h3>7. Refund & Cancellation Policy</h3>
        <p>All payments for subscriptions, courses, or research 
        services are final and non-refundable. By making a payment 
        you acknowledge and accept this policy. For any concerns 
        regarding services, please contact apnamanish9@gmail.com. 
        We are committed to addressing your concerns promptly.</p>
      </div>

      <!-- Section 8 -->
      <div class="terms-block">
        <h3>8. Information Disclaimer</h3>
        <p>Research content published on www.arthashastrainsights.com 
        is compiled from sources believed to be reliable. However, 
        Arthashastra Insights does not warrant the accuracy, 
        completeness, or suitability of any information. All research 
        is provided for informational and educational purposes only 
        and does not constitute personalized investment advice.</p>
        <p>You assume full responsibility for any investment decisions 
        made based on content from this website. Arthashastra Insights 
        does not endorse any particular security, broker, or market 
        participant.</p>
      </div>

      <!-- Section 9 -->
      <div class="terms-block">
        <h3>9. Third Party Links</h3>
        <p>This website may contain links to third party websites. 
        Arthashastra Insights has not reviewed these sites and is 
        not responsible for their content. Inclusion of any link 
        does not imply endorsement.</p>
      </div>

      <!-- Section 10 -->
      <div class="terms-block">
        <h3>10. Indemnification</h3>
        <p>You agree to indemnify and hold harmless Manish Mishra 
        and Arthashastra Insights from any claims, losses, or damages 
        arising from: (a) your use of this website; (b) your 
        non-compliance with these terms; or (c) any third party 
        actions related to your use of research content.</p>
      </div>

      <!-- Section 11 -->
      <div class="terms-block">
        <h3>11. Governing Law & Jurisdiction</h3>
        <p>These Terms of Use shall be governed by the laws of India. 
        All disputes shall be subject to the exclusive jurisdiction 
        of the Courts of Bangalore, Karnataka, India.</p>
      </div>

      <!-- Section 12 -->
      <div class="terms-block">
        <h3>12. Dispute Resolution</h3>
        <p>Any disputes arising from use of this website or services 
        shall first be attempted to be resolved amicably. If 
        unresolved, disputes shall be referred to arbitration under 
        the Arbitration and Conciliation Act, 1996. Arbitration 
        proceedings shall be held in Bangalore, Karnataka, India.</p>
      </div>

      <!-- Section 13 -->
      <div class="terms-block">
        <h3>13. Entire Agreement</h3>
        <p>These Terms of Use constitute the entire agreement between 
        you and Arthashastra Insights. By using this website you 
        assume full responsibility for all gains and losses arising 
        from any investment decisions made based on content 
        published here.</p>
      </div>

      <!-- Contact Box -->
      <div style="background: rgba(26,36,86,0.8); 
        border: 1px solid rgba(245,166,35,0.3); 
        border-radius: 8px; padding: 20px; margin-top: 40px;">
        <p style="color: #f5a623; font-weight: 600; 
          margin: 0 0 8px 0;">Contact for Terms Related Queries</p>
        <p style="color: #e2e8f0; margin: 0; font-size: 0.95rem;">
          Manish Mishra &nbsp;|&nbsp; 
          <a href="mailto:apnamanish9@gmail.com" 
            style="color: #f5a623; text-decoration: none;">
            apnamanish9@gmail.com</a> &nbsp;|&nbsp; 
          +91 9480322410
        </p>
      </div>

      <!-- Back to Home -->
      <div style="text-align: center; margin-top: 40px;">
        <a href="index.html" style="display: inline-block; 
          background: #f5a623; color: #0a0f2e; 
          padding: 12px 32px; border-radius: 6px; 
          text-decoration: none; font-weight: 600; 
          font-size: 0.95rem;">← Back to Home</a>
      </div>

    </div>
  </section>

  <!-- Copy EXACT footer from index.html -->
  <!-- Copy EXACT JS scripts from index.html -->

</body>
</html>

---

## ADD CSS IN assets/css/style.css FOR TERMS PAGE

.terms-block {
  margin-bottom: 28px;
  padding-bottom: 28px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}

.terms-block:last-of-type {
  border-bottom: none;
}

.terms-block h3 {
  color: #f5a623;
  font-size: 1.05rem;
  font-weight: 600;
  margin-bottom: 12px;
  letter-spacing: 0.3px;
}

.terms-block p {
  color: #cbd5e1;
  font-size: 0.92rem;
  line-height: 1.85;
  margin-bottom: 10px;
}

.terms-block ul {
  color: #cbd5e1;
  font-size: 0.92rem;
  line-height: 1.85;
  padding-left: 22px;
  margin: 10px 0;
}

.terms-block ul li {
  margin-bottom: 8px;
}

---

## TASK 2 — UPDATE FOOTER LINK IN index.html

In index.html find the footer section.
Find the "Terms of Use" link in the footer.

Update it to:
<a href="terms-of-use.html" target="_blank" 
   style="color: rgba(255,255,255,0.7); text-decoration: none;">
  Terms of Use
</a>

This opens the terms page in a new tab when clicked.

Also check if "Terms of Use" appears anywhere else in index.html 
footer or elsewhere — update all such links to 
href="terms-of-use.html" target="_blank"

---

## TASK 3 — UPDATE sitemap.xml

In sitemap.xml add this new URL entry:

<url>
  <loc>https://www.arthashastrainsights.com/terms-of-use.html</loc>
  <lastmod>2025-04-20</lastmod>
  <changefreq>yearly</changefreq>
  <priority>0.3</priority>
</url>

---

## FINAL VERIFICATION

After all changes confirm:
1. terms-of-use.html file exists in project root
2. Page has same navbar and footer as index.html
3. All 13 sections present with correct content
4. No references to MaxxWealth, Anil Rai, or Prayagraj
5. Contact shows apnamanish9@gmail.com and +91 9480322410
6. Jurisdiction shows Bangalore, Karnataka
7. Footer "Terms of Use" link in index.html points to 
   terms-of-use.html and opens in new tab
8. Back to Home button works
9. Page is mobile responsive
10. sitemap.xml updated

Report all files created and modified.
