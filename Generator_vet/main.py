from generator_vet import Generator_vet

generator = Generator_vet()
# pocet vet


for _ in range(10):
    veta = generator.generuj_vetu()
    print(veta, end="\n")