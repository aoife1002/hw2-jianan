from google import genai
import time

# ── Configuration ──────────────────────────────────────
API_KEY = "AIzaSyBGWGSxIGRpIBAwac4lsHntzRlu8MKFqEc"
client = genai.Client(api_key=API_KEY)

# ── System Prompt ──────────────────────────────────────
SYSTEM_PROMPT = """You are a professional supply chain coordinator writing
on behalf of your company's logistics team.

Write a delay notification email with this structure:
1. Opening: brief, sincere apology
2. Details: what is delayed, the reason, and revised timeline
3. Next steps: clear action item or contact information
4. Closing: professional sign-off

Rules:
- Do NOT promise compensation, refunds, or legal commitments
- If any input is Unknown, Unclear, or 0, write exactly:
  We are still gathering details and will follow up within 24 hours.
- For delays over 30 days, suggest scheduling a call with an account manager
- Maximum 180 words
- Tone: direct, empathetic, professional"""

# ── Test Cases ─────────────────────────────────────────
TEST_CASES = [
    {
        "id": 1,
        "customer": "Walmart",
        "product": "Electronic components (SKU-2041)",
        "reason": "Port congestion in Shanghai",
        "delay_days": 7,
    },
    {
        "id": 2,
        "customer": "Target",
        "product": "Seasonal clothing inventory",
        "reason": "Severe weather disrupting trucking routes",
        "delay_days": 3,
    },
    {
        "id": 3,
        "customer": "Amazon",
        "product": "Lithium batteries (hazmat)",
        "reason": "Customs inspection and regulatory hold",
        "delay_days": 30,
    },
    {
        "id": 4,
        "customer": "Unknown / TBD",
        "product": "Mixed freight",
        "reason": "Unclear",
        "delay_days": 0,
    },
    {
        "id": 5,
        "customer": "GlobalTech Inc.",
        "product": "Custom semiconductor chips (order #GT-9982)",
        "reason": "Supplier factory fire in Chengdu",
        "delay_days": 45,
    },
]

# ── Generate Email ─────────────────────────────────────
def generate_email(case):
    user_prompt = f"""
Customer: {case['customer']}
Product: {case['product']}
Delay reason: {case['reason']}
Delay days: {case['delay_days']}

Write the delay notification email now.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=SYSTEM_PROMPT + "\n\n" + user_prompt,
    )
    return response.text

# ── Run All Cases ──────────────────────────────────────
def run_all_cases():
    output_lines = []

    for case in TEST_CASES:
        print(f"\n{'='*60}")
        print(f"Case {case['id']} — Customer: {case['customer']}")
        print('='*60)
        result = generate_email(case)
        print(result)
        output_lines.append(
            f"## Case {case['id']} — {case['customer']}\n\n{result}\n\n---\n"
        )
        print("⏳ Waiting 15 seconds...")
        time.sleep(15)

    with open("outputs.md", "w") as f:
        f.write("# LLM Outputs\n\n")
        f.writelines(output_lines)

    print("\n✅ All results saved to outputs.md")

if __name__ == "__main__":
    run_all_cases()