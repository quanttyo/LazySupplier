import win32com.client
from onec_dict import sources, funcs, methods


class COMInjection:

    def __init__(self, CONN_STRING, connector):
        self.V83 = win32com.client.Dispatch(connector).Connect(CONN_STRING)
        
    def query(self, query):
        q = self.V83.NewObject("Query", query).Execute().Choose()
        return q

    def get(self, query, value):
        f = query.split('.')
        template = "getattr(self.V83.{}, '{}').{}('{}')"

        if isinstance(value, str):
            return eval(template.format(sources[f[0]], f[1], funcs[f[2]], value))
        
        return eval(template.format(sources[f[0]], f[1], funcs[f[2]], value))

    def sets(self, obj, param, value):
        return setattr(obj, param, value)

    def variable(self, query):
        f = query.split('.')
        template = "getattr(self.V83.{}, '{}').{}()"
        return eval(template.format(sources[f[0]], f[1], methods[f[2]]))

    def link(self, obj):
        return getattr(obj, 'Ссылка')




