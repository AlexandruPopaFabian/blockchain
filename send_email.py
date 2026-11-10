import smtplib
import sys
from email.message import EmailMessage

if len(sys.argv) < 3:
    print("Utilizare: python send_email.py <HOST_COLEG> <PORT_COLEG>")
    sys.exit(1)

target_host = sys.argv[1]
target_port = int(sys.argv[2])

msg = EmailMessage()
msg.set_content('Salut! Acesta este emailul de test trimis prin serverul meu SMTP via Bore.')
msg['Subject'] = 'Test Tema SMTP & Blockchain'
msg['From'] = 'alexandrupopa@local.domain'
msg['To'] = 'raulpodean@partner.domain'

try:
    with smtplib.SMTP(target_host, target_port) as server:
        server.send_message(msg)
        print("[SUCCESS] Emailul a fost trimis cu succes către coleg!")
except Exception as e:
    print(f"[ERROR] Nu s-a putut trimite emailul: {e}")