
## README - Serviço RPC em Python

### Introdução

Este projeto consiste em dois tipos diferentes de serviços RPC (Remote Procedure Call) em Python: RPyC e XML-RPC. Os serviços RPC permitem que funções sejam executadas em um servidor remoto, como se estivessem sendo executadas localmente.

---

### Bibliotecas

- **RPyC**: Biblioteca Python para RPC.
- **xmlrpc.client e xmlrpc.server**: Módulos padrão do Python para implementação de cliente e servidor XML-RPC.

---

### Diferenças entre RPyC e XML-RPC

#### RPyC (Remote Python Call)

- **Facilidade de uso**: Mais simples e Pythonic.
- **Transparência**: Permite que objetos Python sejam usados através da rede como se fossem locais.
- **Segurança**: Permite a autenticação e outras características de segurança.
  
#### XML-RPC

- **Portabilidade**: Utiliza XML como protocolo de codificação, o que o torna mais portável entre diferentes linguagens.
- **Padrão**: É um padrão mais antigo e amplamente suportado.
- **Verbosidade**: A natureza do XML torna as mensagens mais verbosas em comparação com as do RPyC.

---

### Endpoints e Métodos


### Requisição

#### RPyC

Para fazer uma chamada RPC usando RPyC, você conecta ao servidor e chama os métodos expostos.

```python
# trecho de rpyc-client.py
conn = rpyc.connect("localhost", 8000)
imc_result = conn.root.calculate_imc(70, 1.75)
```

#### XML-RPC

Para fazer uma chamada RPC usando XML-RPC, você também conecta ao servidor e chama os métodos expostos.

```python
# trecho de xml-rpc-client.py
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    imc_result = proxy.calculate_imc(70, 1.75)
```

