class Veiculos():
  def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor_veiculo):
    self.cor = cor
    self.tipo = tipo
    self.ano_fabricacao = ano_fabricacao
    self.modelo = modelo
    self.placa = placa
    self.valor_veiculo = valor_veiculo
    self.valor_ipva = self.calcula_ipva()

#calculo_ipva
  def calcula_ipva(self):
    if 2021 - self.ano_fabricacao > 15:
      return 0.0
    if self.tipo == "Utilitário":
      return (self.valor_veiculo * 1) / 100
    if self.tipo == "Automóvel":
      return (self.valor_veiculo * 2) / 100
    

#get
  @property
  def cor(self):
    return self._cor

#get
  @property
  def tipo(self):
    return self._tipo

#get
  @property
  def ano_fabricacao(self):
    return self._ano_fabricacao

#get
  @property
  def modelo(self):
    return self._modelo

#get
  @property
  def placa(self):
    return self._placa

#get
  @property
  def valor_veiculo(self):
    return self._valor_veiculo

#get
  @property
  def valor_ipva(self):
    return self._valor_ipva

#set
  @valor_veiculo.setter
  def valor_veiculo(self, valor_veiculo):
    self._valor_veiculo = valor_veiculo

#set
  @valor_ipva.setter
  def valor_ipva(self, valor_ipva):
    self._valor_ipva = valor_ipva

#set
  @cor.setter
  def cor(self, cor):
    self._cor = cor

#set
  @tipo.setter
  def tipo(self, tipo):
    self._tipo = tipo
#set
  @ano_fabricacao.setter
  def ano_fabricacao(self, ano):
    self._ano_fabricacao = ano

#set
  @modelo.setter
  def modelo(self, modelo):
    self._modelo = modelo

  #set
  @placa.setter
  def placa(self, placa):
    self._placa = placa

  def dados_veiculo(self):
    print(f"cor: {self.cor}", end = "\n")
    print(f"tipo: {self.tipo}", end = "\n")
    print(f"ano_fabricacao: {self.ano_fabricacao}", end = "\n")
    print(f"modelo: {self.modelo}", end = "\n")
    print(f"placa: {self.placa}", end = "\n")
    print(f"valor_veiculo: {self.valor_veiculo}", end = "\n")
    print(f"valor_ipva: {self.valor_ipva}", end = "\n\n\n")