The website arthashastrainsights.com has a hero section with a rotating 
background image carousel (4 slides, indicated by 4 dots at the bottom of 
the hero). Currently, NONE of the background images are displaying — only 
the dark navy fallback background and the grid overlay are visible. The 
text "Data-Driven Research. Disciplined Investing." renders correctly, 
and the carousel dots render, so the HTML/CSS structure is partially 
working but the images themselves aren't loading.

Please investigate and fix. Specifically:

1. INSPECT THE PROJECT
   - Find the hero section component/HTML in the project files
   - Identify how the 4 background images are being loaded (CSS background-image, 
     <img> tags, JS-driven, or a library like Swiper/Slick?)
   - Check the image file paths/URLs being referenced

2. DIAGNOSE WHY IMAGES AREN'T SHOWING
   Check all of these:
   - Are the image files actually present in the project's assets/images folder?
   - Are the file paths correct (case sensitivity matters — Image1.jpg ≠ image1.jpg)?
   - Are the file extensions correct (.jpg vs .jpeg vs .png vs .webp)?
   - Open browser DevTools → Network tab → reload — are the images returning 
     200 OK, 404 Not Found, or 403 Forbidden?
   - Open DevTools → Console tab — any JS errors related to the carousel/slider?
   - If images are loaded via CSS, is the `background-image: url(...)` path 
     resolving correctly from the CSS file's location?
   - If the carousel uses opacity/z-index transitions, is the first slide 
     stuck at opacity:0?
   - Are images very large and timing out? Check file sizes.
   - Is there a CORS or mixed-content (http vs https) issue?

3. FIX THE ROOT CAUSE — don't just hide symptoms
   Once you find the actual cause, fix it properly. Common fixes:
   - Correct broken paths
   - Re-upload missing images
   - Fix the carousel JS init code
   - Add proper fallback / preloading
   - Convert to optimized formats (WebP) if size is the issue

4. ENSURE IT WORKS ON BOTH DESKTOP AND MOBILE
   - Test responsive behavior
   - Check that background-size: cover is set correctly
   - Verify mobile media queries aren't accidentally hiding images
   - Make sure image dimensions/aspect ratios work on narrow viewports
   - Confirm the carousel autoplay/swipe works on touch devices

5. REPORT BACK
   Tell me:
   - What was the root cause
   - What you changed (file names + line numbers)
   - How to test it locally before I redeploy

Don't deploy automatically — show me the diff first.