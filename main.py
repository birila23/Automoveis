from veiculos import Veiculos as v
from veiculo_carga import Veiculo_carga as vc
from concessionaria import Concessionaria as c

print("---*Informacões*---\n")

veiculo = v("vermelho", "Automovel", 2001, "Corsinha", "1111xxx", 1000)

veiculo2 = v("Azul", "Automovel", 2004, "Corsinha", "1231xxx", 10000)

veiculo3 = v("Verde", "Utilitario", 2017, "Corsinha", "4211xxx", 1500)

veiculoCarga = vc(4, 1000, "Prata", "Utilitario", 2012, "Volvo", "42asdxx", 15000)

mario = c("Mario")


mario.adiciona_veiculo(veiculo)
mario.adiciona_veiculo(veiculo2)
mario.adiciona_veiculo(veiculo3)
mario.adiciona_veiculo(veiculoCarga)

mario.listar_veiculos()


print("\n------------------------------------")