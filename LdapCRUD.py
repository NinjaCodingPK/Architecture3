import sys, ldap

LDAP_HOST = 'ldap://'
LDAP_BASE_DN = 'dc=ubuntu,dc=local'
MGR_CRED = 'cn=admin,dc=ubuntu,dc=local'
MGR_PASSWD = 'apocalypse'
STOOGE_FILTER = 'o=UbuntuOrg'


class CRUD:
    def __init__(self, ldap_host=None, ldap_base_dn=None, mgr_cred=None, mgr_passwd=None):
        if not ldap_host:
            ldap_host = LDAP_HOST
        if not ldap_base_dn:
            ldap_base_dn = LDAP_BASE_DN
        if not mgr_cred:
            mgr_cred = MGR_CRED
        if not mgr_passwd:
            mgr_passwd = MGR_PASSWD
        self.ldapconn = ldap.initialize(ldap_host)
        self.ldapconn.bind_s(mgr_cred, mgr_passwd)
        self.ldap_base_dn = ldap_base_dn

    def list_stooges(self, stooge_filter=None, attrib=None):
        if not stooge_filter:
            stooge_filter = STOOGE_FILTER
        #s = self.ldapconn.search_s(self.ldap_base_dn, ldap.SCOPE_SUBTREE, stooge_filter, attrib)
        s = self.search(stooge_filter, attrib)
        print s
        print "Here is the complete list of stooges:"
        stooge_list = []
        for stooge in s:
            attrib_dict = stooge[1]
            for a in attrib:
                out = "%s: %s" % (a, attrib_dict[a])
                # print out
                stooge_list.append(out)

        print stooge_list
        # self.ldapconn.unbind()
        return stooge_list

    def add_stooge(self, stooge_name, stooge_ou, stooge_info):
        stooge_dn = 'cn=%s,ou=%s,%s' % (stooge_name, stooge_ou, self.ldap_base_dn)
        stooge_attrib = [(k, v) for (k, v) in stooge_info.items()]
        print "Adding stooge %s with ou=%s" % (stooge_name, stooge_ou)
        try:
            print "------------"
            #self.ldapconn.add_s(stooge_dn, stooge_attrib)
            self.add(stooge_dn, stooge_attrib)
            print "Adding completed"
            return True
        except ldap.LDAPError, error:
            print "not Okay: " + error
            return False
        # self.ldapconn.unbind()

    def modify_stooge(self, stooge_name, stooge_ou, stooge_attrib):
        stooge_dn = 'cn=%s,ou=%s,%s' % (stooge_name, stooge_ou, self.ldap_base_dn)
        print "Modifying stooge %s with ou=%s" % (stooge_name, stooge_ou)
        try:
            print self.modify(stooge_dn, stooge_attrib)
            print "Modifying completed"
            return True
        except ldap.LDAPError:
            return False
        # self.ldapconn.modify_s(stooge_dn, stooge_attrib)
        # self.ldapconn.unbind()

    def delete_stooge(self, stooge_name, stooge_ou):
        stooge_dn = 'cn=%s,ou=%s,%s' % (stooge_name, stooge_ou, self.ldap_base_dn)
        print "Deleting stooge %s with ou=%s" % (stooge_name, stooge_ou)
        #self.ldapconn.delete_s(stooge_dn)
        # self.ldapconn.unbind()
        try:
            print self.delete(stooge_dn)
            print "Deleting completed"
            return True
        except ldap.LDAPError:
            return False

    def add(self, stooge_dn, stooge_attrib):
        return self.ldapconn.add_s(stooge_dn, stooge_attrib)

    def delete(self, stooge_dn):
        return self.ldapconn.delete_s(stooge_dn)

    def modify(self, stooge_dn, stooge_attrib):
        return self.ldapconn.modify_s(stooge_dn, stooge_attrib)

    def search(self, stooge_filter, attrib):
        return self.ldapconn.search_s(self.ldap_base_dn, ldap.SCOPE_SUBTREE, stooge_filter, attrib)