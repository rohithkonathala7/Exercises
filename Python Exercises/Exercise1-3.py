dictionary = {'stream_group01': {'stream_group01-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '219874', 'Rx Frames': '1978866', 'Loss %': '', 'Frames Delta': '1758992', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '9000.000'}}, 'stream_group02': {'stream_group02-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '209257', 'Rx Frames': '1255542', 'Loss %': '', 'Frames Delta': '1046285', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '6000.000'}}}



for i in range(len(dictionary)):
    d = list(list(dictionary.values())[i].values())[0]
    string = (list((list(dictionary.values())[i]).keys())[0])
    print(f'Transmitted rate is {d["Tx Frame Rate"]} and Received rate is {d["Rx Frame Rate"]} on {string} of {list(dictionary.keys())[i]}')

