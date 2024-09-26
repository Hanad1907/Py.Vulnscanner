from vulnerability_scanner import scan_ports, check_os_vulnerabilities
from reporter import generate_report
from utils import log_event  # Importer logger-funksjonen

def print_logo():
    logo = r"""
    ███████╗ █████╗ ██╗   ██╗██╗   ██╗██╗    ██╗███████╗███╗   ██╗██╗     ███████╗
    ██╔════╝██╔══██╗██║   ██║██║   ██║██║    ██║██╔════╝████╗  ██║██║     ██╔════╝
    █████╗  ███████║██║   ██║██║   ██║██║    ██║█████╗  ██╔██╗ ██║██║     █████╗  
    ██╔══╝  ██╔══██║██║   ██║██║   ██║██║    ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝  
    ███████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗██║ ╚████║███████╗███████╗
    ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
    """
    print(logo)

def main():
    print_logo()  # Print logo when starting
    print("Velkommen til sårbarhetsskanneren!")

    # Change the input prompt to make it clearer that users can input their own target
    target = input("Skriv inn målet (IP eller domenenavn) (f.eks. 192.168.1.1 eller example.com): ").strip()

    # Kjør portskanning
    open_ports = scan_ports(target)
    log_event(f"Åpne porter funnet for {target}: {open_ports}")

    # Sjekk etter vanlige OS-sårbarheter
    os_vulnerabilities = check_os_vulnerabilities()
    log_event(f"Sårbarheter funnet i OS for {target}: {os_vulnerabilities}")

    # Generer en rapport
    generate_report(target, open_ports, os_vulnerabilities)

    print("Skanningen er fullført. Rapporten er generert.")


if __name__ == "__main__":
    main()
