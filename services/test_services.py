from cores.parser import parse_swagger
from cores.generator import generate_cases
from cores.runner import run_cases

def run_flow(swagger):
    apis = parse_swagger(swagger)
    cases = generate_cases(apis)
    result = run_cases(cases)

    return {
        "apis": apis,
        "cases": cases,
        "result": result
    }