import os, time
from dotenv import load_dotenv
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

#as variáveis de ambiente, como o IP do gateway, devem ser armazenadas em arquivos .env

#lê o arquivo .env e busca as variáveis armazenadas
load_dotenv()
ip_porta_pushgateway = os.getenv("IP_PUSHGATEWAY")

registry = CollectorRegistry()

#gauge_temp = Gauge('cpu_temp_rasp','CPU temperature', registry=registry)
gauge_cpu = Gauge('cpu_usage_rasp','CPU usage', registry=registry)
#gauge_mem = Gauge('memory_usage_rasp','Memory usage', registry=registry)

while True:
    # Lê a temperatura da CPU
    temp = os.popen("vcgencmd measure_temp").readline()
    #gauge_temp = temp
    print("Temperatura da CPU: " + temp)

    # Lê o uso de CPU
    cpu = os.popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'").readline()
    gauge_cpu = cpu
    print("Uso de CPU: " + cpu)

    # Lê o uso de memória
    mem = os.popen("free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }'").readline()
    #gauge_mem = mem
    print("Uso de memória: " + mem)

    #envia informação para o pushgateway do Prometheus
    push_to_gateway("ip_porta_pushgateway", job="rasp_monitor", registry=registry)

    # Aguarda 1 segundo antes de atualizar novamente
    time.sleep(5)
    os.system('clear')

