class Config:
    HOST_IP = "192.168.222.127"
    KAFKA_PORT = "9092"
    FLUENTD_PORT = 24224

    KAFKA_BOOTSTRAP_SERVERS = f"{HOST_IP}:{KAFKA_PORT}"
    FLUENTD_HOST = HOST_IP