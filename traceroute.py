from scapy.all import IP, ICMP, sr1
import time

def traceroute(target, max_hops=30):
    print(f"Traceroute to {target}, max hops: {max_hops}")
    
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        start_time = time.time()
        
        # Send the packet and receive a reply
        reply = sr1(pkt, verbose=0, timeout=1)
        end_time = time.time()
        
        if reply is None:
            print(f"{ttl}: Request timed out.")
        elif reply.type == 11:  # ICMP Time Exceeded
            rtt = round((end_time - start_time) * 1000, 2)
            print(f"{ttl}: {reply.src} - {rtt} ms")
        elif reply.type == 0:  # ICMP Echo Reply (Destination reached)
            rtt = round((end_time - start_time) * 1000, 2)
            print(f"{ttl}: {reply.src} - Reached - {rtt} ms")
            break
        else:
            print(f"{ttl}: Unexpected reply type {reply.type}")

if __name__ == "__main__":
    target = input("Enter target IP or domain for traceroute: ")
    traceroute(target)
