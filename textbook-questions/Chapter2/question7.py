class StreamCipherLFSR:
    def __init__(self, coefficients, initial_seed):
        self.coefficients = coefficients
        self.initial_seed = initial_seed
        self.initial_seed.reverse() #s0s1s2...
        self.coefficients.reverse() #p0p1p2...
        
    def generate_key_stream(self, num_bits):
        lfsr = self.initial_seed[:]
        key_stream = []
        print(lfsr)
        for _ in range(num_bits):
            feedback_bit = 0
            for i in range(len(self.initial_seed)):
                if self.coefficients[i] == 1:
                    feedback_bit ^= lfsr[i]
                    print(feedback_bit)
            temp = lfsr.pop(0)
            key_stream.append(temp)# Remove the oldest bit
            lfsr.append(feedback_bit)       # Append the feedback bit to the LFSR
            print(lfsr)
        return key_stream
    
coefficients = [1, 0, 1]
initial_seed = [1, 0, 0]
lfsr = StreamCipherLFSR(coefficients, initial_seed)
key_stream = lfsr.generate_key_stream(2 ** 3 - 1)
print(key_stream)