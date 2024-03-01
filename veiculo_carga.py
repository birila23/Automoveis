from veiculos import Veiculos as V

class Veiculo_carga(V):
  def __init__(self, eixos, capacidade_carga, cor, tipo, ano_fabricacao, modelo, placa, valor_veiculo):
    super().__init__(cor, tipo, ano_fabricacao, modelo, placa, valor_veiculo)
    self.eixos = eixos
    self.capacidade_carga = capacidade_carga

  def dados_veiculo(self):
    print(f"cor: {self.cor}", end = "\n")
    print(f"eixos: {self.eixos}", end = "\n")
    print(f"capacidade de carga: {self.capacidade_carga}", end = "\n")
    print(f"tipo: {self.tipo}", end = "\n")
    print(f"ano_fabricacao: {self.ano_fabricacao}", end = "\n")
    print(f"modelo: {self.modelo}", end = "\n")
    print(f"placa: {self.placa}", end = "\n")
    print(f"valor_veiculo: {self.valor_veiculo}", end = "\n")
    print(f"valor_ipva: {self.valor_ipva}", end = "\n\n\n")

#get
  @property
  def eixos(self):
    return self._eixos

#get
  @property
  def capacidade_carga(self):
    return self._capacidade_carga

#set
  @eixos.setter
  def eixos(self, eixos):
    self._eixos = eixos

#set
  @capacidade_carga.setter
  def capacidade_carga(self, capacidade_carga):
    self._capacidade_carga = capacidade_carga