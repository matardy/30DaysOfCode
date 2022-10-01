def main():
    pass

def mapping_alphabet(input_str):
    table = []
    j = 0
    for i in (input_str):
        table.append([i,j])
        j = j+1

    return table

if __name__ == '__main__':
    res = mapping_alphabet("hola")
    for i in range(len(res)):
        print(res[i][1])