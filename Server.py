from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
from ServerOperations import ServOperation

def adder(a, b):
    "Add two values"
    return a+b

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location="http://localhost:8000/",
    action='http://localhost:8000/', # SOAPAction
    namespace="http://example.com/sample.wsdl", prefix="ns0",
    trace=True,
    ns=True)

# register the user function
dispatcher.register_function('Adder', adder,
    returns={'AdderResult': int},
    args={'a': int, 'b': int})

Operation = ServOperation()
dispatcher.register_function('Show', Operation.Show,
                             #returns={'cn': str, 'name': str, 'surname': str, 'mail': str, 'phone': str},
                             returns={'ShowResult': str},
                             args={'cn': str})

dispatcher.register_function('Add', Operation.Add,
                             returns={'AddResult': bool},
                             args={'name': str, 'surname': str, 'mail': str, 'phone': str})

dispatcher.register_function('Delete', Operation.Delete,
                             returns={'DeleteResult': bool},
                             args={'cn': str})

dispatcher.register_function('Edit', Operation.Edit,
                             returns={'EditResult': bool},
                             args={'cn': str, 'name': str, 'surname': str, 'mail': str, 'phone': str})

print "Starting server..."
httpd = HTTPServer(("", 8000), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()