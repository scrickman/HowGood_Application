import hashlib, hmac, json, requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Steven Crickman",
    "email": "spcrickman@gmail.com",
    "resume": "",       # URL to your resume
    "location": "Marriottsville, MD",     # e.g. "New York, NY"
    "linkedin": "https://www.linkedin.com/in/stevencrickman/",
    "codeLink": "",     # URL to the repo/gist containing THIS script
    "yearsPython": 4.75,
    "yearsDjango": 4.25,
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

resp = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature,
    },
)
print(resp.status_code, resp.json())