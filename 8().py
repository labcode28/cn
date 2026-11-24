8. Write a program for congestion control using Leaky bucket 
algorithm.
Procedure:
1. Start with an empty bucket (capacity is fixed).
2. Packets come in one by one.
3. If the packet is bigger than the bucket capacity → Drop it.
4. If the bucket has no space left for the packet → Drop it.
5. If there is space → Put the packet into the bucket.
6. At every step, the bucket leaks (sends out) data at a fixed rate (output 
rate).
7. Continue until all packets are processed.
8. Finally, send out the remaining data from the bucket


  
def leaky_bucket():
    # Input bucket size, outgoing rate, and number of inputs
    bucket_size = int(input("Enter bucket size: "))
    outgoing_rate = int(input("Enter outgoing rate: "))
    num_inputs = int(input("Enter number of inputs: "))

    store = 0  # Initial amount in the bucket

    while num_inputs > 0:
        incoming = int(input("\nEnter the incoming packet size: "))
        print(f"Incoming packet size: {incoming}")

        # Check if the packet can fit in the bucket
        if incoming <= (bucket_size - store):
            store += incoming
            print(f"Bucket buffer size: {store} out of {bucket_size}")
        else:
            dropped = incoming - (bucket_size - store)
            print(f"Dropped {dropped} packets.")
            store = bucket_size
            print(f"Bucket buffer size: {store} out of {bucket_size}")

        # Send packets out of the bucket
        if store >= outgoing_rate:
            store -= outgoing_rate
        else:
            store = 0

        print(f"After outgoing, {store} packets left in buffer out of {bucket_size}")

        num_inputs -= 1


if __name__ == "__main__":
    leaky_bucket()
  
