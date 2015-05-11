from LdapCRUD import CRUD
import ldap


class ServOperation:
    def Add(self, name, surname, mail, phone):
        if name==None or surname==None or mail==None or phone==None:
            return False
        print name, surname, mail, phone

        db = CRUD()
        stooge_name = name + ' ' + surname
        stooge_ou = 'MemberGroupA'
        stooge_info = {'cn': [str(stooge_name)], 'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                'uid': [str(name)],
                'userPassword': [str(name) + 'secret'],
                'mail': [str(mail)],
                'telephoneNumber': [str(phone)],
                'givenName': [str(name)],
                'o': ['stooges'],
                'sn': [str(surname)],
                'ou': ['MemberGroupA']
        }
        """"stooge_info = {'cn': ['Harry Potter'], 'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                'uid': ['harry'],
                'userPassword': ['harrysecret'],
                'mail': ['HPotter@unisonis.com'],
                'telephoneNumber': ['(800)555-1214'],
                'givenName': ['Harry'],
                'o': ['stooges'],
                'sn': ['Potter'],
                'ou': ['MemberGroupA']
        }"""""
        try:
            db.add_stooge(stooge_name, stooge_ou, stooge_info)
        except ldap.LDAPError, error:
            return False
        return True

    def Delete(self, cn):
        if cn==None:
            return False

        db = CRUD()
        try:
            db.delete_stooge(stooge_name=cn, stooge_ou='MemberGroupA')
        except ldap.LDAPError, error:
            return False
        return True

    def Edit(self, cn, name, surname, mail, phone):
        if name != None:
            db = CRUD()
            stooge_modified_attrib = [(ldap.MOD_REPLACE, 'givenName', str(name))]
            try:
                db.modify_stooge(cn, 'MemberGroupA', stooge_modified_attrib)
            except ldap.LDAPError, error:
                return False

        if surname != None:
            db = CRUD()
            stooge_modified_attrib = [(ldap.MOD_REPLACE, 'sn', str(surname))]
            try:
                db.modify_stooge(cn, 'MemberGroupA', stooge_modified_attrib)
            except ldap.LDAPError, error:
                return False

        if mail != None:
            db = CRUD()
            stooge_modified_attrib = [(ldap.MOD_REPLACE, 'mail', str(mail))]
            try:
                db.modify_stooge(cn, 'MemberGroupA', stooge_modified_attrib)
            except ldap.LDAPError, error:
                return False

        if phone != None:
            db = CRUD()
            stooge_modified_attrib = [(ldap.MOD_REPLACE, 'telephoneNumber', str(phone))]
            try:
                db.modify_stooge(cn, 'MemberGroupA', stooge_modified_attrib)
            except ldap.LDAPError, error:
                return False

        return True

    def Show(self, cn):
        print cn
        stooge_filter = 'cn=' + str(cn)
        attributes = ['cn', 'givenName', 'sn', 'mail', 'telephoneNumber']

        db = CRUD()
        try:
            list = db.list_stooges(stooge_filter=stooge_filter, attrib=attributes)
            print "OKOKOK"
        except ldap.LDAPError, error:
            return "Empty"

        toRet=''
        for s in list:
            toRet = toRet + s + '\n'

        print toRet
        return toRet
