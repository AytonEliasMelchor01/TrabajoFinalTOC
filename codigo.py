import random
 
# Clase para representar a un agente económico
class AgenteEconomico:
    def __init__(self, estrategia, saldo_inicial=200):
        self.estrategia = estrategia  # Estrategia del agente (cooperar o no cooperar)
        self.saldo = saldo_inicial  # Saldo inicial del agente
 
    def tomar_decision(self):
        return self.estrategia
 
    def actualizar_saldo(self, recompensa):
        self.saldo += recompensa
 
# Función para simular un juego entre agentes económicos
def jugar_juego(agentes):
    for i in range(len(agentes)):
        for j in range(i + 1, len(agentes)):
            agente1 = agentes[i]
            agente2 = agentes[j]
            decision1 = agente1.tomar_decision()
            decision2 = agente2.tomar_decision()
 
            recompensa1, recompensa2 = calcular_recompensas(decision1, decision2)
            agente1.actualizar_saldo(recompensa1)
            agente2.actualizar_saldo(recompensa2)
 
# Función para calcular las recompensas en función de las decisiones de dos agentes
def calcular_recompensas(decision1, decision2):
    if decision1 and decision2:
        return (4, 4)
    elif decision1 and not decision2:
        return (0, 6)
    elif not decision1 and decision2:
        return (6, 0)
    else:
        return (2, 2)
 
# Función para mostrar los saldos de los agentes
def mostrar_saldos(agentes):
    for i, agente in enumerate(agentes):
        print(f"Agente {i + 1}: Saldo = ${agente.saldo}")
 
# Función principal para ejecutar la simulación
def simulacion(numero_agentes, numero_iteraciones):
    agentes = [AgenteEconomico(random.choice([True, False])) for _ in range(numero_agentes)]
 
    for _ in range(numero_iteraciones):
        jugar_juego(agentes)
 
    mostrar_saldos(agentes)
 
# Ejecutar la simulación con diferentes valores
if __name__ == "__main__":
    numero_agentes = 8  # Cambia el número de agentes a 8
    numero_iteraciones = 15  # Cambia el número de iteraciones a 15
    simulacion(numero_agentes, numero_iteraciones)