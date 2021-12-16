raw_binary_map = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111"""

binary_map = {}
for line in raw_binary_map.splitlines():
    [b, v] = line.split(" = ")
    binary_map[b] = v


def get_binary_string(s):
    return "".join([binary_map[c] for c in s])


class Packet:
    def __init__(self, version, _id) -> None:
        self.version = version
        self._id = _id
        self.packets = []
        self.value = None


def parse_packet(binary_string):
    b_version = binary_string[0:3]
    b_id = binary_string[3:6]

    version = int(b_version, 2)
    _id = int(b_id, 2)

    packet = Packet(version, _id)

    new_string = binary_string[6:]
    new_packets = []
    if _id == 4:
        # Literal Value
        b_string = ""
        while True:
            next_5_bits = new_string[:5]
            b_string += next_5_bits[1:]
            new_string = new_string[5:]
            if next_5_bits[0] == "0":
                # last
                packet.value = int(b_string, 2)
                break
    else:
        # Operator
        l_type = new_string[0]
        new_string = new_string[1:]
        if l_type == '0':
            # length of subpackets
            b_subpackets_len = new_string[:15]
            subpackets_len = int(b_subpackets_len, 2)
            new_string = new_string[15:]

            while subpackets_len > 0 and new_string:
                prev_len = len(new_string)
                sub_packet, new_string = parse_packet(new_string)
                curr_len = len(new_string)
                subpackets_len -= prev_len - curr_len
                new_packets.append(sub_packet)
        else:
            # number of subpackets
            num_of_subpackets = int(new_string[:11], 2)
            new_string = new_string[11:]

            while num_of_subpackets > 0 and new_string:
                sub_packet, new_string = parse_packet(new_string)
                num_of_subpackets -= 1
                new_packets.append(sub_packet)

    for p in new_packets:
        packet.packets.append(p)
    return packet, new_string


def count_versions(packet):
    count = packet.version
    for p in packet.packets:
        count += count_versions(p)
    return count


def calculate_packet_value(packet):
    if packet._id == 0:
        value = 0
        for p in packet.packets:
            value += calculate_packet_value(p)
        packet.value = value
    elif packet._id == 1:
        value = 1
        for p in packet.packets:
            value *= calculate_packet_value(p)
        packet.value = value
    elif packet._id == 2:
        packet.value = min([calculate_packet_value(p) for p in packet.packets])
    elif packet._id == 3:
        packet.value = max([calculate_packet_value(p) for p in packet.packets])
    elif packet._id == 5:
        sub1 = packet.packets[0]
        sub2 = packet.packets[1]
        packet.value = 1 if (
            calculate_packet_value(sub1) > calculate_packet_value(sub2)
        ) else 0
    elif packet._id == 6:
        sub1 = packet.packets[0]
        sub2 = packet.packets[1]
        packet.value = 1 if (
            calculate_packet_value(sub1) < calculate_packet_value(sub2)
        ) else 0
    elif packet._id == 7:
        sub1 = packet.packets[0]
        sub2 = packet.packets[1]
        packet.value = 1 if (
            calculate_packet_value(sub1) == calculate_packet_value(sub2)
        ) else 0

    return packet.value


if __name__ == "__main__":
    input = "C20D59802D2B0B6713C6B4D1600ACE7E3C179BFE391E546CC017F004A4F513C9D973A1B2F32C3004E6F9546D005840188C51DA298803F1863C42160068E5E37759BC4908C0109E76B00425E2C530DE40233CA9DE8022200EC618B10DC001098EF0A63910010D3843350C6D9A252805D2D7D7BAE1257FD95A6E928214B66DBE691E0E9005F7C00BC4BD22D733B0399979DA7E34A6850802809A1F9C4A947B91579C063005B001CF95B77504896A884F73D7EBB900641400E7CDFD56573E941E67EABC600B4C014C829802D400BCC9FA3A339B1C9A671005E35477200A0A551E8015591F93C8FC9E4D188018692429B0F930630070401B8A90663100021313E1C47900042A2B46C840600A580213681368726DEA008CEDAD8DD5A6181801460070801CE0068014602005A011ECA0069801C200718010C0302300AA2C02538007E2C01A100052AC00F210026AC0041492F4ADEFEF7337AAF2003AB360B23B3398F009005113B25FD004E5A32369C068C72B0C8AA804F0AE7E36519F6296D76509DE70D8C2801134F84015560034931C8044C7201F02A2A180258010D4D4E347D92AF6B35B93E6B9D7D0013B4C01D8611960E9803F0FA2145320043608C4284C4016CE802F2988D8725311B0D443700AA7A9A399EFD33CD5082484272BC9E67C984CF639A4D600BDE79EA462B5372871166AB33E001682557E5B74A0C49E25AACE76D074E7C5A6FD5CE697DC195C01993DCFC1D2A032BAA5C84C012B004C001098FD1FE2D00021B0821A45397350007F66F021291E8E4B89C118FE40180F802935CC12CD730492D5E2B180250F7401791B18CCFBBCD818007CB08A664C7373CEEF9FD05A73B98D7892402405802E000854788B91BC0010A861092124C2198023C0198880371222FC3E100662B45B8DB236C0F080172DD1C300820BCD1F4C24C8AAB0015F33D280"

    b_string = get_binary_string(input)
    packet, s = parse_packet(b_string)
    print(count_versions(packet))
    print(calculate_packet_value(packet))
