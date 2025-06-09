from app.falloParaBandit import run_this_dangerous_code

def test_fallo_para_bandit():
    result = run_this_dangerous_code()
    assert result == "Este código tiene fallas de seguridad"
