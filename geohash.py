class GeoHash:
    def __init__(self):
        self.table = '0123456789bcdefghjkmnpqrstuvwxyz'
        self.bits = [0b10000, 0b01000, 0b00100, 0b00010, 0b00001]

    def encode(self, lng: float, lat: float, prec=0.00001):
        min_lng = -180
        max_lng = 180
        min_lat = -90
        max_lat = 90

        hashed_geo = []
        error = 180
        is_even = True
        chr_value = 0b00000
        b = 0

        while error >= prec:
            if is_even:
                next_value = (min_lng + max_lng) / 2
                if lng > next_value:
                    chr_value |= self.bits[b]
                    min_lng = next_value
                else:
                    max_lng = next_value
            else:
                next_value = (min_lat + max_lat) / 2
                if lat > next_value:
                    chr_value |= self.bits[b]
                    min_lat = next_value
                else:
                    max_lat = next_value
            is_even = not is_even

            if b < 4:
                b += 1
            else:
                hashed_geo.append(self.table[chr_value])
                error = max(max_lng - min_lng, max_lat - min_lat)
                b = 0
                chr_value = 0b00000
        return ''.join(hashed_geo)

    def decode(self, hashed_geo: str):
        min_lng = -180
        max_lng = 180
        min_lat = -90
        max_lat = 90

        for i in range(len(hashed_geo)):
            v = self.table.find(hashed_geo[i])
            if 1 & i:
                if 16 & v:
                    min_lat = (min_lat + max_lat) / 2
                else:
                    max_lat = (min_lat + max_lat) / 2
                if 8 & v:
                    min_lng = (min_lng + max_lng) / 2
                else:
                    max_lng = (min_lng + max_lng) / 2
                if 4 & v:
                    min_lat = (min_lat + max_lat) / 2
                else:
                    max_lat = (min_lat + max_lat) / 2
                if 2 & v:
                    min_lng = (min_lng + max_lng) / 2
                else:
                    max_lng = (min_lng + max_lng) / 2
                if 1 & v:
                    min_lat = (min_lat + max_lat) / 2
                else:
                    max_lat = (min_lat + max_lat) / 2
            else:
                if 16 & v:
                    min_lng = (min_lng + max_lng) / 2
                else:
                    max_lng = (min_lng + max_lng) / 2
                if 8 & v:
                    min_lat = (min_lat + max_lat) / 2
                else:
                    max_lat = (min_lat + max_lat) / 2
                if 4 & v:
                    min_lng = (min_lng + max_lng) / 2
                else:
                    max_lng = (min_lng + max_lng) / 2
                if 2 & v:
                    min_lat = (min_lat + max_lat) / 2
                else:
                    max_lat = (min_lat + max_lat) / 2
                if 1 & v:
                    min_lng = (min_lng + max_lng) / 2
                else:
                    max_lng = (min_lng + max_lng) / 2
        return [min_lng, max_lng, min_lat, max_lat]


if __name__ == '__main__':
    geo = GeoHash()
    decoded = geo.decode('wydj54xyt21')
    print(decoded)
    encoded = geo.encode(126.70520558953285, 37.456254959106445)
    print(encoded)
