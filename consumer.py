import pika

print("Consumer called !!!")

def on_message_received (ch, method, properties, body):
    print(f" new message received : {body}")

credentials = pika.PlainCredentials("guest", "guest")  # Replace with your RabbitMQ username and password
connection_params = pika.ConnectionParameters(
    host="34.125.173.157",  # Replace with the IP address of your GCP VM hosting RabbitMQ
    port=5672,  # Default RabbitMQ port
    virtual_host="/",  # Replace with the appropriate virtual host if needed
    credentials=credentials
)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue="letterbox")
channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=on_message_received)

print("Started Consuming ... !!!")

channel.start_consuming()