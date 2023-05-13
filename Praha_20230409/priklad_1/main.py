from clovek import Clovek

#vytvoření instance s kulatými závorkami
karel = Clovek("Karel",43)
karel.pozdrav("Bububu")

irena = Clovek("Irena", 22)
irena.pozdrav("Ahojky zlato","Jak ti jde programování?")

pepa = Clovek("Pepan", 10)
pepa.pozdrav(" ","Nemáš cígo, vole?")
pepa.get_jmeno()
pepa.set_vek(5)