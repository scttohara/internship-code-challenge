#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:48:54 2019

@author: scttohara
"""

playDecision = raw_input("\n\nWould you like to play again (Y/N)? ").lower() 
            
    if playDecision == 'y':
        #needed for .execl
        import os 
        #needed for .executable
        import sys
        os.execl(sys.executable, "python", 'TheGameImpl.py')
            
                
        #found above three lines of code in first answer here:
        #https://stackoverflow.com/questions/34393714/run-python-script-from-another-python-script-but-not-as-an-child-process
                
        else: #playDecision == 'n'
            print "\n\nGoodbye!"
            from sys import exit
            exit();
