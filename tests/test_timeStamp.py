from Algorithms.timeStamp import timestamp_encode


def test_timestamp_encode():
    symboltable=['$','A','B','P','R']
    input_s= 'BA$APBP'
    actual_output = [2, 1, 0, 1, 3, 2, 3]
    calculated_output = timestamp_encode(input_s, symboltable)
    assert actual_output == calculated_output

# def test_timestamp_dncode():
#     symboltable=['$','A','B','P','R']
#     actual_output= 'BA$APBP'
#     input_l = [2, 1, 0, 1, 3, 2, 3]
#     calculated_output = timestamp_decode(input_l, symboltable)
#     assert actual_output == calculated_output