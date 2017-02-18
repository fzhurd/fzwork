#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

'''
    read the txt or csv file info to create the Turing Machine
'''
def read_file(file_name):

    info={}

    with open(file_name, 'r') as file:

        file_contents=file.readlines()
        info['contents']=file_contents[0].rstrip()
        info['start_position']=file_contents[1].rstrip()
        info['start_state']=file_contents[2].rstrip()
        info['halt_state']=file_contents[3].rstrip()
        info['actions']=[f.rstrip().split() for f in file_contents[4:]]
        
    return info

'''
    class Tape to control move and print out the Tape
'''
class Tape:

    def __init__(self, initial_str, initial_pos, blank):

        self.tape = []
        self.pos = initial_pos
        self.blank = blank
        self.initial_str = initial_str

        '''
            load the tape
        '''
        if len(initial_str) > 0:
            for ch in initial_str:
                self.tape.append(ch)
        else:
            self.tape.append(blank)

    '''
        method to replace the char and dicide move direction
    '''
    def move(self, read_char, write_new_char, direction):

        if read_char != self.tape[self.pos]:
            self.exit_value(-1)
        
        if write_new_char !='*':
            self.tape[self.pos] = write_new_char
        
        if direction == "-1":
            self.move_left()
        elif direction == "1":
            self.move_right()
    
    '''
        read the char in current position
    '''
    def read(self):
        return self.tape[self.pos]
    
    '''
        move the head left, if outside, add blank
    '''
    def move_left(self):
        if self.pos <= 0: 
            self.tape.insert(-1, self.blank)
            self.pos = 0
        else:
            self.pos += -1

    '''
        move the head right, if outside, add blank
    '''
    def move_right(self):
        self.pos += 1
        if self.pos >= len(self.tape): 
            self.tape.append(self.blank)
    
    '''
        print out the current tape
    '''
    def print_tape(self):

        sys.stdout.write("\n"); 
        sys.stdout.write(" "*self.pos + "*"); 
        sys.stdout.write("\n")

        for ch in self.tape:
            sys.stdout.write(ch)
        sys.stdout.write("\n")
        
'''
    class for TuringMachine
'''
class TuringMachine:

    def __init__(self, initial_str, initial_pos=0, initial_state=0, 
        final_state=9, blank="-"):

        self.tape = Tape(initial_str=initial_str, initial_pos=initial_pos, blank="-")
        self.state = initial_state
        self.final_state = final_state
        self.blank = blank
        self.lenth = len(initial_str)

        self.program = {}    
    
    '''
        add the transition rule
    '''
    def add_each_transition(self, state, char_read, char_write, movement, dest_state):

        if not self.program.has_key(state):
            self.program[state] = {}

        tup = (dest_state, char_write, movement)
        self.program[state][char_read] = tup

    '''
        run one action/transition
    '''
    def make_one_action(self):

        if self.lenth == 0 and self.state in self.final_state:
            self.exit_value(-1)

        if self.state == self.final_state:
            self.exit_value(0)

        if self.state not in self.program.keys(): 
            self.exit_value(-1)

        head = self.tape.read()

        sys.stdout.write('current head value: '+head+'\n')
        sys.stdout.write('current state: '+str(self.state)+'\n')

        # Check whether has wild card match
        matched=self.check_wildcard('*', self.program[self.state].keys())

        if head in self.program[self.state].keys(): 
            (dest_state, char_write, movement) = self.program[self.state][head]
        elif matched:
            (dest_state, char_write, movement) = self.program[self.state]['*']
        else:
            self.exit_value(-1)
            
        sys.stdout.write('new state: '+str(dest_state)+'\n')

        self.state = dest_state

        if char_write =='*':
            char_write=head

        self.tape.move(head, char_write, movement)

    '''
        check whether has wild card
    '''
    def check_wildcard(self, wd, collection):

        matched=False

        if wd in collection:
            matched=True

        return matched

    '''
        exit the process with code
    '''
    def exit_value(self, value):

        if value != 0:
            sys.stdout.write(str(value))
            sys.stdout.write("\n")
        sys.exit(value)

    '''
        keep steping until the halt flag
    '''
    def execute(self):
        while True:
            self.tape.print_tape()
            self.make_one_action()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', required=False, dest='file_name', 
        default='./s1.txt',type=str, 
        help='please input the file name, default will be s1.txt in current directory' )

    args = parser.parse_args()
    input_file=args.file_name

    info=read_file(input_file)
    actions=info['actions']
    
    tm = TuringMachine(info['contents'], int(info['start_position']), 
                        int(info['start_state']), int(info['halt_state']), "-")

    # load all the actions
    for a in actions:
        tm.add_each_transition(int(a[0]), a[1], a[2], a[3], int(a[4]))

    tm.execute()