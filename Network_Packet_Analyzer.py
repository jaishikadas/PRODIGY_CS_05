import random
import string

def generate_packet(source_ip, dest_ip, protocol):
    """Simulates a network packet with random data."""
    payload = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
    return {
        'source_ip': source_ip,
        'dest_ip': dest_ip,
        'protocol': protocol,
        'payload': payload
    }

def analyze_packet(packet):
    """Analyzes a simulated packet and displays relevant information."""
    print(f"Source IP: {packet['source_ip']}")
    print(f"Destination IP: {packet['dest_ip']}")
    print(f"Protocol: {packet['protocol']}")
    print(f"Payload (sample): {packet['payload'][:20]}...")  # Display first 20 characters

def main():
    """Simulates network traffic and analyzes packets."""
    packets = [
        generate_packet("122.139.1.11", "8.8.8.8", "TCP"),
        generate_packet("10.0.0.1", "172.16.0.2", "UDP"),
        generate_packet("137.0.0.1", "localhost", "HTTP")
    ]

    for packet in packets:
        analyze_packet(packet)

if __name__ == "__main__":
    main()
