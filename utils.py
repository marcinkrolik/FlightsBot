from selenium.common.exceptions import NoSuchElementException
# this is my second change
# this is my third change
class WrongNumberOfParameters(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#def is_element_present(driver, how, what):
#    try: driver.find_element(by=how, value=what)
#    except NoSuchElementException, e: return False
#    return True

def is_element_present(driver, how, what):
    
    found = True
    
    map = {
           "class": "find_element_by_class_name",
           "css": "find_element_by_css_selector",
           "id": "find_element_by_id",
           "link_text": "find_element_by_link_text",
           "name": "find_element_by_name",
           "partial_link_text": "find_element_by_partial_link_text",
           "tag_name": "find_element_by_tag_name",
           "xpath": "find_element_by_xpath",
           "classes": "find_elements_by_class_name",
           "csses": "find_elements_by_css_selector",
           "ids": "find_elements_by_id",
           "link_texts": "find_elements_by_link_text",
           "names": "find_elements_by_name",
           "partial_link_texts": "find_elements_by_partial_link_text",
           "tag_names": "find_elements_by_tag_name",
           "xpaths": "find_elements_by_xpath"
           }
    try: 
        method = getattr(driver, map[how])
        obj = method(what)
    except NoSuchElementException, e: 
        found = False
    return found

def find(driver, how_what):
    map = {
           "class": "find_element_by_class_name",
           "css": "find_element_by_css_selector",
           "id": "find_element_by_id",
           "link_text": "find_element_by_link_text",
           "name": "find_element_by_name",
           "partial_link_text": "find_element_by_partial_link_text",
           "tag_name": "find_element_by_tag_name",
           "xpath": "find_element_by_xpath",
           "classes": "find_elements_by_class_name",
           "csses": "find_elements_by_css_selector",
           "ids": "find_elements_by_id",
           "link_texts": "find_elements_by_link_text",
           "names": "find_elements_by_name",
           "partial_link_texts": "find_elements_by_partial_link_text",
           "tag_names": "find_elements_by_tag_name",
           "xpaths": "find_elements_by_xpath"
           }
    how, what = how_what
    try: 
        method = getattr(driver, map[how])
        obj = method(what)
    except NoSuchElementException, e: 
        raise e("Given object %s not found by %s!" % how_what)
    return obj

def readCsv(filename):
    
    filein = open(filename, 'r')
    lines = filein.readlines()
    filein.close()
    lines.pop(0)
    data = [line.replace('\n','').split(';') for line in lines]
    for dt in data:
        if len(dt) != 4:
            raise WrongNumberOfParameters("Line ... %s ... has wrong number of parameters!" % dt)
    return data
    
    
    
    
