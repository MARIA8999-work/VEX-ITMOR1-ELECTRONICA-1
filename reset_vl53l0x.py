from machine import I2C, Pin
import time
from vl53l0x import VL53L0X

# Configuración de I2C
i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)

# Inicializar el sensor
sensor = VL53L0X(i2c)

# Función para restablecer la dirección
def reset_sensor_address(sensor):
    # Dirección por defecto del VL53L0X
    default_address = 0x29
    # Reiniciar el sensor
    sensor.stop()
    time.sleep(0.1)
    sensor.start()
    time.sleep(0.1)
    # Cambiar la dirección
    try:
        sensor.set_address(default_address)
        print("Dirección del sensor restablecida a:", hex(default_address))
    except Exception as e:
        print("Error al restablecer la dirección:", e)

# Llamar a la función
reset_sensor_address(sensor)

# Medir distancia como prueba
try:
    distance = sensor.read()
    print("Distancia medida:", distance, "mm")
except Exception as e:
    print("Error al medir la distancia:", e)