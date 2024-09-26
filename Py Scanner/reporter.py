from utils import log_event  # Importer logger-funksjonen

def generate_report(target, open_ports, os_vulnerabilities):
    report = f"""
    Sårbarhetsrapport for: {target}
    ================================
    Åpne porter:
    {', '.join(map(str, open_ports)) if open_ports else 'Ingen åpne porter funnet.'}
    
    Sårbarheter i OS:
    {', '.join(os_vulnerabilities) if os_vulnerabilities else 'Ingen OS-sårbarheter funnet.'}
    """
    
    # Lagre rapporten med UTF-8-koding
    with open("vulnerability_report.txt", "w", encoding="utf-8") as file:
        file.write(report)
    
    print("Rapport lagret som 'vulnerability_report.txt'.")

    # Loggfør rapportgenerering
    log_event(f"Rapport generert for {target}.")
