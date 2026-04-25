
def parse_swagger(swagger):
    result = []

    for url, methods in swagger["paths"].items():
        for method, detail in methods.items():
            params = [p["name"] for p in detail.get("parameters", [])]

            result.append({
                "url": url,
                "method": method.upper(),
                "params": params
            })

    return result