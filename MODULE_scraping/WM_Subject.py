import time
import requests
import os
from bs4 import BeautifulSoup

from .models import Course
from MODULE_API.send_message import send_message

# By Connor Yu: For utilizing the BeautifulSoup package to scrape course
# registration status from the web.

class Subject_Scraper:
    def __init__( self, term ):
        self.__courselist = 'https://courselist.wm.edu/courselist/'

        self.__term = ""
        self.__get_term(str(term))   #Declares self.__term: What term it is

        
        self.__setup()

        self.search()

    def search( self ):
        while(True):
            print("Searching... " + str(os.getpid()))
            for subject_parser in self.subjects:
                webpage = f'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={self.__term}&term_subj={subject_parser}&attr=0&attr2=0&levl=UG&status=0&ptrm=0&search=Search'
                page = BeautifulSoup( requests.get( webpage ).text, 'html.parser')
                # time.sleep(1)
                for key in self.__subjects_CRN[subject_parser]:
                    if key == 0:
                        continue
                    element = page.find( text = key )

                    try:
                        for j in range( 31 ):
                            element = element.next
                        if Course.objects.get(CRN = key).status != element:
                            update = Course.objects.get(CRN = key)
                            update.status = element
                            update.save() 
                            self.__status_change(key)

                    except AttributeError:
                        send_message(str(key),'2027319090')
                        spot = self.__subjects_CRN[subject_parser].index(key)
                        self.__subjects_CRN[subject_parser][spot] = 0
                        continue

                    except Exception as e:
                        send_message(e,'2027319090')
                        continue

    def __status_change( self, key ):
        update = Course.objects.get(CRN = key)
        message = update.section + update.course_name + " is " + update.status
        send_message(message, '2027319090')
        for user in update.followers.all():
            send_message(message, user.phone_number)


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
        # print("SETTING UP THE SCRAPER")
        self.subjects = [""]
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

            # print(option[ 'value' ])
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
            end = True
            while( end ):
                #Will throw ValueError at the end of the HTML table
                try:
                    CRN = int( element )
                except ValueError as e:
                    end = False
                    continue
                

                element = element.next.next.next.next
                section = element

                element = element.next.next.next.next.next.next
                course_name = element

                for j in range( 3 ):
                    element = element.next.next.next.next.next.next.next
                status = element

                if Course.objects.filter(CRN=CRN).exists():
                    pass
                else:   
                    sqlite_record = Course(
                        CRN = CRN,
                        subject = subject_iteration,
                        section = section,
                        course_name = course_name,
                        status = status,
                    )

                    sqlite_record.save()

               
                element = element.next.next.next.next.next.next
                
                class_amt += 1
            
            tmp_subject_list = [ 0 ] * class_amt
            index = 0
            for key in Course.objects.all().iterator():
                if key.subject == subject_iteration:
                    tmp_subject_list[ index ] = key.CRN
                    index += 1
            self.__subjects_CRN[subject_iteration] = tmp_subject_list
