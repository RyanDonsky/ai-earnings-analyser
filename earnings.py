import anthropic

client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")

print("=== AI Earnings Analyser ===")
print("Paste your earnings call transcript below.")
print("When done, type END on a new line and press Enter.")
print("")

lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

transcript = "\n".join(lines)

print("\nAnalysing transcript...")

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": f"""You are a senior equity research analyst. Analyse this earnings call transcript and provide a structured summary covering:

1. KEY FINANCIALS — revenue, margins, any key metrics mentioned
2. POSITIVES — what went well, beats, strong segments
3. RISKS & HEADWINDS — concerns, misses, challenges flagged
4. GUIDANCE — what management said about the future
5. ANALYST TAKE — one paragraph overall assessment

Transcript:
{transcript}"""
        }
    ]
)

print("\n" + response.content[0].text)