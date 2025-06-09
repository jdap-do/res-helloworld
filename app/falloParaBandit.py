def uso_eval(dato):
    # Esto genera una alerta de seguridad (B307) en Bandit
    return eval(dato)

def run_this_dangerous_code():
    return "Este código tiene fallas de seguridad"