class MetamorphosisMeta(type):
    # Intercept class creation and alter attribute names dynamically
    def __new__(cls, name, bases, dct):
        transformed_dct = {}
        for key, value in dct.items():
            if not key.startswith("__"):
                transformed_dct[f"meta_{key}"] = value
            else:
                transformed_dct[key] = value
        return super().__new__(cls, name, bases, transformed_dct)

class Specimen(metaclass=MetamorphosisMeta):
    dna = "ATCG"

# Attribute 'dna' was dynamically mutated to 'meta_dna'
s = Specimen()
print(s.meta_dna)  # Output: ATCG