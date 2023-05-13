from enum import Enum

class Jazyk(Enum):
    CSHARP = "C#"
    JAVA = "Java"
    PHP = "PHP"
    PYTHON = "Python"

jazyk = Jazyk.PYTHON
print(jazyk.value)
