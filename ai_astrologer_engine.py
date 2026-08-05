from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_ai_astrologer(
    birth_chart: dict,
    user_question: str,
    palm_report: dict | None = None
):
    prompt = f"""
You are a world-class Vedic Astrologer.

Birth Chart:
{birth_chart}

Palm Report:
{palm_report}

User Question:
{user_question}

Instructions:
- Answer only using Vedic Astrology.
- Use the birth chart as the primary source.
- Use palm reading only if available.
- Be practical, detailed and accurate.
- Include reasoning.
- Give remedies if required.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
