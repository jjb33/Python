'''
This application parses prospect information from HTML copied from is******ers.org and is tailored specifically to the data structure of that HTML file.
Putting all the information into a single file was too messy when viewed in Excel, so it will traverse the HTML file several times, looking for
different data and creating separate .csv files for each pass. 4 files are created: [Company phone, general email, and website], 
[Company HQ address], [Company officers by position, name and direct email], [Company geographical sales areas]. 
'''
import re
import csv
#-----------------------------------------------------------------------------------------------------------
stuffin = open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r')
datalistall = []
newlist = []
i=0

with open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r') as meat:
    for line in meat:
        i+=1 #Line really for testing
#
#Skip lines containing reference to images
        if re.search('<img src=', line):
            continue
    #
    #Enountering a new company section, so put "newlist" into the list "datalistall" and then clear out newlist for the next set of company data
        if re.search('search-result opened', line):
            datalistall.append(newlist) 
            newlist = []
#------------------------------------Above code will run for each dataset---------------------------------------------------------------
    #        
    #Get Company Name, Telephone, email, and website. Going to be branches included. Use Excel to mod.
        if re.search('data-name="', line):
            pos1 = line.find('data-name')
            pos2 = line.find('"',pos1)
            pos3 = line.find('"',pos2+1)        
            coname = line[pos2+1:pos3]
            newlist.append(coname) 
        if re.search('tel:', line):
            pos1 = line.find('tel:+')
            phone = line[pos1+5:pos1+18]
            newlist.append(phone)
        if re.search('mailto:', line):
            pos1 = line.find('mailto:')
            pos2 = line.find('"',pos1)
            email = line[pos1+7:pos2]
            newlist.append(email)
        if re.search('www.', line):
            pos1 = line.find('www')
            pos2 = line.find('"',pos1)
            website = line[pos1:pos2]
            newlist.append(website)
datalistall.append(newlist)
with open('R:\OneDrive\PythonProjects\ParsedLists\Output\\name+tel+email+website.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(datalistall)
print('finished with Company Name, Telephone, email, and website')
#############################################################################################################
#Get the position, name, and email of company officers
stuffin = open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r')
datalistall = []
newlist = []
i=0

with open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r') as meat:
    for line in meat:
        i+=1 #Line really for testing
#
#Skip image lines
        if re.search('<img src=', line):
            continue
    #
    #Enountering a new company section, so put newlist into the list"datalistall" and then clear out newlist for the new company
        if re.search('search-result opened', line):
            datalistall.append(newlist) 
            newlist = []
        if re.search('data-name="', line):
            pos1 = line.find('data-name')
            pos2 = line.find('"',pos1)
            pos3 = line.find('"',pos2+1)        
            coname = line[pos2+1:pos3]
            newlist.append(coname) 
    #
    #Officers
        if re.search('div class="officer"', line):
            next(meat)
            offposln = next(meat)
            pos1 = offposln.find('<li>')
            pos2 = offposln.find('</li>', pos1)
            offpos = offposln[pos1+4:pos2]
            offnameln = next(meat)
            pos1 = offnameln.find('<li>')
            pos2 = offnameln.find('</li>', pos1)
            offname = offnameln[pos1+4:pos2]
            offemailln = next(meat)
            pos1 = offemailln.find('mailto:')
            pos2 = offemailln.find('"',pos1)
            offemail = offemailln[pos1+7:pos2]
            newlist.extend((offpos, offname, offemail))
datalistall.append(newlist)
with open('R:\OneDrive\PythonProjects\ParsedLists\Output\officers+info.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(datalistall)
print('finished with Officers')
#######################################################################################################      
#Get mailing addresses. Will include branches
stuffin = open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r')
datalistall = []
newlist = []
i=0

with open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r') as meat:
    for line in meat:
        i+=1 #Line really for testing
#
#Skip image lines
        if re.search('<img src=', line):
            continue
    #
    #Enountering a new company section, so put newlist into the list"datalistall" and then clear out newlist for the new company
        if re.search('search-result opened', line):
            datalistall.append(newlist)
            newlist = []
            if re.search('data-name="', line):
                pos1 = line.find('data-name')
                pos2 = line.find('"',pos1)
                pos3 = line.find('"',pos2+1)        
                coname = line[pos2+1:pos3]
                newlist.append(coname) 
            if re.search('<br>', line):
                if re.search('<li>', line):
                    pos1 = line.find('<br>')
                    pos2 = line.find('<li>')        
                    addr1 = line[pos2+4:pos1]
                    newlist.append(addr1)
                else:
                    pos2 = line.find('<br>')
                    addr2 = line[0:pos2]
                    newlist.append(addr2)
            if re.search('</li>', line):
                if re.search('<li>', line) == None:
                    pos2 = line.find('</li>')
                    addr3 = line[0:pos2]
                    newlist.append(addr3)
            continue
datalistall.append(newlist)
with open('R:\OneDrive\PythonProjects\ParsedLists\Output\mailingaddresses.csv', 'w',) as f:
    writer = csv.writer(f)
    writer.writerows(datalistall)
print('finished with mailing addresses')        
#############################################################################################################
#Get sales areas
stuffin = open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r')
datalistall = []
newlist = []
i=0

with open('R:\OneDrive\PythonProjects\ParsedLists\Distributors_wcontacts.html', 'r') as meat:
    for line in meat:
        i+=1 #Line really for testing
#
#Skip image lines
        if re.search('<img src=', line):
            continue
    #
    #Enountering a new company section, so put newlist into the list"datalistall" and then clear out newlist for the new company
        if re.search('search-result opened', line):
            datalistall.append(newlist)
            newlist = []
        if re.search('data-name="', line):
            pos1 = line.find('data-name')
            pos2 = line.find('"',pos1)
            pos3 = line.find('"',pos2+1)        
            coname = line[pos2+1:pos3]
            newlist.append(coname) 
    #SalesArea
        if re.search('section-content', line):
            pos1 = line.find('section-content')
            pos2 = line.find('</p>',pos1)
            salesarea = line[pos1+17:pos2]
            newlist.append(salesarea)
#            datalistall.append(newlist) #This line was added to the for loop to clear the newlist when new company is reached.  #(old. see to the left)This line should be under the if statement of the last-encountered dataset within a section. e.g. If company officer names are added, this will need to be moved there as they appear after sales areas. 
datalistall.append(newlist)
with open('R:\OneDrive\PythonProjects\ParsedLists\Output\salesareas.csv', 'w') as f: #Change this directory if using on diff PC and make sure dir has write permissions
    writer = csv.writer(f)
    writer.writerows(datalistall)
print('finished with sales areas') 