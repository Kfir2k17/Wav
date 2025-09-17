from scipy.io import wavfile

def wav_to_list(filename, only_two=False): # Converts the files into a list of binary numbers
    rate, data = wavfile.read(filename)

    bin_list = []
    index = 0

    chunk_num = 1 if only_two else 4

    ZERO = 0 if only_two else - 3 # Setting the number that would represent zero

    for amplitude in data:
        list_length = len(bin_list)

        fixed_amplitude = int((amplitude / 1000) -3) if not only_two else amplitude

        if fixed_amplitude == ZERO and index + 1 == list_length:
            index += 1

        elif index == list_length and only_two:
            if amplitude == 6000:
                bin_list.append(0)

            elif amplitude == 16000:
                bin_list.append(1)

        elif index == list_length and not only_two:
            bin_num = format(fixed_amplitude, 'b')
            bin_str = bin_num.zfill(4)
            bin_list.append(bin_str)


    return turn_list_to_string(bin_list, chunk_num)

def turn_list_to_string(ls, chunks=1): # Converts a list of binary numbers into text
    list_length = len(ls)

    msg = ""
    byte = ""

    divider = 8 / chunks

    for index in range(list_length):
        byte += str(ls[index])

        if (index+1) % divider == 0:
            byte_converted = int(byte, 2) if chunks == 1 else byte.encode()
            msg += chr(byte_converted)
            byte = ""

    return msg

# message1 = wav_to_list('distress_signal_1.wav', True)
message2 = wav_to_list('distress_signal_2.wav')

print(message2)