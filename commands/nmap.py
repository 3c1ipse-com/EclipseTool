import subprocess
import re
from utils import openai_client

def run_nmap_scan(ip):
    print(f"Realizando un escaneo rápido de todos los puertos en {ip}...")
    fast_scan_command = f"nmap -p- --open -T5 --min-rate 5000 -vvv -n -Pn {ip}"
    fast_scan_result = subprocess.check_output(fast_scan_command, shell=True, text=True)
    print(f"Resultado del escaneo rápido:\n{fast_scan_result}")

    open_ports = re.findall(r"(\d+)/tcp\s+open", fast_scan_result)

    if open_ports:
        open_ports_str = ",".join(open_ports)
        print(f"Realizando un escaneo más profundo en los puertos: {open_ports_str}")
        deep_scan_command = f"nmap -p {open_ports_str} -Pn -sCV {ip}"
        deep_scan_result = subprocess.check_output(deep_scan_command, shell=True, text=True)
        print(f"Resultado del escaneo profundo:\n{deep_scan_result}")

        return deep_scan_result
    else:
        print("No se encontraron puertos abiertos en el escaneo rápido.")
        return None


def analyze_with_openai(scan_result):
    print("Analizando resultados con OpenAI...")
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en ciberseguridad."},
            {"role": "user", "content": f"Estos son los resultados de un escaneo de puertos:\n{scan_result}\nIdentifica posibles vulnerabilidades y ataques que podrían realizarse."},
        ]
    )
    analysis = response.choices[0].message.content
    print(f"Análisis de OpenAI:\n{analysis}")
