import time
import requests
from bs4 import BeautifulSoup

from .models import Course

# By Connor Yu: For utilizing the BeautifulSoup package to scrape course
# registration status from the web.

class Subject_Scraper:
    def __init__( self, term ):
        print("INITIALIZING SUBJECT SCRAPER")
        self.__courselist = 'https://courselist.wm.edu/courselist/'

        self.__term = ""
        self.__get_term(str(term)) 
        #Declares self.__term: What term it is

        self.__setup()

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
                time.sleep(1)

        
        #TODO: Instead of just setting it up, delete that particular model.
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

    def __setup( self ):
        #Fills out a list with all of the subjects
        #Gets all of the courses, stores the CRN in a dictionary, then stores the CRNs in a dictionary with their subjects as keys
        print("SETTING UP THE SCRAPER")
        self.subjects = [""]
        self.__courses = {}
        self.__subjects_CRN = {}
        
        

        #Get to the HTML homepage with the subjects
        homepage = BeautifulSoup( requests.get( self.__courselist ).text, 'html.parser' )
        subject_options = homepage.find( id = "term_subj" )
        
        #Count the amount of subjects to allocate the correct amount of spaces to the list
        subject_count = 0
        for option in subject_options.find_all( 'option' ):
            subject_count += 1
        self.subjects = [ "" ] * ( subject_count - 1 )
        
        #Allocate the spaces. 
        subject_index = 0
        for option in subject_options.find_all( 'option' ):
            #There exists an option value of 0 to signify all subjects.
            if option[ 'value' ] == "0":
                continue
            subject_iteration = option[ 'value' ]
            self.subjects[ subject_index ] = subject_iteration
            subject_index += 1

        #Finding the classes
            webpage = f'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={self.__term}&term_subj={subject_iteration}&attr=0&attr2=0&levl=UG&status=0&ptrm=0&search=Search'
           
            page = BeautifulSoup( requests.get( webpage ).text, 'html.parser')

            CRN = 0
            section = ""
            course_name = ""
            status = 'OPEN'
            class_amt = 0

            element = page.find( id = "results" )
            for i in range( 19 ):
                element = element.next.next.next

            #After this, will have all courses for that subject
            try:
                while( True ):
                    CRN = int( element )

                    element = element.next.next.next.next
                    section = element

                    element = element.next.next.next.next.next.next
                    course_name = element

                    for j in range( 3 ):
                        element = element.next.next.next.next.next.next.next
                    status = element

                    
                    self.__courses[ CRN ] =  [ subject_iteration, section, course_name, status ]

                    element = element.next.next.next.next.next.next
                    
                    class_amt += 1

            #Will throw ValueError at the end of the HTML table
            except ValueError:
                pass
            
            
            subject_list = [ 0 ] * class_amt
            index = 0
            for key in self.__courses:
                if self.__courses[ key ][ 0 ] == subject_iteration:
                    subject_list[ index ] = key
                    index += 1
            self.__subjects_CRN[subject_iteration] = subject_list
        
        if len(list(Course.objects.all())) == 0:
            self.database()
    
    def database( self ):
        for subject_parser in self.subjects: #assume subjects is set up
            webpage = f'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={self.__term}&term_subj={subject_parser}&attr=0&attr2=0&levl=UG&status=0&ptrm=0&search=Search'
            page = BeautifulSoup( requests.get( webpage ).text, 'html.parser')
            for key in self.__subjects_CRN[subject_parser]:
                sqlite_record = Course(
                    CRN = key,
                    subject = self.__courses[key][0],
                    section = self.__courses[key][1],
                    course_name = self.__courses[key][2],
                    status = self.__courses[key][3],
                )

                sqlite_record.save()
    
        
