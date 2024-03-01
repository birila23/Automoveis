class Concessionaria():

  def __init__(self, nome):
    self.nome = nome
    self.veiculos = []

  def adiciona_veiculo(self, veiculo):
    self._veiculos.append(veiculo)

  def listar_veiculos(self):
    for veiculo in self.veiculos:
      veiculo.dados_veiculo()


  #get
  @property
  def nome(self):
    return self._nome
  

  #get
  @property
  def veiculos(self):
    return self._veiculos


  #set
  @nome.setter
  def nome(self, nome):
    self._nome = nome


  #set
  @veiculos.setter
  def veiculos(self, veiculos):
    self._veiculos = veiculos