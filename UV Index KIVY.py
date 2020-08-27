#Imports the required modules.
# kivy used to build the UI.
# requests to download the xml content and make a new file.
# ElementTree to parse the xml file.
# os to delete the file once finished with it.
import kivy
import requests as rq
import xml.etree.ElementTree as et
import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

#Sets a minimum version of kivy required to run the app.
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

#Creates a new xml file in the location of this script.
#Propagates content based on downloaded xml data.
def ARPANSARetrieval(self):
    url = ('https://uvdata.arpansa.gov.au/xml/uvvalues.xml')
    r = rq.get (url)
    with open ('UVDATA.xml', 'wb') as self.UVDATA:
        self.UVDATA.write(r.content)
        self.UVDATA = ('UVDATA.xml')
        
    #Uses ElementTree to parse xml iteratively.
    #Looks for 'time' and 'index' values assigned to 'Melbourne'.
    tree = et.parse(self.UVDATA)
    root = tree.getroot()
    for child in root.iter():
        locationofinterest = str(child.attrib)
        lc = locationofinterest
        if 'Melbourne' in lc:
            for y in child.iter('time'):
                time = y.text
            for x in child.iter('index'):
                #Needs to select part of the lc string because it contains characters
                #prior to 'Melbourne'.
                UVINDEX.L1.font_size ='60'
                UVINDEX.L1.bold =True
                UVINDEX.L1.text = (lc[8:17] + '''\n'''+ x.text +' at ' +  time)
                
                #Deletes the xml file that was created.
                os.remove(self.UVDATA)

    
#Closes the app.    
def Close(self):
    App.get_running_app().stop()
    
#Provides the kivy code to build the UI.
class UVINDEX(App):
    def build(self):
        layout = BoxLayout(padding=2, spacing =10, orientation ='vertical')
    

       
        B1 = Button(text='GET UV', font_size ='40', bold =True, background_normal = '', background_color =(0.3,0.3,0.3,0.5), color =(1,1,1,1))
        B1.bind(on_release =ARPANSARetrieval)
        
        B2 =Button(text ='EXIT', font_size ='40', background_normal = '', background_color =(0.3,0.3,0.3,0.5))
        B2.bind(on_release =Close)
        UVINDEX.L1 =Label(text ='', color =(1,0.3,0.1,1))
        layout.add_widget(self.L1)
        layout.add_widget(B1)
        layout.add_widget(B2)
        
        return layout



#Calls the app and keeps it active.
if __name__ == '__main__':
    UVINDEX().run()

