import time
import requests
from bs4 import BeautifulSoup

# By Connor Yu: For utilizing the BeautifulSoup package to scrape course
# registration status from the web.

#TODO:: COMBINE THIS AND CLASS. SHOULD HAVE ALL SUBJECTS, BUT NO STARTING CRNS. ONLY SCAN CRNS IN SYSTEM.
#TODO:: CRN DICTIONARY (SELF.__COURSES) SHOULD HAVE A WATCHING ENTRY, IF WATCH, START AT 1, IF SOMEONE ELSE WATCHES, ADD 1, 
#TODO:: DELETE IF ZERO

class Subject_Scraper:
    def __init__( self, term ):
        print("INITIALIZING SUBJECT SCRAPER")
        self.__courselist = 'https://courselist.wm.edu/courselist/'

        self.__term = ""
        self.__get_term(str(term)) 
        #Declares self.__term: What term it is

        self.__setup()
       
    def __setup( self ):
        print("SETTING UP THE SCRAPER")
        self.subjects = [""]
        self.__get_subjects()
        #Fills out a list with all of the subjects

        self.__courses = {}
        self.__subjects_CRN = {}
        self.__get_courses()
        #Gets all of the courses, stores the CRN in a dictionary, then stores the CRNs in a dictionary with their subjects as keys

    def search( self ):
        print("SEARCHING!!!")
        try:
            for subject_parser in self.subjects:
                webpage = f'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={self.__term}&term_subj={subject_parser}&attr=0&attr2=0&levl=UG&status=0&ptrm=0&search=Search'
                page = BeautifulSoup( requests.get( webpage ).text, 'html.parser')
                for key in self.__subjects_CRN[subject_parser]:
                    element = page.find( text = key )
                    for j in range( 31 ):
                        element = element.next

                    if ( self.__courses[ key ][ 3 ] != element):
                        self.__courses[ key ][ 3 ] = element
                        self.__status_change(key)
        except Exception as e:
            print(e)
            self.__setup()
        print("Done searching")
            

    def __status_change( self, key ):
        name = self.__courses[ key ][ 1 ] + self.__courses[ key ][ 2 ]
        status = self.__courses[ key ][3]
        message = name + " is " + status + " " + time.ctime() 
        # req = requests.post(self.__link, data = {'token' : self.__token, 'user' : self.__user_key, 'message' : message})
        print("STATUS CHANGE!!! " + message)

    

    #Setup

    def __get_term( self, term ):
        tmp_page = BeautifulSoup( requests.get( self.__courselist ).text, 'html.parser')
        term_options = tmp_page.find(id = "term_code")

        terms = [""] * 4
        index = 0

        for option in term_options.find_all('option'):
            terms[index] = option['value']
            index += 1

        year_list = list(terms[0])
        del year_list[4]
        del year_list[4]

        self.__term = "".join(year_list) + term + '0'

    def __get_subjects(self):
        tmp_page = BeautifulSoup( requests.get( self.__courselist ).text, 'html.parser')
        subject_options = tmp_page.find(id = "term_subj")

        count = 0
        for option in subject_options.find_all('option'):
            count += 1
        self.subjects = [""] * (count - 1)

        index = 0
        for option in subject_options.find_all('option'):
            if(option['value'] == "0"):
                continue
            self.subjects[index] = option['value']
            index += 1

    def __get_courses( self ):
        for subject_option in self.subjects:  
            webpage = f'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={self.__term}&term_subj={subject_option}&attr=0&attr2=0&levl=UG&status=0&ptrm=0&search=Search'

            page = BeautifulSoup( requests.get( webpage ).text, 'html.parser')

            count = 0
            CRN = 0
            section = ""
            course_name = ""
            status = 'OPEN'

            element = page.find( id = "results" )
            for i in range(57):
                element = element.next

            try:
                while( True ):
                    CRN = int(element)

                    element = element.next.next.next.next
                    section = element

                    element = element.next.next.next.next.next.next
                    course_name = element

                    for j in range( 3 ):
                        element = element.next.next.next.next.next.next.next
                    status = element

                    self.__courses[ CRN ] =  [ subject_option, section, course_name, status ]

                    element = element.next.next.next.next.next.next
                    
                    count += 1

            except ValueError:
                pass
            
            tmp_list = [0] * count
            index = 0
            for key in self.__courses:
                if self.__courses[key][0] == subject_option:
                    tmp_list[index] = key
                    index += 1
            self.__subjects_CRN[subject_option] = tmp_list