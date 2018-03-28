import pytest
import copy

dlist = []
d = {}
d1 = {}

@pytest.fixture()
def insert_record(x,y,z):
    d1['name'] = y
    d1['address'] = z
    d[x] = copy.deepcopy(d1)
    dlist.append(copy.deepcopy(d))
    for i in dlist:
        if x in i.keys():
           return "True"

@pytest.mark.parametrize("x,y,z,expected",[
   (1,'Chetan','Pune',"True"),
   (2,'Yash','Bsl',"True"),
   (3,'Ujwal','Akurdi',"True"),
])
def test_ins(x,y,z,expected,insert_record):
    assert insert_record == expected



@pytest.fixture()
def search_record(x):
    for i in dlist:
        if x in i.keys():
            return i

@pytest.mark.parametrize("x,expected",[
   (1,{1:{'name':'Chetan','address':'Pune'}}),
])
def test_op(x,expected,search_record):
    assert search_record == expected


@pytest.fixture()
def delete_record(x):
    for i in dlist:
        if x in i.keys():
            dlist.remove(i)
            return "True"

@pytest.mark.parametrize("x,expected",[
   (1,"True"),
])
def test_del(x,expected,delete_record):
    assert delete_record == expected
