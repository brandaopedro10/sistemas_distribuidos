import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Esperando mensagens. Para sair pressione CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Recebido {body}")

channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()
