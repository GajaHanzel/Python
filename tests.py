from racunanje import kalkulator

def testiranje_funkcije_kalkulator():
    assert kalkulator(3, 4, "*") == 12
    return "testiranje_funkcije_kalkulator() passed successfully"

print testiranje_funkcije_kalkulator()