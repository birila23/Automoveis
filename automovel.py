from veiculos import Veiculos as V

class Automovel(V):
  def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor_veiculo, valor_ipva,capacidade_passageiros, numero_portas):
    super().__init__(cor, tipo, ano_fabricacao, modelo, placa, valor_veiculo, valor_ipva)
    self.capacidade_passageiros = capacidade_passageiros
    self.numero_portas = numero_portas

#get
  @property
  def capacidade_passageiros(self):
    return self.capacidade_passageiros

#get
  @property
  def numero_portas(self):
    return self.numero_portas

#set
  @capacidade_passageiros.setter
  def capacidade_passageiros(self, capacidade_passageiros):
    return self.capacidade_passageiros

#set
  @numero_portas.setter
  def numero_portas(self, numero_portas):
    return self.numero_portas