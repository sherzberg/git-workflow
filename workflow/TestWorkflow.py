#   Copyright 2013 Sean L. Mooney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from git import *
import Workflow as wf

"""
Stubs for testing.
"""

def createBranchName(issueName, desc):
    return wf.createBranchName(issueName, desc)

def startIssue(issueName, root, desc=None):
    print issueName, root, desc
    branchName = createBranchName(issueName, desc)
    print("Checkout: " + branchName + " from " + root)

def deleteIssue(issueName, desc=None, defaultBranch='master'):
    branchName = createBranchName(issueName, desc)
    print ("Checking out " + str(defaultBranch))
    print ("Deleting " + str(branchName))
