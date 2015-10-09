# -*- Mode:python; c-file-style:"gnu"; indent-tabs-mode:nil -*- */
#
# Copyright (c) 2013-2014 Regents of the University of California.
# Copyright (c) 2014 Susmit Shannigrahi, Steve DiBenedetto
#
# This file is part of ndn-cxx library (NDN C++ library with eXperimental eXtensions).
#
# ndn-cxx library is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# ndn-cxx library is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
#
# You should have received copies of the GNU General Public License and GNU Lesser
# General Public License along with ndn-cxx, e.g., in COPYING.md file.  If not, see
# <http://www.gnu.org/licenses/>.
#
# See AUTHORS.md for complete list of ndn-cxx authors and contributors.
#
# @author Wentao Shang <http://irl.cs.ucla.edu/~wentao/>
# @author Steve DiBenedetto <http://www.cs.colostate.edu/~dibenede>
# @author Susmit Shannigrahi <http://www.cs.colostate.edu/~susmit>
# pylint: disable=line-too-long

import sys
import time
import argparse
import traceback

from pyndn import Interest
from pyndn import Name
from pyndn import Face


class Consumer(object):
    '''Sends Interest, listens for data'''

    def __init__(self, name):
        self.name = Name(name)
        self.face = Face()
        self.isDone = False


    def run(self):
        try:
            interest = Interest(self.name)
            uri = self.name.toUri()

            interest.setInterestLifetimeMilliseconds(4000)
            interest.setMustBeFresh(True)

            self.face.expressInterest(interest, self._onData, self._onTimeout)

            while not self.isDone:
                self.face.processEvents()
                time.sleep(0.01)

            print "Sent Interest for %s" % uri

        except RuntimeError as e:
            print "ERROR: %s" % e


    def _onData(self, interest, data):
        payload = data.getContent()
        name = data.getName()

        print "Received data: %s\n" % payload.toRawStr()
        self.isDone = True


    def _onTimeout(self, interest):
        name = interest.getName()
        uri = name.toUri()

        print "TIMEOUT ", uri
        self.isDone = True



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse command line args for ndn consumer')
    parser.add_argument("-n", "--name", required=True, help='ndn URI to retrieve')

    arguments = parser.parse_args()

    try:
        name = arguments.name
        Consumer(Name(name)).run()

    except:
        traceback.print_exc(file=sys.stdout)
        print "Error parsing command line arguments"
        sys.exit(1)
