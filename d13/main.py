import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        pairs = []
        line1 = fd.readline().strip()
        resume_read = True
        while resume_read:
            line2 = fd.readline().strip()
            pair = [eval(line1), eval(line2)]
            pairs.append(pair)

            fd.readline().strip()
            line1 = fd.readline().strip()
            if len(line1) == 0:
                resume_read = False

    sum_indices_of_valid_pairs(pairs)
    
    sorted_lists = sort_lists(pairs)

    divider_packets_indices = []
    divider_packets_indices.append(insert_packet_list(sorted_lists, [[2]]))
    divider_packets_indices.append(insert_packet_list(sorted_lists, [[6]]))
    print("Decoder key is:", divider_packets_indices[0]*divider_packets_indices[1])


def insert_packet_list(sorted_lists, packet):
    for i_packet in range(len(sorted_lists)):
        if is_valid_pair(packet, sorted_lists[i_packet]):
            sorted_lists.insert(i_packet, packet)
            return i_packet + 1
    else:
        sorted_lists.append(packet)
        return len(sorted_lists)


def sort_lists(pairs):
    flat_lists = []
    for pair in pairs:
        flat_lists.append(pair[0])
        flat_lists.append(pair[1])
    
    sorted_lists = [flat_lists[0]]
    for i_list in range(1, len(flat_lists)):
        for j_list in range(len(sorted_lists)):
            if is_valid_pair(flat_lists[i_list], sorted_lists[j_list]):
                sorted_lists.insert(j_list, flat_lists[i_list])
                break
        else:
            sorted_lists.append(flat_lists[i_list])

    return sorted_lists


def sum_indices_of_valid_pairs(pairs):
    valid_pairs = []
    for i_pair, pair in enumerate(pairs):
        if is_valid_pair(pair[0], pair[1]):
            valid_pairs.append(i_pair+1)
    print("Sum of valid pairs:", sum(valid_pairs))


def is_valid_pair(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for i_left, e_left in enumerate(left):
            if i_left < len(right):
                valid_pair = is_valid_pair(e_left, right[i_left])
                if valid_pair is None:
                    continue
                else:
                    return valid_pair
            else:
                return False
        if len(left) < len(right):
            return True
        else:
            return None
    elif isinstance(left, int) and isinstance(right, int):
        return left < right if left != right else None
    elif isinstance(left, int) and isinstance(right, list):
        return is_valid_pair([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return is_valid_pair(left, [right])



if __name__ == "__main__":
    main()