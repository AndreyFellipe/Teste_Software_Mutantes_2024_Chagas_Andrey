# Teste de Mutação

Este repositório contém um projeto Python focado em cálculos relacionados a corridas, implementado com boas práticas de desenvolvimento e testes. O objetivo deste projeto é servir como um exemplo prático de como configurar e utilizar pytest e mutmut para testes unitários e testes de mutação, respectivamente.

## Índice

- [Escolha do Projeto](#escolha-do-projeto)
- [Clonagem do Repositório e Configuração Inicial](#clonagem-do-repositório-e-configuração-inicial)
  - [Clone o Repositório](#clone-o-repositório)
  - [Verifique o Python](#verifique-o-python)
  - [Atualize o requirements.txt](#atualize-o-requirements)
  - [Crie um Ambiente Virtual](#crie-um-ambiente-virtual)
  - [Ative o Ambiente Virtual](#ative-o-ambiente-virtual)
  - [Instale as Dependências](#instale-as-dependências)
- [Execução dos Testes](#execução-dos-testes)
  - [Testes Unitários](#testes-unitários)
  - [Testes de Mutação](#testes-de-mutação)
- [Alteração nos Casos de Teste](#alteração-nos-casos-de-teste)
- [Realização dos Novos Testes de Mutação](#realização-dos-novos-testes-de-mutação)
- [Próximos Passos](#próximos-passos)

## Escolha do Projeto

O projeto escolhido para este estudo foi o "runningCalculator", disponível em: [GitHub - runningCalculator](https://github.com/ronek22/runningCalculator).

## Clonagem do Repositório e Configuração Inicial

### Clone o Repositório

Para clonar o repositório, utilize o comando:

```bash
git clone https://github.com/ronek22/runningCalculator.git
```
### Verifique o Python

Certifique-se de que o Python está instalado em sua máquina. Se necessário, instale o Python com o comando:

```bash
pip install python
```
### Atualize o requirements

Atualize o arquivo requirements.txt com as seguintes versões de pacotes:

```plaintext
numexpr==2.8.6
numpy==1.25.2
pandas==2.0.3
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
pytest==7.4.2
pytest-cov==4.1.0
coverage==7.3.1
codecov==2.1.13
```
### Crie um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```
### Ative o Ambiente Virtual

Ative o ambiente virtual com o comando:

No Windows:
```bash
.\venv\Scripts\Activate
```
No MacOS/Linux:
```bash
source venv/bin/activate
```
### Instale as Dependências

Após ativar o ambiente virtual, instale as dependências necessárias:

```bash
pip install wheel
pip install -r requirements.txt
```
## Execução dos Testes

### Testes Unitários

Os arquivos principais do projeto são calculator.py, running_index.py, utils.py e seus respectivos testes: test_calculator.py, test_running_index.py, test_utils.py.

<div align="center">
    <img src="https://i.imgur.com/6LKzwIb.png" alt="Arquivos em Foco" />
</div>

Para executar os testes unitários com detalhes e medir a cobertura de código, utilize o comando:

```bash
pytest -vv --cov
```
Exemplo de execução para o arquivo test_calculator.py:

```bash
pytest -vv tests/test_calculator.py --cov
```

![image](https://github.com/user-attachments/assets/f9d335b7-d292-420c-9ac3-353b4ded50d7)

Para gerar um relatório de cobertura em HTML:

```bash
pytest -vv tests/test_calculator.py --cov  --cov-branch  --cov-report html
```
O relatório será gerado na pasta htmlcov. Abra o arquivo htmlcov/index.html para visualizar os resultados.
O relatório possui a seguinte representação:

![image](https://github.com/user-attachments/assets/ce8c13ee-dc7a-4564-b5a0-71e402d6ceda)

É possível detalhar o relatório ao clicar no mesmo:

![image](https://github.com/user-attachments/assets/7701d6ed-3a66-48ae-bd8a-8170a5f688c7)

O mesmo procedimento é aplicado para os outros arquivos restantes.


### Testes de Mutação

Após a geração dos relatórios de cobertura, aplique os testes de mutação utilizando mutmut. Para realizar o teste de mutação em um arquivo específico, utilize o seguinte comando:

```bash
mutmut run --paths-to-mutate=running_calculator/core/calculator.py
```
Durante a execução do teste, é possível visualizar o progresso na tela, como mostrado na imagem abaixo, onde o processo ainda está em andamento, percorrendo e verificando cada mutante.

![image](https://github.com/user-attachments/assets/9a1a7d63-1965-4b93-ad4e-375052c93061)

Após a conclusão do teste, podemos perceber que dos 23 mutantes gerados, 18 foram eliminados com sucesso, indicando testes eficazes. Cinco mutantes sobreviveram, sugerindo a necessidade de ampliar ou melhorar os testes para cobrir esses casos específicos, garantindo uma análise mais robusta do código.

![image](https://github.com/user-attachments/assets/e6975916-9e29-4bf0-a81f-e979784acacb)

Visualize os mutantes sobreviventes com:

```bash
mutmut results
```
Após a execução do comando, podemos visualizar a seguinte tela:

![image](https://github.com/user-attachments/assets/cbfbfef5-68d0-4f13-9ecc-d6298970f3f9)


Você também pode inspecionar um mutante específico com o comando:

```bash
mutmut show [ID do mutante]
```
Por exemplo:

![image](https://github.com/user-attachments/assets/16b4e8fc-b024-48a2-9575-0998525795d4)

Para gerar um relatório em HTML dos mutantes sobreviventes:

```bash
mutmut html
```
O relatório possui a seguinte representação:

![image](https://github.com/user-attachments/assets/946dec17-37c1-4709-add7-a3e0c98272d0)

É possível detalhar o relatório ao clicar no mesmo:

![image](https://github.com/user-attachments/assets/93506029-2d9d-4388-822e-a6743a735cc0)

O mesmo procedimento é aplicado aos outros arquivos.
Ao executar o mutmut nos 3 arquivos, essa será nossa visualização do html do relatório:

![image](https://github.com/user-attachments/assets/157afb83-d7e8-4c86-a295-334e72dda7c0)

Veja que dos 89 mutantes, 58 foram eliminados e 31 sobreviveram.

## Alteração nos Casos de Teste
Para diminuir o número de mutantes sobreviventes, adicione ou altere casos de teste nos arquivos de teste correspondentes.

Exemplos de Casos Adicionados:

calculator.py: Adicionado mais um caso de teste para eliminar o mutante 17.
O Mutante:

![image](https://github.com/user-attachments/assets/592adeaa-c718-4961-8595-49c6c1f23ab5)

O caso de teste(Destacado em vermelho):

![image](https://github.com/user-attachments/assets/9e1cca17-9cd5-46e3-b1ef-00363cd21522)

running_index.py: Adicionados dois casos de teste para eliminar os mutantes 25 e 31.
Os Mutantes:

![image](https://github.com/user-attachments/assets/1f4d1fb2-82b1-4a72-bed9-8b4b32ccef6d)

Os casos de teste(Destacados em vermelho):

![image](https://github.com/user-attachments/assets/52acdf88-8f9a-4711-956d-d87726645fdf)


utils.py: Adicionado um caso de teste para eliminar o mutante 84.
O Mutante:

![image](https://github.com/user-attachments/assets/7b0bfc64-e736-4e01-8f2d-6b96d8fd8b00)

O caso de teste(Destacado em vermelho):

![image](https://github.com/user-attachments/assets/77e30912-18e3-40e6-90e5-805d67562367)

## Realização dos Novos Testes de Mutação

Após as alterações nos casos de teste, execute novamente os testes de mutação:

```bash
mutmut run --paths-to-mutate=running_calculator/core/[arquivo].py
```
Utilize o comando abaixo para evitar erros de codificação:

```bash
set PYTHONIOENCODING=utf-8
```

Após a execução dos testes para os 3 arquivos o resultados mostrados na tela foram esses:

![image](https://github.com/user-attachments/assets/635a2116-43c7-4d22-9684-0ca1183b05b5)

![image](https://github.com/user-attachments/assets/9f90607b-0ebf-40ad-9a46-9893fb73d297)

![image](https://github.com/user-attachments/assets/08528ea7-e2ff-41c6-9b51-691b547e5f44)

Dessa forma, dos 89 mutantes, 62 foram eliminados e 27 sobreviveram, conforme demonstra o relatório abaixo.

![image](https://github.com/user-attachments/assets/5a9f7abd-1953-4ddf-a247-d71e619065c6)

Note que os mutantes que foram eliminados não aparecem mais nos resultados, conforme mostra a imagem abaixo ao executar o comando:
```bash
mutmut results
```
![image](https://github.com/user-attachments/assets/56ecb69d-b292-4e64-8bc7-408849629fbb)



## Próximos Passos

Para continuar eliminando os mutantes restantes, continue adicionando ou ajustando casos de teste conforme necessário e gere novos relatórios.

