import pika

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

message = "Hello this is my first rabbitMQ message"
channel.basic_publish(exchange="",routing_key="letterbox", body=message)

print(f"sent message: {message}")

connection.close()