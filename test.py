import LdapCRUD
import unittest
import mock
import ldap
from mock import patch


class TestDB(unittest.TestCase):
    #@mock.patch('LdapCRUD.CRUD.add_stooge', return_value=True)
    @mock.patch('LdapCRUD.CRUD.add', return_value=(105, []))
    def test_add(self, func_mock):
        temp = LdapCRUD.CRUD()
        result = temp.add_stooge("cn=Test", "ou=Testou", {"cn": "TestCn"})
        self.assertEqual(result, True)

    @mock.patch('LdapCRUD.CRUD.delete', return_value=(107, [], 2, []))
    def test_delete(self, func_mock):
        temp = LdapCRUD.CRUD()
        result = temp.delete_stooge("cn=Test", "ou=Testou")
        self.assertEqual(result, True)

    @mock.patch('LdapCRUD.CRUD.modify', return_value=(103, []))
    def test_modify(self, func_mock):
        temp = LdapCRUD.CRUD()
        stooge_modified_attrib = [(ldap.MOD_REPLACE, 'givenName', "testname")]
        result = temp.modify_stooge("cn=Test", "ou", stooge_modified_attrib)
        self.assertEqual(result, True)

    @mock.patch('LdapCRUD.CRUD.search', return_value=[('cn=test test,ou=MemberGroupA,dc=ubuntu,dc=local', {'telephoneNumber': ['2222222'], 'mail': ['test@t.com'], 'givenName': ['test'], 'cn': ['test test'], 'sn': ['test']})])
    def test_list(self, func_mock):
        temp = LdapCRUD.CRUD()
        # stooge_modified_attrib = [(ldap.MOD_REPLACE, 'givenName', "testname")]
        result = temp.list_stooges("cn=test", ['cn', 'givenName', 'sn', 'mail', 'telephoneNumber'])
        self.assertEqual(result, ["cn: ['test test']", "givenName: ['test']", "sn: ['test']", "mail: ['test@t.com']", "telephoneNumber: ['2222222']"])

if __name__ == "__main__":
    unittest.main()