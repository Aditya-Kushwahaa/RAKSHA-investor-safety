import re
from urllib.parse import urlparse

RULES = [
    ("Guaranteed returns", [r"guaranteed\s+(?:return|profit|income)", r"fixed\s+(?:return|profit)", r"100%\s*(?:profit|return)", r"no\s+risk"]),
    ("Urgency / pressure", [r"act\s+now", r"limited\s+(?:slot|slots|time)", r"last\s+chance", r"today\s+only", r"immediately", r"urgent"]),
    ("Payment before verification", [r"pay\s+(?:now|today)", r"activation\s+fee", r"registration\s+fee", r"send\s+(?:₹|rs\.?|inr)", r"deposit\s+(?:₹|rs\.?|inr)"]),
    ("Messaging-platform redirection", [r"telegram", r"whatsapp", r"join\s+(?:our|the)\s+group"]),
    ("Regulatory impersonation / claim", [r"sebi\s+(?:approved|registered|authorized)", r"rbi\s+(?:approved|registered|authorized)", r"government\s+approved"]),
    ("Credential / remote-access request", [r"otp", r"password", r"remote\s+access", r"anydesk", r"teamviewer", r"screen\s+share"]),
]

URL_RED_FLAGS = [
    ("Suspicious URL structure", [r"@", r"\d{1,3}(?:\.\d{1,3}){3}", r"xn--"]),
]

def _find_matches(text, patterns):
    return any(re.search(p, text, flags=re.I) for p in patterns)

def analyze_content(content: str, language: str = "English") -> dict:
    text = content.strip()
    flags = []
    lower = text.lower()

    for name, patterns in RULES:
        if _find_matches(text, patterns):
            flags.append(name)

    parsed = urlparse(text if re.match(r"^https?://", text, re.I) else "")
    if parsed.netloc:
        for name, patterns in URL_RED_FLAGS:
            if _find_matches(text, patterns):
                flags.append(name)

    score = min(95, 20 + len(flags) * 13)
    if not flags:
        score = 10

    if score >= 70:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    if language == "Hindi":
        explanation = {
            "High": "इस सामग्री में कई चेतावनी संकेत मिले हैं। पैसे भेजने या निजी जानकारी देने से पहले स्वतंत्र रूप से सत्यापन करें।",
            "Medium": "कुछ चेतावनी संकेत मिले हैं। आगे बढ़ने से पहले दावे और संस्था की आधिकारिक स्रोतों से जांच करें।",
            "Low": "इस शुरुआती जांच में कम चेतावनी संकेत मिले हैं, लेकिन यह सामग्री अपने-आप में वैध होने का प्रमाण नहीं है।"
        }[level]
    else:
        explanation = {
            "High": "Multiple warning signs were detected. Do not transfer money or share sensitive information until the claims and entity are independently verified.",
            "Medium": "Some warning signs were detected. Verify the claims and entity through trusted official sources before proceeding.",
            "Low": "Few warning signs were detected in this initial check. This does not prove that the content is legitimate; verify important claims independently."
        }[level]

    return {
        "risk_level": level,
        "risk_score": score,
        "flags": flags,
        "explanation": explanation,
        "next_steps": [
            "Pause before transferring money.",
            "Verify the person/entity using an official source you navigate to yourself.",
            "Do not share OTPs, passwords, or remote-access control.",
            "Preserve screenshots, messages, URLs, and transaction evidence if something has already happened."
        ]
    }
