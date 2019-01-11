import numbers
'''用元类编程实现orm'''

class Field:
    pass
class IntField(Field):
    def __init__(self,db_column,min_value=None,max_value=None):
        self._value=None
        self.db_column=db_column
        self.min_value=min_value
        self.max_value=max_value
        if min_value:
            if not isinstance(min_value,numbers.Integral):
                raise ValueError("min_value must be int")
        if max_value:
            if not isinstance(max_value,numbers.Integral):
                raise ValueError("max_value must be int")
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("paramter must be int")
        if value<self.min_value or value>self.max_value:
            raise ValueError("beyond max_length or min_value")
        self._value=value

class CharField(Field):
    def __init__(self,db_column,max_length=None):
        self._value=None
        self.db_column = db_column
        if not max_length:
            raise ValueError("must have max_length")
        self.max_length=max_length
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError("must be str")
        if len(value)>self.max_length:
            raise ValueError("beyond max_length")
        self._value=value

class ModelMetaClass(type):
    '''
    name='User'
    attrs:
        '__module__'='__main__'
        '__qualname__'='User'
        'name'={CharField}<__main__.CharField object at 0x00000151AF3E6278>
            _value=None
            db_column='name'
            max_length=10
        'age'={IntField}<__main__.IntField object at 0x00000151AF3E62B0>
            _value=None
            db_column='age'
            max_value=100
            min_value=0
        'Meta'={type}<class '__main__.User.Meta'>
            db_table='user'
    '''
    def __new__(cls,*args,**kwargs):                #__new__本质是添加一系列的属性到args[2]中
        name=args[0]
        attrs=args[2]                               #args的第三个参数是存放属性值的
        if name=="BaseModel":                       #如果是BaseModel则不进行下面的方法，而使用type初始化类
            return super().__new__(cls,*args,**kwargs)
        fields={}                                   #attrs中创建一个fields存放表字段
        for key,value in attrs.items():
            if isinstance(value,Field):
                fields[key]=value

        db_table=name.lower()                       #如果有class Meta:则取，没有则取默认
        if attrs.get("Meta",None):
            db_table=getattr(attrs.get("Meta",None),"db_table",db_table)
        _meta = {"db_table":db_table}               #attrs中创建一个_meta存放表名

        attrs["_meta"]=_meta
        attrs["fields"]=fields
        if attrs.get("Meta", None):
            del attrs["Meta"]
        print("===============================")
        print(attrs)
        print("===============================")
        '''
        {'__module__': '__main__', 
        '__qualname__': 'User', 
        'name': <__main__.CharField object at 0x0000023B73038A58>, 
        'age': <__main__.IntField object at 0x0000023B73040320>, 
        '_meta': {'db_table': 'userr'}, 
        'fields': {'name': <__main__.CharField object at 0x0000023B73038A58>, 'age': <__main__.IntField object at 0x0000023B73040320>}}
        '''
        return super().__new__(cls,*args,**kwargs)

class BaseModel(metaclass=ModelMetaClass):
    # def __init__(self,*args,**kwargs):    #解除封印可使用user=User(name="air",age=23)的A级忍术
    #     for key,value in kwargs.items():
    #         setattr(self,key,value)
    #     return super().__init__()
    '''
    self:
        name='air'
        age=23
        fields={dict}:
            'name'={CharField}<__main__.CharField object at 0x000001F60B0A9438>
                _value='air'
                db_column='name'
                max_length=10
            'age'={IntField}<__main__.IntField object at 0x000001F60B0A9470>
                _value=23
                db_column='age'
                max_value=100
                min_value=0
            'Meta'={type}<class '__main__.User.Meta'>
                db_table='user'
        _meta={dict}
            'db_table'='userr'
        '''
    def save(self):
        fields=[]
        values=[]
        for key,value in self.fields.items():
            db_column=value.db_column
            if db_column is None:
                db_column=key.lower()
            fields.append(db_column)
            value=getattr(self,key)
            values.append(str(value))
        sql="insert into {db_table}({fields}) value({values})".format(
            db_table=self._meta["db_table"],fields=",".join(fields),values=",".join(values))
        print(sql)

class User(BaseModel):
    name=CharField(db_column="name",max_length=10)
    age=IntField(db_column="age",min_value=0,max_value=100)

    class Meta:
        db_table="userr"

if __name__ == '__main__':
    user=User()
    user.name="air"
    user.age=23
    user.save()