/* ============================================================
   Arthashastra Insights — Single Page JS
   Manish Mishra | SEBI RA INH000024620
   ============================================================ */
(function () {
  'use strict';

  const $ = (s, ctx = document) => ctx.querySelector(s);
  const $$ = (s, ctx = document) => [...ctx.querySelectorAll(s)];
  const on = (el, ev, fn, opts) => el && el.addEventListener(ev, fn, opts);

  /* ────────────────────────────────────────
     0. Hero Slideshow
  ──────────────────────────────────────── */
  const slides = document.querySelectorAll('.hero-slide');
  const dots   = document.querySelectorAll('.slide-dot');
  let current  = 0;

  function goToSlide(n) {
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
  }

  if (slides.length > 0) {
    slides[0].classList.add('active');
    if (dots.length > 0) dots[0].classList.add('active');
    setInterval(() => goToSlide(current + 1), 6000);
    dots.forEach((dot, i) => {
      dot.addEventListener('click', () => goToSlide(i));
    });
  }

  /* ────────────────────────────────────────
     1. Ticker duplicate for seamless loop
  ──────────────────────────────────────── */
  const tickerTrack = $('.ticker-track');
  if (tickerTrack) tickerTrack.innerHTML += tickerTrack.innerHTML;

  /* ────────────────────────────────────────
     2. Sticky Header
  ──────────────────────────────────────── */
  const header = $('.site-header');
  if (header) {
    on(window, 'scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
  }

  /* ────────────────────────────────────────
     3. Mobile Navigation
  ──────────────────────────────────────── */
  const hamburger = $('.hamburger');
  const navLinks  = $('#nav-links');
  if (hamburger && navLinks) {
    on(hamburger, 'click', () => {
      const open = navLinks.classList.toggle('active');
      hamburger.classList.toggle('open', open);
      hamburger.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    $$('a', navLinks).forEach(a => {
      on(a, 'click', () => {
        navLinks.classList.remove('active');
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
    on(document, 'click', e => {
      if (header && !header.contains(e.target) && !hamburger.contains(e.target)) {
        navLinks.classList.remove('active');
        hamburger.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  /* ────────────────────────────────────────
     4. Active Nav Link on Scroll
         Uses IntersectionObserver on sections
  ──────────────────────────────────────── */
  const navLinks = $$('.nav-links a[href^="#"]');
  const sections = $$('section[id]');

  if (navLinks.length && sections.length) {
    const setActive = id => {
      navLinks.forEach(a => {
        const href = a.getAttribute('href');
        a.classList.toggle('active', href === '#' + id);
      });
    };

    const sectionObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    }, {
      rootMargin: '-30% 0px -60% 0px',
      threshold: 0
    });

    sections.forEach(s => sectionObserver.observe(s));
  }

  /* ────────────────────────────────────────
     5. Smooth Scroll for Anchor Links
  ──────────────────────────────────────── */
  $$('a[href^="#"]').forEach(a => {
    on(a, 'click', e => {
      const id = a.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        const offset = (header ? header.offsetHeight : 80) +
                       (tickerTrack ? 38 : 0) + 8;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ────────────────────────────────────────
     6. Accordion
  ──────────────────────────────────────── */
  $$('.accordion-header').forEach(btn => {
    on(btn, 'click', () => {
      const body   = btn.nextElementSibling;
      const isOpen = btn.classList.contains('open');
      // Close siblings
      const acc = btn.closest('.accordion');
      if (acc) {
        $$('.accordion-header.open', acc).forEach(h => {
          h.classList.remove('open');
          h.nextElementSibling.classList.remove('open');
        });
      }
      if (!isOpen) {
        btn.classList.add('open');
        body.classList.add('open');
      }
    });
  });

  /* ────────────────────────────────────────
     7. Back to Top
  ──────────────────────────────────────── */
  const backToTop = $('#backToTop');
  if (backToTop) {
    on(window, 'scroll', () => {
      backToTop.classList.toggle('visible', window.scrollY > 300);
    }, { passive: true });
    on(backToTop, 'click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ────────────────────────────────────────
     8. Cookie Consent Banner
  ──────────────────────────────────────── */
  const cookieBanner = $('#cookieBanner');
  const cookieBtn    = $('#cookieAccept');
  if (cookieBanner) {
    if (!localStorage.getItem('cookieOk')) {
      cookieBanner.style.display = 'flex';
    }
    if (cookieBtn) {
      on(cookieBtn, 'click', () => {
        localStorage.setItem('cookieOk', '1');
        cookieBanner.style.display = 'none';
      });
    }
  }

  /* ────────────────────────────────────────
     9. Helpers for forms
  ──────────────────────────────────────── */
  function showError(id, msg) {
    const el = document.getElementById(id);
    if (el) { el.textContent = msg; el.style.display = 'block'; }
  }
  function clearErrors(form) {
    $$('.form-error', form).forEach(el => { el.textContent = ''; el.style.display = 'none'; });
  }
  function isValidEmail(v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }
  function isValidPhone(v) { return /^[6-9]\d{9}$/.test(v.replace(/[\s\-]/g, '')); }

  /* ────────────────────────────────────────
     10. Contact Form — Formspree
  ──────────────────────────────────────── */
  const FORMSPREE_CONTACT   = 'https://formspree.io/f/xnjlvavz';
  const FORMSPREE_GRIEVANCE = 'https://formspree.io/f/xaqajwjl';

  const contactForm = $('#contactForm');
  if (contactForm) {
    on(contactForm, 'submit', e => {
      e.preventDefault();
      clearErrors(contactForm);
      const data    = new FormData(contactForm);
      const name    = data.get('name')?.trim();
      const email   = data.get('email')?.trim();
      const phone   = data.get('phone')?.trim();
      const subject = data.get('subject')?.trim();
      const message = data.get('message')?.trim();
      let valid = true;

      if (!name || name.length < 2) { showError('c-nameErr', 'Please enter your full name.'); valid = false; }
      if (!email || !isValidEmail(email)) { showError('c-emailErr', 'Please enter a valid email address.'); valid = false; }
      if (phone && !isValidPhone(phone)) { showError('c-phoneErr', 'Please enter a valid 10-digit mobile number.'); valid = false; }
      if (!subject) { showError('c-subjErr', 'Please select a subject.'); valid = false; }
      if (!message || message.length < 10) { showError('c-msgErr', 'Please enter a message (at least 10 characters).'); valid = false; }

      if (!valid) return;

      const btn = contactForm.querySelector('button[type="submit"]');
      btn.disabled = true; btn.textContent = 'Sending…';

      fetch(FORMSPREE_CONTACT, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: data
      })
      .then(r => r.json())
      .then(json => {
        if (json.ok) {
          contactForm.style.display = 'none';
          const s = $('#contactSuccess');
          if (s) s.style.display = 'block';
        } else {
          const msg = json.errors ? json.errors.map(x => x.message).join('. ') :
            'Submission failed. Please email apnamanish9@gmail.com or call +91 9480322410.';
          showError('c-msgErr', msg);
          btn.disabled = false; btn.textContent = 'Send Message';
        }
      })
      .catch(() => {
        showError('c-msgErr', 'Network error. Please email apnamanish9@gmail.com or call +91 9480322410.');
        btn.disabled = false; btn.textContent = 'Send Message';
      });
    });
  }

  /* ────────────────────────────────────────
     11. Grievance Form — Formspree
  ──────────────────────────────────────── */
  const grievanceForm = $('#grievanceForm');
  if (grievanceForm) {
    on(grievanceForm, 'submit', e => {
      e.preventDefault();
      const btn    = grievanceForm.querySelector('button[type="submit"]');
      const refNum = 'GR' + Date.now().toString().slice(-8);
      const data   = new FormData(grievanceForm);
      data.append('_reference', refNum);

      btn.disabled = true; btn.textContent = 'Submitting…';

      fetch(FORMSPREE_GRIEVANCE, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: data
      })
      .then(r => r.json())
      .then(json => {
        if (json.ok) {
          grievanceForm.innerHTML = `
            <div style="background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);
              border-radius:12px;padding:1.5rem;text-align:center;">
              <p style="color:#86efac;font-weight:600;font-size:1rem;">✓ Complaint Registered</p>
              <p style="color:rgba(255,255,255,.7);margin-top:.5rem;font-size:.9rem;">
                Reference No: <strong style="color:#fbbf24;">${refNum}</strong><br>
                We will respond within <strong>10 business days</strong>.
                You will receive acknowledgement at your registered email.
              </p>
            </div>`;
        } else {
          const msg = json.errors ? json.errors.map(x => x.message).join('. ') :
            'Submission failed. Please email apnamanish9@gmail.com or call +91 9480322410.';
          grievanceForm.insertAdjacentHTML('afterbegin',
            `<div style="background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.3);
              border-radius:8px;padding:1rem;margin-bottom:1rem;font-size:.875rem;color:#fca5a5;">
              ⚠ ${msg}</div>`);
          btn.disabled = false; btn.textContent = 'Submit Complaint';
        }
      })
      .catch(() => {
        grievanceForm.insertAdjacentHTML('afterbegin',
          `<div style="background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.3);
            border-radius:8px;padding:1rem;margin-bottom:1rem;font-size:.875rem;color:#fca5a5;">
            ⚠ Network error. Please email apnamanish9@gmail.com or call +91 9480322410.</div>`);
        btn.disabled = false; btn.textContent = 'Submit Complaint';
      });
    });
  }

})();
