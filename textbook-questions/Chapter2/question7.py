class StreamCipherLFSR:
    # initialize the feedback coefficients and initial seed
    def __init__(self, coefficients, initial_seed):
        self.coefficients = coefficients
        self.initial_seed = initial_seed
        self.coefficients.reverse()
        self.initial_seed.reverse()
        
    # uses the initial seed to generate the number of bits prompted
    def generate_key_stream(self, num_bits):
        lfsr = self.initial_seed[:]
        key_stream = []
        for _ in range(num_bits):
            feedback_bit = 0
            for i in range(len(self.initial_seed)):
                if self.coefficients[i] == 1:
                    feedback_bit ^= lfsr[i]
            temp = lfsr.pop(0)
            key_stream.append(temp)         # Remove the oldest bit
            lfsr.append(feedback_bit)       # Append the feedback bit to the LFSR
        key_stream.reverse()
        return key_stream
    
coefficients = [1, 0, 1]
initial_seed = [1, 0, 0]
lfsr = StreamCipherLFSR(coefficients, initial_seed)
key_stream = lfsr.generate_key_stream(2 ** 3 - 1)
print(key_stream)