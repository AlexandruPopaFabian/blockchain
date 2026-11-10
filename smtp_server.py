import asyncio
from aiosmtpd.controller import Controller

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print("\n================ EMAIL NOU PRIMIT ================")
        print(f"De la: {envelope.mail_from}")
        print(f"Către: {envelope.rcpt_tos}")
        print("--- Conținut ---")
        print(envelope.content.decode('utf8', errors='replace'))
        print("==================================================\n")
        return '250 Message accepted for delivery'

if __name__ == '__main__':
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname='127.0.0.1', port=1025)
    print("Serverul SMTP pornește pe portul local 1025...")
    controller.start()
    
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("\nOprire server...")
        controller.stop()