from pysimplesoap.client import SoapClient
from gladebuilder import Gtk


class SOAPconnect:
    def __init__(self):
        self.client = SoapClient(
            location="http://127.0.0.1:8000/webservices/sample/call/soap",
            action='http://127.0.0.1:8000/webservices/sample/call/soap', # SOAPAction
            namespace="http://127.0.0.1:8000/webservices/sample/call/soap",
            soap_ns='soap', trace=False, ns=False, exceptions=True)

        # initialize window
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gladeDir/test1.glade")
        self.window = self.builder.get_object("window1")
        self.window.show_all()


        # Show button check
        ShowButton = self.builder.get_object('sButton')
        ShowButton.connect("clicked", self.ShowClicked)

        # Add button check
        ShowButton = self.builder.get_object('aButton')
        ShowButton.connect("clicked", self.AddClicked)

        # Delete button check
        DeleteButton = self.builder.get_object('dButton')
        DeleteButton.connect("clicked", self.DeleteClicked)

        # Edit button check
        EditButton = self.builder.get_object('eButton')
        EditButton.connect("clicked", self.EditClicked)

        #SOAP client test
        response = self.client.Adder(a=1, b=2)
        result = response.AdderResult # manually convert returned type
        print int(result)

        # Starting Window
        Gtk.main()

    def ShowClicked(self, ShowButton):
        print "Show Clicked"
        ShowEntry = self.builder.get_object('sEntry')
        ShowOut = self.builder.get_object('sOut')

        response = self.client.Show(cn=ShowEntry.get_text())
        result = response.ShowResult
        print result

        ShowOut.set_text(str(result))

    def AddClicked(self, AddButton):
        print "Add Clicked"
        AddEntry=[]
        AddEntry.append(self.builder.get_object('aEntryName').get_text())
        AddEntry.append(self.builder.get_object('aEntrySurname').get_text())
        AddEntry.append(self.builder.get_object('aEntryMail').get_text())
        AddEntry.append(self.builder.get_object('aEntryPhone').get_text())
        print AddEntry
        response = self.client.Add(name=AddEntry[0], surname=AddEntry[1], mail=AddEntry[2], phone=AddEntry[3])
        # response = self.client.Add(name='a', surname='c', mail='a@a.com', phone='aca')
        result = response.AddResult
        print bool(result)

    def DeleteClicked(self, DeleteButton):
        print "Delete Clicked"
        DeleteEntry = self.builder.get_object('dEntry')
        response = self.client.Delete(cn=DeleteEntry.get_text())
        result = response.DeleteResult
        print bool(result)

    def EditClicked(self, EditButton):
        print "Edit Clicked"
        AddEntry = []
        AddEntry.append(self.builder.get_object('eEntryCn').get_text())
        AddEntry.append(self.builder.get_object('eEntryName').get_text())
        AddEntry.append(self.builder.get_object('eEntrySurname').get_text())
        AddEntry.append(self.builder.get_object('eEntryMail').get_text())
        AddEntry.append(self.builder.get_object('eEntryPhone').get_text())
        print AddEntry
        response = self.client.Edit(cn=AddEntry[0], name=AddEntry[1], surname=AddEntry[2], mail=AddEntry[3], phone=AddEntry[4])
        #response = self.client.Edit(cn='a c', name='a', surname='c', mail='a@a.com', phone='2')
        result = response.EditResult
        print bool(result)

SOAP = SOAPconnect()
