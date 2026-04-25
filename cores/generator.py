def generate_cases(apis):
    cases = []

    for api in apis:
        cases.append({
            "name": "正常请求",
            "url": api["url"],
            "method": api["method"],
            "data": {p: "test" for p in api["params"]},
            "expect": 200
        })

        cases.append({
            "name": "缺参",
            "url": api["url"],
            "method": api["method"],
            "data": {},
            "expect": 400
        })

    return cases