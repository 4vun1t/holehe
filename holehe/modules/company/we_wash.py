from holehe.core import *
from holehe.localuseragent import *

async def we_wash(email, client, out):
    name = "we-wash"
    domain = "we-wash.com"
    method = "register"
    frequent_rate_limit = False

    # Standard headers based on your curl request
    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://app.we-wash.com/',
        'Origin': 'https://app.we-wash.com',
        'Content-Type': 'application/json',
        'WW-App-Version': '2.76.0',
        'WW-Client': 'USERAPP',
        'Connection': 'keep-alive',
    }

    # Data payload required by the registration endpoint
    data = {
        "firstName": " ",
        "lastName": " ",
        "email": email,
        "marketingCommunicationAccepted": False,
        "password": "Ch4ng3m3!!!",
        "lang": "en",
        "confirmedPrivacyPolicyId": 48,
        "confirmedTermsAndConditionsId": 53,
        "analyticsAccepted": False,
        "countryCode": "DE"
    }

    try:
        response = await client.post(
            'https://backend.we-wash.com/v3/accounts', 
            headers=headers, 
            json=data
        )
    except Exception:
        out.append({
            "name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None
        })
        return None

    # Logic: 400 means account exists, 200/201 means it's available
    if response.status_code == 400:
        out.append({
            "name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None
        })
    elif response.status_code in [200, 201]:
        out.append({
            "name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None
        })
    else:
        # Likely a rate limit or a change in API behavior
        out.append({
            "name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None
        })