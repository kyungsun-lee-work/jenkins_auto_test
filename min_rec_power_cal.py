
SNR_dB = 20                    #% Desired SNR in dB
B = 500000                     # % Bandwidth in Hz
BS_Noise_Power_dBm = -100      #% BS equivalent noise power in dBm

#% Calculate noise power in linear scale
N_BS = 10**(BS_Noise_Power_dBm / 10)

#% Calculate minimum received power
P_received = SNR_dB * N_BS * B

#% Display the result
print('Minimum Received Power at the BS:', P_received)

print('add')
print('great!')
print("wow")
