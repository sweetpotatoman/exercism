class Matrix:
    def __init__(self, matrix_string):
        self.data = []
        lines = matrix_string.split('\n')

        for line in lines:
            row = []
            for num in line.split(' '):
                row.append(int(num))
            self.data.append(row)
            # print(self.data)

        
    def row(self, index):
        return(self.data[index-1])

    def column(self, index):
        # print(self.data)
        return([x[index-1] for x in self.data])

if __name__ == "__main__":
    # pass 这些      
    # print(Matrix('1 2\n3 4').row(2))
    print(Matrix('1 2\n3 4').column(2))