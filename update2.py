"""
INSTRUCTIONS_UPDATE2 — bulk changes across all HTML files
Tasks: 1 (tagline), 4 (YouTube nav+footer), 5 (legal), 6 (ticker)
"""
import os, re

base = r'D:\Claude code folder\arthashastrainsights'

HTML = [
    'index.html', 'about.html', 'services.html', 'stock-picks.html',
    'disclaimer.html', 'grievance-redressal.html', 'investor-charter.html',
    'terms-of-use.html', 'contact.html'
]

YT_URL = 'https://www.youtube.com/@Arthashastrainsights'

YT_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
    'width="18" height="18" fill="#f5a623" style="display:block;">'
    '<path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 '
    '12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 '
    '3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s'
    '7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93'
    '-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'
)

YT_NAV = (
    f'<a href="{YT_URL}" target="_blank" rel="noopener noreferrer" '
    f'class="nav-youtube" title="Watch on YouTube" aria-label="Watch on YouTube" '
    f'style="padding:0.375rem 0.5rem;display:flex;align-items:center;line-height:1;">'
    f'{YT_SVG}</a>'
)

YT_FOOTER = (
    '\n          <div class="footer-contact-item" style="margin-top:.75rem;">'
    '\n            <span class="icon">▶</span>'
    f'\n            <span><a href="{YT_URL}" target="_blank" rel="noopener noreferrer" '
    'style="color:var(--accent-light);">YouTube Channel</a></span>'
    '\n          </div>'
)

NEW_TICKER = (
    'Manish Mishra | SEBI Registered Research Analyst (Individual, Part-Time) | '
    'Reg. No. INH000024620 | Arthashastra Insights is a brand name, not a SEBI '
    'registered entity | Investments in securities market are subject to market risk. '
    'Read all related documents carefully before investing. | Registration granted by '
    'SEBI and certification from NISM in no way guarantee performance or assurance of '
    'returns | Past performance is not indicative of future results | '
    'NISM Certificate No.: 202400095615 |'
)

NEW_COMPLIANCE = (
    '\n            <strong>Manish Mishra</strong>, SEBI Registered Research Analyst '
    '(Part-Time), <strong>Reg. No. INH000024620</strong>, operating under the brand name '
    '<strong>Arthashastra Insights</strong>. Arthashastra Insights is not a SEBI '
    'registered entity. Registration is held by Manish Mishra as an individual. '
    'Investments in securities are subject to market risks. Read all related documents '
    'carefully before investing. Past performance is not indicative of future results.\n          '
)

NEW_SEBI_BAR = (
    '<strong>⚠ Investments are subject to market risk. Past performance is not indicative '
    'of future results.</strong> Manish Mishra is a SEBI Registered Research Analyst '
    '(Part-Time), Reg. No. INH000024620, operating under the brand name Arthashastra '
    'Insights. Arthashastra Insights is not a SEBI registered entity. Research reports '
    'are not personalised investment recommendations. Investors are advised to conduct '
    'independent due diligence and consult a SEBI Registered Investment Adviser (RIA) '
    'before investing. For grievances, contact SEBI SCORES at '
    '<a href="https://scores.sebi.gov.in" target="_blank" rel="noopener noreferrer" '
    'style="color:rgba(255,180,180,0.8);">scores.sebi.gov.in</a>.'
)

# Ordered global text replacements (most specific first)
TEXT_REPLACEMENTS = [
    # Compliance commitment text in grievance page
    ('Arthashastra Insights (SEBI RA Reg. No. INH000024620) is committed to',
     'Manish Mishra (SEBI RA Reg. No. INH000024620), operating as Arthashastra Insights, is committed to'),

    # Disclaimer page
    ('Arthashastra Insights is a SEBI Registered Research Analyst firm (Registration No. INH000024620)',
     'Manish Mishra (SEBI RA Reg. No. INH000024620), trading as Arthashastra Insights, is a SEBI Registered Research Analyst (Individual, Part-Time)'),

    # About / index intro
    ('Arthashastra Insights is a SEBI Registered Research Analyst firm committed to delivering',
     'Manish Mishra, operating as Arthashastra Insights, is a SEBI Registered Research Analyst (Individual, Part-Time) committed to delivering'),

    ('Arthashastra Insights is a SEBI Registered Research Analyst firm',
     'Manish Mishra (trading as Arthashastra Insights) is a SEBI Registered Research Analyst (Individual, Part-Time)'),

    # Footer compliance text patterns (also handled by regex below, belt-and-suspenders)
    ('<strong>Arthashastra Insights</strong> is registered with SEBI as a Research Analyst under SEBI (Research Analyst) Regulations, 2014.',
     '<strong>Manish Mishra</strong> is registered with SEBI as an Individual Research Analyst (Part-Time) under SEBI (Research Analyst) Regulations, 2014, operating under the brand name <strong>Arthashastra Insights</strong>.'),

    ('Arthashastra Insights is registered with SEBI as a Research Analyst under SEBI (Research Analyst) Regulations, 2014.',
     'Manish Mishra is registered with SEBI as an Individual Research Analyst (Part-Time) under SEBI (Research Analyst) Regulations, 2014, operating as Arthashastra Insights.'),

    ('Arthashastra Insights is registered with SEBI as a <strong>Research Analyst (Reg. No. INH000024620)</strong>',
     'Manish Mishra is registered with SEBI as a <strong>Research Analyst (Individual, Part-Time) (Reg. No. INH000024620)</strong>, operating as Arthashastra Insights'),

    ('Arthashastra Insights is registered with SEBI as a Research Analyst (Reg. No. INH000024620)',
     'Manish Mishra is registered with SEBI as an Individual Research Analyst (Part-Time) (Reg. No. INH000024620), operating as Arthashastra Insights'),

    # Investor charter Section A
    ('Arthashastra Insights, registered with SEBI as a Research Analyst (Reg. No. INH000024620), provides',
     'Manish Mishra, registered with SEBI as an Individual Research Analyst (Part-Time) (Reg. No. INH000024620), operating as Arthashastra Insights, provides'),

    # Risk notice band index.html
    ('Arthashastra Insights is a SEBI Registered Research Analyst (Reg. No. INH000024620) and does not provide portfolio management or investment advisory services.',
     'Manish Mishra (SEBI RA Reg. No. INH000024620), operating as Arthashastra Insights, does not provide portfolio management or investment advisory services.'),

    # Broader pattern
    ('Arthashastra Insights is a SEBI Registered Research Analyst (Reg. No. INH000024620)',
     'Manish Mishra (SEBI RA Reg. No. INH000024620), operating as Arthashastra Insights'),

    # Research Analyst Regulations reference
    ('Arthashastra Insights operates under the full purview of SEBI (Research Analyst) Regulations, 2014.',
     'Manish Mishra operates under the full purview of SEBI (Research Analyst) Regulations, 2014, under the brand name Arthashastra Insights.'),

    # footer-reg type
    ('<p><strong>Type:</strong> Research Analyst</p>',
     '<p><strong>Type:</strong> Research Analyst (Individual, Part-Time)</p>'),

    # Methodology section note
    ('Research reports published by Arthashastra Insights reflect the views of the analyst',
     'Research reports published under Arthashastra Insights reflect the views of Manish Mishra, the SEBI Registered Research Analyst'),

    # About page sebi compliance section header para
    ('Regulatory registration is not an endorsement of quality or guarantee of returns.',
     'Manish Mishra holds the SEBI Research Analyst registration (INH000024620) as an individual. Regulatory registration is not an endorsement of quality or guarantee of returns.'),

    # About page registration table - Entity Name row
    ('<td style="padding:.75rem .5rem;font-weight:600;color:var(--text-dark);">Arthashastra Insights</td>',
     '<td style="padding:.75rem .5rem;font-weight:600;color:var(--text-dark);">Manish Mishra (Individual)<br><span style="font-size:.8rem;color:var(--text-light);">Brand: Arthashastra Insights</span></td>'),

    # About page Registration Type row
    ('<td style="padding:.75rem .5rem;font-weight:600;">Research Analyst</td>',
     '<td style="padding:.75rem .5rem;font-weight:600;">Research Analyst (Individual, Part-Time)</td>'),
]

changed = []

for fname in HTML:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    out = src

    # ── Task 1: Logo tagline ─────────────────────────────────────────────
    out = out.replace(
        '<span class="logo-tagline">SEBI Registered Research Analyst</span>',
        '<span class="logo-tagline">Insights from SEBI Registered Research Analyst</span>'
    )

    # ── Task 4: YouTube in navbar ────────────────────────────────────────
    if YT_URL not in out or 'nav-youtube' not in out:
        def _add_yt_nav(m):
            return m.group(1) + '\n        ' + YT_NAV + m.group(2)
        out = re.sub(
            r'(<a href="contact\.html" class="nav-cta">Contact Us</a>)(\s*\n\s*</nav>)',
            _add_yt_nav,
            out
        )

    # ── Task 4: YouTube in footer ────────────────────────────────────────
    if 'YouTube Channel' not in out:
        # Works for both single-line and multi-line phone entries
        out = re.sub(
            r'(<span class="icon">📞</span>\s*<span>\+91\s*9480322410</span>\s*</div>)',
            lambda m: m.group(1) + YT_FOOTER,
            out
        )

    # ── Task 5: Footer compliance-text ───────────────────────────────────
    out = re.sub(
        r'<p class="compliance-text">.*?</p>',
        '<p class="compliance-text">' + NEW_COMPLIANCE + '</p>',
        out,
        flags=re.DOTALL
    )

    # ── Task 5: Footer sebi-bar ───────────────────────────────────────────
    out = re.sub(
        r'(<div class="footer-sebi-bar">\s*<div class="container">\s*<p>).*?(</p>\s*</div>\s*</div>)',
        lambda m: m.group(1) + NEW_SEBI_BAR + m.group(2),
        out,
        flags=re.DOTALL
    )

    # ── Task 6: Ticker text ───────────────────────────────────────────────
    out = re.sub(
        r'(<span class="ticker-item">)[^<]*(</span>)',
        r'\g<1>' + NEW_TICKER + r'\g<2>',
        out
    )

    # ── Task 5: Global text replacements ─────────────────────────────────
    for old, new in TEXT_REPLACEMENTS:
        out = out.replace(old, new)

    if out != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(out)
        changed.append(fname)
        print(f'  CHANGED: {fname}')
    else:
        print(f'  no change: {fname}')

print(f'\nDone. {len(changed)} file(s) changed: {changed}')
