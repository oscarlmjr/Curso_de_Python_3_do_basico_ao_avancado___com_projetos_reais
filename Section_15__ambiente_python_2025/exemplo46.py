from dataclasses import dataclass
from typing import Annotated, get_args, get_origin, get_type_hints

from utils import cyan_print, sep_print

p = cyan_print
s = sep_print

################################################################################
#
# Python Annotated: O Que é Tão Especial Nele? (Type Hints - Aula 19)
#
# Annotated é um tipo parametrizado especial do Python usado para adicionar
# metadados em outros tipos. Ele recebe um tipo para o primeiro argumento e pelo
# menos um valor para o segundo.
#
# Inteiro = Annotated[int, "Um número inteiro"] # int para o type checker
#
# Você pode passar o que preferir do segundo argumento em diante, incluindo
# funções, classes, valores escalares, etc.
#
# O Type Checker considera o primeiro argumento como tipo, o restante
# pode ser usado para várias situações, como: documentação, validação,
# informações em geral, modificação, enfim... Depende do que a sua imaginação
# conseguir produzir.
#
# A parte mais interessante de Annotated é que você consegue usar os metadados
# em runtime, por isso você vê várias libs e frameworks abusando do seu uso
# (você também deveria usar). Pydantic, FastAPI, Langchain e Langgraph são
# algumas das ferramentas que usam bastante Annotated para tipagem e metadados
# em runtime.
#
# Com o que usar Annotated? classes, funções, módulos e objetos.
#
# Funções que acompanham Annotated:
#
# - get_type_hints - Retorna os dados de tipagem para função, método, objeto ou módulo.
# - get_args - Retorna os argumentos internos do tipo parametrizado ou composto.
# - get_origin - Retorna o tipo "externo". Ex. Se o tipo é X[A, B, ...], retorna X.
# - e outras...
#
################################################################################


def simple_annotation(
    annotated: Annotated[object, "I have annotation"],
) -> Annotated[object, "I have annotation"]:
    return annotated


s()

type_hints = get_type_hints(simple_annotation, include_extras=True)
type_args = get_args(type_hints["annotated"])
type_return = get_args(type_hints["return"])
type_origin = get_origin(type_hints["annotated"])

p(f"{type_hints=!r}")
p(f"{type_args=!r}")
p(f"{type_return=!r}")
p(f"{type_origin=!r}")

s()


################################################################################

# Exemplo de classe com atributos anotados


@dataclass
class Person:
    """A person object"""

    name: Annotated[str, "O nome completo da pessoa"]
    age: Annotated[int | None, "A idade"] = None


################################################################################

#
# Exemplo para verificar os metadados em runtime (prints para simplicidade)
#
# Observação: não fiz todos os testes possíveis nessa função. Isso vai depender
# do que você for fazer.
#


def print_annotated[T: object](obj: T) -> T:
    # Pegamos a classe do objeto
    obj_class = obj.__class__
    # Tentamos obter o __name__ se tiver um
    obj_name = getattr(obj, "__name__", "")

    if not obj_name:
        # Se não tiver nome, vamos pegar o nome da classe.
        # Geralmente isso vai ser instância da classe (tem que checar)
        obj_name = obj_class.__name__

    # Pega os dados das annotations
    # get_type_hints retorna um dicionário com chave e tipo anotado
    # o include_extras=True é para vir os metadados (padrão False)
    hints = get_type_hints(obj, include_extras=True)

    if not hints:
        # Se não tem hints, nada a fazer
        return obj

    # Agora é só exibir tudo
    p("🧐 Verificando a tipagem de:", obj_name)
    p(f"🎲 Objeto Real: {obj!r}")
    for key, value in hints.items():
        # IMPORTANTE: podemos receber uma instância de classe, uma classe,
        # um método ou função. Em termos de classe, funções, métodos e módulos,
        # não temos nenhum valor disponível.
        val = getattr(obj, key, "NO VALUE")

        # get_args vai trazer o tipo e o resto que estiver dentro de Annotated
        type_, *metadata = get_args(value)
        p(
            f"🔑 Key={key!r} 📋 Type={type_!r} 📝 Meta={metadata!r} Value={val!r}",
        )
    p()
    s()

    return obj


################################################################################


if __name__ == "__main__":
    print_annotated(simple_annotation)

    person = Person("Luiz", 30)
    print_annotated(person)

    print_annotated(Person)


################################################################################
