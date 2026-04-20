You are working on a website UI.

Task: Make the header (navigation bar with Home, About, Services, Training, Disclaimer, Grievance, Contact) scroll normally instead of staying fixed.

Context:
- Currently, the header is "sticky" or "fixed" and remains visible at the top while scrolling.
- This takes up unnecessary screen space and affects the viewing experience.
- We want the header to scroll away with the page content.

Requirements:
1. Remove any CSS that fixes the header in place:
   - position: fixed
   - position: sticky
   - top: 0 (if used with sticky/fixed)
2. Ensure the header behaves like a normal block element in the document flow.
3. Remove or adjust any extra padding/margin added to compensate for fixed header spacing.
4. Maintain the current visual design (colors, layout, alignment).
5. Ensure no layout shift or overlap issues occur after the change.

Files to check:
- Header component (HTML/JSX)
- Global CSS / Tailwind classes / layout styles

Output:
- Show exactly what was removed and what was updated.
- Provide final corrected HTML/CSS (or JSX/Tailwind) snippet.