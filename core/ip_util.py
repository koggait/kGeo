def cidr_to_ip_suffix(cidr):
    ip = cidr.split('/')[0]
    suffix = cidr.split('/')[1]
    return ip, suffix


def count_to_cidr_suffix(cidr):
    import math
    x = 32 - math.log2(int(cidr))
    isInt = float(x).is_integer()
    if isInt:
        return True, x
    else:
        return False, x


def ipv4_cidr_suffix_to_count(suffix):
    return 2 ** (32 - int(suffix))


def ipv6_cidr_suffix_to_count(suffix):
    return 2 ** (128 - int(suffix))


def ipv6_extend(ip):
    s = ':'
    if (ip.startswith('::')):
        ip = '0' + ip
    if (ip.endswith('::')):
        ip = ip + '0'
    if ('::' in ip):
        c = 8 - ip.count(':')
        for x in range(c):
            s = s + '0:'
        ip_split = ip.split('::')
        ip = ip_split[0] + s + ip_split[1]
    return ip


def ipv4_to_integer(ip):
    ip_list = ip.split('.')
    value = int(ip_list[0]) * (256 ** 3) + int(ip_list[1]) * (256 ** 2) + int(ip_list[2]) * 256 + int(ip_list[3])
    return value


def ipv6_to_integer(ip):
    ip_list = ip.split(':')
    value = int(ip_list[0], 16) * (65536 ** 7) + int(ip_list[1], 16) * (65536 ** 6) + int(ip_list[2], 16) * (
            65536 ** 5) + int(ip_list[3], 16) * (65536 ** 4) + int(ip_list[4], 16) * (65536 ** 3) + int(ip_list[5],
                                                                                                        16) * (
                    65536 ** 2) + int(ip_list[6], 16) * 65536 + int(ip_list[7], 16)
    return value


def ipv4_cidr_to_integer_count(cidr):
    ip, suffix = cidr_to_ip_suffix(cidr)
    value = ipv4_to_integer(ip)
    count = ipv4_cidr_suffix_to_count(suffix)
    return value, count


def ipv6_cidr_to_integer_count(cidr):
    ip, suffix = cidr_to_ip_suffix(cidr)
    ip = ipv6_extend(ip)
    value = ipv6_to_integer(ip)
    count = ipv6_cidr_suffix_to_count(suffix)
    return value, count


def integer_ip_count_to_startip_endip(ip, count):
    return ip, ip + count


def networks_intersect(network_start, network_end, subnet_start, subnet_end):
    if subnet_start >= network_start and subnet_start <= network_end:
        return True
    elif subnet_end >= network_start and subnet_end <= network_start:
        return True
    else:
        return False


def drop_asn(asn_ip_end, network_ip_start):
    if asn_ip_end < network_ip_start:
        return True
    else:
        return False
