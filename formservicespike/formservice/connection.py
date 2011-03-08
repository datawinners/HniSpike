#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Couchdb server connection tools. Provide a single unique entry point.
"""

from couchdb.client import Server
from couchdb.http import PreconditionFailed

import settings


class Connection(object):
    """
        Connect to CouchDb according to params in the settings.py file
        and store that internally.

        Access is made with this class cause it's a singleton.
    """

    _inst = None

    def __new__(cls, address=None, port=None, db_name=None,  *args, **kwargs):
        """
            Ensure we have only one instance for the connection.
        """
        if not cls._inst:
            cls._inst = object.__new__(cls, *args, **kwargs)
            cls._inst.connect(address, port, db_name)
        return cls._inst


    def close(self):
        Connection._inst = None


    def connect(self, address=None, port=None, db_name=None):
        """
            Connect to the CouchDB server and work on the databse mentioned in
            the settngs.
        """
        address = address or settings.SERVER_ADDRESS

        self.url = "%s:%s/" % (address.rstrip("/"), port or settings.SERVER_PORT)
        self.server = Server(self.url)

        db_name = db_name or settings.DATABASE_NAME
        try:
            self.db = self.server.create(db_name)
        except PreconditionFailed:
            self.db = self.server[db_name]


    def __unicode__(self):
        return u"Connected on %s - working on %s" % (self.url, self.db.name)

    def __str__(self):
        return unicode(self)

    def __repr__(self):
        return repr(self.db)
