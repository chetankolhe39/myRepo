import pytest
import copy

dlist = []
d = {}
@pytest.fixture()
def insert_record(x,y,z):
    d['id'] = x
    d['name'] = y
    d['address'] = z
    dlist.append(copy.deepcopy(d))
    for i in dlist:
       if i['id'] == x:
          return i

@pytest.mark.parametrize("x,y,z,expected",[
    (1,'Chetan','Pune',{'id':1,'name':'Chetan','address':'Pune'}),
    (2,'Yash','Bsl',{'id':2,'name':'Yash','address':'Bsl'}),
    (3,'Ujwal','Akurdi',{'id':3,'name':'Ujwal','address':'Akurdi'}),
])
def test_ins(x,y,z,expected,insert_record):
    assert insert_record == expected



@pytest.fixture()
def search_record(x):
   # dlist = [{'id':1,'name':'Chetan','address':'Pune'},{'id':2,'name':'Yash','address':'Bsl'}]
    for i in dlist:
       if i['id'] == x:
          return i

@pytest.mark.parametrize("x,expected",[
   (1,{'id':1,'name':'Chetan','address':'Pune'}),
])
def test_find(x,expected,search_record):
    assert search_record == expected


@pytest.fixture()
def delete_record(x):
   # dlist = [{'id':1,'name':'chet','addr':'pune'},{'id':2,'name':'yash','addr':'bsl'}]
    for i in dlist:
      if i['id'] == x:
         dlist.remove(i)
         return "True"


@pytest.mark.parametrize("x,expected",[
   (1,"True"),
])
def test_del(x,expected,delete_record):
    assert delete_record == expected
