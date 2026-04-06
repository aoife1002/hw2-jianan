# Report — Supply Chain Delay Notification Email Generator

## Business Use Case

Supply chain coordinators frequently need to notify customers about shipment
delays. This prototype automates first-draft email generation, reducing time
per email from approximately 5 minutes to under 30 seconds, while maintaining
a consistent and professional tone across all communications.

## Model Choice

I used Gemini 1.5 Flash via Google AI Studio (free tier). It was chosen for
its accessibility, fast response time, and adequate quality for structured
business writing tasks.

## Baseline vs. Final Prompt Comparison

| Aspect | Version 1 (Baseline) | Version 3 (Final) |
|--------|---------------------|-------------------|
| Structure | Unspecified | Explicit 4-part structure |
| Missing info handling | Not handled | 24-hour follow-up response |
| Long delays | No guidance | Suggests account manager call |
| Hallucination risk | High | Low (explicit rules added) |
| Word limit | 150 words | 180 words |

## Where the Prototype Still Fails

- **Case 4 (missing info):** Even with Version 3, the output can feel
  awkward. A real system should validate inputs before calling the API.
- **Tone calibration:** The model defaults to a formal tone, which may
  not suit all client relationships.
- **No factual grounding:** The model cannot verify real ETAs or order
  numbers — human review is essential before any email is sent.

## Deployment Recommendation

This prototype is suitable for assisted drafting only, not autonomous
sending. A coordinator should review every output before it is sent,
especially for delays over 14 days or cases involving regulatory holds.
I would not recommend fully automated deployment without a human-in-the-loop
review step.