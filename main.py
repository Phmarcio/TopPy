import os
import time

#leitura de CPU, temperatura e memória para raspberry pi

while True:
    # Lê a temperatura da CPU
    temp = os.popen("vcgencmd measure_temp").readline()
    print("Temperatura da CPU: " + temp)

    # Lê o uso de CPU
    cpu = os.popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'").readline()
    print("Uso de CPU: " + cpu)

    # Lê o uso de memória
    mem = os.popen("free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }'").readline()
    print("Uso de memória: " + mem)

    # Aguarda 1 segundo antes de atualizar novamente
    time.sleep(1)
    os.system('clear')
