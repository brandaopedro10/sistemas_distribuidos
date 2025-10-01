# 📨 Sistemas Distribuídos – Exercícios com RabbitMQ

Este repositório reúne duas práticas iniciais baseadas no tutorial oficial do [RabbitMQ](https://www.rabbitmq.com/tutorials/), implementadas em **Python** utilizando a biblioteca `pika`.

---

## 🔧 Requisitos

* **Python 3.9** instalado
* Instalação da dependência `pika`:

  ```bash
  pip install pika
  ```

---

## 🟢 Atividade 1 – Hello World

**Objetivo:**
Criar o exemplo mais simples de comunicação entre processos: um produtor envia uma mensagem para a fila **hello** e um consumidor a lê.

**Arquivos principais:**

* `atividade1-hello-world/send.py` → script do produtor
* `atividade1-hello-world/receive.py` → script do consumidor

**Como executar:**

1. Inicie o consumidor:

   ```bash
   python atividade1-hello-world/receive.py
   ```
2. Em outro terminal, rode o produtor:

   ```bash
   python atividade1-hello-world/send.py
   ```

**Saída esperada no consumidor:**

```
 [*] Aguardando mensagens. Para sair pressione CTRL+C
 [x] Recebido b'Hello World!'
```

---

## 🟡 Atividade 2 – Work Queues

**Objetivo:**
Implementar filas de trabalho, onde várias tarefas são enfileiradas e distribuídas entre múltiplos consumidores (workers).

**Arquivos principais:**

* `atividade2-work-queues/new_task.py` → gera tarefas
* `atividade2-work-queues/worker.py` → executa as tarefas recebidas

**Como executar:**

1. Inicie um ou mais workers:

   ```bash
   python atividade2-work-queues/worker.py
   ```
2. Em outro terminal, crie novas tarefas:

   ```bash
   python atividade2-work-queues/new_task.py "Tarefa 1..."
   python atividade2-work-queues/new_task.py "Tarefa 2..."
   python atividade2-work-queues/new_task.py "Tarefa 3..."
   ```

**Exemplo de saída (Worker 1):**

```
 [*] Aguardando mensagens. Para sair pressione CTRL+C
 [x] Recebido Tarefa 1...
 [x] Feito
```

**Exemplo de saída (Worker 2):**

```
 [*] Aguardando mensagens. Para sair pressione CTRL+C
 [x] Recebido Tarefa 2...
 [x] Feito
```

---

## 📖 Conclusão

* **Hello World:** introduz o básico de filas no RabbitMQ, mostrando como enviar e receber mensagens.
* **Work Queues:** demonstra distribuição de tarefas entre múltiplos consumidores, um passo além da comunicação simples.

Esses exemplos servem como ponto de partida para explorar recursos mais avançados, como **Exchanges, Routing, Topics e RPC**.

---

