# INSTRUCTIONS — GRIEVANCE REDRESSAL TABLES UPDATE
# Save as INSTRUCTIONS_GRIEVANCE_TABLES.md in:
# D:\Claude code folder\arthashastrainsights\
# Tell Claude Code: "Read INSTRUCTIONS_GRIEVANCE_TABLES.md and execute all instructions"

---

## TASK 1 — UPDATE GRIEVANCE REDRESSAL PROCESS TEXT

In index.html find the Grievance Redressal section (id="grievance").

Replace the existing grievance process steps with this updated content:

---

### Grievance Redressal Process

**Step 1 — Contact Us Directly**
Reach out to Manish Mishra (SEBI RA, INH000024620) with your concern.
We are committed to resolving all grievances within 7 working days.
Email: apnamanish9@gmail.com
Phone: +91 9480322410

**Step 2 — Email Escalation**
If your concern is not resolved at Step 1, send a detailed email to
apnamanish9@gmail.com clearly describing the nature of your complaint.
We will investigate and provide a full written response within
7 working days of receipt.

**Step 3 — SEBI SCORES Portal**
If your complaint remains unresolved within 30 days, you may escalate
to SEBI through their centralized grievance redressal system SCORES.
Portal: https://scores.sebi.gov.in
Registration: https://scores.gov.in/scores/complaintRegister.html
SEBI Toll Free: 1800 266 7575

**Step 4 — ODR Portal**
If your complaint is not resolved on SCORES, you may initiate dispute
resolution through the Online Dispute Resolution portal.
Portal: https://smartodr.in/login

---

## TASK 2 — DELETE COMPLAINT STATUS SUMMARY

In index.html find and DELETE the existing complaint status summary
section in the grievance area. This may be a table or div showing:
- Sr No, Month-Year, Received, Resolved, Pending columns
- OR any simple complaints data table currently on the page

Remove it completely including its heading.

---

## TASK 3 — ADD THREE NEW SEBI MANDATED TABLES

After the grievance process steps, add these three tables in order.
Style all tables consistently:
- Full width (width: 100%)
- Border: 1px solid #e2e8f0
- Header background: #1a2456 (dark navy)
- Header text: white, font-size 13px, padding 10px
- Body text: #333, font-size 13px, padding 10px
- Alternating row background: white and #f8fafc
- Responsive: on mobile scroll horizontally (overflow-x: auto)
- Add section heading above each table in gold (#f5a623)

---

### TABLE 1 — Complaint Data to be Displayed by RAs

Add this heading above table:
"Complaint Data to be Displayed by RAs"
Subheading: "Formats for investors complaints data to be disclosed 
monthly by RAs on their website/mobile application:"

Then add sub-heading: "Data for the Month Ending — APRIL 2025"

Table structure:

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr>
      <th>RECEIVED FROM</th>
      <th>PENDING AT THE END OF LAST MONTH</th>
      <th>RECEIVED</th>
      <th>RESOLVED*</th>
      <th>TOTAL PENDING#</th>
      <th>PENDING COMPLAINTS > 3 MONTHS</th>
      <th>AVERAGE RESOLUTION TIME^ (IN DAYS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Directly from Investors</td>
      <td>0</td><td>0</td><td>0</td>
      <td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>SEBI (SCORES)</td>
      <td>0</td><td>0</td><td>0</td>
      <td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>Other Sources (if any)</td>
      <td>0</td><td>0</td><td>0</td>
      <td>0</td><td>0</td><td>0</td>
    </tr>
    <tr style="font-weight:bold;">
      <td>Grand Total</td>
      <td>0</td><td>0</td><td>0</td>
      <td>0</td><td>0</td><td>0</td>
    </tr>
  </tbody>
</table>
</div>

Add this footnote below table:
"^ Average Resolution time is the sum total of time taken to resolve 
each complaint in days, in the current month divided by total number 
of complaints resolved in the current month."
"* Inclusive of complaints of previous months resolved in the 
current month."
"# Inclusive of complaints pending as on the last day of the month."

---

### TABLE 2 — Trend of Monthly Disposal of Complaints

Add this heading: "Trend of Monthly Disposal of Complaints"

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr>
      <th>MONTH</th>
      <th>CARRIED FORWARD FROM PREVIOUS MONTH</th>
      <th>RECEIVED</th>
      <th>RESOLVED</th>
      <th>PENDING</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>November 2024</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>December 2024</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>January 2025</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>February 2025</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>March 2025</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    <tr>
      <td>April 2025</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    <tr style="font-weight:bold;">
      <td>Grand Total</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
  </tbody>
</table>
</div>

Add this footnote below table:
"* Inclusive of complaints of previous months resolved in the 
current month."
"# Inclusive of complaints pending as on the last day of the month."

---

### TABLE 3 — Trend of Annual Disposal of Complaints

Add this heading: "Trend of Annual Disposal of Complaints"

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr>
      <th>YEAR</th>
      <th>CARRIED FORWARD FROM PREVIOUS YEAR</th>
      <th>RECEIVED</th>
      <th>RESOLVED*</th>
      <th>PENDING#</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2024-25</td>
      <td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
  </tbody>
</table>
</div>

Add this footnote below table:
"* Inclusive of complaints of previous years resolved in the 
current year."
"# Inclusive of complaints pending as on the last day of the year."

---

### TABLE 4 — Escalation Matrix

Add this heading: "Escalation Matrix"

<div style="overflow-x:auto;">
<table>
  <thead>
    <tr>
      <th>Designation</th>
      <th>Contact Person</th>
      <th>Address</th>
      <th>Contact No.</th>
      <th>Email-ID</th>
      <th>Working Hours</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Principal Officer / SEBI RA</td>
      <td>Mr. Manish Mishra</td>
      <td>GF-06, Winds Of Change, Judicial Layout, 
      Thalaghattapura, Bangalore - 560062, Karnataka</td>
      <td>+91 9480322410</td>
      <td>apnamanish9@gmail.com</td>
      <td>Mon-Fri: 9:00 AM to 6:00 PM IST
      Sat: 9:00 AM to 1:00 PM IST</td>
    </tr>
  </tbody>
</table>
</div>

---

## TASK 4 — ADD CSS FOR TABLES

In assets/css/style.css add these table styles:

.grievance-tables {
  margin-top: 40px;
}

.grievance-table-section {
  margin-bottom: 40px;
}

.grievance-table-section h3 {
  color: #f5a623;
  font-size: 1.2rem;
  margin-bottom: 8px;
  font-weight: 600;
}

.grievance-table-section h4 {
  color: #ffffff;
  font-size: 1rem;
  margin-bottom: 12px;
  opacity: 0.9;
}

.grievance-table-section .table-wrap {
  overflow-x: auto;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.1);
}

.grievance-table-section table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  min-width: 600px;
}

.grievance-table-section thead tr {
  background: #0a0f2e;
}

.grievance-table-section thead th {
  color: #f5a623;
  padding: 12px 10px;
  text-align: center;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 0.5px;
  border: 1px solid rgba(255,255,255,0.1);
}

.grievance-table-section tbody tr:nth-child(even) {
  background: rgba(255,255,255,0.03);
}

.grievance-table-section tbody tr:nth-child(odd) {
  background: rgba(255,255,255,0.07);
}

.grievance-table-section tbody td {
  color: #e2e8f0;
  padding: 10px;
  text-align: center;
  border: 1px solid rgba(255,255,255,0.08);
  font-size: 13px;
}

.grievance-table-section tbody tr:last-child td {
  font-weight: 700;
  color: #ffffff;
  background: rgba(245,166,35,0.1);
}

.grievance-table-section .table-footnote {
  font-size: 11px;
  color: rgba(255,255,255,0.6);
  margin-top: 8px;
  line-height: 1.6;
  font-style: italic;
}

---

## FINAL VERIFICATION

After all changes confirm:
1. Old complaint status summary table is deleted
2. Grievance process shows 4 steps with correct contact details
3. Table 1 — Monthly complaint data with 7 columns present
4. Table 2 — Monthly disposal trend with 6 months present
5. Table 3 — Annual disposal with 2024-25 row present
6. Table 4 — Escalation matrix with Manish Mishra details present
7. All tables styled consistently with dark navy/gold theme
8. All tables mobile responsive (horizontal scroll on small screens)
9. No references to Anil Rai anywhere in grievance section
10. All contact details show apnamanish9@gmail.com and +91 9480322410

Report all changes made.
