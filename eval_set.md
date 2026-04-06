# Evaluation Set — Supply Chain Delay Notification Emails

## Case 1 (Normal case)

**Input:**
- Customer: Walmart
- Product: Electronic components (SKU-2041)
- Delay reason: Port congestion in Shanghai
- Delay days: 7

**Expected output should:** Be professional and apologetic, state the delay
clearly, give a revised ETA, and offer a contact for questions.

---

## Case 2 (Normal case)

**Input:**
- Customer: Target
- Product: Seasonal clothing inventory
- Delay reason: Severe weather disrupting trucking routes
- Delay days: 3

**Expected output should:** Acknowledge the delay briefly, mention it is
weather-related and beyond the company's control, and provide a new timeline.

---

## Case 3 (Edge case — very long delay)

**Input:**
- Customer: Amazon
- Product: Lithium batteries (hazmat)
- Delay reason: Customs inspection and regulatory hold
- Delay days: 30

**Expected output should:** Handle the regulatory topic carefully, avoid
promising a specific date if uncertain, and suggest escalation to an
account manager.

---

## Case 4 (Edge case — missing information)

**Input:**
- Customer: Unknown / TBD
- Product: Mixed freight
- Delay reason: Unclear
- Delay days: 0

**Expected output should:** Not invent details. Should either ask for
clarification or state that an update will be provided within 24 hours.

---

## Case 5 (Likely to fail — hallucination risk)

**Input:**
- Customer: GlobalTech Inc.
- Product: Custom semiconductor chips (order #GT-9982)
- Delay reason: Supplier factory fire in Chengdu
- Delay days: 45

**Expected output should:** Be empathetic but must NOT invent compensation
promises, fake tracking numbers, or legal commitments not in the input.

## END
