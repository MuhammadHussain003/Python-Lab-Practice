from multipledispatch import dispatch

class DataProcessor:


    @dispatch(list)
    def sort_data(data):
        data = sorted(data)
        print("Integer",sorted(data))

    @dispatch(list)
    def sort_data(data):
        print( "Float",sorted(data))
    @dispatch(list)
    def sort_data(data):
        print("String",sorted(data))

d = DataProcessor()
d.sort_data([1,2,6,3])