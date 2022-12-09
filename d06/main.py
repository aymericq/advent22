import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        line = fd.readline().strip()

    start_of_packet_position = find_start_of_packet_position(line)
    print("Start of packet :", start_of_packet_position)
    start_of_message_position = find_start_of_message_position(line)
    print("Start of packet :", start_of_message_position)


def find_start_of_message_position(line):
    for i_char in range(14-1, len(line)):
        is_start_of_message = True
        for i_prev_char in range(13):
            if line[i_char-i_prev_char] in line[i_char-13:i_char-i_prev_char]:
                is_start_of_message = False
                break
        if is_start_of_message:
            return i_char + 1


def find_start_of_packet_position(line):
    for i in range(3, len(line)):
        if line[i] not in line[i - 3:i] and line[i - 1] not in line[i - 3:i - 1] and line[i - 2] not in line[i-3:i-2]:
            return i + 1


if __name__ == "__main__":
    main()
