import requests

def run_cases(cases):
    results = []

    for c in cases:
        try:
            if c["method"] == "POST":
                r = requests.post("http://127.0.0.1:5000" + c["url"], json=c["data"])
            else:
                r = requests.get("http://127.0.0.1:5000" + c["url"], params=c["data"])

            results.append({
                "name": c["name"],
                "pass": r.status_code == c["expect"]
            })

        except Exception as e:
            results.append({
                "name": c["name"],
                "pass": False,
                "error": str(e)
            })

    return results