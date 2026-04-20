In index.html find the Disclaimer section (id="disclaimer").

There is a box/div with a light yellow or white background 
(background color like #fffef0 or #fefce8 or similar light color).

Inside this box the text is white or very light colored making 
it invisible against the light background.

Fix this by:

1. Find the div/box in the disclaimer section that has a 
   light/white/yellow background

2. Change ALL text inside that box to dark color: #1a1a2e
   This includes:
   - Any <p> tags inside the box
   - Any <span> tags inside the box  
   - Any <h3> or <h4> tags inside the box
   - Any <li> tags inside the box
   - Any <strong> or <b> tags inside the box

3. In assets/css/style.css find any CSS rule that sets 
   text color to white (#ffffff or white) inside the 
   disclaimer section's light colored box and change it to:
   color: #1a1a2e !important;

4. Also check if the box has a class name and add this CSS:
   .disclaimer-highlight-box,
   .disclaimer-note,
   .important-note,
   .disclaimer-box {
     color: #1a1a2e !important;
   }
   
   .disclaimer-highlight-box *,
   .disclaimer-note *,
   .important-note *,
   .disclaimer-box * {
     color: #1a1a2e !important;
   }

After fixing confirm the text inside the light colored 
box is now dark and readable.