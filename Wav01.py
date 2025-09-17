from scipy.io import wavfile

def wav_to_list(filename): # Converts the files into a list of binary numbers
    rate, data = wavfile.read(filename)

    bin_list = []
    index = 0

    for amplitude in data:
        list_length = len(bin_list)

        if amplitude == 0 and index + 1 == list_length:
            index += 1

        elif index == list_length:
            if amplitude == 6000:
                bin_list.append(0)

            elif amplitude == 16000:
                bin_list.append(1)

    return bin_list

def turn_list_to_string(ls): # Converts a list of binary numbers into text
    list_length = len(ls)

    msg = ""
    byte = ""

    for index in range(list_length):
        byte += str(ls[index])

        if (index+1) % 8 == 0:
            byte_converted = int(byte, 2)
            msg += chr(byte_converted)
            byte = ""

    return msg


file1 = wav_to_list('distress_signal_1.wav')
message = (turn_list_to_string(file1))
print(message)