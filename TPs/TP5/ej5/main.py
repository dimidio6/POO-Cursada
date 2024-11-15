from Director import Director
from ConcreteBuilderChocolate import ConcreteBuilderChocolate
from ConcreteBuilderCoco import ConcreteBuilderCoco
from ConcreteBuilderVainilla import ConcreteBuilderVainilla

director1 = Director()  # creo un Director
constructor_chocolate = ConcreteBuilderChocolate()  # creo un Constructor
director1.builder = constructor_chocolate  # le asigno al director el Constructor

director1.build_torta()  # Construyo la torta según el constructor que le pase (en este caso Chocolate)
print(director1.builder.torta)  # Imprimo la torta

constructor_coco = ConcreteBuilderCoco()
director1.builder = constructor_coco
director1.build_torta()
print(director1.builder.torta)

constructor_vainilla = ConcreteBuilderVainilla()
director1.builder = constructor_vainilla
director1.build_torta()
print(director1.builder.torta)
