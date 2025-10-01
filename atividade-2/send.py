import pika

# Conexão com o servidor RabbitMQ (localhost por padrão)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garante que a fila exista
channel.queue_declare(queue='hello')

# Envia a mensagem
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Enviado 'Hello World!'")

connection.close()

