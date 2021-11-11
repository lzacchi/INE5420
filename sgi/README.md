# INE5420

## INSTRUÇÕES
Este programa utiliza Poetry como gerenciador de dependências. Para executar o projeto através, dele, siga as intruções de instalação disponíveis em:
https://python-poetry.org/

Execução:
- `poetry install` para instalar as dependências do projeto
- `poetry run python3 app/main.py` para executar o projeto.

## Estrutura do projeto

Os diretórios do projeto estão organizados da seguinte maneira:
- `qt_designer`: arquivos .ui utilizados durante a criação das janelas através da ferramenta Qt Designer
- `app`: diretório raiz
- `app/gui`: arquivos .py da descrição e funcionamento das janelas e interfaces gráficas
- `app/utils`: funções e estruturas específicas utilizadas no projeto, como a transformada de viewport e a declaração da estrutura wireframe
